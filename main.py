from machine import Pin, PWM, ADC
import time

# Configuração do buzzer
buzzer = PWM(Pin(19))

# Potenciômetro (ADC)
pot = ADC(28)

# Configuração dos botões (pull-down)
buttons = [
    Pin(2, Pin.IN, Pin.PULL_DOWN),
    Pin(3, Pin.IN, Pin.PULL_DOWN),
    Pin(4, Pin.IN, Pin.PULL_DOWN),
    Pin(5, Pin.IN, Pin.PULL_DOWN),
    Pin(6, Pin.IN, Pin.PULL_DOWN),
    Pin(7, Pin.IN, Pin.PULL_DOWN),
    Pin(8, Pin.IN, Pin.PULL_DOWN),
    Pin(9, Pin.IN, Pin.PULL_DOWN),
    Pin(10, Pin.IN, Pin.PULL_DOWN),
    Pin(11, Pin.IN, Pin.PULL_DOWN),
    Pin(12, Pin.IN, Pin.PULL_DOWN),
    Pin(13, Pin.IN, Pin.PULL_DOWN)
]

led = Pin(25, Pin.OUT)

# Botões de oitava
oct_down = Pin(17, Pin.IN, Pin.PULL_DOWN)
oct_up = Pin(16, Pin.IN, Pin.PULL_DOWN)


# Frequências das notas
notes = [
    261, 277, 293, 311, 329, 349,
    369, 392, 415, 440, 466, 493
]
# Controle de oitava
octave = 0
MIN_OCT = -2
MAX_OCT = 2

last_oct_down = 0
last_oct_up = 0

def get_volume():
    raw = pot.read_u16()  # 0 - 65535
    
    # Ajuste de volume (evita muito alto)
    volume = int((raw / 65535)*5000)  # reduz escala
    return volume

def apply_octave(freq):
    return int(freq * (2 ** octave))

def ok():
    led.on()
    time.sleep(0.019)
    led.off()
    
def play_tone(freq):
    buzzer.freq(freq)
    buzzer.duty_u16(get_volume())  # volume (0 a 65535)

def stop_tone():
    buzzer.duty_u16(0)

 # Loop principal
ok()
while True:
    
    # Controle de oitava (com debounce simples)
    if oct_down.value() == 1 and last_oct_down == 0:
        if octave > MIN_OCT:
            octave -= 1
            print("Oitava:", octave) 
        time.sleep(0.2)
    last_oct_down = oct_down.value()

    if oct_up.value() == 1 and last_oct_up == 0:
        if octave < MAX_OCT:
            octave += 1
            print("Oitava:", octave)
        time.sleep(0.2)
    last_oct_up = oct_up.value()
    
    played = False
    
    for i in range(12):
        if buttons[i].value() == 1:
            ok()
            freq = apply_octave(notes[i])
            play_tone(freq)
            played = True
            #break
    
    if not played:
        stop_tone()
    
    #time.sleep(0.0001,,)z