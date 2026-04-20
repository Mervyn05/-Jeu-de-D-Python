# 🔢 Devinette de Nombres — Python

Jeu de devinette en console : trouve le nombre secret avant d'épuiser tes essais. 4 niveaux de difficulté et un système d'indices chaud/froid.

## 🎮 Fonctionnalités

- 4 niveaux : Facile / Moyen / Difficile / Expert
- Indices chaud/froid selon la proximité
- Historique des parties dans la session
- Gestion des erreurs de saisie

## ▶️ Lancer le projet

```bash
python devinette.py
```

## 💡 Concepts Python utilisés

| Concept | Utilisation |
|---|---|
| `random.randint()` | Générer le nombre secret |
| Fonctions | Découpage en `jouer_manche()`, `indice()`... |
| Dictionnaires | Niveaux et historique |
| Boucle `for` + `break` | Gestion des essais |
| Gestion d'exceptions | `try/except ValueError` |

## 📸 Aperçu

```
🤫 J'ai choisi un nombre entre 1 et 100.
   Tu as 7 essais. Bonne chance !

  Essai 1/7
  Ton nombre (1-100) : 50
  → ❄️  Froid  C'est plus grand !

  Essai 2/7
  Ton nombre (1-100) : 80
  → 🔥 Brûlant !  C'est plus petit !
```

## 👤 Auteur
Mervyn OBEN — BUT Informatique
