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
| Gustavo Henrique Rivero Pasqualin | 23.00531-9 |
---

## 📷 Imagens

A tabela abaixo apresenta os requisitos funcionais e não funcionais definidos para o projeto.

<div align="center"><img width="533" height="230" alt="image" src="https://github.com/user-attachments/assets/bb23d93b-ec67-438f-a646-3a38e6fb6622" />

Tabela de Requisitos

A tabela apresenta a estimativa de custos dos componentes utilizados no projeto, permitindo avaliar ao impacto econômico do piano.

<img width="565" height="246" alt="image" src="https://github.com/user-attachments/assets/dfe93867-8d40-42bd-82cd-f420f760b125" />

Tabela de Custos

O diagrama representa simplificadamente a arquitetura do piano.

<img width="521" height="298" alt="image" src="https://github.com/user-attachments/assets/857ddd6e-4b56-4037-8497-7b31675ad453" />

Diagrama de Componentes

<img width="576" height="432" alt="WhatsApp Image 2026-04-13 at 17 17 00" src="https://github.com/user-attachments/assets/c6188526-a087-4c88-a42a-63a11d258fc1" />

Versão 1    Teste/Protótipo

<img width="576" height="422" alt="image" src="https://github.com/user-attachments/assets/fde9cd59-0b57-44c6-8975-7dceddf270c7" />

Versão 2    Final/1º Semestre</div>


<img width="4000" height="3000" alt="foto grupo micro" src="https://github.com/user-attachments/assets/af3462fa-8281-49e3-a44f-4bcbba260fb6" />

Foto dos integrantes do grupo


---

## Vídeo de Funcionamento do Projeto

<div align="center">
  <video src="https://github.com/user-attachments/assets/04ac594f-8ff8-4192-b54c-71de347631cb.mp4" width="600" controls="controls"></video>
  <br>
  Demonstração do Projeto
</div>


## 🛠️ Tecnologias Utilizadas

### Software
| Ferramenta | Descrição |
|---|---|
| [Thonny](https://thonny.org/) | IDE para desenvolvimento e gravação de firmware |
| [AutoDesk Fusion](https://www.autodesk.com/products/fusion-360/personal) | Ferramenta para criação de modelos 2D e 3D |

### Linguagens
| Linguagem | Uso |
|---|---|
| MicroPython | Programação do microcontrolador Raspberry Pi Pico |

### Hardware
| Componente | Funcionalidade |
|---|---|
| Raspberry Pi Pico | Microcontrolador principal do projeto |
| Potenciômetro 10k | Regulador de Volume |
| Resistores | Filtro |
| Botões | Entrada do Usuário |
| Capacitor | Filtragem de Onda |

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
- Prototipagem 3D (Fusion)
- Impressão 3D
- Montagem

### 4. Integração e Testes

| Teste | Objetivo |
|---|---|
| Testes individuais de cada tecla e nota | Verificar se cada tecla aciona corretamente sua respectiva nota musical. |
| Validação da resposta temporal | Avaliar se o som é reproduzido sem atraso perceptível após o acionamento da tecla. |
| Ajuste de timbre e duração das notas | Ajustar a qualidade sonora e o tempo de reprodução das notas. |
| Pseudoacordes | Validar a reprodução de combinações de notas simulando acordes. |
| Oitavas alteráveis | Verificar se o sistema altera corretamente a altura das notas entre diferentes oitavas. |


- Documentação técnica do projeto
### 5. Demonstração funcional

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
│  [Filtro de Passa-Baixo]                            |
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
│   └── testepiano.py     # Protótipo da lógica de controle do piano
├── docs/
│   └── relatorio.pdf     # Relatório técnico do projeto
├── main.py               # Código Principal do funcionamento Piano
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
   mpremote connect /dev/ttyUSB0 run src/testepiano.py
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

*Desenvolvido com 🎵 pelo Grupo IMT, 2026*
