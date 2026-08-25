"""Ponto de entrada: `python -m notas`."""

from .armazenamento import carregar, salvar
from .interface import menu


def main():
    """Carregar os dados e iniciar o menu interativo da CLI."""
    turma = carregar()
    try:
        menu(turma)
    except KeyboardInterrupt:
        salvar(turma)
        print("\nDados salvos. Ate logo!")


if __name__ == "__main__":
    main()
