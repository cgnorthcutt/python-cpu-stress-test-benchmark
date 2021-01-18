import multiprocessing
import tqdm
import argparse

# Benchmarking settings
parser = argparse.ArgumentParser(description='Python CPU benchmarking stress test.')
parser.add_argument('--threads', type=int, default=2, metavar='N',
                    help='Number of threads to use. Set to 1 for single-threaded.')
parser.add_argument('--duration', type=int, default=10, metavar='N',
                    help='How long to stress test in seconds (default: 10)')

def main(args):
    if args.threads == 1:
        pass
    else:
        pool = multiprocessing.Pool(processes = 3)
        print(pool.map(worker, range(5)))


if __name__ == '__main__':
    args = parser.parse_args()
    main(args)
