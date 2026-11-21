🎰 Reto Integrador: Sistema de Tragamonedas en PythonEste repositorio contiene la solución completa al reto integrador de Programación Orientada a Objetos (POO) en Python. El proyecto simula un entorno de casino con múltiples máquinas tragamonedas, cada una con sus propias reglas, símbolos y sistema de apuestas.🚀 Características del ProyectoEl sistema es interactivo y se ejecuta en la consola. Permite al usuario:Elegir entre diferentes tipos de máquinas tragamonedas (Frutas, Clásica y Mundial 2026).Realizar apuestas y ver los giros con emojis generados de forma aleatoria.Ganar premios basados en la coincidencia de símbolos o reglas especiales (polimorfismo).Consultar un panel de estadísticas protegido que muestra el total apostado, ganado y el balance de cada máquina.🧠 Conceptos de POO AplicadosPilar/ConceptoImplementación en el códigoClase y constructorSe creó la clase base Tragamonedas con el método __init__.AbstracciónSe modeló el comportamiento de una máquina real con los métodos girar() y jugar().HerenciaSe crearon las clases hijas TragamonedasFrutas, TragamonedasClasico y TragamonedasMundial.PolimorfismoSe sobrescribió el método jugar() en la máquina del Mundial para darle reglas de premio distintas.EncapsulaciónSe protegió el saldo y las estadísticas usando el guion bajo (_creditos), limitando su modificación directa.💻 Código Fuente Completo (Versión Final)Este es el script principal que unifica todas las partes del reto:import random

class Tragamonedas:
    def __init__(self, nombre, creditos):
        self.nombre = nombre
        self._creditos = creditos
        self._total_jugado = 0
        self._total_ganado = 0

    def mostrar(self):
        estado = f"S/ {self._creditos}" if self._creditos > 0 else "💀 SIN CRÉDITOS"
        print(f"🎰 {self.nombre} — {estado}")

    def girar(self):
        simbolos = ["🍒", "🔔", "💎", "🍀", "⭐", "7️⃣"]
        resultado = []
        for _ in range(3):
            indice = random.randint(0, len(simbolos) - 1)
            resultado.append(simbolos[indice])
        print(f"[ {resultado[0]}  {resultado[1]}  {resultado[2]} ]")
        return resultado

    def jugar(self, apuesta):
        if self._creditos == 0:
            print("💀 Esta máquina no tiene créditos.")
            return False
        if apuesta > self._creditos:
            print(f"❌ No tienes suficiente saldo. Créditos: {self._creditos}")
            return False

        self._creditos -= apuesta
        self._total_jugado += apuesta
        resultado = self.girar()

        if resultado[0] == resultado[1] == resultado[2]:
            premio = apuesta * 10
            print(f"🎉 ¡JACKPOT! Ganaste S/ {premio}")
            self._creditos += premio
            self._total_ganado += premio
        elif resultado[0] == resultado[1] or resultado[1] == resultado[2] or resultado[0] == resultado[2]:
            premio = apuesta * 2
            print(f"✨ ¡Dos iguales! Ganaste S/ {premio}")
            self._creditos += premio
            self._total_ganado += premio
        else:
            print(f"😢 Perdiste S/ {apuesta}")
        return True

    def mostrar_estadisticas(self):
        print(f"   {self.nombre}")
        print(f"   Apostado: S/ {self._total_jugado} | Ganado: S/ {self._total_ganado}")
        balance = self._total_ganado - self._total_jugado
        signo = "+" if balance >= 0 else ""
        print(f"   Balance: S/ {signo}{balance} | Créditos actuales: S/ {self._creditos}")
        print()

class TragamonedasFrutas(Tragamonedas):
    def __init__(self, nombre, creditos):
        super().__init__(nombre, creditos)

    def girar(self):
        simbolos = ["🍒", "🍋", "🍊", "🍇", "🍉", "🍓"]
        resultado = []
        for _ in range(3):
            indice = random.randint(0, len(simbolos) - 1)
            resultado.append(simbolos[indice])
        print(f"[ {resultado[0]}  {resultado[1]}  {resultado[2]} ]")
        return resultado

