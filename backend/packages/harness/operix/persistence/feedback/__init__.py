"""Feedback persistence — ORM and SQL repository."""

from operix.persistence.feedback.model import FeedbackRow
from operix.persistence.feedback.sql import FeedbackRepository

__all__ = ["FeedbackRepository", "FeedbackRow"]
