# Projeto — agente-aula · CLI de Notas

CLI de terminal para gerenciar as notas de uma disciplina: cadastro de alunos,
lançamento de três avaliações, cálculo de média ponderada e classificação da
situação final. Persistência em CSV local — sem banco de dados, sem rede.

Projeto acadêmico: o código será lido por alunos do 3º semestre. Clareza vale
mais que esperteza — prefira a solução óbvia à concisa.

## Stack e ambiente

- Python 3.12 · pytest · apenas biblioteca padrão (`csv`, `dataclasses`, `pathlib`).
- Windows nativo, PowerShell. Venv em `.venv`, na raiz do projeto.
- Não existe `pyproject.toml` nem `requirements.txt`. Se achar que precisa de um, pergunte antes de criar.

## Comandos

| O que | Comando |
| --- | --- |
| Rodar todos os testes | `.venv\Scripts\pytest -q` |
| Rodar um arquivo de teste | `.venv\Scripts\pytest tests\test_media.py` |
| Rodar a aplicação | `.venv\Scripts\python -m notas` |
| Ativar o venv | `.venv\Scripts\Activate.ps1` |

Chame sempre os executáveis de dentro do `.venv`. O `python` do sistema não
enxerga o pytest, e o `ModuleNotFoundError` que aparece nesse caso não diz
qual é a causa real.

## Estrutura

- `notas/` — pacote da aplicação, um módulo por responsabilidade
- `tests/` — testes pytest, um arquivo por módulo de `notas/`
- CSV de dados fica na raiz e **não** vai para o git

## Regras de negócio

Vêm da especificação da disciplina. Não invente variações nem "melhore" os limites.

- Três avaliações por aluno, com pesos **3, 3 e 4**.
- Média ponderada arredondada em uma casa decimal.
- Situação: `>= 7` aprovado · `>= 5` e `< 7` exame · `< 5` reprovado.
- Aluno identificado pela matrícula, que é única. Matrícula repetida é erro.

## Convenções

- Um módulo por responsabilidade — não concentre tudo em um arquivo só.
- Nomes de variáveis, funções e mensagens ao usuário em português.
- Toda função pública tem docstring e pelo menos um teste.
- Ao abrir ou gravar CSV, use sempre `encoding="utf-8"` e `newline=""`.
  Sem isso, no Windows os nomes com acento quebram e cada linha vem duplicada.

## Nunca

- Não versionar dados de alunos reais.
- Não instalar dependência sem me perguntar antes.
- Não escrever chave de API em nenhum arquivo do projeto.
- Não apagar nem reescrever testes existentes para fazê-los passar.