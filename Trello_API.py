import requests
import datetime
import configparser

config = configparser.ConfigParser()
config.read('trello_API.ini')
key = config['Authentication']['key']
token = config['Authentication']['token']


def create_board(board_name):
    url = "https://api.trello.com/1/boards/"
    query = {
        'key': key,
        'token': token,
        'name': board_name,
        'prefs_permissionLevel': 'public'
    }

    response = requests.request(
        "POST",
        url,
        params=query
    )
    board_id = response.json()["id"]
    return board_id


def create_list(board_id, list_name):
    url = "https://api.trello.com/1/lists"
    query = {
        'key': key,
        'token': token,
        'name': list_name,
        'idBoard': board_id
    }

    response = requests.request(
        "POST",
        url,
        params=query
    )
    list_id = response.json()["id"]
    return list_id


def create_card(list_id, name_card, due_card):
    url = "https://api.trello.com/1/cards"
    query = {
        'key': key,
        'token': token,
        'name': name_card,
        'due': due_card,
        'idList': list_id
    }

    response = requests.request(
        "POST",
        url,
        params=query
    )
    card_id = response.json()["id"]
    return card_id


def main():
    start_time_2 = datetime.datetime.strptime('25/06/2020', '%d/%m/%Y')
    start_time_1 = datetime.datetime.strptime('30/06/2020', '%d/%m/%Y')
    board_id = create_board("Học Python Hà Nội PYMI_HN2006")
    list_id_1 = create_list(board_id, "Thứ 3")
    list_id_2 = create_list(board_id, "Thứ 5")
    for i in range(1, 13):
        if i % 2 == 0:
            create_card(list_id_1, "Bài {}".format(i), due_card=start_time_1)
            start_time_1 += datetime.timedelta(days=7)
        else:
            create_card(list_id_2, "Bài {}".format(i), due_card=start_time_2)
            start_time_2 += datetime.timedelta(days=7)


if __name__ == "__main__":
    main()
