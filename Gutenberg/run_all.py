import pandas as pd
import numpy as np
import os
import nltk
from sklearn.model_selection import KFold
import sys
import argparse
from evaluate_classifier import evaluate_classifier


clf_names=[
#'freq_table_chisq',
'freq_table_cosine',
#'freq_table_LL',
#'freq_table_CR',
#'freq_table_HC',
#'multinomial_NB',
#'KNN_5',
#'KNN_2',
#'logistic_regression',
'NeuralNet',
#'SVM',
]


def main() :
  parser = argparse.ArgumentParser()
  parser = argparse.ArgumentParser(description='Evaluate hardcoded list of '
  'classifiers Authorship challenge')
  parser.add_argument('-i', type=str, help='data file (csv)')
  parser.add_argument('-n', type=str, help='n split (integer)', default=10)
  args = parser.parse_args()
  if not args.i:
      print('ERROR: The data file is required')
      parser.exit(1)
  else :
    data_path = args.i

  print('\tData: {}'.format(data_path))
  print('\tNumber of train/val splits = {}'.format(args.n))

  vocab_sizes=[250, 1000, 3000]
  df = pd.DataFrame()

  n_split = args.n
  no_vocab_sizes = len(vocab_sizes)
  no_clf = len(clf_names)

  for ic in range(no_clf) :
    for iv in range(no_vocab_sizes) :
        vocab_size = vocab_sizes[iv] 
        clf_name = clf_names[ic]
        print("classifier = {}".format(clf_name))
        print("vocab size = {}".format(vocab_size))
        acc, std = evaluate_classifier(clf_name, data_path, vocab_size, n_split)
        print("Average accuracy = {}".format(acc))  
        print("STD = {}".format(std))

        df = df.append({'clf_name' : clf_name,
            'vocab_size' : vocab_size,
            'accuracy' : acc,
            'std' : std,
            'n_split' : n_split
            }, ignore_index = True)        
        df.to_csv('results.csv')

if __name__ == '__main__':
  main()
