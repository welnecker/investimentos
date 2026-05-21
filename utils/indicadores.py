def formatar_milhoes(valor):

    return f"{valor / 1000000:.2f} M"


# =========================================================
# STATUS
# =========================================================

def definir_status(row):

    if row["PVP"] < 0.95 and row["DY"] > 9:
        return "🟢 Comprar"

    elif row["PVP"] <= 1:
        return "🟡 Neutro"

    return "🔴 Caro"


# =========================================================
# COLORIR SCORE
# =========================================================

def colorir_score(val):

    if val >= 8:
        return "background-color: #14532d; color: white"

    elif val >= 5:
        return "background-color: #854d0e; color: white"

    return "background-color: #7f1d1d; color: white"
