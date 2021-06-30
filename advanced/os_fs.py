"""
    Stampa i percorsi di file e directory
    contenute in una specifica directory
"""
import os


def print_dir(dirpath):
    """ Stampa i percorsi di file e directory
        contenute nella directory dirpath
    """
    for name in os.listdir(dirpath):
        # per evitare file nascosti
        if name.startswith('.'):
            continue
        print(os.path.join(dirpath, name))


def print_dir_tree(dirpath):
    """ Stampa i percorsi di tutti i file e directory
    contenuti, a qualsiasi livello, nella directory
    dirpath """
    for name in os.listdir(dirpath):
        # per evitare file nascosti
        if name.startswith('.'):
            continue
        pathname = os.path.join(dirpath, name)
        print(pathname)
        # se e' una directory
        if os.path.isdir(pathname):
            # chiama ricorsivamente la funzione
            print_dir_tree(pathname)


print_dir('e:\\tmp')
print("=" * 79)
print_dir_tree('e:\\tmp')
