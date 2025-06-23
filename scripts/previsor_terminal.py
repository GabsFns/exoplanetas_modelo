import lightkurve as lk
import numpy as np
import matplotlib.pyplot as plt
import joblib

def extrair_features(curva):
    flux = curva.normalize().flux
    time = curva.time.value
    max_flux = np.max(flux)
    min_flux = np.min(flux)
    std_flux = np.std(flux)
    limite = 1 - 3 * std_flux
    eventos = flux < limite
    num_quedas = np.sum(eventos)
    profundidades = 1 - flux[eventos] if num_quedas > 0 else [0]
    duracoes = np.diff(time[eventos]) if num_quedas > 1 else [0]
    profundidade_media = np.mean(profundidades)
    duracao_media = np.mean(duracoes) if len(duracoes) > 0 else 0
    intervalo_amostragem = np.mean(np.diff(time))
    tempos_transito = time[eventos]
    return {
        "max_flux": max_flux,
        "min_flux": min_flux,
        "std_flux": std_flux,
        "num_quedas": num_quedas,
        "profundidade_media": profundidade_media,
        "duracao_media": duracao_media,
        "intervalo_amostragem": intervalo_amostragem,
        "tempos_transito": tempos_transito
    }

modelo = joblib.load("models/modelo_rf.pkl")

estrela = input("Digite o nome da estrela (ex: Kepler-10)")
resultado = lk.search_lightcurve(estrela)

if len(resultado) == 0:
    print("Nenhum dado encontrado")
else:
    curva = resultado.download()
    features_dict = extrair_features(curva)
    features_lista = [
        features_dict["max_flux"],
        features_dict["min_flux"],
        features_dict["std_flux"],
        features_dict["num_quedas"],
        features_dict["profundidade_media"],
        features_dict["duracao_media"],
        features_dict["intervalo_amostragem"]
    ]
    
    predicao = modelo.predict([features_lista])[0]

    print("\nAnálise de Curva de Luz — Detecção de Exoplanetas")
    print("-" * 65)
    print(f"Estrela Analisada: {estrela}")
    print("Missão: Kepler Space Telescope")
    print(f"Número de Observações: {len(curva.time)} registros")
    print(f"Período de Observação: {curva.time.value.min():.2f} a {curva.time.value.max():.2f} (Julian Days)")
    print(f"Intervalo de Amostragem: {features_dict['intervalo_amostragem']:.4f} dias")
    print("Fluxo Normalizado: Sim\n")

    print("Parâmetros da Curva:")
    print(f"- Fluxo Máximo: {features_dict['max_flux']:.4f}")
    print(f"- Fluxo Mínimo: {features_dict['min_flux']:.4f}")
    print(f"- Desvio Padrão do Fluxo: {features_dict['std_flux']:.5f}\n")

    print("Detecção de Eventos:")
    print(f"- Quedas de Fluxo Detectadas: {features_dict['num_quedas']}")
    print(f"- Média da Profundidade de Trânsito: {features_dict['profundidade_media']:.4f} ({features_dict['profundidade_media']*100:.2f}%)")
    print(f"- Duração Média do Trânsito: {features_dict['duracao_media']:.3f} dias")
    if features_dict['num_quedas'] > 0:
        tempos_str = ', '.join(f"{t:.2f}" for t in features_dict['tempos_transito'])
        print(f"- Tempo dos Trânsitos: [{tempos_str}]")
    else:
        print("- Tempo dos Trânsitos: Nenhum registrado")

    print("\nResultado da Classificação:")
    if predicao == 1:
        print("→ POSSÍVEL PLANETA DETECTADO")
    else:
        print("→ Nenhum planeta detectado.")

    print("\n" + "-" * 65)
    print("Observação:")
    print("A detecção se baseou em quedas de fluxo superiores a 3σ (3 desvios padrão abaixo da média).")
    print("Para confirmação, recomenda-se análise espectroscópica complementar.")

    # Exibe o gráfico
    curva.plot()
    plt.title(f"Curva de Luz de {estrela}")
    plt.show()