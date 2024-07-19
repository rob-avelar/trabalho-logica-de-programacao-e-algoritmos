Trabalho de lógica de programação e Algoritmos do curso de Eng. de Software da UNINTER.

QUESTÃO 1 de 4 - Conteúdo até Aula 03
Enunciado: Imagina-se que você é um dos programadores responsáveis pela construção de app de vendas para uma determinada empresa X que aceita cartões de crédito. Uma das estratégias de vendas dessa empresa X é cobrar um Juros maior conforme a quantidade de parcelas que o cliente desejar, conforme a listagem abaixo:

	Se a quantidade de parcelas for menor que 4, o Juros será de 0% (0 / 100);
	Se a quantidade de parcelas for igual ou maior que 4 e menor que 6, o Juros será de 4% (4 / 100);
	Se a quantidade de parcelas for igual ou maior que 6 e menor que 9, o Juros será de 8% (8 / 100);
	Se a quantidade de parcelas for igual ou maior que 9 e menor que 13, o Juros será de 16% (16 / 100);
	Se a quantidade de parcelas for igual ou maior que 13, o Juros será de 32% (32 / 100);

O valor da parcela é calculado da seguinte maneira:
valorDaParcela=  (valorDoPedido*(1+juros))/quantidadeParcelas
O valor total parcelado é calculado da seguinte maneira:
valorTotalParcelado=valorDaParcela*quantidadeParcelas

Elabore um programa em Python que:
	Deve-se implementar o print com o seu nome completo (somente print, não usar input aqui). 
Por exemplo: print(“Bem-vindos a loja do Bruno Kostiuk”) [EXIGÊNCIA DE CÓDIGO 1 de 6];
	Deve-se implementar o input do valorDoPedido e da quantidadeParcelas [EXIGÊNCIA DE CÓDIGO 2 de 6];
	Deve-se implementar o Juros conforme a enunciado acima (obs.: atente-se as condições de menor, igual e maior) [EXIGÊNCIA DE CÓDIGO 3 de 6];
	Deve-se implementar o valorDaParcela e valorTotalParcelado [EXIGÊNCIA DE CÓDIGO 4 de 6];
	Deve-se implementar as estruturas if, elif e else (todas elas) [EXIGÊNCIA DE CÓDIGO 5 de 6];  
	Deve-se inserir comentários relevantes no código [EXIGÊNCIA DE CÓDIGO 6 de 6];
	Deve-se apresentar na saída de console uma mensagem com seu nome completo [EXIGÊNCIA DE SAÍDA DE CONSOLE 1 de 2];
	Deve-se apresentar na saída de console um parcelamento com Juros (quantidadeParcelas maior ou igual a 4) apresentando o valor da Parcela e o valor Total Parcelado [EXIGÊNCIA DE SAÍDA DE CONSOLE 2 de 2];  


QUESTÃO 2 de 4 - Conteúdo até aula 04
Enunciado: Você e sua equipe de programadores foram contratados para desenvolver um app de vendas para uma loja que vende Marmitas de Bife Acebolado ou Filé de Frango. Você ficou com a parte de desenvolver a interface do cliente para retirada do produto.

A Loja possui seguinte relação:
•	Tamanho P de Bife Acebolado (BA) custa 16 reais e o Filé de Frango (FF) custa 15 reais;
•	Tamanho M de Bife Acebolado (BA) custa 18 reais e o Filé de Frango (FF) custa 17 reais;
•	Tamanho G de Bife Acebolado (BA) custa 22 reais e o Filé de Frango (FF) custa 21 reais;

Elabore um programa em Python que: 
A.	Deve-se implementar o print com o seu nome completo (somente print, não usar input aqui). 
Por exemplo: print(“Bem vindos a loja de Marmitas do Bruno Kostiuk”) 
Além do seu nome completo, deve-se implementar um print com um Menu para o cliente. [EXIGÊNCIA DE CÓDIGO 1 de 8];
B.	Deve-se implementar o input do sabor (BA/FF) e o print “Sabor inválido. Tente novamente" se o usuário entra com valor diferente de BA e FF [EXIGÊNCIA DE CÓDIGO 2 de 8];
C.	Deve-se implementar o input do tamanho (P/M/G) e o print “Tamanho inválido. Tente novamente" se o usuário com entra valor diferente de P, M ou G [EXIGÊNCIA DE CÓDIGO 3 de 8];
D.	Deve-se implementar if, elif e/ou else, utilizando o modelo aninhado (aula 3 – Tema 4) com cada uma das combinações de sabor e tamanho [EXIGÊNCIA DE CÓDIGO 4 de 8];
E.	Deve-se implementar um acumulador para somar os valores dos pedidos [EXIGÊNCIA DE CÓDIGO 5 de 8];
F.	Deve-se implementar o input com a pergunta: “Deseja pedir mais alguma coisa?”. Se sim repetir a partir do item B, senão encerrar o programa executar o print do acumulador [EXIGÊNCIA DE CÓDIGO 6 de 8];
G.	Deve-se implementar as estruturas de while, break, continue (todas elas) [EXIGÊNCIA DE CÓDIGO 7 de 8];
H.	Deve-se inserir comentários relevantes no código [EXIGÊNCIA DE CÓDIGO 8 de 8];
I.	Deve-se apresentar na saída de console uma mensagem com o seu nome completo e o menu para o cliente conhecer as opções  [EXIGÊNCIA DE SAÍDA DE CONSOLE 1 de 4];
J.	Deve-se apresentar na saída de console um pedido em que o usuário errou o sabor [EXIGÊNCIA DE SAÍDA DE CONSOLE 2 de 4]; 
K.	Deve-se apresentar na saída de console um pedido em que o usuário errou o tamanho [EXIGÊNCIA DE SAÍDA DE CONSOLE 3 de 4];
L.	Deve-se apresentar na saída de console um pedido com duas opções sabores diferentes e com tamanhos diferentes [EXIGÊNCIA DE SAÍDA DE CONSOLE 4 de 4];  


