import random
import time

def lancer_de(nb_faces=6):
    """Simule le lancer d'un dé à nb_faces faces"""
    return random.randint(1, nb_faces)

def afficher_de(valeur):
    """Affiche une représentation visuelle du dé (1-6)"""
    faces = {
        1: ["┌─────┐", "│     │", "│  ●  │", "│     │", "└─────┘"],
        2: ["┌─────┐", "│ ●   │", "│     │", "│   ● │", "└─────┘"],
        3: ["┌─────┐", "│ ●   │", "│  ●  │", "│   ● │", "└─────┘"],
        4: ["┌─────┐", "│ ● ● │", "│     │", "│ ● ● │", "└─────┘"],
        5: ["┌─────┐", "│ ● ● │", "│  ●  │", "│ ● ● │", "└─────┘"],
        6: ["┌─────┐", "│ ● ● │", "│ ● ● │", "│ ● ● │", "└─────┘"],
    }
    if valeur in faces:
        for ligne in faces[valeur]:
            print("  " + ligne)
    else:
        print(f"  [ {valeur} ]")

def mode_solo():
    """Mode solo : lancer des dés et cumuler les points"""
    print("\n🎲 MODE SOLO — Lance le dé et cumule les points !")
    print("  Règle : tape STOP pour arrêter (mais si tu fais 1, tu perds tout !)\n")

    score_total = 0
    continuer = True

    while continuer:
        input("  Appuie sur Entrée pour lancer le dé...")
        print("  🎲 Lancement en cours", end="", flush=True)
        for _ in range(3):
            time.sleep(0.3)
            print(".", end="", flush=True)
        print()

        valeur = lancer_de()
        afficher_de(valeur)
        print(f"  Résultat : {valeur}")

        if valeur == 1:
            print("  💀 Tu as fait 1 ! Tu perds tous tes points de ce tour !")
            score_total = 0
            continuer = False
        else:
            score_total += valeur
            print(f"  ✅ Score actuel : {score_total}")
            choix = input("\n  Continuer ? (o = lancer / n = arrêter) : ").lower()
            if choix != "o":
                continuer = False

    print(f"\n🏁 Score final : {score_total} points")

def mode_duel():
    """Mode duel : deux joueurs s'affrontent sur N lancers"""
    print("\n⚔️  MODE DUEL — Chaque joueur lance le dé, le plus grand score gagne !\n")

    nom1 = input("  Nom du Joueur 1 : ").strip() or "Joueur 1"
    nom2 = input("  Nom du Joueur 2 : ").strip() or "Joueur 2"

    try:
        nb_lancers = int(input("  Nombre de lancers chacun (1-10) : "))
        nb_lancers = max(1, min(nb_lancers, 10))
    except ValueError:
        nb_lancers = 3
        print("  Valeur invalide, 3 lancers par défaut.")

    scores = {nom1: 0, nom2: 0}

    for i in range(1, nb_lancers + 1):
        print(f"\n--- Manche {i}/{nb_lancers} ---")
        for nom in [nom1, nom2]:
            input(f"  {nom}, appuie sur Entrée pour lancer...")
            val = lancer_de()
            afficher_de(val)
            print(f"  {nom} fait : {val}")
            scores[nom] += val

    print("\n📊 Scores finaux :")
    for nom, score in scores.items():
        print(f"  {nom} : {score} points")

    if scores[nom1] > scores[nom2]:
        print(f"\n🏆 {nom1} gagne !")
    elif scores[nom2] > scores[nom1]:
        print(f"\n🏆 {nom2} gagne !")
    else:
        print("\n🤝 Égalité !")

def menu():
    print("╔══════════════════════════╗")
    print("║      JEU DE DÉ 🎲        ║")
    print("╚══════════════════════════╝")

    while True:
        print("\n  1. Mode Solo (cumul de points)")
        print("  2. Mode Duel (2 joueurs)")
        print("  3. Quitter")

        choix = input("\n  Ton choix : ").strip()

        if choix == "1":
            mode_solo()
        elif choix == "2":
            mode_duel()
        elif choix == "3":
            print("\n👋 À bientôt !")
            break
        else:
            print("  ❌ Choix invalide.")

if __name__ == "__main__":
    menu()
