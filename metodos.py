class Metodos:

    def __init__(self, anyo):
        self.anyo = anyo

    def calculo(self):
        horoscopo = ['mono', 'gallo', 'perro', 'cerdo', 'rata', 'buey',
                     'tigre', 'gato', 'dragon', 'serpiente', 'caballo', 'cabra']
        resultado = self.anyo % 12
        animal = horoscopo[resultado]
        return (animal)
