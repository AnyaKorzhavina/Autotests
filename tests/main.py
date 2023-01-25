import requests
import json

token = 'ad36816d99b9be4ebcbd247246f8bbd4'
response_post = requests.post('https://pokemonbattle.me:5000/pokemons', headers={'trainer_token': token},json={
    "name": "Джеки",
    "photo": "https://static.wikia.nocookie.net/pokemon/images/2/21/001Bulbasaur.png"
})

print(response_post.text)

response_put = requests.put('https://pokemonbattle.me:5000/pokemons', headers={'trainer_token': token},json={
    "pokemon_id": 3348,
    "name": "Lady",
    "photo": ""
})
print(response_put.text)

response_post_pokeball = requests.post('https://pokemonbattle.me:5000/trainers/add_pokeball', headers={'trainer_token': token},json={
   "pokemon_id": "3350"
})
print(response_post_pokeball.text)
