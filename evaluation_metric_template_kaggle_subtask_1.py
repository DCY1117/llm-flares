"""
TODO: Enter any documentation that only people updating the metric should read here.

All columns of the solution and submission dataframes are passed to your metric, except for the Usage column.

Your metric must satisfy the following constraints:
- You must have a function named score. Kaggle's evaluation system will call that function.
- You can add your own arguments to score, but you cannot change the first three (solution, submission, and row_id_column_name).
- All arguments for score must have type annotations.
- score must return a single, finite, non-null float.
"""

import pandas as pd

catList = ['WHAT', 'WHEN', 'WHERE', 'WHO', 'WHY', 'HOW']


class ParticipantVisibleError(Exception):
    # If you want an error message to be shown to participants, you must raise the error as a ParticipantVisibleError
    # All other errors will only be shown to the competition host. This helps prevent unintentional leakage of solution data.
    pass


def detect_and_classify_texts(textTag, df):

    #Order the real and predicted arrays by start, and if start is the same, by tag
    real = sorted(textTag['real'], key=lambda row: (row["Tag_Start"], row["5W1H_Label"]))
    predicted = sorted(textTag['predicted'], key=lambda row: (row["Tag_Start"], row["5W1H_Label"]))

    #CORRECT - Ca
    for annR in real.copy():
        for annP in predicted.copy():
            if annR['Tag_Start'] == annP['Tag_Start'] and annR['Tag_End'] == annP['Tag_End'] and annR['5W1H_Label'] == annP['5W1H_Label']:
                df.loc[annR['5W1H_Label'], 'Ca'] += 1
                real.remove(annR)
                predicted.remove(annP)
                break

    #PARTIAL - Ca
    for annR in real.copy():
        #Get all the annotation within the range of the real annotation
        partialMatch = []

        for annP in predicted.copy():
            if (annP['Tag_Start'] >= annR['Tag_Start'] and annP['Tag_End'] <= annR['Tag_End']) or \
            (annP['Tag_Start'] <= annR['Tag_Start'] and annP['Tag_End'] >= annR['Tag_Start'] and annP['Tag_End'] <= annR['Tag_End']) or \
            (annP['Tag_Start'] >= annR['Tag_Start'] and annP['Tag_Start'] <= annR['Tag_End'] and annP['Tag_End'] >= annR['Tag_End']) or \
            (annP['Tag_Start'] <= annR['Tag_Start'] and annP['Tag_End'] >= annR['Tag_End']):

                #Append the element to the partialMatch array
                partialMatch.append(annP)

        if partialMatch:

                #Order the partialMatch elements by size (end - start)
                partialMatch = sorted(partialMatch, key = lambda row: (row["Tag_End"] - row["Tag_Start"]))

                #Check if some of the element tags are the same as the real annotation
                for annP in partialMatch:
                    if annP['5W1H_Label'] == annR['5W1H_Label']:
                        df.loc[annR['5W1H_Label'], 'Pa'] += 1
                        real.remove(annR)
                        predicted.remove(annP)
                        break

    #INCORRECT - Ia
    for annR in real.copy():
        for annP in predicted.copy():
            if annP['Tag_Start'] == annR['Tag_Start'] and annP['Tag_End'] == annR['Tag_End'] and annP['5W1H_Label'] != annR['5W1H_Label']:
                df.loc[annR['5W1H_Label'], 'Ia'] += 1
                real.remove(annR)
                predicted.remove(annP)
                break

    #MISSING - Ma
    for annR in real.copy():
        df.loc[annR['5W1H_Label'], 'Ma'] += 1

    #SPURIOUS - Sa
    for annP in predicted:
        df.loc[annP['5W1H_Label'], 'Sa'] += 1

    del real, predicted

    return df


