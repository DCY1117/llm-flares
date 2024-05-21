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
from sklearn.metrics import precision_score, recall_score, f1_score, accuracy_score


class ParticipantVisibleError(Exception):
    # If you want an error message to be shown to participants, you must raise the error as a ParticipantVisibleError
    # All other errors will only be shown to the competition host. This helps prevent unintentional leakage of solution data.
    pass


def eval_dataset(solution: pd.DataFrame, submission: pd.DataFrame):
    if list(solution['Id']) != list(submission['Id']):
        raise ParticipantVisibleError(f'The ID Column of the solution and submission do not match')
    y_test = list(solution['Reliability_Label'])
    y_hat = list(submission['Reliability_Label'])

    f1_score_value = f1_score(y_test, y_hat, average='macro')
    accuracy_value = accuracy_score(y_test, y_hat)
    precision_value = precision_score(y_test, y_hat, average='macro')
    recall_value = recall_score(y_test, y_hat, average='macro')
    metrics = {'F1': f1_score_value, 'Accuracy': accuracy_value, 'Precision': precision_value, 'Recall': recall_value}
    return metrics


def score(solution: pd.DataFrame, submission: pd.DataFrame, row_id_column_name: str) -> float:
    '''
    TODO: Document your metric here. This docstring will be shown when selecting the metric on Kaggle.
    The docstring must be fewer than 8,000 characters long.

    Accuracy, Precision, Recall, and F1 metrics calculated using the sklearn library.
    Precision, Recall, and F1 are calculated using the macro average method.
    Return F1 macro score
    '''
    metrics = eval_dataset(solution, submission)

    # Delete the row ID column, which Kaggle's system uses to align the solution and submission before passing these dataframes to score().
    del solution[row_id_column_name]
    del submission[row_id_column_name]

    #Return the metric
    return metrics['F1']