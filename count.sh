for keyword in I_JUMP I_WALK I_RUN I_LOOK
do
    for file in gold_tst.txt default_tst_np.txt default_tst.txt default_glove_tst.txt
    do
        echo $keyword $file
        python count.py predictions/$file $keyword
    done
done