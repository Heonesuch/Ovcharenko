import datetime
def printTimeStamp(name):
    print('Овчаренко Иван Кожушко Андрей: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))



bis_sextus = lambda year: (not year % 4 and year % 100) or not year % 400

print(bis_sextus(int(input())))


