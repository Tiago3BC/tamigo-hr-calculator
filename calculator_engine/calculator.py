from utils.helpers import get_sub_almocos
from utils.helpers import get_horas_noturnas
from utils.helpers import get_gozo_ferias
import math
import pandas as pd

def calcular_total_sub_almocos(filepath_or_file, nomes_selecionados):
    sub_almoco = get_sub_almocos(filepath_or_file, nomes_disponiveis=nomes_selecionados)
    valores_validos = [a for a in sub_almoco if isinstance(a, (int, float)) and pd.notna(a)]
    return sum(valores_validos) if valores_validos else 0.0


def calcular_total_horas_noturnas(filepath_or_file, nomes_selecionados):
    hora_noturna = get_horas_noturnas(
        filepath_or_file, nomes_disponiveis=nomes_selecionados
    )
    total_hora_noturnas = sum(
        h for h in hora_noturna if isinstance(h, (int, float)) and not math.isnan(h)
    )
    return total_hora_noturnas


def calcular_total_gozo_ferias(filepath_or_file, nomes_selecionados):
    gozo_feria = get_gozo_ferias(filepath_or_file, nomes_disponiveis=nomes_selecionados)
    total_gozo_ferias = sum(
        f for f in gozo_feria if isinstance(f, (int, float)) and not math.isnan(f)
    )
    return total_gozo_ferias
