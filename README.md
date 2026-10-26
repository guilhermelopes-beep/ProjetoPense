# Protótipo do Sistema da 11ª Jornada Científica do IFRS

A 11ª Jornada Científica, Tecnológica e Cultural do IFRS está se aproximando! Para apoiar o evento, sua equipe vai desenvolver a versão inicial e o protótipo do PEnsE-Submite, um sistema web que permite simular o envio de resumos acadêmicos e a visualização dos trabalhos dinamicamente na tela.

O objetivo principal desta atividade é aplicar os conceitos de rotas web, métodos HTTP e a renderização de páginas dinâmicas.

- Trabalho em Grupo

- Front-end (HTML5 e CSS3): Crie páginas visualmente organizadas e agradáveis para o usuário. Você deve criar pelo menos:

1 - Uma página inicial (Dashboard/Listagem).

2 - Uma página com o formulário de envio.

- Rotas e Métodos HTTP (Flask): O aplicativo Flask deve gerenciar as requisições utilizando os métodos corretos:

    - GET: Para renderizar as páginas e os formulários.

    - POST: Para receber os dados enviados pelos formulários.

- Exibição Dinâmica (Jinja2): Utilize o Jinja2 para:

    - Criar um template base (base.html) com herança para evitar repetição de código HTML (como menu e rodapé).

    - Percorrer e exibir na tela a lista de trabalhos que foram enviados.

- Armazenamento Temporário (Simulação de Banco de Dados): Como ainda não estamos utilizando um Banco de Dados (SGBD), os dados enviados pelo formulário devem ser salvos em uma lista Python na memória do servidor (ex: uma lista global trabalhos = []).

    - Nota: Toda vez que o servidor Flask for reiniciado, a lista voltará a ficar vazia. Isso é normal para este protótipo! Então sugiro deixa-la com alguns dados pré-preenchida para fins de testes.

 
## 1. Dashboard (Página Inicial)
- Uma página que lista todos os trabalhos que já foram enviados até o momento.

- Para cada trabalho, exiba: Título, Autor e Modalidade.

- Se nenhuma submissão tiver sido feita ainda, utilize uma estrutura condicional do Jinja ({% if %}) para exibir a mensagem: "Nenhum trabalho submetido ainda. Seja o primeiro!".

## 2. Formulário de Submissão
- Uma página contendo um formulário HTML (<form>) que use o método POST para enviar os dados para o Flask.

- O formulário deve conter os seguintes campos:

    - Título do Trabalho (campo de texto)

    - Nome do Autor (campo de texto)

    - Campus/Instituição (campo de texto)

    - Resumo (área de texto / textarea)

    - Modalidade (opções de escolha, ex: Ensino, Pesquisa ou Extensão)

- Ao clicar no botão "Enviar", o Flask deve capturar esses dados, adicioná-los à lista global e redirecionar o usuário de volta para a Página Inicial (Dashboard), onde o novo trabalho já deve aparecer listado.
