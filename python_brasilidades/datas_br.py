from datetime import datetime, timedelta

class DatasBr:
    def __init__(self) -> None:
        self.momento_cadastro = datetime.today()
    
    def __str__(self) -> str:
        return self.format_data()

    def tempo_cadastro(self):
        tempo_cadastro = (datetime.today() +timedelta(days=30))- self.momento_cadastro
        return tempo_cadastro

    def mes_cadastro(self):
        meses_do_ano = (
            'janeiro', 'fevereiro', 'marco,', 'abril', 'maio',
            'junho', 'julho', 'agosto', 'setembro',
            'outubro', 'novembro', 'dezembro'
        )

        mes_cadastro = self.momento_cadastro.month
        return meses_do_ano[mes_cadastro -1]

    def dia_semana(self):
        dia_semana_lista = (
            'segunda', 'terça', 'quarta', 'quinta', 'sexta',
            'sabado', 'domingo'
        )

        dia = self.momento_cadastro.weekday()
        return dia_semana_lista[dia -1]

    def format_data(self):
        string_data = self.momento_cadastro.strftime("%d/%m/%Y %H:%M")
        return string_data

