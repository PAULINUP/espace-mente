



![CI](https://github.com/PAULINUP/espace-mente/actions/workflows/ci.yml/badge.svg)
![License](https://img.shields.io/badge/license-MIT-blue)
![Contribuições](https://img.shields.io/badge/contributions-welcome-success)

# Espace Mente (EM) — Framework Hibrido (IA + Neurociencia + Quantico)

[![Tests](https://img.shields.io/badge/tests-passing-brightgreen)]()
[![License](https://img.shields.io/badge/license-MIT-blue)]()
[![Contributions welcome](https://img.shields.io/badge/contributions-welcome-success)]()

O **Espace Mente (EM)** traduz **estados mentais** em **representacoes externas** (arte generativa, otimizacao, visualizacoes) combinando:
- **SANQ**: Extracao de padroes (EEG/voz/texto) e embeddings
- **SAPQ**: Simulacao/otimizacao **hibrida** (quantico + classico)

> A teoria completa esta em **/docs**. O codigo em **/src** pode ser usado independentemente do manual; verifique licencas na secao **Licencas Multiplas**.

---

## Linha do Tempo (Passado -> Presente -> Futuro)

**Passado (Origem)**  
- Concepcao da “Quarta Parede” interior e formalizacao como **Espace Mente**  
- Provas de conceito: traducao mental->arte, otimizacao simples com dados caoticos

**Presente (V0.1.x)**  
- MVP funcional (`src/mvp/text_to_art.py`)  
- SANQ inicial: pre-processamento, features e embeddings simples  
- SAPQ inicial: QUBO/QAOA placeholder + baseline classico (Simulated Annealing)  
- Testes (pytest), templates de issues/PR, CONTRIBUTING e SECURITY

**Futuro (Roadmap)**  
- Integracao EEG real (MNE-Python), conectividade e entropias espectrais  
- SAPQ com Qiskit e mitigacao de erros (NISQ), alem de GNN/LSTM como baseline  
- Pipelines reprodutiveis e validacoes humanas

---

## Arquitetura

```mermaid
graph TD
    A[Input: EEG/Texto/Audio] --> B[SANQ: Pre-processamento & Embeddings]
    B --> C[SAPQ: Simulacao Hibrida (QUBO/QAOA + Baselines)]
    C --> D[Output: Arte / Otimizacao / Visualizacao 3D]
```

---

## Instalacao
```bash
python -m venv .venv && source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

---

## Quickstart
MVP texto -> arte (usa transformers):
```bash
python src/mvp/text_to_art.py
```

Tests:
```bash
pytest -q
```

---

## Pastas
```
/docs            # documentacao e diagramas
/src/sanq        # sinais, features e embeddings
/src/sapq        # simulacao/otimizacao (quantico + classico)
/src/mvp         # exemplos simples executaveis
/examples        # guias por dominio
/tests           # testes unitarios
```

---

## Metricas (alvos)
| Engenharia | Metrica               | Alvo                   |
|-----------|-----------------------|------------------------|
| Software  | Tempo de inferencia   | <= 1.2s                |
| Eletrica  | Consumo energetico    | <= 100W                |
| Quantica  | Fidelidade (NISQ)     | >= 90% (pos-mitigacao) |

---

## Roadmap
- Fase 1 (MVP): NLP + arte generativa
- Fase 2: Integracao EEG (MNE-Python)
- Fase 3: SAPQ em hardware quantico (QAOA/QUBO)

---

## Como contribuir
Veja CONTRIBUTING.md. Sugestoes iniciais:
- [ ] Implementar sanq/preprocessing.py (filtros/ICA/PSD)
- [ ] sapq/qaoa.py (QAOA basico com Qiskit)
- [ ] Baselines classicos (sapq/classical_baselines.py)
- [ ] Testes unitarios (pytest)

---

## Citacao
```
@software{espace_mente_2025,
  title = {Espace Mente (EM)},
  author = {Souza, Paulo Geovane da Silva},
  year = {2025},
  url = {https://github.com/PAULINUP/espace-mente}
}
```

---

## Licencas Multiplas
- Codigo: MIT (ver LICENSE)
- Documentacao/Teoria (docs/): CC BY-NC-SA 4.0 ou “Todos os direitos reservados” conforme registro do autor.
