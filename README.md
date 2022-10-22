# GG App - OpenAPI 3.0

This is the OpenAPI 3.0 Documentation of the GG App.

- [See the page here](https://domkoc.github.io/GGApp-OpenAPI)

## Communication sequences:

### Starting a lobby:
1. POST - /lobby/new
2. POST - /lobby/{lobby_id}/start

### Joining a lobby:
1. POST - /lobby/join

### Playing a game:
1. GET - /game/{lobby_id}
2. GET - /game/{lobby_id}/round
3. POST - /game/{lobby_id}/round
4. GET - /game/{lobby_id}
5. 2-4 repeating ...
6. POST - /scoreboard

### Viewing the scoreboard:
1. GET - /scoreboard
