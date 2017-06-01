#!/usr/bin/env python3

import argparse
import glob
import re


def build_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('--pacbio', action='store_true', help='Open the PacBio search mode (check ZMW labels)')
    parser.add_argument('--list', help='A list file containing sequences ID you want to find, with one ID per line')
    parser.add_argument('--input',
                        help='You can use this parameter to specify a fasta file as pool\n'
                             'Or all files with ".fa" and ".fasta" suffixes will be used.')
    parser.add_argument('--output', default='results', help='Output file name. Default: results')

    return parser


def main(args):
    if not args.list:
        raise Exception(
            "You must provide a list containing all IDs you're interested in!\n{}".format(parser.print_help()))

    def fasta_file_to_dict(file):
        with open(file) as f:
            for line in f.readlines():
                if line.startswith('>'):
                    query_id = line.rstrip()
                else:
                    fasta_pool.setdefault(query_id, '')
                    fasta_pool[query_id] += line.rstrip()

    fasta_pool = {}
    query_id_regex = re.compile(r'/\d+/$')

    with open(args.output, 'w') as output:
        if args.input:
            fasta_file_to_dict(args.input)
            with open(args.list) as f:
                for line in f.readlines():
                    query_id = line.rstrip()
                    if args.pacbio and not query_id_regex.search(query_id):
                        raise Exception('There\'s at least one query ID in your list does not end with pattern /\d+/!')
                    print('Searching for... {}'.format(query_id))
                    try:
                        query_contents = next([k, v] for (k, v) in fasta_pool.items() if query_id in k)
                        output.writelines('{}\n'.format('\n'.join(query_contents)))
                    except StopIteration:
                        output.writelines('{} not found!\n'.format(query_id))

        else:
            id_to_file = {}
            extensions = ('*.fa', '*.fasta')
            fasta_file_pool = []
            for extension in extensions:
                fasta_file_pool.extend(glob.glob(extension))
            for file in fasta_file_pool:
                with open(file) as f:
                    for line in f.readlines():
                        if line.startswith('>'):
                            id_to_file[line.rstrip()] = file

            with open(args.list) as f:
                file_contain_queries = {}
                for line in f.readlines():
                    query_id = line.rstrip()
                    if args.pacbio and not query_id_regex.search(query_id):
                        raise Exception('There\'s at least one query ID in your list does not end with pattern /\d+/!')
                    query_list = next([k, v] for (k, v) in id_to_file.items() if query_id in k)
                    file_contain_queries.setdefault(query_list[1], [])
                    file_contain_queries[query_list[1]].append(query_list[0])

            for k, v in file_contain_queries.items():
                fasta_file_to_dict(k)
                for query_contents in v:
                    output.writelines('{}\n'.format('\n'.join([query_contents, fasta_pool[query_contents]])))


if __name__ == '__main__':
    parser = build_parser()
    args = parser.parse_args()
    main(args)
