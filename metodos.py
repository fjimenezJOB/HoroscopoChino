import json

class Metodos:

    def calculo(self ,anyo):
        horoscopo = ['mono', 'gallo', 'perro', 'cerdo', 'rata', 'buey',
                     'tigre', 'gato', 'dragon', 'serpiente', 'caballo', 'cabra']
        resultado = anyo % 12
        animal = horoscopo[resultado]
        return (animal)
    

    def consultar(self ,animal):
        with open('descripciones.json', encoding='utf-8') as datos:
            contenido = json.load(datos)
            for i in range(0 , 12):
                if contenido[i]['animal'] == animal:
                    consulta = contenido[i]['texto']
        return consulta