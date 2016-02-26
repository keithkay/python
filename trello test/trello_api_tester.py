# test of trello python integration
# pypi page: 
# documentation: https://pythonhosted.org/trello/index.html

from trello import TrelloApi
myTrello = TrelloApi("5c0d5de81fad5b32bb71379cba2f7777")

token = myTrello.get_token_url('My App', expires='30days', write_access=True)

