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

## 🛠️ Tecnologias Utilizadas

### Software
| Ferramenta | Descrição |
|---|---|
| [Thonny](https://thonny.org/) | IDE para desenvolvimento e gravação de firmware |

### Linguagens
| Linguagem | Uso |
|---|---|
| MicroPython | Programação do microcontrolador Raspberry Pi Zero W |

### Hardware
| Componente | Descrição |
|---|---|
| Raspberry Pi Zero W | Microcontrolador principal do projeto |

---

## 🎯 Escopo de Desenvolvimento

O projeto é dividido nas seguintes etapas:

### 1. Configuração do Hardware
- Montagem do circuito com o Raspberry Pi Zero W
- Conexão das teclas (botões/sensores de toque) às GPIOs
- Conexão do módulo de saída de áudio (buzzer ou DAC + alto-falante)

### 2. Desenvolvimento do Firmware
- Configuração do ambiente MicroPython no Raspberry Pi Zero W
- Implementação da leitura de entradas digitais (teclas do piano)
- Mapeamento de cada tecla para sua respectiva frequência de nota musical
- Geração de sinal de áudio via PWM ou I2S

### 3. Integração e Testes
- Testes individuais de cada tecla e nota
- Validação da resposta temporal (latência de acionamento)
- Ajuste de timbre e duração das notas

### 4. Documentação e Apresentação
- Documentação técnica do projeto
- Esquemático elétrico
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
│  [ GPIO - Raspberry Pi Zero W ]                     │
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
| 1 | Dó (C4) | 261,63 |
| 2 | Ré (D4) | 293,66 |
| 3 | Mi (E4) | 329,63 |
| 4 | Fá (F4) | 349,23 |
| 5 | Sol (G4) | 392,00 |
| 6 | Lá (A4) | 440,00 |
| 7 | Si (B4) | 493,88 |
| 8 | Dó (C5) | 523,25 |

---

## 📁 Estrutura do Repositório

```
EEN251-ProjetoPiano/
├── src/
│   ├── main.py           # Código principal MicroPython
│   ├── notes.py          # Mapeamento de frequências das notas
│   └── piano.py          # Lógica de controle do piano
├── hardware/
│   ├── schematic.pdf     # Esquemático elétrico
│   └── bom.csv           # Lista de componentes (Bill of Materials)
├── docs/
│   └── relatorio.pdf     # Relatório técnico do projeto
└── README.md
```

---

## 🚀 Como Executar

### Pré-requisitos
- Raspberry Pi Zero W configurado com MicroPython
- Thonny IDE ou `mpremote` instalado no computador host

### Passos

1. **Clone o repositório:**
   ```bash
   git clone https://github.com/BrunoMaster30/EEN251-ProjetoPiano.git
   cd EEN251-ProjetoPiano
   ```

2. **Transfira os arquivos para o Raspberry Pi Zero W:**
   ```bash
   mpremote connect /dev/ttyUSB0 cp src/notes.py :notes.py
   mpremote connect /dev/ttyUSB0 cp src/piano.py :piano.py
   mpremote connect /dev/ttyUSB0 cp src/main.py :main.py
   ```

3. **Execute o programa:**
   ```bash
   mpremote connect /dev/ttyUSB0 run src/main.py
   ```

---

## 📚 Referências

- [Documentação oficial do MicroPython](https://docs.micropython.org/)
- [Raspberry Pi Zero W — Pinout](https://pinout.xyz/)
- [Microchip Studio — Getting Started](https://www.microchip.com/en-us/tools-resources/develop/microchip-studio)
- Instituto Mauá de Tecnologia — Material de apoio EEN251

---

## 📄 Licença

Este projeto é de uso acadêmico, desenvolvido para a disciplina EEN251 do Instituto Mauá de Tecnologia.

---

*Desenvolvido com 🎵 pelo Grupo EEN251 — IMT, 2026*
