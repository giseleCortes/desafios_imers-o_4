import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

url = 'https://gist.githubusercontent.com/tgcsantos/3bdb29eba6ce391e90df2b72205ba891/raw' \
      '/22fa920e80c9fa209a9fccc8b52d74cc95d1599b/dados_imoveis.csv '
dados = pd.read_csv(url)
bairros_e_metragem = dados[['Bairro', 'Metragem']]


def media_metragem_bairros():
    # print(bairros_e_metragem)
    # print(bairros_e_metragem.groupby('Bairro').mean())
    media_por_bairro = (bairros_e_metragem.groupby('Bairro').mean())
    print(media_por_bairro)


if __name__ == '__main__':
    media_metragem_bairros()
