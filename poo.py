class Personaje:
    def __init__(self, nombre, salud, ataque):
        self.nombre = nombre
        self.salud = salud
        self.ataque = ataque
        self.inventario = []  

    def atacar(self, enemigo):
        print(f"{self.nombre} ataca a {enemigo.nombre} causando {self.ataque} puntos de daño.")
        enemigo.salud -= self.ataque
        if enemigo.salud < 0:
            enemigo.salud = 0

    def curarse(self, puntos_curacion):
        self.salud += puntos_curacion
        print(f"{self.nombre} se cura {puntos_curacion} puntos. Salud actual: {self.salud}")

    def mostrar_estado(self):
        print(f"--- Estado de {self.nombre} ---")
        print(f"Salud: {self.salud}")
        print(f"Ataque: {self.ataque}")
        print(f"Inventario: {self.inventario}\n")

    def recoger_objeto(self, objeto):
        self.inventario.append(objeto)
        print(f"{self.nombre} ha recogido: {objeto}")


class Enemigo:
    def __init__(self, nombre, salud, ataque):
        self.nombre = nombre
        self.salud = salud
        self.ataque = ataque

    def atacar(self, personaje):
        print(f"{self.nombre} ataca a {personaje.nombre} causando {self.ataque} puntos de daño.")
        personaje.salud -= self.ataque
        if personaje.salud < 0:
            personaje.salud = 0

    def mostrar_estado(self):
        print(f"--- Estado de {self.nombre} ---")
        print(f"Salud: {self.salud}")
        print(f"Ataque: {self.ataque}\n")


heroe = Personaje("Aventurero", 100, 20)
enemigo1 = Enemigo("Enemigo", 80, 15)

heroe.mostrar_estado()
enemigo1.mostrar_estado()

heroe.atacar(enemigo1)
enemigo1.mostrar_estado()

enemigo1.atacar(heroe)
heroe.mostrar_estado()

heroe.curarse(10)
heroe.recoger_objeto("Espada mágica")
heroe.mostrar_estado()
