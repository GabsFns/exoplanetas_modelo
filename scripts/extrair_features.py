import lightkurve as lk
import pandas as pd
import numpy as np
from tqdm import tqdm

def extrair_features(curva):
    flux = curva.normalize().flux.value
    time = curva.time.value
    max_flux = np.max(flux)
    min_flux = np.min(flux)
    std_flux = np.std(flux)
    limite = 1 - 3 * std_flux
    eventos = flux < limite
    num_quedas = np.sum(eventos)
    profundidades = 1 - flux[eventos] if num_quedas > 0 else [0]
    duracoes = np.diff(time[eventos]) if num_quedas > 1 else [0]
    profundidade_media = np.mean(profundidades) if len(profundidades) > 0 else 0
    duracao_media = np.mean(duracoes) if len(duracoes) > 0 else 0
    intervalo_amostragem = np.mean(np.diff(time))
    return [max_flux, min_flux, std_flux, num_quedas, profundidade_media, duracao_media, intervalo_amostragem]

estrelas = [
    "Kepler-4", "Kepler-5", "Kepler-6", "Kepler-7", "Kepler-8", "Kepler-9", "Kepler-12", "Kepler-14",
    "Kepler-16", "Kepler-18", "Kepler-19", "Kepler-21", "Kepler-23", "Kepler-25", "Kepler-26",
    "Kepler-27", "Kepler-28", "Kepler-30", "Kepler-31", "Kepler-33", "Kepler-35", "Kepler-36",
    "Kepler-37", "Kepler-38", "Kepler-39", "Kepler-40", "Kepler-41", "Kepler-42", "Kepler-43",
    "TRAPPIST-1", "K2-18", "K2-33", "K2-38", "K2-141", "GJ 1214", "55 Cnc", "WASP-12", "WASP-18",
    "WASP-19", "WASP-43", "WASP-121", "HD 189733", "HD 209458", "Betelgeuse", "Rigel", "Aldebaran",
    "Vega", "Sirius", "Procyon"
]
kic_ids = range(757700, 758000)

planetas_confirmados = ["Kepler-10", "Kepler-22", "Kepler-20", "TRAPPIST-1"]

dados = []

for estrela in tqdm(estrelas, desc="Analisando Estrelas"):
    resultado = lk.search_lightcurve(estrela, mission=["Kepler", "TESS", "K2"])
    if len(resultado) > 0:
        try:
            curvas = resultado.download_all()
            print(f"  → {len(curvas)} curvas encontradas para {estrela}.")
            for curva in curvas:
                features = extrair_features(curva)
                label = 1 if estrela in planetas_confirmados else 0
                dados.append(features + [label])
        except Exception as e:
            print(f"  [ERRO] Ao processar {estrela}: {e}")
    else:
        print(f"  → Nenhum dado para {estrela}")


for kic_id in tqdm(kic_ids, desc="Analisando KIC IDs"):
    resultado = lk.search_lightcurve(f"KIC {kic_id}", mission="Kepler")
    if len(resultado) > 0:
        try:
            curvas = resultado.download_all()
            print(f"  → {len(curvas)} curvas para KIC {kic_id}.")
            for curva in curvas:
                features = extrair_features(curva)
                # Assume label 0 para KIC desconhecido (sem confirmação)
                dados.append(features + [0])
        except Exception as e:
            print(f"  [ERRO] Ao processar KIC {kic_id}: {e}")
    else:
        print(f"  → Nenhum dado para KIC {kic_id}")



df = pd.DataFrame(dados, columns=[
    "max_flux", "min_flux", "std_flux", "num_quedas", 
    "profundidade_media", "duracao_media", "intervalo_amostragem", "label"])

df.to_csv("data/dataset_features.csv", index=False)
print(f"\n Processamento finalizado. Total de registros coletados: {len(dados)}")