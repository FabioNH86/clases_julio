# RETO: Calculadora de Vida Restante
# Instrucciones: 
# 1. El daño real se calcula restando la 'defensa' al 'ataque'.
# 2. Luego, resta ese daño a la 'salud_jugador'.
# 3. Imprime el resultado final.

salud_jugador = 100
ataque_enemigo = 35
defensa_jugador = 10
dano_final = 0
# TODO: Calcula el daño_final y actualiza la salud_jugador
# Tu código aquí:
dano_final = ataque_enemigo - defensa_jugador
salud_jugador -= dano_final
print(f"Salud restante: {salud_jugador}") # Debería dar 75