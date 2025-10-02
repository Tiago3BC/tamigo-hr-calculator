import pandas as pd


def convert_to_float(value):
    if isinstance(value, str):
        value = value.strip().replace(",", ".")
        try:
            return float(value)
        except ValueError:
            return None
    return value if isinstance(value, (int, float)) else None


def get_employee_names(filepath_or_file):
    names = []
    try:
        excel_file = pd.ExcelFile(filepath_or_file)
        for sheet_name in excel_file.sheet_names:
            df = pd.read_excel(
                excel_file, sheet_name=sheet_name, header=None, engine="openpyxl"
            )
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
            df = pd.read_excel(
                excel_file, sheet_name=sheet_name, header=None, engine="openpyxl"
            )
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


def get_unique_departments(filepath_or_file):
    departments = get_departments(filepath_or_file)
    unique_departments = list(set(departments))
    return unique_departments


def get_date(filepath_or_file):
    date = []
    try:
        excel_file = pd.ExcelFile(filepath_or_file)
        for sheet_name in excel_file.sheet_names:
            df = pd.read_excel(
                excel_file, sheet_name=sheet_name, header=None, engine="openpyxl"
            )
            try:
                date_value = df.iloc[2, 2]
                date.append(date_value)
            except Exception as sheet_err:
                print(f"Erro ao ler B1 da folha '{sheet_name}': {sheet_err}")
                date.append(None)
    except Exception as e:
        print(f"Erro ao abrir o ficheiro Excel: {e}")
        return []
    return date


def get_unique_date(filepath_or_file):
    dates = get_date(filepath_or_file)
    unique_dates = list(set(dates))
    return unique_dates


def get_sub_almocos(filepath_or_file, nomes_disponiveis=None):
    sub_almocos = []
    try:
        excel_file = pd.ExcelFile(filepath_or_file)
        for sheet_name in excel_file.sheet_names:
            if nomes_disponiveis and sheet_name not in nomes_disponiveis:
                continue
            df = pd.read_excel(
                excel_file, sheet_name=sheet_name, header=None, engine="openpyxl"
            )
            try:
                coluna_index = 11  # Coluna L
                valores_validos = []

                for row in range(len(df)):
                    valor = df.iloc[row, coluna_index]
                    valor_float = convert_to_float(valor)
                    if isinstance(valor_float, (int, float)) and not pd.isna(
                        valor_float
                    ):
                        valores_validos.append(valor_float)

                if valores_validos:
                    sub_almocos.append(max(valores_validos))
                    print(
                        f"Folha: {sheet_name} | Máximo encontrado em Subsídios de Almoço: {max(valores_validos)}"
                    )
                else:
                    sub_almocos.append(None)

            except Exception as sheet_err:
                print(
                    f"Erro ao processar coluna L da folha '{sheet_name}': {sheet_err}"
                )
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
            df = pd.read_excel(
                excel_file, sheet_name=sheet_name, header=None, engine="openpyxl"
            )
            try:
                coluna_index = 12  # Coluna M
                valores_validos = []

                for row in range(len(df)):
                    valor = df.iloc[row, coluna_index]
                    valor_float = convert_to_float(valor)
                    if isinstance(valor_float, (int, float)) and not pd.isna(
                        valor_float
                    ):
                        valores_validos.append(valor_float)

                if valores_validos:
                    horas_noturnas.append(max(valores_validos))
                    print(
                        f"Folha: {sheet_name} | Máximo encontrado em Horas Noturnas: {max(valores_validos)}"
                    )
                else:
                    horas_noturnas.append(None)

            except Exception as sheet_err:
                print(
                    f"Erro ao processar coluna M da folha '{sheet_name}': {sheet_err}"
                )
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
            df = pd.read_excel(
                excel_file, sheet_name=sheet_name, header=None, engine="openpyxl"
            )
            try:
                coluna_index = 28  # Coluna AC
                valores_validos = []

                for row in range(len(df)):
                    valor = df.iloc[row, coluna_index]
                    valor_float = convert_to_float(valor)
                    if isinstance(valor_float, (int, float)) and not pd.isna(
                        valor_float
                    ):
                        valores_validos.append(valor_float)

                if valores_validos:
                    gozo_ferias.append(max(valores_validos))
                    print(
                        f"Folha: {sheet_name} | Máximo encontrado em Férias: {max(valores_validos)}"
                    )
                else:
                    gozo_ferias.append(None)

            except Exception as sheet_err:
                print(
                    f"Erro ao processar coluna AC da folha '{sheet_name}': {sheet_err}"
                )
                gozo_ferias.append(None)
    except Exception as e:
        print(f"Erro ao abrir o ficheiro Excel: {e}")
        return []
    return gozo_ferias


# def get_horas_noturnas(filepath_or_file, nomes_disponiveis=None):
#     horas_noturnas = []
#     try:
#         excel_file = pd.ExcelFile(filepath_or_file)
#         for sheet_name in excel_file.sheet_names:
#             if nomes_disponiveis and sheet_name not in nomes_disponiveis:
#                 continue
#             df = pd.read_excel(
#                 excel_file, sheet_name=sheet_name, header=None, engine="openpyxl"
#             )
#             try:
#                 hora_noturna = df.iloc[37, 12]
#                 horas_noturnas.append(convert_to_float(hora_noturna))
#             except Exception as sheet_err:
#                 print(f"Erro ao ler M38 da folha '{sheet_name}': {sheet_err}")
#                 horas_noturnas.append(None)
#     except Exception as e:
#         print(f"Erro ao abrir o ficheiro Excel: {e}")
#         return []
#     return horas_noturnas


# def get_gozo_ferias(filepath_or_file, nomes_disponiveis=None):
#     gozo_ferias = []
#     try:
#         excel_file = pd.ExcelFile(filepath_or_file)
#         for sheet_name in excel_file.sheet_names:
#             if nomes_disponiveis and sheet_name not in nomes_disponiveis:
#                 continue
#             df = pd.read_excel(
#                 excel_file, sheet_name=sheet_name, header=None, engine="openpyxl"
#             )
#             try:
#                 gozo_feria = df.iloc[37, 28]
#                 gozo_ferias.append(convert_to_float(gozo_feria))
#             except Exception as sheet_err:
#                 print(f"Erro ao ler AC38 da folha '{sheet_name}': {sheet_err}")
#                 gozo_ferias.append(None)
#     except Exception as e:
#         print(f"Erro ao abrir o ficheiro Excel: {e}")
#         return []
#     return gozo_ferias
