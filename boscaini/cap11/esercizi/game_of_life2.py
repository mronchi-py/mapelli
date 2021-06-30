import tkinter, random, copy

N = 20 # Dimensione della matrice, numero di colonne = numero di righe
DEAD, ALIVE = 0, 1
SIZE = 30 # Dimensione della cella in pixel
DELAY = 500 # Intervallo in millisecondi tra uno step e il successivo

def init_matrix(n):
    '''Imposta in una matrice n celle allo stato ALIVE, vivo'''
    matrix = []

    for x in range(N): # Crea la matrice di riferimenti con valori DEAD
        row = []

        for y in range(N):
            row.append(DEAD)

        matrix.append(row)

    while n > 0:
        x = random.randint(0, N - 1) 
        y = random.randint(0, N - 1)
        
        if matrix[x][y] == DEAD: # Se la cella è morta cambia il suo stato
            matrix[x][y] = ALIVE
            n -= 1 # Ne ho una in meno da impostare come viva

    return matrix

def count_neighbors(matrix, x, y):
    '''Ritorna il numero di vicini ALIVE della cella di coordinate (x=col, y=row)'''
    count = 0
    neighbors = [(x-1, y-1), (x, y-1), (x+1, y-1), # Coordinate delle 8 celle sopra,
                 (x-1, y), (x+1, y),                             # laterali
                 (x-1, y+1), (x, y+1), (x+1, y+1)]     # e sotto la cella considerata    

    for x, y in neighbors:
        if x >= 0 and x < N and y >= 0 and y < N: # Se x e y sono validi
            if matrix[x][y] >= ALIVE:
                count += 1

    return count        
    
def draw_matrix(matrix, canvas):
    '''Disegna una data matrice sul canvas'''
    for x in range(N):
        for y in range(N):
            color = cell_color(matrix[x][y])
            canvas.create_rectangle(x*SIZE, y*SIZE, x*SIZE + SIZE, y*SIZE + SIZE,
                                    width=1, outline="lightgrey", fill=color)

def cell_color(age):
    color = "white", "red", "red3", "red4", "brown"
    index_color = min(age, len(color) - 1)
    return color[index_color]

def print_matrix(matrix):
    '''Stampa una data matrice nel terminale'''
    for y in range(N):
        for x in range(N):
            print(matrix[x][y], end=" ")
        print("\n")
    print("\n")

def transition(matrix):
    '''Data una matrice, ritorna la nuova matrice che si ottiene
    dopo aver applicato alle celle le 4 regole del gioco'''
    next_matrix = copy.deepcopy(matrix) # Crea un copia a se stante della matrice    

    for x in range(N):
        for y in range(N):
            n_neighbors = count_neighbors(matrix, x, y) # Considera la matrice corrente

            if n_neighbors < 2 or n_neighbors > 3: #...per calcolare quella successiva
                next_matrix[x][y] = DEAD
            elif n_neighbors == 3 and matrix[x][y] == DEAD:
                next_matrix[x][y] = ALIVE
            elif matrix[x][y] >= ALIVE:
                next_matrix[x][y] += 1

    return next_matrix

def next_step(event=None):
    '''Effettua il prossimo step del gioco'''
    global matrix # Così la funzione può modificare la matrice globale
    #print_matrix(matrix)
    draw_matrix(matrix, canvas) # Disegna la matrice
    matrix = transition(matrix) # e passa a quella successiva
    root.after(DELAY, next_step) # Dopo l'intervallo next_step() verrà rieseguita

if __name__ == "__main__":    
    matrix = init_matrix(n=200) # Inizializza la matrice con un certo numero di celle ALIVE
    root = tkinter.Tk()
    root.title("Game of life")
    root.geometry("{}x{}".format(N*SIZE, N*SIZE)) # Dimensiona la finestra
    canvas = tkinter.Canvas(root) # Recupera il canvas associato alla finestra
    canvas.pack(fill=tkinter.BOTH, expand=1)
    next_step() # Inizia il gioco
    root.mainloop()
