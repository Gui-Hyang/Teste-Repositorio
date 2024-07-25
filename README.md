## Desafio 3

## Protocolo de Transferência de Hipertexto

- HTTP é a sigla para Hypertext Transfer Protocol, ou Protocolo de Transferência de Hipertexto. Esse é o principal protocolo responsável pela transferência de dados na Internet, criando as bases necessárias para a conexão entre um cliente e um servidor.

- REST, ou Representational State Transfer, é um estilo arquitetônico aplicado para fornecer padrões entre sistemas de computador na web, facilitando a comunicação entre eles. Os sistemas em conformidade com REST, muitas vezes conhecidos como sistemas RESTful, são reconhecidos pelo jeito como separam as preocupações do cliente e do servidor. as interações baseadas em REST acontecem usando estruturas que são familiares a qualquer um que esteja acostumado a usar o HTTP da Internet.

- Para entender o que é uma web API, precisamos dar um passo para trás e entender o que é uma API em si. Segundo a Mozilla Foundation, APIs (Application Programming Interfaces) são construções que permitem que se interaja com uma aplicação através de software.

## Métodos de Solicitações HTTP utilizados pelo padrão REST

- #### POST (CREATE) cria um recurso.
- #### GET (READ) retorna uma representação de um recurso.
- #### PUT (UPDATE) atualiza um recurso existente.
- #### DELETE exclui o recurso.

## Desafio 4

##  Camadas da Aplicação

A camada de aplicação é um termo utilizado em redes de computadores para designar uma camada de abstração que engloba protocolos que realizam a comunicação fim-a-fim entre aplicações.

### Entity:

O Entity Framework fornece as seguintes maneiras de consultar um modelo conceitual e retornar objetos: LINQ to Entities. Fornece suporte à LINQ (consulta integrada à linguagem) para consultar tipos de entidade que são definidos em um modelo conceitual.

### Controller:

A camada Controller é o cérebro do aplicativo baseado no padrão de arquitetura MVC. Fazendo com que os models possam ser repassados para as views e vice-versa. Isso torna o aplicativo interativo.

### Repository:

É uma abordagem de design que visa isolar a lógica de acesso a dados em uma camada separada da aplicação. Ele define uma interface comum para acesso aos dados e implementa essa interface em classes concretas, conhecidas como repositórios.

### Service:

Ela faz contato com a camada de Controller, a camada de controller faz o "primeiro contato" com as requisições, enviando a camada de Service apenas as informações revelantes para completar a requesições.


## Desafio 5

## Padrão de Projetos

- Padrões de projeto são soluções típicas para problemas comuns em projeto de software. Eles são como plantas de obra pré fabricadas que você pode customizar para resolver um problema de projeto recorrente em seu código. Você não pode apenas encontrar um padrão e copiá-lo para dentro do seu programa, como você faz com funções e bibliotecas que encontra por aí. O padrão não é um pedaço de código específico, mas um conceito geral para resolver um problema em particular. Você pode seguir os detalhes do padrão e implementar uma solução que se adeque às realidades do seu próprio programa.

## Arquitetura de Software

- Para entendermos os padrões arquiteturais, primeiro é necessário compreendermos o que é arquitetura de software. As apropriações de nomenclaturas do mundo real são comuns no universo de tecnologia, e não poderia ser diferente com o termo arquitetura. No mundo físico, profissionais de arquitetura constroem projetos e desenhos de casas, prédios, entre outras estruturas, baseando-se em um contexto que envolve diversas variáveis e situações. O objetivo é tornar o sistema mais compreensível, manutenível e escalável, além de facilitar o desenvolvimento e a evolução contínua do software.

## O que significa SOLID?

- SOLID é um acrônimo para cada um dos cinco princípios que fazem parte desse grupo:

- ### Single Responsability Principle (Princípio da Responsabilidade Única);
- ### Open/Closed Principle (Princípio do “Aberto para Extensão/Fechado para Implementação);
- ### Liskov Substitution Principle (Princípio da Substituição de Liskov);
- ### Interface Segregation Principle (Princípio da Segregação de Interfaces);
- ### Dependency Inversion Principle (Princípio da Inversão de Dependências)