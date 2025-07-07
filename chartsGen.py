# python3 chartsGen.py

import json
import urllib.parse
import requests
from pathlib import Path

# Diretório de saída
output_dir = Path("content/stats")
output_dir.mkdir(parents=True, exist_ok=True)

def limpa_imagens():
    arquivos = [
        "topFinders.png",
        "totalCVEsRegistred.png",
        "vulnerabilityType.png",
        "severity.png"
    ]
    for arq in arquivos:
        caminho = output_dir / arq
        if caminho.exists():
            caminho.unlink()
            print(f"[✂] {arq} removido.")

# Limpa imagens antigas
limpa_imagens()

def urlencode_chart_config(config):
    return "https://image-charts.com/chart.js/2.8.0?bkg=%230d1117&chs=700x400&c=" + urllib.parse.quote(json.dumps(config))

def save_chart(url, filename):
    img = requests.get(url)
    (output_dir / filename).write_bytes(img.content)
    print(f"[✔] {filename} gerado.")

# Carrega os dados
with open("cvestats.json") as f:
    data = json.load(f)

### Gráfico 1: Top Finders (doughnut estilizado)
top_finders = data["top_finders"]["data"]
colors = data["top_finders"]["colors"]
labels = list(top_finders.keys())
values = list(top_finders.values())

top_finders_config = {
    "type": "doughnut",
    "data": {
        "labels": labels,
        "datasets": [{
            "data": values,
            "backgroundColor": colors
        }]
    },
    "options": {
        "plugins": {
            "legend": {"display": False},
            "datalabels": {
                "color": "white",
                "font": {"size": 14},
                "formatter": "(value,ctx) => ctx.chart.data.labels[ctx.dataIndex]"
            }
        }
    }
}
save_chart(urlencode_chart_config(top_finders_config), "topFinders.png")

### Gráfico 2: Total CVEs Registered (linha)
total_by_year = data["total_by_year"]
years = [k.split(":")[0] for k in total_by_year.keys()]
values = list(total_by_year.values())
labels = [f"{year}: {value} CVEs" for year, value in zip(years, values)]

total_url = (
    "https://image-charts.com/chart"
    "?cht=lc"
    "&chs=700x400"
    f"&chd=t:{','.join(map(str, values))}"
    "&chxt=y,x"
    "&chxr=0,0,100,10"
    f"&chxl=1:|{'|'.join(labels)}"
    "&chco=e918d5"
    "&chf=bg,s,0d1117"
    "&chxs=0,FFFFFF,14|1,FFFFFF,14"
)
save_chart(total_url, "totalCVEsRegistred.png")

### Gráfico 3: Vulnerability Types (pizza clássico)
vuln = data["vuln_types"]
labels = list(vuln["data"].keys())
values = list(vuln["data"].values())
colors = [c.lstrip('#') for c in vuln["colors"]]  # Remove o # das cores

chl = "|".join(str(v) for v in values)  # valores dentro das fatias
chdl = "|".join(urllib.parse.quote_plus(label) for label in labels)  # legenda
chco = ",".join(colors)

vuln_url = (
    "https://image-charts.com/chart"
    "?cht=p"
    "&chs=700x400"
    f"&chd=t:{','.join(map(str, values))}"
    f"&chco={chco}"
    f"&chl={chl}"
    f"&chdl={chdl}"
    "&chf=bg,s,0d1117"
    "&chdlp=r"
    "&chdls=FFFFFF,14"
    "&chxs=0,FFFFFF,14"
)
save_chart(vuln_url, "vulnerabilityType.png")

### Gráfico 4: Severity (barras verticais)
severity = data["severity"]
labels = list(severity.keys())
values = list(severity.values())
colors = ["c00000", "ff0000", "ffc000"]
legend = "|".join([f"{label}: {value}" for label, value in zip(labels, values)])

severity_url = (
    "https://image-charts.com/chart"
    "?cht=bvg"
    "&chs=700x400"
    f"&chd=t:{'%7C'.join(map(str, values))}"
    "&chxt=y,x"
    "&chxr=0,0,50,5"
    "&chxl=1:||"
    f"&chco={','.join(colors)}"
    "&chf=bg,s,0d1117"
    "&chxs=0,FFFFFF,14|1,FFFFFF,14"
    f"&chdl={urllib.parse.quote(legend)}"
    "&chdlp=r"
    "&chdls=FFFFFF,14"
)
save_chart(severity_url, "severity.png")