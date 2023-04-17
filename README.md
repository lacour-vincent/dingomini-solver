# Dingomini

Dingomini, un casse-tête de 9 pièces chacune composée de 4 couleurs. Un jeu créé par Jacky Bonnet.

**Composition :** 9 pièces carrées différentes de 4 cases chacune.<br/>
**Règle** : Prendre les pièces carrées et composer les figures géométriques proprosées.<br/>
**Règle d'or** : Pour chaque figure réalisée, on ne doit jamais voir 2 fois la même couleur sur les lignes, les colonnes ou des diagonales.<br/>

## Figures

### Le petit carré

Composé de 4 pièces (2 diagonales) :

```
##|##
##|##
-- --
##|##
##|##
```

### Le rectangle

Composé de 6 pièces (4 diagonales) :

```
##|##|##
##|##|##
-- -- --
##|##|##
##|##|##
```

### Le grand carré

Composé de 9 pièces (2 diagonales) :

```
##|##|##
##|##|##
-- -- --
##|##|##
##|##|##
-- -- --
##|##|##
##|##|##
```

## Requirements

- (pyenv)[https://github.com/pyenv/pyenv]
- (poetry)[https://python-poetry.org/]

## Install

```bash
pyenv install 3.9
pyenv local 3.9
poetry install
```

## Run

```bash
bash bin/run-main.sh
bash bin/run-test.sh
```

## Crédits

Tous droits réservées © : Jacky Bonnet - 06 32 97 23 88
