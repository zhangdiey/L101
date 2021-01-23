echo "default_train_np"
python eval.py predictions/gold_train_np.txt predictions/default_train_np.txt
echo "default_val_np"
python eval.py predictions/gold_val_np.txt predictions/default_val_np.txt
echo "default_tst_np"
python eval.py predictions/gold_tst.txt predictions/default_tst_np.txt
echo "default_train"
python eval.py predictions/gold_train.txt predictions/default_train.txt
echo "default_val"
python eval.py predictions/gold_val.txt predictions/default_val.txt
echo "default_tst"
python eval.py predictions/gold_tst.txt predictions/default_tst.txt
echo "default_glove_train"
python eval.py predictions/gold_train.txt predictions/default_glove_train.txt
echo "default_glove_val"
python eval.py predictions/gold_val.txt predictions/default_glove_val.txt
echo "default_glove_tst"
python eval.py predictions/gold_tst.txt predictions/default_glove_tst.txt