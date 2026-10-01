"""ORM model registration entry point.

Importing this module ensures all ORM models are registered with
``Base.metadata`` so Alembic autogenerate detects every table.

The actual ORM classes have moved to entity-specific subpackages:
- ``operix.persistence.thread_meta``
- ``operix.persistence.run``
- ``operix.persistence.feedback``
- ``operix.persistence.user``

``RunEventRow`` remains in ``operix.persistence.models.run_event`` because
its storage implementation lives in ``operix.runtime.events.store.db`` and
there is no matching entity directory.
"""

from operix.persistence.agents.model import AgentRow
from operix.persistence.channel_connections.model import (
    ChannelConnectionRow,
    ChannelConversationRow,
    ChannelCredentialRow,
    ChannelOAuthStateRow,
)
from operix.persistence.feedback.model import FeedbackRow
from operix.persistence.managed_subagents.model import ManagedSubagentRow
from operix.persistence.mcp_tasks.model import McpTaskRow
from operix.persistence.models.run_event import RunEventRow
from operix.persistence.notification_deliveries.model import NotificationDeliveryRow
from operix.persistence.personal_access_tokens.model import PersonalAccessTokenRow
from operix.persistence.projects.model import ProjectDocumentRow, ProjectRow
from operix.persistence.run.model import RunChangeClockRow, RunRow
from operix.persistence.scheduled_task_runs.model import ScheduledTaskRunRow
from operix.persistence.scheduled_tasks.model import ScheduledTaskRow
from operix.persistence.subagent_batches.model import SubagentBatchItemRow, SubagentBatchRow
from operix.persistence.thread_meta.model import ThreadMetaRow
from operix.persistence.user.model import UserPreferenceRow, UserRow
from operix.persistence.webhook_delivery.model import WebhookDeliveryRow

__all__ = [
    "AgentRow",
    "ChannelConnectionRow",
    "ChannelConversationRow",
    "ChannelCredentialRow",
    "ChannelOAuthStateRow",
    "FeedbackRow",
    "McpTaskRow",
    "ManagedSubagentRow",
    "NotificationDeliveryRow",
    "PersonalAccessTokenRow",
    "ProjectDocumentRow",
    "ProjectRow",
    "RunEventRow",
    "RunChangeClockRow",
    "RunRow",
    "ScheduledTaskRow",
    "ScheduledTaskRunRow",
    "SubagentBatchRow",
    "SubagentBatchItemRow",
    "ThreadMetaRow",
    "UserPreferenceRow",
    "UserRow",
    "WebhookDeliveryRow",
]
