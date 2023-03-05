import numpy as np


def compute_mse(theta_0, theta_1, data):
    """
    Calcula o erro quadratico medio
    :param theta_0: float - intercepto da reta
    :param theta_1: float -inclinacao da reta
    :param data: np.array - matriz com o conjunto de dados, x na coluna 0 e y na coluna 1
    :return: float - o erro quadratico medio
    """

    hSum = 0
    for coord in data:
        h0 = (theta_0 + theta_1 * coord[0]) - coord[1]
        hSum += (h0 ** 2)
    return hSum / len(data)


def step_gradient(theta_0, theta_1, data, alpha):
    """
    Executa uma atualização por descida do gradiente  e retorna os valores atualizados de theta_0 e theta_1.
    :param theta_0: float - intercepto da reta
    :param theta_1: float -inclinacao da reta
    :param data: np.array - matriz com o conjunto de dados, x na coluna 0 e y na coluna 1
    :param alpha: float - taxa de aprendizado (a.k.a. tamanho do passo)
    :return: float,float - os novos valores de theta_0 e theta_1, respectivamente
    """

    # gradiente theta0: 2/n*sum((h0*x)-y)
    # gradiente theta1: 2/n*sum((h0*x)-y)*x
    # atualizando o theta: theta = theta-alfa * grad

    h0 = 0
    h1 = 0
    for coord in data:
        h0 += (theta_0 + theta_1 * coord[0]) - coord[1]
        h1 += ((theta_0 + theta_1 * coord[0]) - coord[1]) * coord[0]
    gradTheta0 = 2 * h0 / len(data)
    gradTheta1 = 2 * h1 / len(data)

    return theta_0 - alpha * gradTheta0, theta_1 - alpha * gradTheta1


def fit(data, theta_0, theta_1, alpha, num_iterations):
    """
    Para cada época/iteração, executa uma atualização por descida de
    gradiente e registra os valores atualizados de theta_0 e theta_1.
    Ao final, retorna duas listas, uma com os theta_0 e outra com os theta_1
    obtidos ao longo da execução (o último valor das listas deve
    corresponder à última época/iteração).

    :param data: np.array - matriz com o conjunto de dados, x na coluna 0 e y na coluna 1
    :param theta_0: float - intercepto da reta
    :param theta_1: float -inclinacao da reta
    :param alpha: float - taxa de aprendizado (a.k.a. tamanho do passo)
    :param num_iterations: int - numero de épocas/iterações para executar a descida de gradiente
    :return: list,list - uma lista com os theta_0 e outra com os theta_1 obtidos ao longo da execução
    """

    lstTheta0 = []
    lstTheta1 = []
    for i in range(num_iterations):
        theta_0, theta_1 = step_gradient(theta_0, theta_1, data, alpha)
        lstTheta0.append(theta_0)
        lstTheta1.append(theta_1)

    return lstTheta0, lstTheta1
