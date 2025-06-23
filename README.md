# 🔭 Previsor de Exoplanetas via Curvas de Luz

Este projeto é um estudo científico e computacional voltado para a detecção de possíveis exoplanetas por meio da análise de curvas de luz de estrelas, utilizando dados públicos das missões **Kepler**, **TESS** e **K2**, associados a técnicas de **Machine Learning**.

## 📄 Documentação

Atualmente, a documentação técnica e científica deste projeto está em fase de elaboração. Em breve, será disponibilizado um documento completo contendo:

- Introdução teórica sobre exoplanetas e curvas de luz.
- Descrição detalhada da metodologia utilizada.
- Explicação das features extraídas e do modelo de machine learning aplicado.
- Resultados e análises obtidas.

Fique à vontade para acompanhar o repositório — a documentação será adicionada nas próximas atualizações!

## 📖 Sobre o Projeto

O objetivo central deste trabalho é automatizar a extração de características (features) de curvas de luz e aplicar algoritmos de aprendizado de máquina para prever a presença ou ausência de exoplanetas em sistemas estelares.  

O projeto utiliza dados reais coletados por telescópios espaciais e propõe uma solução acessível e escalável para análise de dados astronômicos, contribuindo para a área de **astroinformática**.

---

## 📌 Funcionalidades

- 📥 Coleta de curvas de luz de estrelas via Lightkurve.
- 📊 Extração automatizada de features estatísticas das curvas.
- 📝 Montagem de dataset estruturado.
- 🤖 Treinamento de modelo Random Forest Classifier.
- 📈 Avaliação de desempenho com métricas como acurácia, precisão, recall e F1-score.
- 💾 Salvamento de datasets e modelos para uso posterior.

---

## 🛠️ Tecnologias e Bibliotecas

- [Python 3.12+](https://www.python.org)
- [Lightkurve](https://docs.lightkurve.org)
- [Pandas](https://pandas.pydata.org)
- [NumPy](https://numpy.org)
- [Scikit-learn](https://scikit-learn.org)
- [TQDM](https://tqdm.github.io)
- [Matplotlib](https://matplotlib.org)
- [Joblib](https://joblib.readthedocs.io)

---

## 📂 Estrutura de Diretórios
📁 data/
└── dataset_features.csv
📁 models/
└── modelo_rf.pkl
📁 scripts/
└── previsor_terminal.py
📄 README.md

## 🚀 Como Executar

1. Clone o repositório:
```bash
git clone https://github.com/GabsFns/exoplanetas_modelo.git

cd exoplanetas_modelo
```

2. Instale as dependências:
```bash
pip install -r requirements.txt
```
3. Execute o script:
```bash
python scripts/previsor_terminal.py
```
