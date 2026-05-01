# chartsGen.py
import json
import matplotlib.pyplot as plt
from pathlib import Path

# 1. Defina a função UMA VEZ no topo para evitar o erro de "obscured declaration"
def make_autopct(values):
    def my_autopct(pct):
        total = sum(values)
        val = int(round(pct*total/100.0))
        return f"{val}" if val > 0 else ""
    return my_autopct

# Diretório de saída
output_dir = Path("static/stats")
output_dir.mkdir(parents=True, exist_ok=True)

# Configuração global de estilo
plt.rcParams["figure.facecolor"] = "#0c1116"
plt.rcParams["axes.facecolor"] = "#0c1116"
plt.rcParams["savefig.facecolor"] = "#0c1116"
plt.rcParams["axes.edgecolor"] = "#0c1116"

# Carrega dados
with open("cvestats.json") as f:
    data = json.load(f)

# =====================================================
# 1) Gráfico: Top Finders (doughnut)
# =====================================================
top_finders = data["top_finders"]["data"]
labels = list(top_finders.keys())
values = list(top_finders.values())
colors = data["top_finders"]["colors"]

fig, ax = plt.subplots(figsize=(8, 6))
# Usamos o _ para ignorar o erro de tipagem do corretor se necessário
wedges, texts, autotexts = ax.pie(
    values,
    autopct=make_autopct(values),
    labels=None,
    colors=colors,
    wedgeprops=dict(width=0.35, edgecolor="white")
)

for t in autotexts:
    t.set_color("white")
    t.set_fontsize(11)

leg = ax.legend(
    wedges, labels,
    loc="center left", bbox_to_anchor=(1, 0.5),
    facecolor="#0c1116", labelcolor="white"
)
plt.savefig(output_dir / "topFinderss.png", dpi=120, bbox_inches="tight")
plt.close()

# =====================================================
# 2) Gráfico: Total CVEs por Ano (linha)
# =====================================================
total_by_year = data["total_by_year"]
labels = list(total_by_year.keys())
values = list(total_by_year.values())

fig, ax = plt.subplots(figsize=(7, 4))
ax.plot(labels, values, marker="o", color="#e918d5", linewidth=2)

ax.set_ylabel("Qtd", color="white")
ax.tick_params(colors="white")
ax.spines[:].set_visible(False)

for i, v in enumerate(values):
    ax.text(i, v + 2, str(v), color="white", ha="center", fontsize=10)

plt.savefig(output_dir / "totalCVEsRegistred.png", dpi=120, bbox_inches="tight")
plt.close()

# =====================================================
# 3) Gráfico: Vulnerability Types (pizza)
# =====================================================
vuln = data["vuln_types"]["data"]
labels = list(vuln.keys())
values = list(vuln.values())
colors = data["vuln_types"]["colors"]

fig, ax = plt.subplots(figsize=(8, 6))
# Aqui usamos a função que já foi definida lá em cima!
wedges, texts, autotexts = ax.pie(
    values,
    autopct=make_autopct(values),
    labels=None,
    colors=colors,
    wedgeprops=dict(edgecolor="white")
)

for t in autotexts:
    t.set_color("white")
    t.set_fontsize(11)

leg = ax.legend(
    wedges, labels,
    loc="center left", bbox_to_anchor=(1, 0.5),
    facecolor="#0c1116", labelcolor="white"
)
plt.savefig(output_dir / "vulnerabilityType.png", dpi=120, bbox_inches="tight")
plt.close()

# =====================================================
# 4) Gráfico: Severidade (barras)
# =====================================================
severity = data["severity"]
ordered_labels = ["Low", "High", "Critical", "Moderate"]
colors = ["#17539c", "#ff1e00", "#ff0000", "#ff9c00"]
values = [severity[l] for l in ordered_labels]

fig, ax = plt.subplots(figsize=(6, 4))
bars = ax.bar(ordered_labels, values, color=colors)

for bar, value in zip(bars, values):
    ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 1,
            f"{value}",
            ha="center", va="bottom",
            color="white", fontsize=11)

ax.tick_params(colors="white")
ax.spines[:].set_visible(False)

plt.savefig(output_dir / "severity.png", dpi=120, bbox_inches="tight")
plt.close()

print("[✔] Todos os gráficos foram gerados em:", output_dir)