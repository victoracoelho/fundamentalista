import pandas as pd

class findata():
    """
    This class will return financial data for listed companies in B3 (Brazil)
    """


    def dre(tick=''):
        """
        :return: Retorna a DRE da empresa definida
        """
        lista_18 = []
        lista_19 = []
        date19_list = ['01/01/2019 a 31/12/2019 (R$ mil)', '01/01/2019 a 30/09/2019 (R$ mil)']
        date18_list = ['01/01/2018 a 31/12/2018 (R$ mil)', '01/01/2018 a 30/09/2018 (R$ mil)']
        site = 'https://www.investsite.com.br/demonstracao_resultado.php?cod_negociacao='
        link = site + tick
        df = pd.read_html(link)
        dre = df[1]
        for pos in date18_list:
            if pos in dre:
                serie_18 = dre[pos][1:]
        transform_18 = list(serie_18)
        for t in transform_18:
            if len(t) == 1:
                lista_18.append(t[:1])
            if len(t) == 2:
                lista_18.append(t[:1])
            if len(t) == 3:
                lista_18.append(t[:2])
            if len(t) == 4:
                lista_18.append(t[:2])
            if len(t) == 5:
                lista_18.append(t[:1])
            if len(t) == 6:
                lista_18.append(t[:2])
            if len(t) == 7:
                lista_18.append(t[:3])
            if len(t) == 8:
                lista_18.append(t[:4])
            if len(t) == 9:
                lista_18.append(t[:5])
            if len(t) == 10:
                lista_18.append(t[:6])
            if len(t) == 12:
                lista_18.append(t[:8])
            if len(t) == 11:
                lista_18.append(t[:7])
        to_float_18 = [float(i) for i in lista_18]
        for pos in date19_list:
            if pos in dre:
                serie_19 = dre[pos][1:]
        transform_19 = list(serie_19)
        for t in transform_19:
            if len(t) == 1:
                lista_19.append(t[:1])
            if len(t) == 2:
                lista_19.append(t[:1])
            if len(t) == 3:
                lista_19.append(t[:2])
            if len(t) == 4:
                lista_19.append(t[:2])
            if len(t) == 5:
                lista_19.append(t[:1])
            if len(t) == 6:
                lista_19.append(t[:2])
            if len(t) == 7:
                lista_19.append(t[:3])
            if len(t) == 8:
                lista_19.append(t[:4])
            if len(t) == 9:
                lista_19.append(t[:5])
            if len(t) == 10:
                lista_19.append(t[:6])
            if len(t) == 12:
                lista_19.append(t[:8])
            if len(t) == 11:
                lista_19.append(t[:7])
        to_float_19 = [float(i) for i in lista_19]
        new_df = pd.DataFrame(dre['Descrição'][0:])
        new_df['2019'] = pd.DataFrame(to_float_19)
        new_df['2018'] = pd.DataFrame(to_float_18)
        new_df['Descrição'] = new_df['Descrição'].shift(-1)
        return new_df


    def bpa(tick=''):
        """

        :return: Retorna o Balanço Patrimonial do Ativo da empresa definida
        """
        lista_18 = []
        lista_19 = []
        date19_list = ['31/12/2019 (R$ mil)', '30/09/2019 (R$ mil)']
        date18_list = ['31/12/2018 (R$ mil)', '30/09/2018 (R$ mil)']
        site = 'https://www.investsite.com.br/balanco_patrimonial_ativo.php?cod_negociacao='
        link = site + tick
        df = pd.read_html(link)
        dre = df[1]
        for pos in date18_list:
            if pos in dre:
                serie_18 = dre[pos][1:]
        transform_18 = list(serie_18)
        for t in transform_18:
            if len(t) == 1:
                lista_18.append(t[:1])
            if len(t) == 2:
                lista_18.append(t[:1])
            if len(t) == 3:
                lista_18.append(t[:2])
            if len(t) == 4:
                lista_18.append(t[:2])
            if len(t) == 5:
                lista_18.append(t[:2])
            if len(t) == 6:
                lista_18.append(t[:2])
            if len(t) == 7:
                lista_18.append(t[:3])
            if len(t) == 8:
                lista_18.append(t[:4])
            if len(t) == 9:
                lista_18.append(t[:5])
            if len(t) == 10:
                lista_18.append(t[:6])
            if len(t) == 12:
                lista_18.append(t[:8])
            if len(t) == 11:
                lista_18.append(t[:7])
        to_float_18 = [float(i) for i in lista_18]
        for pos in date19_list:
            if pos in dre:
                serie_19 = dre[pos][1:]
        transform_19 = list(serie_19)
        for t in transform_19:
            if len(t) == 1:
                lista_19.append(t[:1])
            if len(t) == 2:
                lista_19.append(t[:1])
            if len(t) == 3:
                lista_19.append(t[:2])
            if len(t) == 4:
                lista_19.append(t[:2])
            if len(t) == 5:
                lista_19.append(t[:1])
            if len(t) == 6:
                lista_19.append(t[:2])
            if len(t) == 7:
                lista_19.append(t[:3])
            if len(t) == 8:
                lista_19.append(t[:4])
            if len(t) == 9:
                lista_19.append(t[:5])
            if len(t) == 10:
                lista_19.append(t[:6])
            if len(t) == 12:
                lista_19.append(t[:8])
            if len(t) == 11:
                lista_19.append(t[:7])
        to_float_19 = [float(i) for i in lista_19]
        new_df = pd.DataFrame(dre['Descrição'][0:])
        new_df['2019'] = pd.DataFrame(to_float_19)
        new_df['2018'] = pd.DataFrame(to_float_18)
        new_df['Descrição'] = new_df['Descrição'].shift(-1)
        return new_df


    def bpp(tick=''):
        """

        :return: Retorna o Balanço Patrimonial do Passivo da empresa definida
        """
        lista_18 = []
        lista_19 = []
        date19_list = ['31/12/2019 (R$ mil)', '30/09/2019 (R$ mil)']
        date18_list = ['31/12/2018 (R$ mil)', '30/09/2018 (R$ mil)']
        site = 'https://www.investsite.com.br/balanco_patrimonial_passivo.php?cod_negociacao='
        link = site + tick
        df = pd.read_html(link)
        dre = df[1]
        for pos in date18_list:
            if pos in dre:
                serie_18 = dre[pos][1:]
        transform_18 = list(serie_18)
        for t in transform_18:
            if len(t) == 1:
                lista_18.append(t[:1])
            if len(t) == 2:
                lista_18.append(t[:1])
            if len(t) == 3:
                lista_18.append(t[:2])
            if len(t) == 4:
                lista_18.append(t[:2])
            if len(t) == 5:
                lista_18.append(t[:2])
            if len(t) == 6:
                lista_18.append(t[:2])
            if len(t) == 7:
                lista_18.append(t[:3])
            if len(t) == 8:
                lista_18.append(t[:4])
            if len(t) == 9:
                lista_18.append(t[:5])
            if len(t) == 10:
                lista_18.append(t[:6])
            if len(t) == 12:
                lista_18.append(t[:8])
            if len(t) == 11:
                lista_18.append(t[:7])
        to_float_18 = [float(i) for i in lista_18]
        for pos in date19_list:
            if pos in dre:
                serie_19 = dre[pos][1:]
        transform_19 = list(serie_19)
        for t in transform_19:
            if len(t) == 1:
                lista_19.append(t[:1])
            if len(t) == 2:
                lista_19.append(t[:1])
            if len(t) == 3:
                lista_19.append(t[:2])
            if len(t) == 4:
                lista_19.append(t[:2])
            if len(t) == 5:
                lista_19.append(t[:1])
            if len(t) == 6:
                lista_19.append(t[:2])
            if len(t) == 7:
                lista_19.append(t[:3])
            if len(t) == 8:
                lista_19.append(t[:4])
            if len(t) == 9:
                lista_19.append(t[:5])
            if len(t) == 10:
                lista_19.append(t[:6])
            if len(t) == 12:
                lista_19.append(t[:8])
            if len(t) == 11:
                lista_19.append(t[:7])
        to_float_19 = [float(i) for i in lista_19]
        new_df = pd.DataFrame(dre['Descrição'][0:])
        new_df['2019'] = pd.DataFrame(to_float_19)
        new_df['2018'] = pd.DataFrame(to_float_18)
        new_df['Descrição'] = new_df['Descrição'].shift(-1)
        return new_df



    def fca(tick=''):
        """

        :return: Retorna o Fluxo de Caixa da empresa definida
        """
        lista_18 = []
        lista_19 = []
        date19_list = ['01/01/2019 a 31/12/2019 (R$ mil)', '01/01/2019 a 30/09/2019 (R$ mil)']
        date18_list = ['01/01/2018 a 31/12/2018 (R$ mil)', '01/01/2018 a 30/09/2018 (R$ mil)']
        site = 'https://www.investsite.com.br/fluxo_caixa.php?cod_negociacao='
        link = site + tick
        df = pd.read_html(link)
        dre = df[1]
        for pos in date18_list:
            if pos in dre:
                serie_18 = dre[pos][1:]
        transform_18 = list(serie_18)
        for t in transform_18:
            if len(t) == 1:
                lista_18.append(t[:1])
            if len(t) == 2:
                lista_18.append(t[:1])
            if len(t) == 3:
                lista_18.append(t[:2])
            if len(t) == 4:
                lista_18.append(t[:2])
            if len(t) == 5:
                lista_18.append(t[:1])
            if len(t) == 6:
                lista_18.append(t[:2])
            if len(t) == 7:
                lista_18.append(t[:3])
            if len(t) == 8:
                lista_18.append(t[:4])
            if len(t) == 9:
                lista_18.append(t[:5])
            if len(t) == 10:
                lista_18.append(t[:6])
            if len(t) == 12:
                lista_18.append(t[:8])
            if len(t) == 11:
                lista_18.append(t[:7])
        to_float_18 = [float(i) for i in lista_18]
        for pos in date19_list:
            if pos in dre:
                serie_19 = dre[pos][1:]
        transform_19 = list(serie_19)
        for t in transform_19:
            if len(t) == 1:
                lista_19.append(t[:1])
            if len(t) == 2:
                lista_19.append(t[:1])
            if len(t) == 3:
                lista_19.append(t[:2])
            if len(t) == 4:
                lista_19.append(t[:2])
            if len(t) == 5:
                lista_19.append(t[:1])
            if len(t) == 6:
                lista_19.append(t[:2])
            if len(t) == 7:
                lista_19.append(t[:3])
            if len(t) == 8:
                lista_19.append(t[:4])
            if len(t) == 9:
                lista_19.append(t[:5])
            if len(t) == 10:
                lista_19.append(t[:6])
            if len(t) == 12:
                lista_19.append(t[:8])
            if len(t) == 11:
                lista_19.append(t[:7])
        to_float_19 = [float(i) for i in lista_19]
        new_df = pd.DataFrame(dre['Descrição'][0:])
        new_df['2019'] = pd.DataFrame(to_float_19)
        new_df['2018'] = pd.DataFrame(to_float_18)
        new_df['Descrição'] = new_df['Descrição'].shift(-1)
        return new_df



    def dva(tick=''):
        """

        :return: Retorna a Demonstração do Valor Adicionado da empresa definida
        """
        lista_18 = []
        lista_19 = []
        date19_list = ['01/01/2019 a 31/12/2019 (R$ mil)', '01/01/2019 a 30/09/2019 (R$ mil)']
        date18_list = ['01/01/2018 a 31/12/2018 (R$ mil)', '01/01/2018 a 30/09/2018 (R$ mil)']
        site = 'https://www.investsite.com.br/demonstracao_valor_adicionado.php?cod_negociacao='
        link = site + tick
        df = pd.read_html(link)
        dre = df[1]
        for pos in date18_list:
            if pos in dre:
                serie_18 = dre[pos][1:]
        transform_18 = list(serie_18)
        for t in transform_18:
            if len(t) == 1:
                lista_18.append(t[:1])
            if len(t) == 2:
                lista_18.append(t[:1])
            if len(t) == 3:
                lista_18.append(t[:2])
            if len(t) == 4:
                lista_18.append(t[:2])
            if len(t) == 5:
                lista_18.append(t[:1])
            if len(t) == 6:
                lista_18.append(t[:2])
            if len(t) == 7:
                lista_18.append(t[:3])
            if len(t) == 8:
                lista_18.append(t[:4])
            if len(t) == 9:
                lista_18.append(t[:5])
            if len(t) == 10:
                lista_18.append(t[:6])
            if len(t) == 12:
                lista_18.append(t[:8])
            if len(t) == 11:
                lista_18.append(t[:7])
        to_float_18 = [float(i) for i in lista_18]
        for pos in date19_list:
            if pos in dre:
                serie_19 = dre[pos][1:]
        transform_19 = list(serie_19)
        for t in transform_19:
            if len(t) == 1:
                lista_19.append(t[:1])
            if len(t) == 2:
                lista_19.append(t[:1])
            if len(t) == 3:
                lista_19.append(t[:2])
            if len(t) == 4:
                lista_19.append(t[:2])
            if len(t) == 5:
                lista_19.append(t[:1])
            if len(t) == 6:
                lista_19.append(t[:2])
            if len(t) == 7:
                lista_19.append(t[:3])
            if len(t) == 8:
                lista_19.append(t[:4])
            if len(t) == 9:
                lista_19.append(t[:5])
            if len(t) == 10:
                lista_19.append(t[:6])
            if len(t) == 12:
                lista_19.append(t[:8])
            if len(t) == 11:
                lista_19.append(t[:7])
        to_float_19 = [float(i) for i in lista_19]
        new_df = pd.DataFrame(dre['Descrição'][0:])
        new_df['2019'] = pd.DataFrame(to_float_19)
        new_df['2018'] = pd.DataFrame(to_float_18)
        new_df['Descrição'] = new_df['Descrição'].shift(-1)
        return new_df

