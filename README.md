# Validador de Senha Forte em Python

Senhas são uma maneira importante de proteger seus dados e o acesso a suas contas. Este é um código em Python que permite verificar a força de uma senha digitada pelo usuário. O script solicita que o usuário insira uma senha sem mostrá-la na tela. Em seguida, ele avalia a força da senha com base em critérios como a presença de caracteres minúsculos, maiúsculos, numerais, caracteres especiais e espaços em branco.

## Funcionamento do Código

1. **Solicitação de Senha**: O código usa o módulo `getpass` para solicitar ao usuário que digite uma senha sem mostrar a entrada na tela.

2. **Inicialização das Variáveis**: As variáveis `strengh` (força), `remarks` (observações) e contadores para diferentes tipos de caracteres são inicializados.

3. **Verificação dos Caracteres da Senha**: O código verifica cada caractere da senha e conta quantos caracteres minúsculos, maiúsculos, numerais, caracteres especiais e espaços em branco estão presentes.

4. **Avaliação da Força da Senha**: Com base nos critérios contados, a força da senha é avaliada. A força é representada por um valor numérico de 1 a 5.

5. **Apresentação dos Resultados**: O código exibe os detalhes da senha inserida pelo usuário, incluindo contagens de diferentes tipos de caracteres e a força da senha.

6. **Sugestões de Melhoria**: Com base na força da senha, são fornecidas sugestões para melhorá-la.

7. **Opção de Digitar Outra Senha**: Após verificar a força da senha, o usuário tem a opção de digitar outra senha ou encerrar o programa.

## Como Utilizar

Para usar este validador de senha forte, siga estas etapas:

1. Execute o script em um ambiente Python.
2. Você será solicitado a inserir sua senha. Digite-a e pressione Enter.
3. O programa avaliará a força da senha e fornecerá sugestões para melhorá-la.
4. Você terá a opção de digitar outra senha ou encerrar o programa, conforme desejado.