def eval_dataset(real, predicted, catList):

    df = pd.DataFrame(columns=['Ca', 'Ia', 'Pa', 'Ma', 'Sa', 'Precision', 'Recall', 'F1', 'Accuracy'], index=catList)
    df = df.fillna(0)

    #Iterate over the real and predicted dataframes



    for indexI, rowI in predicted.iterrows():
        for indexR, rowR in real.iterrows():
            #Check if the id and the text are the same
            if rowI.Id == rowR.Id:
                textTag = {'real': eval(rowR['Tags']), 'predicted': eval(rowI['Tags'])}
                df = detect_and_classify_texts(textTag, df)
                break


    #Calculate precision, recall, F1 and accuracy
    df['Precision'] = (df['Ca'] + 0.5 * df['Pa']) / (df['Ca'] + df['Ia'] + df['Pa'] + df['Sa'])
    df['Recall'] = (df['Ca'] + 0.5 * df['Pa']) / (df['Ca'] + df['Ia'] + df['Pa'] + df['Ma'])
    df['F1'] = 2 * (df['Precision'] * df['Recall']) / (df['Precision'] + df['Recall'])
    df['Accuracy'] = (df['Ca'] + 0.5 * df['Pa']) / (df['Ca'] + df['Ia'] + df['Pa'] + df['Ma'] + df['Sa'])

    #Delete rows where Ca,Ia, Pa, Ma and Sa are all 0
    df = df[(df.T != 0).any()]

    #Fill the NaN values with 1
    df = df.fillna(1)

    for row in df.index:
        if df.loc[row, 'Ca'] == 0 and df.loc[row, 'Pa'] == 0 and df.loc[row, 'Ia'] == 0 and df.loc[row, 'Ma'] == 0 and df.loc[row, 'Sa'] == 0:
            df = df.drop(row)

    precision = (df['Ca'].sum() + 0.5 * df['Pa'].sum()) / (df['Ca'].sum() + df['Ia'].sum() + df['Pa'].sum() + df['Sa'].sum())
    recall = (df['Ca'].sum() + 0.5 * df['Pa'].sum()) / (df['Ca'].sum() + df['Ia'].sum() + df['Pa'].sum() + df['Ma'].sum())
    F1 = 2 * (precision * recall) / (precision + recall)
    accuracy = (df['Ca'].sum() + 0.5 * df['Pa'].sum()) / (df['Ca'].sum() + df['Ia'].sum() + df['Pa'].sum() + df['Ma'].sum() + df['Sa'].sum())

    #Get the average metrics of each dataframe
    infoMetrics = [{'Precision': precision, 'Recall': recall, 'F1': F1, 'Accuracy': accuracy}]

    return [df, infoMetrics]


def score(solution: pd.DataFrame, submission: pd.DataFrame, row_id_column_name: str) -> float:
    '''
    TODO: Document your metric here. This docstring will be shown when selecting the metric on Kaggle.
    The docstring must be fewer than 8,000 characters long.

    TODO: Add unit tests. We recommend using doctests so your tests double as usage demonstrations for competition hosts.
    https://docs.python.org/3/library/doctest.html
    The metrics code can be downloaded and run locally with the solution and submission CSVs as input.
    '''

    df, metrics = eval_dataset(solution, submission, catList)

    # Delete the row ID column, which Kaggle's system uses to align the solution and submission before passing these dataframes to score().
    del solution[row_id_column_name]
    del submission[row_id_column_name]

    # TODO: adapt or remove this check depending on what data types make sense for your metric
    '''
    for col in submission.columns:
        if not pandas.api.types.is_numeric_dtype(submission[col]):
            raise ParticipantVisibleError(f'Submission column {col} must be a number')
    '''

    # TODO: add additional checks appropriate for your metric. Common things to check include:
    # Non-negative inputs, the wrong number of columns in the submission, values that should be restricted to a range, etc.
    # The more errors you tag as participant visible, the easier it will be for participants to debug their submissions.

    #Return the metric
    return metrics[0]['F1']