QUESTÃO 3 de 4 - Conteúdo até aula 05
Enunciado: Você foi contratado para desenvolver um sistema de cobrança de serviços de uma fábrica que vende Camisetas em atacado. Você ficou com a parte de desenvolver a interface com o funcionário.
A Fábrica opera as vendas da seguinte maneira:

•	Camiseta Manga Curta Simples (MCS), o valor unitário é de um real e oitenta centavos;
•	Camiseta Manga Longa Simples (MLS), o valor unitário é de dois reais e dez centavos;
•	Camiseta Manga Curta Com Estampa (MCE), o valor unitário é de dois reais e noventa centavos; 
•	Camiseta Manga Longa Com Estampa (MLE), o valor unitário é de três reais e vinte centavos; 

•	Se número de camisetas for menor que 20 não há desconto na venda;
•	Se número de camisetas for igual ou maior que 20 e menor que 200, o desconto será de 5%;
•	Se número de camisetas for igual ou maior que 200 e menor que 2000, o desconto será de 7%;
•	Se número de camisetas for igual ou maior que 2000 e menor ou igual que 20000, o desconto será de 12%;
•	Se número de camisetas for maior que 20000, não é aceito pedidos nessa quantidade de camisetas;
	
♦	Para o adicional de frete por transportadora (1) é cobrado um valor extra de 100 reais;
♦	Para o adicional de frete por Sedex (2) é cobrado um valor extra de 200 reais;
♦	Para o adicional de retirar o pedido na fábrica (0) é cobrado um valor extra de 0 reais;

O valor final da conta é calculado da seguinte maneira:

total = (modelo * num_camisetas) + frete

Elabore um programa em Python que: 
A.	Deve-se implementar o print com o seu nome completo (somente print, não usar input aqui). 
Por exemplo: print(“Bem vindos a Fábrica de Camisetas do Bruno Kostiuk”)  [EXIGÊNCIA DE CÓDIGO 1 de 7];
B.	Deve-se implementar a função escolha_modelo() em que: [EXIGÊNCIA DE CÓDIGO 2 de 7];
a.	Pergunta o modelo desejado;
b.	Retorna o valor do modelo com base na escolha do usuário (use return);
c.	Repete a pergunta do item B.a se digitar uma opção diferente de: MCS/MLS/MCE/MLE;
C.	Deve-se implementar a função num_camisetas() em que: [EXIGÊNCIA DE CÓDIGO 3 de 7];
a.	Pergunta o número de camisetas;
b.	Retorna (use return) o número de camisetas com desconto seguindo a regra do enunciado (desconto calculado em cima do número de camisetas);
c.	Repete a pergunta do item C.a se digitar um valor acima de 20000 ou valor não numérico (use try/except para não numérico)
D.	Deve-se implementar a função frete() em que: [EXIGÊNCIA DE CÓDIGO 4 de 7];
a.	Pergunta pelo serviço adicional de frete;
b.	Retorna (use return) o valor de apenas uma das opções de frete 
c.	Repetir a pergunta item D.a se digitar uma opção diferente de: 1/2/0;
E.	Deve-se implementar o total a pagar no código principal (main), ou seja, não pode estar dentro de função, conforme o enunciado [EXIGÊNCIA DE CÓDIGO 5 de 7];
F.	Deve-se implementar try/except [EXIGÊNCIA DE CÓDIGO 6 de 7];
G.	Deve-se inserir comentários relevantes no código [EXIGÊNCIA DE CÓDIGO 7 de 7];
H.	Deve-se apresentar na saída de console uma mensagem com o seu nome completo [EXIGÊNCIA DE SAÍDA DE CONSOLE 1 de 4];
I.	Deve-se apresentar na saída de console um pedido no qual o usuário errou a opção de modelo [EXIGÊNCIA DE SAÍDA DE CONSOLE 2 de 4];
J.	Deve-se apresentar na saída de console um pedido no qual o usuário digitou ultrapassou no número de camisetas [EXIGÊNCIA DE SAÍDA DE CONSOLE 3 de 4];
K.	Deve-se apresentar na saída de console um pedido com opção de modelo, número de camisetas e frete válidos [EXIGÊNCIA DE SAÍDA DE CONSOLE 4 de 4];




