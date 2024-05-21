
import argparse
import os
import pandas as pd
from evaluation_metric_template_kaggle_subtask_1 import eval_dataset

"""
    Id,Tags
    0,"[{'Tag_Start': 13, 'Tag_End': 61, '5W1H_Label': 'WHEN'}, {'Tag_Start': 63, 'Tag_End': 83, '5W1H_Label': 'WHAT'}, {'Tag_Start': 96, 'Tag_End': 126, '5W1H_Label': 'HOW'}]"
    1,"[{'Tag_Start': 0, 'Tag_End': 12, '5W1H_Label': 'WHEN'}, {'Tag_Start': 14, 'Tag_End': 28, '5W1H_Label': 'WHO'}, {'Tag_Start': 45, 'Tag_End': 99, '5W1H_Label': 'WHERE'}, {'Tag_Start': 117, 'Tag_End': 163, '5W1H_Label': 'WHAT'}]"
    2,"[{'Tag_Start': 21, 'Tag_End': 38, '5W1H_Label': 'WHAT'}, {'Tag_Start': 39, 'Tag_End': 73, '5W1H_Label': 'WHO'}, {'Tag_Start': 74, 'Tag_End': 88, '5W1H_Label': 'WHERE'}, {'Tag_Start': 90, 'Tag_End': 126, '5W1H_Label': 'WHO'}, {'Tag_Start': 128, 'Tag_End': 185, '5W1H_Label': 'WHO'}, {'Tag_Start': 187, 'Tag_End': 244, '5W1H_Label': 'WHO'}, {'Tag_Start': 246, 'Tag_End': 291, '5W1H_Label': 'WHO'}, {'Tag_Start': 293, 'Tag_End': 332, '5W1H_Label': 'WHO'}, {'Tag_Start': 335, 'Tag_End': 375, '5W1H_Label': 'WHO'}]"
    3,"[{'Tag_Start': 0, 'Tag_End': 23, '5W1H_Label': 'WHO'}, {'Tag_Start': 46, 'Tag_End': 90, '5W1H_Label': 'WHAT'}, {'Tag_Start': 91, 'Tag_End': 122, '5W1H_Label': 'WHEN'}]"
    4,"[{'Tag_Start': 24, 'Tag_End': 45, '5W1H_Label': 'WHAT'}]"
"""


def main(args):
    pathDataGold = args.pathDataGold
    pathDataInfered = args.pathDataInfered
    dataGold = pd.read_csv(os.getcwd() + pathDataGold, sep=",")
    dataInfered = pd.read_csv(os.getcwd() + pathDataInfered, sep=",")

    df, metrics = eval_dataset(dataGold, dataInfered, ['WHAT', 'WHEN', 'WHERE', 'WHO', 'WHY', 'HOW'])
    print(metrics)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('--pathDataGold', metavar='pathDataGold', type=str, help='Path to the data real',
                        default='/data/gold.csv')
    parser.add_argument('--pathDataInfered', metavar='pathDataInfered', type=str, help='Path to the data infered',
                        default='/data/submission.csv')
    args = parser.parse_args()
    main(args)


