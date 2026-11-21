"""
Reto Integrador: Sistema de Tragamonedas con Programación Orientada a Objetos (POO)
Curso de Programación en Python

Este script integra las 5 partes del taller:
1. Clase base Tragamonedas y constructor (__init__)
2. Generación aleatoria de símbolos (random)
3. Lógica de apuestas y premios (jugar)
4. Herencia y Polimorfismo (Frutas, Clásico y Mundial 2026)
5. Encapsulación (_creditos) y menú multi-máquina con estadísticas
"""

import random


class Tragamonedas:
    """Clase base que modela una máquina tragamonedas estándar."""

    def __init__(self, nombre, creditos):
        self.nombre = nombre
        self._creditos = creditos
        self._total_jugado = 0
        self._total_ganado = 0

    def mostrar(self):
        """Muestra el nombre de la máquina y su saldo disponible."""
        estado = f"S/ {self._creditos}" if self._creditos > 0 else "💀 SIN CRÉDITOS"
        print(f"🎰 {self.nombre} — {estado}")

    def girar(self):
        """Genera y muestra 3 símbolos aleatorios."""
        simbolos = ["🍒", "🔔", "💎", "🍀", "⭐", "7️⃣"]
        resultado = []
        for _ in range(3):
            indice = random.randint(0, len(simbolos) - 1)
            resultado.append(simbolos[indice])
        print(f"[ {resultado[0]}  {resultado[1]}  {resultado[2]} ]")
        return resultado

    def jugar(self, apuesta):
        """Procesa una apuesta, gira los rodillos y calcula los premios."""
        if self._creditos == 0:
            print("💀 Esta máquina no tiene créditos.")
            return False
        if apuesta <= 0:
            print("⚠️ La apuesta debe ser mayor a 0.")
            return False
        if apuesta > self._creditos:
            print(f"❌ No tienes suficiente saldo. Créditos: S/ {self._creditos}")
            return False

        self._creditos -= apuesta
        self._total_jugado += apuesta
        resultado = self.girar()

        if resultado[0] == resultado[1] == resultado[2]:
            premio = apuesta * 10
            print(f"🎉 ¡JACKPOT! Ganaste S/ {premio}")
            self._creditos += premio
            self._total_ganado += premio
        elif (
            resultado[0] == resultado[1]
            or resultado[1] == resultado[2]
            or resultado[0] == resultado[2]
        ):
            premio = apuesta * 2
            print(f"✨ ¡Dos iguales! Ganaste S/ {premio}")
            self._creditos += premio
            self._total_ganado += premio
        else:
            print(f"😢 Perdiste S/ {apuesta}")
        return True

    def mostrar_estadisticas(self):
        """Imprime el resumen financiero encapsulado de la máquina."""
        print(f"   🎰 {self.nombre}")
        print(f"   Apostado: S/ {self._total_jugado} | Ganado: S/ {self._total_ganado}")
        balance = self._total_ganado - self._total_jugado
        signo = "+" if balance >= 0 else ""
        print(f"   Balance:  S/ {signo}{balance} | Créditos actuales: S/ {self._creditos}")
        print()


class TragamonedasFrutas(Tragamonedas):
    """Subclase temática de frutas."""

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
    """Subclase temática de casino clásico."""

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
    """Subclase personalizada (Reto 4B) con temática del Mundial y reglas especiales."""

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
        """Sobrescribe las reglas: Triplete paga x15 y si sale 🇵🇪 se recupera la apuesta."""
        if self._creditos == 0:
            print("💀 Esta máquina no tiene créditos.")
            return False
        if apuesta <= 0:
            print("⚠️ La apuesta debe ser mayor a 0.")
            return False
        if apuesta > self._creditos:
            print(f"❌ No tienes suficiente saldo. Créditos: S/ {self._creditos}")
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
        elif (
            resultado[0] == resultado[1]
            or resultado[1] == resultado[2]
            or resultado[0] == resultado[2]
        ):
            premio = apuesta * 2
            print(f"⚽ ¡Dos iguales! Ganaste S/ {premio}")
            self._creditos += premio
            self._total_ganado += premio
        elif tiene_peru:
            print("🇵🇪 ¡Perú apareció! Recuperas tu apuesta.")
            self._creditos += apuesta
        else:
            print(f"😢 Perdiste S/ {apuesta}")
        return True


def jugar_en_maquina(maquina):
    """Bucle de apuestas dentro de una máquina seleccionada."""
    while maquina._creditos > 0:
        maquina.mostrar()
        try:
            apuesta = int(input("¿Cuánto apuestas? (0 para volver al casino): "))
        except ValueError:
            print("⚠️ Ingresa un número válido.")
            continue

        if apuesta == 0:
            break

        maquina.jugar(apuesta)
        print()
    else:
        print(f"💸 {maquina.nombre} se quedó sin créditos. ¡GAME OVER en esta máquina!")


def main():
    """Función principal que administra el menú del Casino Royale."""
    maquinas = [
        TragamonedasFrutas("La Frutal", 200),
        TragamonedasClasico("La Clásica", 300),
        TragamonedasMundial("Mundial 2026", 150),
    ]

    while True:
        print("\n" + "=" * 38)
        print("         🎰 CASINO ROYALE 🎰")
        print("=" * 38)

        for i, m in enumerate(maquinas, 1):
            estado = f"S/ {m._creditos}" if m._creditos > 0 else "💀 SIN CRÉDITOS"
            print(f"  {i}. {m.nombre} ({estado})")

        print(f"  {len(maquinas) + 1}. Mostrar estadísticas de todas")
        print(f"  {len(maquinas) + 2}. Salir")

        try:
            opcion = int(input("\nElige una opción: "))
        except ValueError:
            print("⚠️ Opción inválida. Ingresa un número.")
            continue

        if 1 <= opcion <= len(maquinas):
            maquina_elegida = maquinas[opcion - 1]
            if maquina_elegida._creditos == 0:
                print("💀 Esta máquina está sin créditos. Elige otra.")
            else:
                jugar_en_maquina(maquina_elegida)

        elif opcion == len(maquinas) + 1:
            print("\n📊 ESTADÍSTICAS DEL CASINO")
            print("-" * 38)
            for m in maquinas:
                m.mostrar_estadisticas()

        elif opcion == len(maquinas) + 2:
            print("\n📊 RESUMEN FINAL DE TU VISITA:")
            print("-" * 38)
            for m in maquinas:
                m.mostrar_estadisticas()
            print("💰 Gracias por visitar el Casino Royale. ¡Vuelve pronto!")
            break

        else:
            print("⚠️ Opción fuera de rango.")


if __name__ == "__main__":
    main()