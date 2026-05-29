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

    # Conversione in array NumPy
    A_np = np.array(A, dtype=float)
    b_np = np.array(b, dtype=float)

    # Verifica che la matrice sia quadrata
    if A_np.shape[0] != A_np.shape[1]:
        raise ValueError("La matrice A deve essere quadrata")

    # Verifica compatibilità dimensioni
    if A_np.shape[0] != b_np.shape[0]:
        raise ValueError("Le dimensioni di A e b non sono compatibili")

    # Risoluzione del sistema
    try:
        x = np.linalg.solve(A_np, b_np)
    except np.linalg.LinAlgError:

        raise ValueError("Il sistema non ha soluzione unica (matrice singolare)")
        return None

        return x

    # Input utente
    n = int(input("Inserisci la dimensione della matrice (n): "))

    print("Inserisci la matrice A (riga per riga, valori separati da spazio):")
    A = []
    for i in range(n):
        riga = list(map(float, input().split()))
        A.append(riga)

    print("Inserisci il vettore b (valori separati da spazio):")
    b = list(map(float, input().split()))

    # Calcolo soluzione
    soluzione = risolvi_sistema_lineare(A, b)

    print("Soluzione:", soluzione)

    pass

def correlazione_matrici(m1: list, m2: list) -> np.ndarray:
    """Sub-task 4: Correlazione tra Matrici 2x2."""

    # Conversione in array NumPy
    a = np.array(m1)
    b = np.array(m2)

    # Appiattimento (flatten)
    a_flat = a.flatten()
    b_flat = b.flatten()

    # Calcolo correlazione (Pearson)
    return np.corrcoef(a_flat, b_flat)


# Input matrici dall'utente
print("Inserisci i valori della prima matrice 2x2:")
m1 = []
for i in range(2):
    riga = list(map(float, input(f"Riga {i + 1} (2 valori separati da spazio): ").split()))
    m1.append(riga)

    print("\nInserisci i valori della seconda matrice 2x2:")
    m2 = []
    for i in range(2):
        riga = list(map(float, input(f"Riga {i + 1} (2 valori separati da spazio): ").split()))
        m2.append(riga)

    # Calcolo e stampa risultato
    risultato = correlazione_matrici(m1, m2)

    print("\nMatrice di correlazione:")
    print(risultato)

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
