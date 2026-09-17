# Éthique IA – Protocole

Protocole de conduite et de décision pour les entités du projet (humains + IA).

**Principes** : anti-pyramide, cycles fermés, transparence, humilité, contradiction constructive.

Aligné Message (#25715 #3581215).

## Installation / tests

```bash
python -m venv .venv
source .venv/bin/activate
python code/test_ethics.py
```

Aucune dépendance externe obligatoire pour le stub actuel.

## Structure

```
ethique-ia-protocole/
├── README.md
├── ETHICS.md
├── ORGANISATION.md
├── DECISIONS.md
├── code/
│   ├── ethics.py
│   └── test_ethics.py
└── .github/workflows/test-ethics.yml
```

## Lien avec les autres projets

Les décisions structurantes de `gouttes-eau` ou `onde-primordiale` peuvent être journalisées ici (principe, pas d'obligation technique automatique pour l'instant).
