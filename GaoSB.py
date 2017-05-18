import os
import re
import subprocess

from PyQt5 import QtWidgets

from gui import Ui_MainWindow


class MyWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.setupUi(self)

    def align_query(self):
        # Transfer subject in Text Edit and make a tmp file
        # TODO check blank line, newline in the end and other format problem
        whole_subject = str(self.textEdit_subject.toPlainText()).splitlines()
        ref_id = whole_subject[0]
        ref_seq = whole_subject[1]
        # TODO raise an error when cannot create tmp file
        with open('tmp_ref', 'w') as f:
            f.writelines('\n'.join(whole_subject))
        # Transfer query in Text Edit and make a tmp file
        whole_query = str(self.textEdit_query.toPlainText()).splitlines()
        with open('tmp_query', 'w') as f:
            f.writelines('\n'.join(whole_query))
        # Transfer filename in Text Edit
        destination_file = str(self.textEdit_destination.toPlainText())
        # Call magicblast and redirect its output (SAM format in default)
        process_magicblast = subprocess.run(
            ['dependencies' + os.sep + 'magicblast', '-query', 'tmp_query', '-subject', "tmp_ref"],
            stdout=subprocess.PIPE)

        tmp_list = ['tmp_ref', 'tmp_query']
        [os.remove(x) for x in tmp_list]

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


if __name__ == '__main__':
    import sys

    app = QtWidgets.QApplication(sys.argv)
    widget = MyWindow()
    widget.show()
    sys.exit(app.exec_())
