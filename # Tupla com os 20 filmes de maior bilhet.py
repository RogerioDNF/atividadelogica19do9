# Tupla com os 20 filmes de maior bilheteria (2023 atualizado)
filmes = (
    "Avatar",
    "Vingadores: Ultimato",
    "Titanic",
    "Star Wars: O Despertar da Força",
    "Vingadores: Guerra Infinita",
    "Jurassic World",
    "O Rei Leão",
    "Velozes & Furiosos 7",
    "Vingadores",
    "Frozen II",
    "Vingadores: Era de Ultron",
    "Black Panther",
    "Harry Potter e as Relíquias da Morte Parte 2",
    "Star Wars: Os Últimos Jedi",
    "Jurassic World: Reino Ameaçado",
    "Frozen",
    "A Bela e a Fera",
    "Os Incríveis 2",
    "A Bela e a Fera",
    "Minions"
)

print("🔹 Os 5 primeiros colocados são:")
print(filmes[:5])

print("\n🔹 Os últimos 4 colocados são:")
print(filmes[-4:])

print("\n🔹 Lista em ordem alfabética:")
print(sorted(filmes))

print(f"\n🔹 O filme Titanic está na {filmes.index('Titanic')+1}ª posição.")
