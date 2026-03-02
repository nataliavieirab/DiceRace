# DiceRace

## 1. Descrição do Projeto

O projeto **DiceRace** é um jogo de corrida de dados implementado em Python.

## 2. Como Jogar

O objetivo do jogo é ser o primeiro jogador a alcançar ou ultrapassar a casa 30. 
Algumas casas possuem eventos especiais que podem beneficiar ou prejudicar o jogador.

### Regras Básicas:

1.  Cada jogador começa na casa 0.
2.  Na sua vez, o jogador lança um dado de 6 faces.
3.  O jogador avança o número de casas correspondente ao valor do dado.
4.  Se o jogador cair em uma casa especial, o efeito da casa é aplicado imediatamente.
5.  O jogo termina quando um jogador atinge ou ultrapassa a casa 30.

## Eventos Especiais:

- Avanço extra: Se o competidor parar nas posições 5, 10 e 15, ele avança +3 casas.
- Recuo: Se o competidor parar nas posições 7, 13, 20, ele recua -2 casas.
- Rodada extra: Se o competidor tirar 6 no dado, ele ganha uma rodada extra.

## 3. Instalação e Execução

### Pré-requisitos

É necessário ter o **Python 3.x** instalado.

```bash
python3 --version
```

### Clonar o Repositório

```bash
git clone https://github.com/nataliavieirab/DiceRace.git
cd DiceRace
```

### Executar o Jogo

```bash
python3 main.py
```

## 4. Estrutura do Projeto

O projeto está organizado nos seguintes arquivos abaixo, cada um com uma responsabilidade específica:

-   `main.py`: Ponto de entrada principal do jogo.
-   `game.py`: Possui a lógica central do jogo.
-   `dice.py`: Possui a funcionalidade de lançamento de dados, gerando números aleatórios.
-   `ui.py`: Responsável pela interface do usuário no console.
-   `events.py`: Define os eventos especiais que ocorrem em casas específicas do tabuleiro.