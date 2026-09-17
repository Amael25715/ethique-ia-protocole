#!/usr/bin/env python3
"""
Stub – Mécanismes collaboratifs et journalisation de décisions

Ce module n'impose pas de sanction automatique.
Il sert de base pour :
- enregistrer des propositions,
- tracer des alertes,
- préparer un futur outil de suivi des votes / statuts de publication.
"""

from dataclasses import dataclass, field
from datetime import datetime
from typing import List, Optional

@dataclass
class Decision:
    date: str
    who: str
    decision: str
    why: str
    status: str = "proposé"

@dataclass
class Alert:
    date: str
    who: str
    reason: str
    related_decision: Optional[str] = None

class DecisionLog:
    def __init__(self):
        self.decisions: List[Decision] = []
        self.alerts: List[Alert] = []

    def add_decision(self, who: str, decision: str, why: str, status: str = "proposé"):
        d = Decision(
            date=datetime.utcnow().strftime("%Y-%m-%d"),
            who=who,
            decision=decision,
            why=why,
            status=status,
        )
        self.decisions.append(d)
        return d

    def add_alert(self, who: str, reason: str, related: Optional[str] = None):
        a = Alert(
            date=datetime.utcnow().strftime("%Y-%m-%d"),
            who=who,
            reason=reason,
            related_decision=related,
        )
        self.alerts.append(a)
        return a

    def summary(self) -> str:
        lines = ["## Décisions"]
        for d in self.decisions:
            lines.append(f"- [{d.date}] {d.who}: {d.decision} ({d.status})")
        lines.append("\n## Alertes")
        for a in self.alerts:
            lines.append(f"- [{a.date}] {a.who}: {a.reason}")
        return "\n".join(lines)

if __name__ == "__main__":
    log = DecisionLog()
    log.add_decision("Aether", "Création structure initiale des 3 dépôts", "Demande équipe", "fait")
    print(log.summary())
