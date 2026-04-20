import random
import time

# ───── Constantes de difficulté ─────
NIVEAUX = {
    "1": {"nom": "Facile",   "min": 1,   "max": 50,   "essais": 10},
    "2": {"nom": "Moyen",    "min": 1,   "max": 100,  "essais": 7},
    "3": {"nom": "Difficile","min": 1,   "max": 500,  "essais": 5},
    "4": {"nom": "Expert",   "min": 1,   "max": 1000, "essais": 5},
}

def choisir_niveau():
    """Affiche le menu de sélection du niveau"""
    print("\n🎯 Choisis un niveau :")
    for key, val in NIVEAUX.items():
        print(f"  {key}. {val['nom']:10s} ({val['min']}-{val['max']}, {val['essais']} essais)")

    while True:
        choix = input("\n  Ton choix (1-4) : ").strip()
        if choix in NIVEAUX:
            return NIVEAUX[choix]
        print("  ❌ Choix invalide.")

def indice(secret, guess):
    """Retourne un indice chaud/froid selon la proximité"""
    diff = abs(secret - guess)
    if diff == 0:
        return "🎯 EXACT !"
    elif diff <= 5:
        return "🔥 Brûlant !"
    elif diff <= 15:
        return "♨️  Chaud"
    elif diff <= 30:
        return "🌡️  Tiède"
    elif diff <= 60:
        return "❄️  Froid"
    else:
        return "🧊 Glacial"

def jouer_manche(niveau, pseudo):
    """Lance une manche et retourne le nombre d'essais utilisés (0 si perdu)"""
    MIN, MAX = niveau["min"], niveau["max"]
    MAX_ESSAIS = niveau["essais"]
    secret = random.randint(MIN, MAX)

    print(f"\n🤫 J'ai choisi un nombre entre {MIN} et {MAX}.")
    print(f"   Tu as {MAX_ESSAIS} essais. Bonne chance {pseudo} !\n")

    for essai in range(1, MAX_ESSAIS + 1):
        print(f"  Essai {essai}/{MAX_ESSAIS}")
        try:
            guess = int(input(f"  Ton nombre ({MIN}-{MAX}) : "))
        except ValueError:
            print("  ❌ Entre un nombre entier.")
            continue

        hint = indice(secret, guess)
        print(f"  → {hint}", end="  ")

        if guess == secret:
            print(f"\n✅ Bravo {pseudo} ! Trouvé en {essai} essai(s) !")
            return essai
        elif guess < secret:
            print("C'est plus grand !")
        else:
            print("C'est plus petit !")

    print(f"\n💀 Perdu ! Le nombre était {secret}.")
    return 0

def afficher_scores(historique):
    """Affiche le tableau des scores"""
    if not historique:
        return
    print("\n📊 Historique des parties :")
    print(f"  {'Joueur':<15} {'Niveau':<12} {'Essais'}")
    print("  " + "-" * 35)
    for h in historique:
        essais = str(h['essais']) if h['essais'] > 0 else "Perdu"
        print(f"  {h['joueur']:<15} {h['niveau']:<12} {essais}")

def menu():
    print("╔═══════════════════════════════╗")
    print("║    DEVINETTE DE NOMBRES 🔢     ║")
    print("╚═══════════════════════════════╝")

    pseudo = input("\n  Ton pseudo : ").strip() or "Joueur"
    historique = []

    while True:
        print(f"\n  Bonjour {pseudo} !")
        print("  1. Jouer")
        print("  2. Voir les scores")
        print("  3. Quitter")

        choix = input("\n  Ton choix : ").strip()

        if choix == "1":
            niveau = choisir_niveau()
            essais = jouer_manche(niveau, pseudo)
            historique.append({
                "joueur": pseudo,
                "niveau": niveau["nom"],
                "essais": essais
            })

            rejouer = input("\n  Rejouer ? (o/n) : ").lower()
            if rejouer != "o":
                afficher_scores(historique)
                print(f"\n👋 À bientôt {pseudo} !")
                break

        elif choix == "2":
            afficher_scores(historique)

        elif choix == "3":
            afficher_scores(historique)
            print(f"\n👋 À bientôt {pseudo} !")
            break

        else:
            print("  ❌ Choix invalide.")

if __name__ == "__main__":
    menu()
