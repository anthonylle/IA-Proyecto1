'''from ..pruebas import normalizer_data

def main():
    normalizer_data()
    
if __name__ == "__main__":
    main()    '''
from NeuralNetwork.NeuralNetwork import NeuralNetwork
import argparse

parser = argparse.ArgumentParser(description="Programa de predicción de datos utilizando Random Forests o Redes Neuronales", epilog="Eso es todo amigos")

forests_group = parser.add_argument_group("Random Forests")
net_group = parser.add_argument_group("Red Neuronal")

forests_group.add_argument("--arbol", help="El modelo por utilizar será: Random Forests", action="store_true")
forests_group.add_argument("--umbral-poda", type=float, default=0.5, metavar='', help="Ganancia mínima requerida para realizar una partición")

net_group.add_argument("--red-neuronal", help="El modelo por utilizar será: Red Neuronal", action="store_true")
net_group.add_argument("--numero-capas", type=int, default=1, metavar='', help="Cantidad de capas creadas en la Red Neuronal")
net_group.add_argument("--unidades-por-capa", type=int, default=1, metavar='', help="Cantidad de neuronas por capa en la Red Neuronal")
net_group.add_argument("--funcion-activacion", type=str, default='relu', metavar='', help='Define la salida de los nodos en una Red Neuronal para un conjunto de entradas dado')

args = parser.parse_args()

if args.arbol:
    print("Arbol has been chosen")


elif args.red_neuronal:
    model = NeuralNetwork()
    model.create_model(kwargs={"layers": args.numero_capas, "units": args.unidades_por_capa, "activation": args.funcion_activacion})
    model.train_model()
    print(model.evaluate_model())

else:
    print("Debe elegir --arbol o sino --red-neuronal")
