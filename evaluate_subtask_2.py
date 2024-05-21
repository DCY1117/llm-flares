
import argparse
import os
import pandas as pd
from evaluation_metric_template_kaggle_subtask_2 import eval_dataset

"""
    Submmission format:
    Id,Reliability_Label
    75,confiable
    179,confiable
    511,confiable
"""


def main(args):
    pathDataGold = args.pathDataGold
    pathDataInfered = args.pathDataInfered
    dataGold = pd.read_csv(os.getcwd() + pathDataGold, sep=",")
    dataInfered = pd.read_csv(os.getcwd() + pathDataInfered, sep=",")

    metrics = eval_dataset(dataGold, dataInfered)
    print(metrics)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('--pathDataGold', metavar='pathDataGold', type=str, help='Path to the data real',
                        default='/data/gold.csv')
    parser.add_argument('--pathDataInfered', metavar='pathDataInfered', type=str, help='Path to the data infered',
                        default='/data/submission.csv')
    args = parser.parse_args()
    main(args)


