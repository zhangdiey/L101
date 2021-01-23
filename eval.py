import sys
from nltk.translate.bleu_score import corpus_bleu
from nltk.metrics import *

path_to_gold = sys.argv[1]
path_to_pred = sys.argv[2]

candidates = []
references = []

with open(path_to_gold, 'r') as gold_f:
    gold = gold_f.readlines()
    gold_size = len(gold)
    with open(path_to_pred, 'r') as pred_f:
        pred = pred_f.readlines()
        pred_size = len(pred)
        if gold_size != pred_size:
            Exception()
        sent_tp = 0
        c_precison = 0
        c_recall = 0
        c_f = 0
        tp = 0
        fp = 0
        tn = 0
        fn = 0
        for i, gold_line in enumerate(gold):
            pred_line = pred[i].strip()
            gold_line = gold_line.strip()
            pred_set = set(pred_line.split())
            gold_set = set(gold_line.split())
            candidates.append(pred_line)
            references.append([gold_line])
            if 'I_JUMP' in gold_set:
                if 'I_JUMP' in pred_set:
                    tp += 1
                else:
                    fn += 1
            else:
                if 'I_JUMP' in pred_set:
                    fp += 1
                else:
                    tn += 1

            if precision(pred_set, gold_set):
                c_precison += precision(pred_set, gold_set)
            if recall(pred_set, gold_set):
                c_recall += recall(pred_set, gold_set)
            if f_measure(pred_set, gold_set):
                c_f += f_measure(pred_set, gold_set)
            if gold_line == pred_line:
                sent_tp += 1

if tp+fp:
    p = tp / (tp+fp)
else:
    p = 0.0
if tp+fn:
    r = tp / (tp+fn)
else:
    r = 0.0
if p+r:
    f1 = 2*r*p/(r+p)
else:
    f1 = 0.0

print('Sent-Level Acc', sent_tp/gold_size)
print('Average Precision', c_precison/gold_size)
print('Average Recall', c_recall/gold_size)
print('Average F1', c_f/gold_size)
print('New Primitive Precision', p)
print('New Primitive Recall', r)
print('New Primitive F1', f1)
print('BLEU', corpus_bleu(references, candidates))