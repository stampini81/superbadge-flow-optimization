# Salesforce Superbadge: Flow Optimization

Projeto Salesforce DX com a metadata utilizada para concluir o superbadge **Flow Optimization** no Developer Edition especial do Trailhead.

## Objetivo

Este repositório documenta e versiona as alterações aplicadas nos fluxos do desafio para melhorar escalabilidade, desempenho e experiência do usuário.

## Escopo Resolvido

Os seguintes flows foram recuperados da org, ajustados e implantados com sucesso:

- `Staff_Recommendation`
- `Book_Order_Count_1` (`Book Order Count`)
- `Create_QA_Task_for_Book_Order`

## Principais Ajustes

### Staff Recommendation

- Substituição da `Decision` por `Collection Filter`.
- Execução bloqueada quando `Favorite_Genre__c` está em branco.
- Ativação da versão atualizada do fluxo.

### Book Order Count

- Remoção da `Decision` de bulk import e transferência da lógica para a condição de entrada.
- Contagem de livros em pré-venda usando:

```text
IF({!BookLineItems.Preordered__c},{!BookLineItems.Quantity__c},0)
```

- Atualização dos campos:
  - `Contact.Book_Count__c`
  - `Contact.Preordered_Book_Count__c`
- Otimização do caminho dos loops para evitar update repetido do contato.

### Create QA Task for Book Order

- Alteração do `OwnerId` para a fila `QA_Team`.
- Criação de tarefa para pedidos terminados em `5` e `0`.

## Estrutura

```text
force-app/
  main/default/
    flows/
    objects/
manifest/
.github/workflows/
scripts/
```

## Como Recuperar Metadata

```powershell
sf project retrieve start --manifest manifest/package.xml --target-org <alias>
```

## Como Fazer Deploy

```powershell
sf project deploy start --source-dir force-app/main/default/flows --target-org <alias> --ignore-conflicts
```

## Validação Local

O workflow de CI valida:

- XML bem formado em `package.xml` e nos flows
- existência dos arquivos principais do projeto
- presença dos três flows do desafio

Você também pode executar localmente:

```powershell
python scripts/validate_metadata.py
```

## Observações

- Não versionar credenciais, aliases locais ou tokens.
- O estado da org pode variar se novos drafts forem criados manualmente no Flow Builder.
- O check oficial do superbadge continua sendo executado no Trailhead.

## Licença

Este projeto está disponível sob a licença MIT. Veja [LICENSE](LICENSE).
