from sklearn.metrics import classification_report, confusion_matrix
from sklearn.metrics import f1_score
import numpy as np


def matthews_corr_coef(y_true, y_pred):
    cm = confusion_matrix(y_true, y_pred)
    TP, FP, FN, TN = cm[0][0], cm[0][1], cm[1][0], cm[1][1]
    return (TN * TP - FP * FN) / np.sqrt((TN + FN) * (FP + TP) * (TN + FP) * (FN + TP))


def evaluate_model(y_true, y_pred):
    n = y_true.shape[0]
    tp = np.sum((y_true == 1) & (y_pred == 1))
    fp = np.sum((y_true == 0) & (y_pred == 1))
    tn = np.sum((y_true == 0) & (y_pred == 0))
    fn = np.sum((y_true == 1) & (y_pred == 0))

    f1 = f1_score(y_true, y_pred)
    precision = tp / (tp + fp)
    recall = tp / (tp + fn)
    accuracy = np.sum(y_pred == y_true) / n

    mmc = matthews_corr_coef(y_true, y_pred)

    return {'f1': np.round(f1, decimals=3),
            'mmc': np.round(mmc, decimals=6),
            'acc': np.round(accuracy, decimals=3),
            'precision': np.round(precision, decimals=3),
            'recall': np.round(recall, decimals=3),
            'tp': tp,
            'fp': fp,
            'tn': tn,
            'fn': fn
            }


def confidence_interval(confidence, values):
    """Computes the confidence interval for the given set of values."""
    lower_p = (1.0 - confidence)/2
    upper_p = 1 - (1.0 - confidence)/2
    return np.percentile(values, lower_p * 100), np.percentile(values, upper_p * 100)
