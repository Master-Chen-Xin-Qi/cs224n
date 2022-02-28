# Calculate the accuracy of a baseline that simply predicts "London" for every
#   example in the dev set.
# Hint: Make use of existing code.
# Your solution here should only be a few lines.
import argparse
import utils

parser = argparse.ArgumentParser()
parser.add_argument('--eval_corpus_path', help='Path to the corpus to evaluate on', default='birth_dev.tsv')
args = parser.parse_args()

if __name__ == '__main__':
    predictions = ['London']*len(open(args.eval_corpus_path).readlines())
    total, correct = utils.evaluate_places(args.eval_corpus_path, predictions)
    acc = correct/total
    print(acc)