QUESTÃO 4 de 4 - Conteúdo até aula 06
Enunciado: Você e sua equipe de programadores foram contratados por pequena empresa para desenvolver o software de gerenciamento de funcionários. Este software deve ter o seguinte menu e opções:

1)	Cadastrar Funcionário
2)	Consultar Funcionário
1.	Consultar Todos 
2.	Consultar por Id
3.	Consultar por setor
4.	Retornar ao menu
3)	Remover Funcionário
4)	Encerrar Programa

Elabore um programa em Python que: 
A.	Deve-se implementar o print com o seu nome completo (somente print, não usar input aqui). 
Por exemplo: print(“Bem vindos a empresa do Bruno Kostiuk”)  [EXIGÊNCIA DE CÓDIGO 1 de 8];
B.	Deve-se implementar uma lista com o nome de lista_funcionarios e a variável id_global com valor inicial igual ao número de seu RU [EXIGÊNCIA DE CÓDIGO 2 de 8];
C.	Deve-se implementar uma função chamada cadastrar_funcionario(id) em que: [EXIGÊNCIA DE CÓDIGO 3 de 8];
a.	Pergunta nome, setor, salario do funcionário;
b.	Armazena o id (este é fornecido via parâmetro da função), nome, setor, salario dentro de um dicionário;
c.	Copiar o dicionário para dentro da lista_funcionarios (utilizar o copy);
D.	Deve-se implementar uma função chamada consultar_funcionarios() em que: [EXIGÊNCIA DE CÓDIGO 4 de 8];
a.	Deve-se perguntar qual opção deseja (1. Consultar Todos / 2. Consultar por Id / 3. Consultar por Setor / 4. Retornar ao menu):
i.	Se Consultar Todos, apresentar todos os funcionários com todos os seus dados cadastrados;
ii.	Se Consultar por Id, solicitar ao usuário que informe um id, e apresentar o funcionário específico com todos os seus dados cadastrados;
iii.	Se Consultar por Setor, solicitar ao usuário que informe o setor, e apresentar o(s) funcionário(s) do setor com todos os seus dados cadastrados;
iv.	Se Retornar ao menu, deve-se retornar ao menu principal (return);
v.	Se Entrar com um valor diferente de 1, 2, 3 ou 4, printar “Opção inválida" e repetir a pergunta D.a.
vi.	Enquanto o usuário não escolher a opção 4, o menu consultar funcionários deve se repetir.
E.	Deve-se implementar uma função chamada remover_funcionario() em que: [EXIGÊNCIA DE CÓDIGO 5 de 8];
a.	Deve-se pergunta pelo id do funcionário a ser removido;
b.	Remover o funcionário da lista_funcionarios;
c.	Se o id fornecido não for de um funcionário da lista, printar “Id inválido” e repetir a pergunta E.a.
F.	Deve-se implementar uma estrutura de menu no código principal (main), ou seja, não pode estar dentro de função, em que: [EXIGÊNCIA DE CÓDIGO 6 de 8];
a.	Deve-se pergunta qual opção deseja (1. Cadastrar Funcionário / 2. Consultar Funcionário / 3. Remover Funcionário / 4. Encerrar Programa):
i.	Se Cadastrar Funcionário, incrementar em um id_ global e chamar a função cadastrar_funcionario(id_ global);
ii.	Se Consultar Funcionário, chamar função consultar_funcionario ();
iii.	Se Remover Funcionário, chamar função remover_funcionario();
iv.	Se Encerrar Programa, sair do menu (e com isso acabar a execução do código);
v.	Se Entrar com um valor diferente de 1, 2, 3 ou 4, printar “Opção inválida" e repetir a pergunta F.a.
vi.	Enquanto o usuário não escolher a opção 4, o menu deve se repetir.
G.	Deve-se implementar uma lista de dicionários (uma lista contento dicionários dentro) [EXIGÊNCIA DE CÓDIGO 7 de 8];
H.	Deve-se inserir comentários relevantes no código [EXIGÊNCIA DE CÓDIGO 8 de 8];
I.	Deve-se apresentar na saída de console uma mensagem com o seu nome completo [EXIGÊNCIA DE SAÍDA DE CONSOLE 1 de 6];
J.	Deve-se apresentar na saída de console um cadastro de 3 funcionários (sendo 2 deles no mesmo setor) [EXIGÊNCIA DE SAÍDA DE CONSOLE 2 de 6];
K.	Deve-se apresentar na saída de console uma consulta de todos os funcionários [EXIGÊNCIA DE SAÍDA DE CONSOLE 3 de 6];
L.	Deve-se apresentar na saída de console uma consulta por código (id) de um dos funcionários [EXIGÊNCIA DE SAÍDA DE CONSOLE 4 de 6];
M.	Deve-se apresentar na saída de console uma consulta por setor em que 2 funcionários sejam do mesmo setor [EXIGÊNCIA DE SAÍDA DE CONSOLE 5 de 6];
N.	Deve-se apresentar na saída de console uma remoção de um dos funcionários seguida de uma consulta de todos os funcionários [EXIGÊNCIA DE SAÍDA DE CONSOLE 6 de 6];


