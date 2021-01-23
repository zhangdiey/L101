import random

random.seed(0)

with open('scan_data/train_raw.txt','r') as source:
    data = [ (random.random(), line) for line in source ]
data.sort()

data_size = len(data)
train_data = data[:int(data_size * 0.9)]
val_data = data[int(data_size * 0.9):]

with open('scan_data/test_raw.txt','r') as source:
    test_data = source.readlines()

with open('scan_data/src_train.txt','w+') as src_train:
    with open('scan_data/tgt_train.txt','w+') as tgt_train:
        mapping = {'src': src_train, 'tgt': tgt_train}
        for _, line in train_data:
            target = 'src'
            for tok in line.strip().split(sep=' '):
                if tok == 'IN:':
                    continue
                elif tok == "OUT:":
                    mapping['src'].write('\n')
                    target = 'tgt'
                else:
                    mapping[target].write(tok+' ')
            mapping['tgt'].write('\n')

with open('scan_data/src_val.txt','w+') as src_val:
    with open('scan_data/tgt_val.txt','w+') as tgt_val:
        mapping = {'src': src_val, 'tgt': tgt_val}
        for _, line in val_data:
            target = 'src'
            for tok in line.strip().split(sep=' '):
                if tok == 'IN:':
                    continue
                elif tok == "OUT:":
                    mapping['src'].write('\n')
                    target = 'tgt'
                else:
                    mapping[target].write(tok+' ')
            mapping['tgt'].write('\n')

with open('scan_data/src_tst.txt','w+') as src_tst:
    with open('scan_data/tgt_tst.txt','w+') as tgt_tst:
        mapping = {'src': src_tst, 'tgt': tgt_tst}
        for line in test_data:
            target = 'src'
            for tok in line.strip().split(sep=' '):
                if tok == 'IN:':
                    continue
                elif tok == "OUT:":
                    mapping['src'].write('\n')
                    target = 'tgt'
                else:
                    mapping[target].write(tok+' ')
            mapping['tgt'].write('\n')