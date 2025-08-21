## Desafio

Você foi contratado por um grande banco para desenvolver o seu novo sistema. Esse banco deseja modernizar suas operações e para isso escolheu a linguagem Python. Para a primeira versão do sistema, você deve implementar apensas 3 operações: depósito, saque e extrato.

### Operação de **Depósito**

Deve ser possível depositar valores positivos para a conta bancária. A v1 do projeto trabalha apenas com 1 usuário, dessa forma não há necessidade de se preocupar em identificar qual é o número de agência e conta bancária. Todos os depósitos devem ser armazenados em uma variável e exebido na operação de extrato.

### Operação de **Saque**

O sistema deve permitir realizar 3 saques diários com limite máximo de $R\$ 500,00$ por saque. Caso o usuário não tenha saldo em conta, o sistema deve exibir uma mensagem informando que não será possível sacar o dinheiro por falta de saldo. Todos os saques devem ser armazenados em uma vairável e exibidos na operação de extratos.

### Operação de **Extrato**

Essa operação deve listar todos os depósitos e saques realizados na conta. No fim da listagem, deve ser exibido o saldo atual da conta.

Os valores devem ser exibidos utilizando o formato $R\$ XXX.XX$, exemplo:
$1500.45 = R\$ 1500.45$