# Dr. <i>**G**</i>aoShanSB's <i>**a**</i>bnormal requirements <i>**o**</i>riented, <i>**S**</i>uper <i>**h**</i>umorous <i>**a**</i>nd <i>**n**</i>ot <i>**S**</i>cientific tool <i>**B**</i>ox

A toolbox for bioinformatics works in Dr. Gao's lab.

## Requirements
- None
- But currently only for Windows user

## Features
This application has the following features:
- Batch align queries to a single reference, and generate a file containing alignments in format for (could be, but not limited to) supplementary files of publication.
- Batch download sequence by *accession number* with specific base location.

## Known issues
- Since *MagicBlast* has been chosen as aligner, the boundaries of alignments may not as accurate as you think. 
It also can occur at `-` (a placeholder representing a base length, known as a deletion in query). 
You **should** check and modify the results yourself. 
**However, the program still saves you a lot of time.**
- ~~I won't provide a archive of one-file bundle for some time to come.~~

## Examples
### 1. Align queries to subject(single-sequence reference)
You may perform as follow picture:
![example_how_align_queries.png](docs/imgs/example_how_align_queries.png)

The result of this tool seems like:
![example_result_align_queries.png](docs/imgs/example_result_align_queries.png)

(a) The file was opened in *notepad++*. Alignments were shown as in-line "fasta" format.

(b) The boundaries (softclip ending) of alignments were added parentheses for distinction.
**Warning: It may not accurate here, and correction by hands may needed.**

(c) The **insertion** (queries according to the subject) will be **deleted** and the **deletion** will be shown as `-`.
**Warning: It may also not accurate near *deletion*, and correction by hands may needed.**

### 2. Batch download sequence (could be specified base location)
You may perform as follow picture:
![example_how_download_seq.png](docs/imgs/example_how_download_seq.png)

The result of this tool seems like:
![example_result_download_seq.png](docs/imgs/example_result_download_seq.png)

## Contributor
- [Yu Sun](http://icannotendure.space/)
- [Zhiguang Chen](https://github.com/Dgmaxxx) (May participate soon）

## TODO
- ~~Handle with error.~~
- ~~New feature: Get sequences with specific region from NCBI databases.~~
- Add logo.
- Add icon.
- ~~Add warnings and other dialog widgets.~~
- Perform UPX compression on certain dependencies for binary release.
- New feature: Batch extract sequences from *FASTA/FASTQ* file.
- Provide Installer release on *Windows* platform.

## License
This project is released under the MIT license. See the included license file.