class TragamonedasClasico(Tragamonedas):
    def __init__(self, nombre, creditos):
        super().__init__(nombre, creditos)

    def girar(self):
        simbolos = ["7️⃣", "💎", "🔔", "⭐", "💲", "🎰"]
        resultado = []
        for _ in range(3):
            indice = random.randint(0, len(simbolos) - 1)
            resultado.append(simbolos[indice])
        print(f"[ {resultado[0]}  {resultado[1]}  {resultado[2]} ]")
        return resultado

class TragamonedasMundial(Tragamonedas):
    def __init__(self, nombre, creditos):
        super().__init__(nombre, creditos)

    def girar(self):
        simbolos = ["🇵🇪", "🇦🇷", "🇫🇷", "🇧🇷", "🇪🇸", "🏴󠁧󠁢󠁥󠁮󠁧󠁿"]
        resultado = []
        for _ in range(3):
            indice = random.randint(0, len(simbolos) - 1)
            resultado.append(simbolos[indice])
        print(f"[ {resultado[0]}  {resultado[1]}  {resultado[2]} ]")
        return resultado

    def jugar(self, apuesta):
        if self._creditos == 0:
            print("💀 Esta máquina no tiene créditos.")
            return False
        if apuesta > self._creditos:
            print(f"❌ No tienes suficiente saldo. Créditos: {self._creditos}")
            return False

        self._creditos -= apuesta
        self._total_jugado += apuesta
        resultado = self.girar()
        tiene_peru = "🇵🇪" in resultado

        if resultado[0] == resultado[1] == resultado[2]:
            premio = apuesta * 15
            print(f"🏆 ¡TRIPLETE! Ganaste S/ {premio}")
            self._creditos += premio
            self._total_ganado += premio
        elif resultado[0] == resultado[1] or resultado[1] == resultado[2] or resultado[0] == resultado[2]:
            premio = apuesta * 2
            print(f"⚽ ¡Dos iguales! Ganaste S/ {premio}")
            self._creditos += premio
            self._total_ganado += premio
        elif tiene_peru:
            print(f"🇵🇪 ¡Perú apareció! Recuperas tu apuesta.")
            self._creditos += apuesta
        else:
            print(f"😢 Perdiste S/ {apuesta}")
        return True

def jugar_en_maquina(maquina):
    while maquina._creditos > 0:
        maquina.mostrar()
        try:
            apuesta = int(input("¿Cuánto apuestas? (0 para volver al casino): "))
        except ValueError:
            print("Ingresa un número válido.")
            continue

        if apuesta == 0:
            break

        maquina.jugar(apuesta)
        print()

# --- EJECUCIÓN PRINCIPAL DEL CASINO ---

maquinas = [
    TragamonedasFrutas("La Frutal", 200),
    TragamonedasClasico("La Clásica", 300),
    TragamonedasMundial("Mundial 2026", 150),
]

while True:
    print("\n" + "=" * 35)
    print("  🎰 CASINO ROYALE 🎰")
    print("=" * 35)

    for i, m in enumerate(maquinas, 1):
        estado = f"S/ {m._creditos}" if m._creditos > 0 else "💀 SIN CRÉDITOS"
        print(f"  {i}. {m.nombre} ({estado})")

    print(f"  {len(maquinas) + 1}. Mostrar estadísticas")
    print(f"  {len(maquinas) + 2}. Salir")

    try:
        opcion = int(input("\nElige una opción: "))
    except ValueError:
        print("Opción inválida.")
        continue

    if 1 <= opcion <= len(maquinas):
        maquina = maquinas[opcion - 1]
        if maquina._creditos == 0:
            print("💀 Esta máquina está sin créditos. Elige otra.")
        else:
            jugar_en_maquina(maquina)

    elif opcion == len(maquinas) + 1:
        print("\n📊 ESTADÍSTICAS DEL CASINO")
        print("-" * 35)
        for m in maquinas:
            m.mostrar_estadisticas()

    elif opcion == len(maquinas) + 2:
        print("\n💰 Gracias por visitar el Casino Royale. ¡Vuelve pronto!")
        break

    else:
        print("Opción inválida.")
