"""Scheduled-task notification delivery outbox persistence (issue #4254)."""

from operix.persistence.notification_deliveries.model import NotificationDeliveryRow
from operix.persistence.notification_deliveries.sql import NotificationDeliveryRepository

__all__ = [
    "NotificationDeliveryRepository",
    "NotificationDeliveryRow",
]
