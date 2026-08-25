"""Entidade Aluno.

Identificado pela matricula (unica), com tres notas facultativas que ficam
None ate serem lancadas. A media e a situacao sao propriedades derivadas.
"""

from dataclasses import dataclass
from typing import Optional

from .media import calcular_media, classificar_situacao


@dataclass
class Aluno:
    """Representar um aluno e suas tres notas de avaliacao.

    Attributes
    ----------
    matricula : str
        Identificador unico.
    nome : str
        Nome completo.
    nota1, nota2, nota3 : float | None
        Notas das avaliacoes; None indica que ainda nao foram lancadas.
    """

    matricula: str
    nome: str
    nota1: Optional[float] = None
    nota2: Optional[float] = None
    nota3: Optional[float] = None

    @property
    def media(self) -> Optional[float]:
        """Media ponderada (uma casa decimal) ou None se faltar alguma nota."""
        if None in (self.nota1, self.nota2, self.nota3):
            return None
        return calcular_media(self.nota1, self.nota2, self.nota3)

    @property
    def situacao(self) -> Optional[str]:
        """Situacao final do aluno, ou None se nao for possivel calcular a media."""
        if self.media is None:
            return None
        return classificar_situacao(self.media)

    def tem_todas_as_notas(self) -> bool:
        """Devolver True quando as tres notas ja foram lancadas."""
        return self.nota1 is not None and self.nota2 is not None and self.nota3 is not None
