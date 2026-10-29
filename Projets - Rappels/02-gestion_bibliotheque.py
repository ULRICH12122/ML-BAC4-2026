
# Gestion d'une petite bibliotheque

bibliotheque = []


# Fonction pour ajouter un livre
def ajouter_livre(titre, auteur, editeur):
    livre = {
        "titre": titre,
        "auteur": auteur,
        "editeur": editeur
    }

    bibliotheque.append(livre)
    print("Livre ajoute avec succes !")


# Fonction pour afficher les livres
def afficher_livres():
    if len(bibliotheque) == 0:
        print("La bibliotheque est vide.")
    else:
        for livre in bibliotheque:
            print("--------------------")
            print("Titre :", livre["titre"])
            print("Auteur :", livre["auteur"])
            print("Editeur :", livre["editeur"])

            if livre.get("emprunteur") is None:
                print("Statut : Disponible")
            else:
                print("Emprunte par :", livre["emprunteur"])


# Fonction pour emprunter un livre
def emprunter_livre(titre, emprunteur):
    for livre in bibliotheque:
        if livre["titre"] == titre:
            if livre.get("emprunteur") is None:
                livre["emprunteur"] = emprunteur
                print("Livre emprunte avec succes !")
            else:
                print("Ce livre est deja emprunte.")
            return

    print("Livre introuvable.")


# Fonction pour retourner un livre
def retourner_livre(titre):
    for livre in bibliotheque:
        if livre["titre"] == titre:
            if livre.get("emprunteur") is not None:
                del livre["emprunteur"]
                print("Livre retourne avec succes !")
            else:
                print("Ce livre n'est pas emprunte.")
            return

    print("Livre introuvable.")


# Fonction pour supprimer un livre
def supprimer_livre(titre):
    for livre in bibliotheque:
        if livre["titre"] == titre:
            bibliotheque.remove(livre)
            print("Livre supprime avec succes !")
            return

    print("Livre introuvable.")


# Menu principal
while True:
    print("\n===== MENU BIBLIOTHEQUE =====")
    print("1. Ajouter un livre")
    print("2. Afficher les livres")
    print("3. Emprunter un livre")
    print("4. Retourner un livre")
    print("5. Supprimer un livre")
    print("6. Quitter")

    choix = input("Entrez votre choix : ")

    if choix == "1":
        titre = input("Titre du livre : ")
        auteur = input("Nom de l'auteur : ")
        editeur = input("Nom de l'editeur : ")

        ajouter_livre(titre, auteur, editeur)

    elif choix == "2":
        afficher_livres()

    elif choix == "3":
        titre = input("Titre du livre : ")
        emprunteur = input("Nom de l'emprunteur : ")

        emprunter_livre(titre, emprunteur)

    elif choix == "4":
        titre = input("Titre du livre : ")

        retourner_livre(titre)

    elif choix == "5":
        titre = input("Titre du livre : ")

        supprimer_livre(titre)

    elif choix == "6":
        print("Au revoir !")
        break

    else:
        print("Choix invalide. Reessayez.")
