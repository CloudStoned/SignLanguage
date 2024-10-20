import pickle

from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import numpy as np

def show_data(data):
    print(data['labels'])
    print(data['data'])

def train(data_dict):
    data = np.asarray(data_dict['data'])
    labels = np.asarray(data_dict['labels'])

    x_train, x_test, y_train, y_test = train_test_split(data, labels, test_size=0.2, shuffle=True, stratify=labels)

    model = RandomForestClassifier()

    model.fit(x_train, y_train)

    y_predict = model.predict(x_test)

    score = accuracy_score(y_predict, y_test)

    print('{}% of samples were classified correctly !'.format(score * 100))

    model_name = 'alph_model'
    f = open(f'{model_name}.p', 'wb')
    pickle.dump({'model': model}, f)
    print("Model Created")
    f.close()

if __name__ == '__main__':
    data_dict = pickle.load(open('ALPH_DATA.pickle', 'rb'))
    # show_data(data_dict)
    train(data_dict)
