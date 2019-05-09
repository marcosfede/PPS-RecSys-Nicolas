#Metric: Recall

def recall(y_true, y_pred,average='binary'):
    """ 
    
    Recall: Ability of the classifier to find all the positive samples.
    The best value is 1 and the worst value is 0.
    
    Parameters
        y_true : 1d array-like, or label indicator array / sparse matrix
            Ground truth (correct) target values.
        y_pred : 1d array-like, or label indicator array / sparse matrix
            Estimated targets as returned by a classifier.
        average : string, [None, ‘binary’ (default), ‘micro’, ‘macro’, ‘samples’, ‘weighted’]
            This parameter is required for multiclass/multilabel targets. If None, the scores for each class are returned. Otherwise, this determines the type of averaging performed on the data:
            'binary': Only report results for the class specified by pos_label. This is applicable only if targets (y_{true,pred}) are binary.
            'micro': Calculate metrics globally by counting the total true positives, false negatives and false positives.
            'macro': Calculate metrics for each label, and find their unweighted mean. This does not take label imbalance into account.
            'weighted': Calculate metrics for each label, and find their average weighted by support (the number of true instances for each label). This alters ‘macro’ to account for label imbalance; it can result in an F-score that is not between precision and recall.
            'samples': Calculate metrics for each instance, and find their average (only meaningful for multilabel classification where this differs from accuracy_score).

    Returns
        recall : float (if average is not None) or array of float, shape = [n_unique_labels]
            Recall of the positive class in binary classification or weighted average of the recall of each class for the multiclass task.

    """
    pass