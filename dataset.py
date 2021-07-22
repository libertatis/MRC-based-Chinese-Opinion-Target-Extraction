from paddlenlp.datasets import load_dataset
from paddlenlp.datasets import MapDataset
from paddlenlp.datasets import DatasetBuilder


def create_dataset(data_name='dp', split='train'):

    assert isinstance(split, str), 'split must be str, it could be "train" or "test".'

    if split == 'train':
        is_test = False
    elif split == 'test':
        is_test = True
    else:
        raise ValueError('split must be "train" or "test".')

    dataset = load_dataset('cote', data_name, splits=[split], lazy=False)

    dataset_list = []
    for idx, example in enumerate(dataset):
        qid = 'qid' + str(idx)
        context = ''.join(example['tokens'])
        context = context.strip()
        question = '评价对象'
        if not is_test:
            answer = example['entity']

            answer_start = context.find(answer)
            if answer_start < 0:
                continue

            new_example = {
                'id': qid,
                'title': '',
                'context': context,
                'question': question,
                'answers': [answer],
                'answer_starts': [answer_start]
            }
        else:            
            new_example = {
                'id': qid,
                'title':'',
                'context': context,
                'question': question,
                'answers': [],
                'answer_starts': []
            }

        dataset_list.append(new_example)

    dataset = MapDataset(dataset_list)

    return dataset


class CoteDataset(DatasetBuilder):
    """TODO: 从本地tsv文件中创建数据集"""
    pass







