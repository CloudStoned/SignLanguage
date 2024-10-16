import numpy as np
import json

labels_dict = {
    0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9', 10: '10',
    11: 'A', 12: 'B', 13: 'C', 14: 'D', 15: 'E', 16: 'F', 17: 'G', 18: 'H', 19: 'I', 20: 'J',
    21: 'K', 22: 'L', 23: 'M', 24: 'N', 25: 'O', 26: 'P', 27: 'Q', 28: 'R', 29: 'S', 30: 'T',
    31: 'U', 32: 'V', 33: 'W', 34: 'X', 35: 'Y', 36: 'Z'
}

with open('CLASSES.json', 'w') as json_file:
    json.dump(labels_dict, json_file)