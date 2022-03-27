import requests

from pprint import pprint


def search_hero_stats(name: str):
    TOKEN = '2619421814940190'
    method = 'search'
    url = f"https://superheroapi.com/api/{TOKEN}/{method}/{name}"
    response = requests.get(url)
    intelligence = response.json()['results'][0]['powerstats']['intelligence']
    return intelligence


def who_is_genius(list_hero):
    max_value = 0
    winner = ''
    for hero in list_hero:
        if int(search_hero_stats(hero)) > max_value:
            max_value = int(search_hero_stats(hero))
            winner = hero
    return f'Самый умный супергерой - {winner}. Intelligence = {max_value}'

if __name__ == '__main__':
    heroes = ['Hulk', 'Captain America', 'Thanos']
    print(who_is_genius(heroes))
    # print(search_hero_stats("Captain America"))
    # print(search_hero_stats("Thanos"))
    # print(search_hero_stats("Hulk"))