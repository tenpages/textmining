print(__doc__)

import itertools
import numpy as np
import matplotlib.pyplot as plt

from sklearn import svm, datasets
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix


def plot_confusion_matrix(cm, classes,
                          normalize=False,
                          title='Confusion matrix',
                          cmap=plt.cm.Blues):
    """
    This function prints and plots the confusion matrix.
    Normalization can be applied by setting `normalize=True`.
    """
    if normalize:
        cm = cm.astype('float') / cm.sum(axis=1)[:, np.newaxis]
        print("Normalized confusion matrix")
    else:
        print('Confusion matrix, without normalization')

    print(cm)

    plt.imshow(cm, interpolation='nearest', cmap=cmap)
    plt.title(title)
    plt.colorbar()
    tick_marks = np.arange(len(classes))
    plt.xticks(tick_marks, classes, rotation=45)
    plt.yticks(tick_marks, classes)

    fmt = '.2f' if normalize else 'd'
    thresh = cm.max() / 2.
    for i, j in itertools.product(range(cm.shape[0]), range(cm.shape[1])):
        plt.text(j, i, format(cm[i, j], fmt),
                 horizontalalignment="center",
                 color="white" if cm[i, j] > thresh else "black")

    plt.tight_layout()
    plt.ylabel('True label')
    plt.xlabel('Predicted label')

# Compute confusion matrix
cnf_matrix = np.array(
[[4502, 676, 132, 169, 418, 253, 135 , 92, 143 ,120, 121 ,141, 384, 493,184, 286, 219 ,244, 293, 290],
 [2165, 3362,201,169,340,183,175,121,177, 86,139,146,512,385 ,250,328,274,260,239,207],
 [ 211, 69,844, 22, 40, 21, 21, 18, 16, 13, 67, 13, 57, 25  ,71, 30, 40, 50, 19, 27],
 [ 208, 60, 20,883, 36, 18, 21, 16, 17, 14, 24, 16, 47, 30  ,23, 36, 44, 29, 32, 11],
 [ 70, 10,5,3,156,8,5,4,7,5,6,3,8, 11,11,6, 18,5,8,8],
 [ 183, 43, 13,8, 17,590, 10,7, 10, 10,9, 10, 24, 44,19, 18, 14, 22, 28, 16],
 [ 153, 37,5, 12, 29,9,674,6, 17,6, 11, 19, 73, 22,21, 32, 20, 21, 13, 15],
 [ 110, 46, 11, 11, 16, 14, 15,622,9,8,8, 15, 68, 20,37, 25, 23, 28, 11, 15],
 [ 103, 45,8,6, 12,7,7, 16,610,8,8, 10, 55, 24,19, 34, 26, 21,9, 10],
 [ 136, 39,6, 10, 11,4,6,9,8,873,4,6, 22, 20, 9, 19, 12, 18,9,7],
 [ 124, 32, 49,8, 17, 10,9, 14, 14,6,654, 12, 34, 26,30, 19, 30, 22,9, 15],
 [ 81, 28, 17,8, 13,4, 13,7,8,4, 10,554, 33, 18,14, 14, 16,9, 11, 11],
 [ 928,390,106, 98, 93, 72,174,188,138, 48,110,148, 3615,152, 246,197,179,117, 97,142],
 [ 732,141, 20, 26, 56, 62, 21, 23, 25, 27, 12, 36, 61, 1417,33, 95, 48, 54, 86, 75],
 [ 205, 60, 40, 23, 38, 16, 26, 46, 25, 15, 38, 22, 95, 34,1451, 41, 58, 49, 30, 15],
 [ 237, 64, 21, 19, 52, 22, 24, 14, 28, 12, 18, 20, 56, 40,23, 1057, 30, 27, 24, 26],
 [ 169, 63, 21, 25, 54, 13, 17, 20, 22,8, 16, 21, 41, 30,36, 29,957, 18, 24, 21],
 [ 136, 38, 13, 14, 22, 12, 12, 13, 13, 11, 24,6, 25, 30,17, 19, 15,882, 14, 12],
 [ 149, 46,6, 11, 25, 14,5,9, 14,3,4,5, 17, 31,13, 16, 13,7,826, 14],
 [ 158, 30,6,3, 17, 14,7,4,5,2,3, 11, 14, 33,10, 16, 13, 11, 14,734]])
np.set_printoptions(precision=2)
class_names=list(range(0,20))
# Plot non-normalized confusion matrix
#plt.figure()
#plot_confusion_matrix(cnf_matrix, classes=class_names,
#                      title='Confusion matrix')

# Plot normalized confusion matrix
plt.figure()
plot_confusion_matrix(cnf_matrix, classes=class_names, normalize=True,
                      title='Normalized confusion matrix')
fig = plt.gcf()

fig.set_size_inches(18, 15)


fig.savefig("fig1.png")
