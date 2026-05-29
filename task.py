import numpy as np

# Controlla il file readme.md per i dettagli su ciascun sub-task

def prodotto_scalare(v1: list, v2: list) -> float:
    """Sub-task 1: Prodotto Scalare."""

    arr1 = np.array(v1)
    arr2 = np.array(v2)

    if arr1.shape != arr2.shape:
        raise ValueError("I due vettori devono avere la stessa lunghezza")

    return float(np.dot(arr1, arr2))


# --- INPUT UTENTE ---
v1 = list(map(float, input("Inserisci il primo vettore (numeri separati da spazio): ").split()))
v2 = list(map(float, input("Inserisci il secondo vettore (numeri separati da spazio): ").split()))

# --- CALCOLO ---
try:
    risultato = prodotto_scalare(v1, v2)

    print("Prodotto scalare:", risultato)
except ValueError as e:
    print("Errore:", e)

    pass

def rango_matrice(m: list) -> int:
    """Sub-task 2: Calcola il rango di una matrice."""

    matrice = np.array(m)
    return int(np.linalg.matrix_rank(matrice))


def leggi_matrice():
    print("Inserisci il numero di righe:")
    righe = int(input())

    print("Inserisci il numero di colonne:")
    colonne = int(input())

    matrice = []

    print("Inserisci gli elementi della matrice riga per riga:")

    for i in range(righe):
        while True:
            riga = input(f"Riga {i + 1} (separa i numeri con spazio): ").split()
            if len(riga) != colonne:
                print("Numero di elementi errato, riprova.")
            else:

                matrice.append([float(x) for x in riga])
                break

    return matrice

if __name__ == "__main__":
   m = leggi_matrice()

   rango = rango_matrice(m)

   print("\nLa matrice inserita è:")
   for r in m:
       print(r)

   print(f"\nIl rango della matrice è: {rango}")

pass

def risolvi_sistema_lineare(A: list, b: list) -> np.ndarray:
    """Sub-task 3: Risolvere un Sistema Lineare."""
    pass

def correlazione_matrici(m1: list, m2: list) -> np.ndarray:
    """Sub-task 4: Correlazione tra Matrici 2x2."""
    pass

def operazioni_elemento_per_elemento(v1: list) -> tuple:
    """Sub-task 5: Restituisce (seno, coseno, arcoseno, arcocoseno) elemento per elemento calcolati sul primo array."""
    pass


def main():
    print("Sub-task 1:", prodotto_scalare([1, 2, 3], [4, 5, 6]))
    print("Sub-task 1:", rango_matrice([[1, 2], [3, 4]]))
    print("Sub-task 3:", risolvi_sistema_lineare([[2, 1], [1, 3]], [5, 7]))
    print("Sub-task 4:", correlazione_matrici([[1, 2], [3, 4]], [[2, 4], [6, 8]]))
    print("Sub-task 5:", operazioni_elemento_per_elemento([0, 0.5, 1, -0.5]))

if __name__ == "__main__":
    main()
