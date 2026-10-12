# Teste técnico Sicredi - Erik Fontoura

## 1. Explicação Breve da Solução

Esta solução automatiza a leitura de solicitações de cadastro armazenadas em um arquivo JSON, seleciona os registros com status `APROVADO` e CPF preenchido e exporta os dados selecionados para um arquivo CSV.

O processamento foi organizado em funções para separar a leitura dos dados, a filtragem e a geração do arquivo de saída. A execução também registra mensagens de acompanhamento e erros em log.

O arquivo main, implementa uma versão bastante simplificada do Reframework da UIPath, baseado em uma máquina de estados, para controlar o processamento e erros durante execução.

Um registro é exportado quando atende aos seguintes critérios:

- O campo `status` é igual a `APROVADO`.
- O campo `cpf` está preenchido, sem espaços em branco.
- Os campos `id` e `nome` estão preenchidos.

Registros com status diferente de `APROVADO` ou com dados incompletos são registrados como avisos no log e não compoem o arquivo final.

Não é realizada validação dos dígitos verificadores do CPF; a verificação considera apenas o preenchimento do campo. Os nomes dos campos são considerados conforme aparecem no JSON: `id`, `nome`, `cpf` e `status`.

O arquivo de saída é `output/Aprovados.csv` e contém as colunas:

```csv
id,nome,cpf
```
O arquivo de log recebe um nome com data e hora para distinguir as execuções.

A solução utiliza `try/except` nas funções de leitura, filtragem e exportação para registrar falhas. Entre os cenários relevantes estão arquivo JSON ausente ou inválido, dados incompletos e falhas na gravação do CSV.

Em caso de erro, consulte o arquivo de log para identificar a etapa em que ocorreu o problema.

## 2. Pré-requisitos

- Python instalado.
- Não é necessário instalar bibliotecas adicionais. A solução utiliza módulos nativos do Python, como `json`, `csv`, `logging`, `datetime` e `pathlib`.

Mantenha a seguinte estrutura de diretórios:

```text
Teste Técnico_Erik Fontoura/
├── main.py
├── config.py
├── funcoes.py
├── README.md
├── solicitacoes.json
├── output/
│   └── Aprovados.csv
└── logs/
    └── <data_hora> Teste Técnico.txt
```

- `main.py`: coordena a execução da automação.
- `config.py`: define os caminhos dos arquivos de entrada e saída com `pathlib`, evitando caminhos absolutos vinculados a um usuário específico.
- `funcoes.py`: contém as funções de leitura do JSON, filtragem dos registros, geração do CSV e configuração dos logs.
- `solicitacoes.json`: arquivo de entrada com os registros.
- `output/Aprovados.csv`: arquivo de saída gerado pelo processamento.
- `logs/`: diretório destinado aos arquivos de log. O nome do arquivo inclui a data e a hora da execução.

**Importante:** as pastas `logs/` e `output/` devem existir antes da execução, pois os caminhos são definidos em `config.py`, mas não são criados automaticamente pelo código atual.

## 3. Instruções para executar o projeto

1. Confirme que o Python está instalado.
2. Mantenha `main.py`, `config.py`, `funcoes.py` e `solicitacoes.json` na pasta do projeto.
3. Confirme que as pastas `logs/` e `output/` existem.
4. Abra um terminal na pasta do projeto.
5. Execute:

```bash
python main.py
```



Após a execução, verifique o arquivo `output/Aprovados.csv` e o log correspondente na pasta `logs/`.

## 4. Premissas Adotadas

O arquivo main, implementa uma versão bastante simplificada do Reframework da UIPath, baseado em uma máquina de estados, para controlar o processamento e erros durante execução.


## 5. Decisões relevantes, como o separador utilizado no CSV
Foi utilizada a **vírgula (`,`) como delimitador**, por ser um separador amplamente utilizado no formato CSV e facilitar a integração com outros sistemas.

O arquivo é gravado com codificação UTF-8. A cada execução, o arquivo de saída é criado ou sobrescrito.


## 6. Ferramentas de consulta e inteligência artificial

Utilizei o ChatGPT como apoio durante o desenvolvimento para investigar erros, revisar trechos de código e relembrar parâmetros de bibliotecas Python. As decisões de implementação, os ajustes no código e a validação da solução foram realizados por mim.

Optei por não utilizar um assistente de código integrado ao VS Code, como Amazon Q ou Kiro, porque o escopo do teste era pequeno e envolvia funcionalidades que eu já havia implementado em outros projetos.

## 7. Como você adaptaria essa solução para um processo de BPM, no qual os registros fossem recebidos por um formulário e o arquivo CSV fosse gerado após uma etapa de aprovação?

Em um processo de BPM, os registros poderiam ser recebidos por meio de um formulário integrado a uma plataforma de workflow. No envio, o processo validaria os campos obrigatórios e salvaria a solicitação em uma base de dados, atribuindo um identificador e um status inicial, como `PENDENTE`.

Em seguida, uma tarefa seria encaminhada ao responsável pela aprovação. A decisão do aprovador atualizaria o status da solicitação para `APROVADO` ou `REPROVADO`, mantendo o histórico da decisão, o responsável e a data da aprovação.

Após a aprovação, uma etapa automatizada consultaria as solicitações aprovadas, aplicaria as validações necessárias e geraria o CSV. O arquivo poderia então ser disponibilizado para download ou enviado ao sistema consumidor. O processo também registraria logs, trataria falhas e permitiria reprocessamento controlado, evitando gerar arquivos com solicitações não aprovadas.

## 8. Caminho para projeto no Github