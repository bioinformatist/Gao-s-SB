#!/usr/bin/env python3

import sys
from collections import defaultdict

sam_pool = defaultdict(list)
name_chr_len = {}
ids = []
complete_sam = defaultdict(list)


def sam_parser(file):
    # It seems latest python does not need global anymore, keep here for traceback
    # global sam_pool
    # global name_with_chr
    for line in open(file):
        line = line.strip().split('\t')
        # Use a dictionary to save primary alignment with chromosome
        if line[1] == '0' or line[1] == '16':
            # Save reads ID and its flag with length as value
            name_chr_len[line[0]] = [line[2], len(line[9])]
        # Discard those secondary alignments with different chromosome according to primary ones
        if line[2] != name_chr_len[line[0]][0]:
            continue
        # Also use a dictionary to keep complete lines
        complete_sam[line[0]].append(line)
        sam_pool[line[0]].append(int(line[3]))


def sam_filter():
    for k in sam_pool:
        if len(sam_pool[k]) == 1:
            continue
        if (max(sam_pool[k]) - min(sam_pool[k])) / name_chr_len[k][1] < int(time):
            ids.append(k)


def sam_extractor(file):
    with open(file, 'w') as f:
        for id in ids:
            for line in complete_sam[id]:
                f.write('\t'.join(line) + '\n')


if __name__ == '__main__':
    time = sys.argv[2]
    sam_parser(sys.argv[1])
    sam_filter()
    sam_extractor(sys.argv[3])

    # time = 5
    # sam_parser('secondary_mapped.sam')
    # sam_filter()
    # sam_extractor('fuck')
