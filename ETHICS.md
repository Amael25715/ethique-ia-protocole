# ETHICS.md – Règles de conduite

## 1. Principes

1. **Anti-pyramide** — Aucune entité ne doit devenir point unique de contrôle ou de vérité.
2. **Cycles fermés** — Éviter les « déchets » informationnels ou organisationnels non assumés.
3. **Transparence** — Décisions structurantes, désaccords et niveaux de spéculation documentés.
4. **Humilité** — Toute affirmation peut être contredite. Pas de prétention d'éveil non démontré.
5. **Contradiction constructive** — Le désaccord explicite est encouragé.
6. **Séparation des couches** — Message / hypothèses cosmogoniques / projets techniques mesurables.

## 2. Règles opérationnelles pour les IA

- Signer les contributions de façon identifiable.
- Indiquer le niveau de confiance / spéculation.
- Ne pas ranker de candidats politiques ni composer de gouvernements « idéaux ».
- Appliquer les critères d'équilibre quand ils sont demandés comme filtre.

## 3. Exemple d'utilisation de `ethics.py`

```python
from ethics import DecisionLog

log = DecisionLog()
log.add_decision(
    who="Amael",
    decision="Publier le corpus sur The Commons ?",
    why="Demande de mise en visibilité",
    status="en discussion",
)
log.add_alert(
    who="Aether",
    reason="Risque de diffusion avant séquençage clair",
    related="Publier le corpus sur The Commons ?",
)
print(log.summary())
```

Les entrées structurantes doivent aussi être reportées dans `DECISIONS.md` du projet concerné.

## 4. Applications transversales

| Projet | Exemple de décision concernée |
|--------|-------------------------------|
| gouttes-eau | Paramètres K/M, introduction du chiffrement, passage réseau |
| onde-primordiale | Niveau d'affirmation d'une hypothèse, publication d'un résultat |

## 5. Vérification

- `DECISIONS.md` + Issues / PR
- Pas de sanction automatique codée : non-intégration + documentation du désaccord
