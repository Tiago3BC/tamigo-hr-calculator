import pandas as pd


def convert_to_float(value):
    if isinstance(value, str):
        return float(value.replace(",", "."))
    return value

def get_employee_names(filepath_or_file):
    names = []
    try:
        excel_file = pd.ExcelFile(filepath_or_file)
        for sheet_name in excel_file.sheet_names:
            df = pd.read_excel(excel_file, sheet_name=sheet_name, header=None)
            try:
                name = df.iloc[1, 2]
                names.append(name)
            except Exception as sheet_err:
                print(f"Erro ao ler C2 da folha '{sheet_name}': {sheet_err}")
                names.append(None)
    except Exception as e:
        print(f"Erro ao abrir o ficheiro Excel: {e}")
        return []

    return names

def get_departments(filepath_or_file):
    departments = []
    try:
        excel_file = pd.ExcelFile(filepath_or_file)
        for sheet_name in excel_file.sheet_names:
            df = pd.read_excel(excel_file, sheet_name=sheet_name, header=None)
            try:
                department = df.iloc[0, 2]
                departments.append(department)
            except Exception as sheet_err:
                print(f"Erro ao ler C1 da folha '{sheet_name}': {sheet_err}")
                departments.append(None)
    except Exception as e:
        print(f"Erro ao abrir o ficheiro Excel: {e}")
        return []

    return departments

def get_sub_almocos(filepath_or_file, nomes_disponiveis=None):
    sub_almocos = []
    try:
        excel_file = pd.ExcelFile(filepath_or_file)
        for sheet_name in excel_file.sheet_names:
            if nomes_disponiveis and sheet_name not in nomes_disponiveis:
                continue
            df = pd.read_excel(excel_file, sheet_name=sheet_name, header=None)
            try:
                sub_almoco = df.iloc[37, 11]
                sub_almocos.append(convert_to_float(sub_almoco))
            except Exception as sheet_err:
                print(f"Erro ao ler L38 da folha '{sheet_name}': {sheet_err}")
                sub_almocos.append(None)
    except Exception as e:
        print(f"Erro ao abrir o ficheiro Excel: {e}")
        return []
    return sub_almocos

def get_horas_noturnas(filepath_or_file, nomes_disponiveis=None):
    horas_noturnas = []
    try:
        excel_file = pd.ExcelFile(filepath_or_file)
        for sheet_name in excel_file.sheet_names:
            if nomes_disponiveis and sheet_name not in nomes_disponiveis:
                continue
            df = pd.read_excel(excel_file, sheet_name=sheet_name, header=None)
            try:
                hora_noturna = df.iloc[37, 12]
                horas_noturnas.append(convert_to_float(hora_noturna))
            except Exception as sheet_err:
                print(f"Erro ao ler M38 da folha '{sheet_name}': {sheet_err}")
                horas_noturnas.append(None)
    except Exception as e:
        print(f"Erro ao abrir o ficheiro Excel: {e}")
        return []
    return horas_noturnas

def get_gozo_ferias(filepath_or_file, nomes_disponiveis=None):
    gozo_ferias = []
    try:
        excel_file = pd.ExcelFile(filepath_or_file)
        for sheet_name in excel_file.sheet_names:
            if nomes_disponiveis and sheet_name not in nomes_disponiveis:
                continue
            df = pd.read_excel(excel_file, sheet_name=sheet_name, header=None)
            try:
                gozo_feria = df.iloc[37, 28]
                gozo_ferias.append(convert_to_float(gozo_feria))
            except Exception as sheet_err:
                print(f"Erro ao ler AC38 da folha '{sheet_name}': {sheet_err}")
                gozo_ferias.append(None)
    except Exception as e:
        print(f"Erro ao abrir o ficheiro Excel: {e}")
        return []
    return gozo_ferias