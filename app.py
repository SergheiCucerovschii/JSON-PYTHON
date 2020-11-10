import json

def menu(title, options):
    print(f'##### {title:^15} #####')
    for k in options:
        print(f'{k}. {options[k]}')
    print(f'##### {"Choose Option":^15} #####')

    selected = int(input('>>'))
    if selected not in options:
        print('Wrong option!')
    return selected


def loadEventData():
    file = open("data/event.json")
    data = json.load(file)
    return data

def printEvent(data):
    print("#"*30)
    print(f"Event: {data['title']}")
    print(f"Data: {data['date']}")
    print(f"Guests: {len(data['guests'])}")
    print("#"*30)

def guestList(data):
    print(f"   GUESTS LIST  [PYCON 2020]")
    i = 0
    while i in range(len(data['guests'])):
        for g in data['guests']:
            i += 1
            print(f"{i:>10}. {g}")


def inviteGuest(data):
    name = input("Enter guest name: ").capitalize()
    data["guests"].append(name)
    return data

def removeGuest(data):
    name = input("Enter the name of the guest you want to remove: ").capitalize()
    if name not in data['guests']:
        print("There is no such guest!!" )
    else:
        data['guests'].remove(name)
    return data

def saveData(data):
    file = open("data/event.json", "w")
    json.dump(data,file)
    file.close()




##################################################
while True:
    result = menu('Main', {
        1: 'View all guests',
        2: 'Add guest',
        3: 'Remove guest',
        0: 'Exit'
    })

    if result == 1:
        data = loadEventData()
        data = guestList(data)

    if result == 2:
        data = loadEventData()
        data = inviteGuest(data)
        saveData(data)
    if result == 3:
        data = loadEventData()
        data = removeGuest(data)
        saveData(data)
    if result == 0:
        print("Thank you!")
        break
