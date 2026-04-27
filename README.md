# 🎹 EEN251 — Projeto Piano

> Projeto desenvolvido para a disciplina **EEN251 - Microcontroladores e Sistemas Embarcados**  
> Instituto Mauá de Tecnologia — 7º Semestre

---

## 📖 Descrição

Este projeto consiste na construção de um **piano digital** utilizando microcontroladores e sistemas embarcados. O sistema é capaz de detectar o acionamento de teclas e reproduzir as notas musicais correspondentes, integrando hardware e software em uma solução compacta e funcional.

---

## 👥 Membros da Equipe

| Nome | RA |
|---|---|
| Arthur Silva Correia | 23.00877-6 |
| Bruno Ferreira Nishiya | 23.01020-7 |
| Felipe Kolanian Pasquini | 23.00118-6 |
| Leonardo Luiz Seixas Iorio | 23.00847-4 |

---

## 📷 Imagens

<img width="1600" height="1200" alt="WhatsApp Image 2026-04-13 at 17 17 00" src="https://github.com/user-attachments/assets/c6188526-a087-4c88-a42a-63a11d258fc1" />

---

## 🛠️ Tecnologias Utilizadas

### Software
| Ferramenta | Descrição |
|---|---|
| [Thonny](https://thonny.org/) | IDE para desenvolvimento e gravação de firmware |
| [Blender](https://www.blender.org/) | Ferramenta para criação de modelos 2D e 3D |

### Linguagens
| Linguagem | Uso |
|---|---|
| MicroPython | Programação do microcontrolador Raspberry Pi Pico |

### Hardware
| Componente | Descrição |
|---|---|
| Raspberry Pi Pico | Microcontrolador principal do projeto |

---

## 🎯 Escopo de Desenvolvimento

O projeto é dividido nas seguintes etapas:

### 1. Configuração do Hardware
- Montagem do circuito com o Raspberry Pi Pico
- Conexão das teclas (botões/sensores de toque) às GPIOs
- Conexão do módulo de saída de áudio (buzzer)

### 2. Desenvolvimento do Firmware
- Configuração do ambiente MicroPython no Raspberry Pi Pico (Thonny)
- Implementação da leitura de entradas digitais (teclas do piano)
- Mapeamento de cada tecla para sua respectiva frequência de nota musical
- Geração de sinal de áudio via PWM

### 3. Desenvolvimento da estrutura
- Esboço
- Prototipagem 3D (Blender)
- Impressão 3D
- Monatgem

### 4. Integração e Testes
- Testes individuais de cada tecla e nota
- Validação da resposta temporal (latência de acionamento)
- Ajuste de timbre e duração das notas

### 5. Documentação e Apresentação
- Documentação técnica do projeto
- Demonstração funcional

---

## 🔌 Integração de Hardware e Software

O diagrama abaixo ilustra o fluxo de funcionamento do sistema:

```
┌─────────────────────────────────────────────────────┐
│                  PIANO DIGITAL                      │
│                                                     │
│  [ Tecla Pressionada ]                              │
│          │                                          │
│          ▼                                          │
│  [ GPIO - Raspberry Pi Pico ]                       │
│          │                                          │
│          ▼                                          │
│  [ Firmware MicroPython ]                           │
│    - Detecção de entrada                            │
│    - Mapeamento nota/frequência                     │
│    - Geração de sinal PWM                           │
│          │                                          │
│          ▼                                          │
│  [ Saída de Áudio ]                                 │
│    - Buzzer / Alto-falante                          │
└─────────────────────────────────────────────────────┘
```

### Mapeamento de Notas

| Tecla | Nota | Frequência (Hz) |
|---|---|---|
| 1 | Dó (C4) | 261 |
| 2 | Dó# (C4#) | 277 |
| 3 | Ré (D4) | 293 |
| 4 | Ré# (D4#) | 311 |
| 5 | Mi (E4) | 329 |
| 6 | Fá (F4) | 349 |
| 7 | Fá# (F4#) | 369 |
| 8 | Sol (G4) | 392 |
| 9 | Sol# (G4#) | 415 |
| 10 | Lá (A4) | 440 |
| 11 | Lá# (A4#) | 466 |
| 12 | Si (B4) | 493 |

---

## 📁 Estrutura do Repositório

```
EEN251-ProjetoPiano/
├── src/
│   └── testepiano.py          # Lógica de controle do piano
├── docs/
│   └── relatorio.pdf     # Relatório técnico do projeto
└── README.md
```

---

## 🚀 Como Executar

### Pré-requisitos
- Raspberry Pi Pico configurado com MicroPython
- Thonny IDE ou `mpremote` instalado no computador host

### Passos

1. **Clone o repositório:**
   ```bash
   git clone https://github.com/BrunoMaster30/EEN251-ProjetoPiano.git
   cd EEN251-ProjetoPiano
   ```

2. **Transfira os arquivos para o Raspberry Pi Pico:**
   ```bash
   mpremote connect /dev/ttyUSB0 cp src/testepiano.py :testepiano.py
   ```

3. **Execute o programa:**
   ```bash
   mpremote connect /dev/ttyUSB0 run src/testepaino.py
   ```

---

## 📚 Referências

- [Documentação oficial do MicroPython](https://docs.micropython.org/)
- [Raspberry Pi Pico — Pinout](https://pinout.xyz/)
- [Thonny](https://thonny.org/)
- Instituto Mauá de Tecnologia — Material de apoio EEN251

---

## 📄 Licença

Este projeto é de uso acadêmico, desenvolvido para a disciplina EEN251 do Instituto Mauá de Tecnologia.

---

*Desenvolvido com 🎵 pelo Grupo EEN251 — IMT, 2026*
