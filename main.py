import argparse
from encryption_and_decryption import encryption, decryption
import binascii

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="This application is the realization of GOST R 34.12-2015")
    parser.add_argument("-i", "--input", type=str, required=True, help="The parameter is needed to specify "
                                                                       "the path to the input file.")
    parser.add_argument("-o", "--output", type=str, required=True, help="The parameter is needed to specify"
                                                                       " the path to the output file.")
    parser.add_argument("-k", "--key", type=str, required=True, help="The key is specified in the Base64 "
                                                                     "format")
    parser.add_argument("-m", "--mode", type=int, required=True, choices=[0, 1], help="0 - encryption; "
                                                                                         "1 - decryption")

    args = parser.parse_args()

    try:
        if args.mode == 0:
            encryption(args.input, args.key, args.output)
        elif args.mode == 1:
            decryption(args.input, args.key, args.output)
    except FileNotFoundError as error:
        print(error)
    except binascii.Error as error:
        print(error)

