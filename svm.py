from sklearn.svm import SVC
import warnings
warnings.filterwarnings("ignore")

trainingdata = 'a1a.txt'
testdata = 'a1a.t'
trainingx = []
trainingy = []
testx = []
testy = []
trainingfile = open(trainingdata, 'r')
testfile = open(testdata, 'r')

def readLine(x, y, file):
    line = file.readline()
    if len(line) == 0:
        return False;
    y.append(float(line[0:line.index(" ")]))
    line = line[line.index(" ") + 1:]
    line = line.split()
    listToAdd = []
    for i in line:
        i = i.split(":")
        # use i[0] for a1a/a2a etc., but this may have to change based
        # on input
        listToAdd.append(float(i[0]))
    x.append(listToAdd)
    while len(listToAdd) != 14:
        listToAdd.append(0)
    return True;

while readLine(trainingx, trainingy, trainingfile):
    readLine(trainingx, trainingy, trainingfile);


while readLine(testx, testy, testfile):
    readLine(testx, testy, testfile);

model = SVC().fit(trainingx, trainingy)
##
result = model.predict(testx)
correct = 0
incorrect = 0
for i in range(len(result)):
    if result[i] != testy[i]:
        incorrect += 1
    else:
        correct += 1

print("number correctly predicted: ", correct)
print("total predictions made: ", correct + incorrect)

