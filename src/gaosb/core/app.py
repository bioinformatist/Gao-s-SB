import os
import re
import subprocess
import sys
from collections import defaultdict

from Bio import Entrez
from Bio import SeqIO
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QDesktopServices
from PyQt5.QtWidgets import QMessageBox

from gaosb.gui.mainwindow import Ui_MainWindow


def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


class Application(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(Application, self).__init__()
        self.setupUi(self)
        self._set_connections()

    def raise_warnings(self, warning_content, warning_details, warning_title ="Warning"):
        def show_warnings(warning_content, warning_details, warning_title="Warning"):
            """
            Raise a warning dialog when the app meets a handled error.
            :param warning_content: the main text of dialog
            :param warning_details: the detailed text
            :param warning_title: the title of the dialog
            :return: None
            """
            msg = QMessageBox()

            msg.setIcon(QMessageBox.Warning)
            msg.setText(warning_content)
            msg.setInformativeText("You may check usage at "
                                   "<a href=https://github.com/bioinformatist/Gao-s-SB#examples>the owner's GitHub</a>."
                                   "Choose <b>Show Details</b> for additional information...")
            msg.setWindowTitle(warning_title)

            msg.setDetailedText("The details are as follows:\n{}\n"
                                .format(warning_details))
            msg.setTextFormat(Qt.RichText)
            msg.setTextInteractionFlags(Qt.TextSelectableByMouse)

            msg.exec_()
        self.statusbar.showMessage('Warning: halted now')
        tmp_excepthook = sys.excepthook
        sys.excepthook = self.show_warnings(warning_content, warning_details)
        sys.excepthook = tmp_excepthook

    def _set_connections(self):
        """
        Build signal/slot connections once the app started.
        :return: None
        """
        self.actionAbout.triggered.connect(self.init_about)
        # To make the link in About page clickable
        self.label_2.linkActivated.connect(open_url)

        self.action_queryAligner.triggered.connect(self.init_align_queries)
        self.pushButton_doAligning.clicked.connect(self.do_align_query)

        self.action_downloadSequence.triggered.connect(self.init_download_sequences)
        self.pushButton_doDownloadSeq.clicked.connect(self.do_download_seq)

    def init_about(self):
        self.stackedWidget_main.setCurrentWidget(self.page_about)

    def monitor_text_edit(self, button, *text_edit_list):
        """
        Apply empty check on certain textEdit boxes.
        :param button: the button which should be set
        :param text_edit_list: the textEdit box which should be monitored
        :return: None
        """
        button.setDisabled(True)

        def set_button(button, text_edit_list):
            if all(t.toPlainText() for t in text_edit_list):
                button.setEnabled(True)
            else:
                button.setEnabled(False)

        check = lambda: set_button(button, text_edit_list)
        [t.textChanged.connect(check) for t in text_edit_list]

    def init_align_queries(self):
        self.stackedWidget_main.setCurrentWidget(self.page_alignQuery)
        self.monitor_text_edit(self.pushButton_doAligning, self.textEdit_query, self.textEdit_subject,
                               self.textEdit_alignmentDestination)

    def init_download_sequences(self):
        self.stackedWidget_main.setCurrentWidget(self.page_downloadSeq)
        self.monitor_text_edit(self.pushButton_doDownloadSeq, self.textEdit_accessionList,
                               self.textEdit_downloadSeqDestination)

    def do_align_query(self):
        # Transfer subject in Text Edit and make a tmp file
        self.statusbar.showMessage('Parsing parameters and creating temp files...')
        try:
            whole_subject = str(self.textEdit_subject.toPlainText()).splitlines()
            ref_id = whole_subject[0]
            ref_seq = whole_subject[1]
        except:
            self.raise_warnings('Format error: Wrong fasta input',
                                                'Only one subject sequence is supported. '
                                                'You provide less or more than one sequence '
                                                'or sequences not in fasta format.')
            return

        try:
            with open('tmp_ref', 'w') as f:
                f.writelines('\n'.join(whole_subject))
            # Transfer query in Text Edit and make a tmp file
            whole_query = str(self.textEdit_query.toPlainText()).splitlines()
            with open('tmp_query', 'w') as f:
                f.writelines('\n'.join(whole_query))
        except:
            self.raise_warnings('I/O error: Can\'t create temp file',
                                                'You should check your privilege and remaining disk space.')
            return
        # Transfer filename in Text Edit
        destination_file = str(self.textEdit_alignmentDestination.toPlainText())

        # Call magicblast and redirect its output (SAM format in default)
        self.statusbar.showMessage('Running magicblast...')
        process_magicblast = subprocess.run(
            [resource_path('dependencies') + os.sep + 'magicblast', '-query', 'tmp_query', '-subject', "tmp_ref"],
            **subprocess_args())

        self.statusbar.showMessage('Removing temp files...')
        tmp_list = ['tmp_ref', 'tmp_query']
        [os.remove(x) for x in tmp_list]

        self.statusbar.showMessage('Parsing blast results...')
        query_id = []
        result_list = []

        for line in process_magicblast.stdout.decode('utf-8').splitlines():
            # Ignore SAM header and empty line
            if line.startswith('@') or not line.strip():
                continue
            else:
                line = line.split('\t')
                # ID is the 1st field in SAM file
                query_id.append(line[0])
                # Reserve all result for further parsing
                result_list.append(line)

        with open(destination_file, 'w') as f_result:
            # Pre-compile regex
            cigar_regex = re.compile(r'(\d+)(\w)')
            # Get the length of the longest id
            max_id_len = max([len(x) for x in query_id])
            # Use the length to reformat id then use double tabular to separate id and sequence
            f_result.writelines(('\t' * 2).join(['{:{max_id_len}}'.format(ref_id, max_id_len=max_id_len), ref_seq]))
            f_result.writelines('\n')

            for result in result_list:
                result_id = '>' + result[0]
                cigar_list = cigar_regex.findall(result[5])
                seq = result[9]
                # Initialize the index of sequence and offset
                position = offset = 0
                if cigar_list[0][1] == "S":
                    position = offset = int(cigar_list[0][0])
                    del cigar_list[0]
                seq = seq[:position] + '(' + seq[position:]
                for cigar in cigar_list:
                    if cigar[1] == 'M':
                        pass
                    elif cigar[1] == 'I':
                        seq = seq[:position] + seq[(position + int(cigar[0])):]
                    elif cigar[1] == 'D':
                        seq = seq[:position] + '-' * int(cigar[0]) + seq[position:]
                    elif cigar[1] == 'S':
                        seq = seq[:position] + ')' + seq[position:]
                    position += int(cigar[0])
                # Since the 4th column of sam file is the start position of alignment, add an offset of one base
                # Another one-base offset for left parenthesis, so we got minus 2
                seq = (int(result[3]) - 2 - offset) * ' ' + seq
                f_result.writelines(('\t' * 2).join(['{:{max_id_len}}'.format(result_id, max_id_len=max_id_len), seq]))
                f_result.writelines('\n')
                self.statusbar.showMessage('done.')

    def do_download_seq(self):
        self.statusbar.showMessage('Parsing parameters...')
        Entrez.email = "sun_yu@mail.nankai.edu.cn"
        accession_list = str(self.textEdit_accessionList.toPlainText()).splitlines()
        destination_file = str(self.textEdit_downloadSeqDestination.toPlainText())

        try:
            [accession_list.remove(s) for s in accession_list if s == '']
            accession_pool_spec = defaultdict(list)
            accession_pool_whole = []
            blank_regex = re.compile('\s+')

            for accession in accession_list:
                if accession.startswith('#'):
                    continue
                if blank_regex.search(accession):
                    accession = blank_regex.split(accession)
                    accession_pool_spec[accession[0]].append([int(x) for x in accession[-2:]])
                else:
                    accession_pool_whole.append(accession)
            accession_pool_whole = list(set(accession_pool_whole))
        except:
            self.raise_warnings('Format error: Wrong input', 'Please check your input content as well as separator.')
            return

        try:
            self.statusbar.showMessage('Fetching sequences from NCBI databases...')
            handle = Entrez.efetch(db="nuccore", rettype='gb', id=list(accession_pool_spec.keys()))
            records_spec = list(SeqIO.parse(handle, "gb"))
            handle = Entrez.efetch(db="nuccore", rettype='gb', id=accession_pool_whole)
            records_whole = list(SeqIO.parse(handle, "gb"))
        except:
            self.raise_warnings('Network error: No connection', 'Please check your network connection.')
            return

        try:
            self.statusbar.showMessage('Parsing downloaded sequences...')
            with open(destination_file, 'w') as f:
                for record in records_whole:
                    f.write('>{}\n{}\n'.format(record.id, record.seq))
                for record in records_spec:
                    for location in accession_pool_spec[record.id]:
                        f.write('>{} | {}-{}\n{}\n'.format(record.id, location[0], location[1],
                                                           record.seq[location[0] - 1:location[1]]))
            self.statusbar.showMessage("Done.")
        except:
            self.raise_warnings('I/O error: Can\'t create output file',
                                                'You should check your privilege and remaining disk space.')
            return


def open_url(url):
    QDesktopServices.openUrl(QtCore.QUrl(url))


# Create a set of arguments which make a ``subprocess.Popen`` (and
# variants) call work with or without Pyinstaller, ``--noconsole`` or
# not, on Windows and Linux. Typical use::
#
#   subprocess.call(['program_to_run', 'arg_1'], **subprocess_args())
#
# When calling ``check_output``::
#
#   subprocess.check_output(['program_to_run', 'arg_1'],
#                           **subprocess_args(False))
def subprocess_args(include_stdout=True):
    # The following is true only on Windows.
    if hasattr(subprocess, 'STARTUPINFO'):
        # On Windows, subprocess calls will pop up a command window by default
        # when run from Pyinstaller with the ``--noconsole`` option. Avoid this
        # distraction.
        si = subprocess.STARTUPINFO()
        si.dwFlags |= subprocess.STARTF_USESHOWWINDOW
        # Windows doesn't search the path by default. Pass it an environment so
        # it will.
        env = os.environ
    else:
        si = None
        env = None

    # ``subprocess.check_output`` doesn't allow specifying ``stdout``::
    #
    #   Traceback (most recent call last):
    #     File "test_subprocess.py", line 58, in <module>
    #       **subprocess_args(stdout=None))
    #     File "C:\Python27\lib\subprocess.py", line 567, in check_output
    #       raise ValueError('stdout argument not allowed, it will be overridden.')
    #   ValueError: stdout argument not allowed, it will be overridden.
    #
    # So, add it only if it's needed.
    if include_stdout:
        ret = {'stdout': subprocess.PIPE}
    else:
        ret = {}

    # On Windows, running this from the binary produced by Pyinstaller
    # with the ``--noconsole`` option requires redirecting everything
    # (stdin, stdout, stderr) to avoid an OSError exception
    # "[Error 6] the handle is invalid."
    ret.update({'stdin': subprocess.PIPE,
                'stderr': subprocess.PIPE,
                'startupinfo': si,
                'env': env})
    return ret
