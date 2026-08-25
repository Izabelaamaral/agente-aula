# CLI de Notas

CLI de terminal para gerenciar as notas de uma disciplina: cadastro de alunos,
lançamento de três avaliações, cálculo de média ponderada (pesos 3, 3, 4) e
classificação da situação final. Os dados ficam em `alunos.csv` (local, sem
banco de dados, sem rede).

## Regras de negócio

- Três avaliações por aluno, com pesos **3, 3 e 4**.
- Média ponderada arredondada em **uma casa decimal**.
- Situação: `>= 7` → **Aprovado** · `>= 5` e `< 7` → **Exame** · `< 5` → **Reprovado**.
- Aluno identificado pela **matrícula** (única). Matrícula repetida é erro.

## Executar

```powershell
.venv\Scripts\python -m notas
```

ou, após ativar o venv:

```powershell
.venv\Scripts\Activate.ps1
python -m notas
```

## Exemplo completo

```
========================================
 MENU DE NOTAS
========================================
 1. Cadastrar aluno
 2. Listar turma
 3. Lancar notas
 4. Buscar aluno
 5. Salvar e sair
========================================
Opcao: 1
Matricula: 2024001
Nome: Ana Silva
Aluno 'Ana Silva' (matricula 2024001) cadastrado.

Opcao: 1
Matricula: 2024002
Nome: Beto Costa
Aluno 'Beto Costa' (matricula 2024002) cadastrado.

Opcao: 3
Matricula: 2024001
Nota 1: 7
Nota 2: 8
Nota 3: 9
Notas lancadas para 'Ana Silva' (2024001). Media: 8.1. Situacao: Aprovado

Opcao: 3
Matricula: 2024002
Nota 1: 4
Nota 2: 5
Nota 3: 4
Notas lancadas para 'Beto Costa' (2024002). Media: 4.4. Situacao: Reprovado

Opcao: 2
==============================================================================
TABELA DA TURMA
==============================================================================
2024001     Ana Silva                     N1=7.0 N2=8.0 N3=9.0 | Media: 8.1 | Aprovado
2024002     Beto Costa                      N1=4.0 N2=5.0 N3=4.0 | Media: 4.4 | Reprovado
==============================================================================

Opcao: 4
Matricula: 2024001
2024001     Ana Silva                     N1=7.0 N2=8.0 N3=9.0 | Media: 8.1 | Aprovado

Opcao: 5
Dados salvos. Ate logo!
```

## Testes

```powershell
.venv\Scripts\pytest -q
```

## Estrutura

```
notas/                 # pacote da aplicacao (um modulo por responsabilidade)
  __init__.py
  __main__.py          # ponto de entrada: python -m notas
  aluno.py             # entidade Aluno (dataclass)
  media.py             # media ponderada + classificacao de situacao
  comandos.py          # regras de negocio (sem acesso a arquivos)
  armazenamento.py     # persistencia CSV (utf-8, newline="")
  interface.py         # menu e formatacao (CLI)
tests/                 # um arquivo de teste por modulo
conftest.py            # raiz no sys.path do pytest (arquivo vazio)
alunos.csv             # dados (nao versionado)
```
