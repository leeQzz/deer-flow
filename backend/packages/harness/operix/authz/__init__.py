"""Pluggable fine-grained authorization (resource-level RBAC and beyond)."""

from operix.authz.adapter import GuardrailAuthorizationAdapter
from operix.authz.enforcement import filter_resources_by_authorization, filter_tools_by_authorization
from operix.authz.plugin_authz import (
    PluginAuthorizationError,
    aenforce_plugin_action,
    aenforce_plugin_management,
    afilter_plugin_management,
    afilter_plugin_pages,
    enforce_plugin_action,
    enforce_plugin_management,
)
from operix.authz.plugin_targets import (
    MANAGEMENT_READ_PART,
    MANAGEMENT_WRITE_PART,
    plugin_action_target,
    plugin_management_target,
    plugin_page_target,
)
from operix.authz.principal import build_principal_from_context, normalize_authz_attributes
from operix.authz.provider import AuthorizationProvider, AuthzDecision, AuthzReason, AuthzRequest, Principal
from operix.authz.rbac import RbacAuthorizationProvider
from operix.authz.runtime import resolve_authorization_provider
from operix.authz.sandbox_authz import authorize_sandbox_execution
from operix.authz.skill_filter import filter_available_skills_by_authorization
from operix.authz.tool_filter import apply_tool_authorization

__all__ = [
    "AuthzDecision",
    "AuthzReason",
    "AuthzRequest",
    "AuthorizationProvider",
    "GuardrailAuthorizationAdapter",
    "MANAGEMENT_READ_PART",
    "MANAGEMENT_WRITE_PART",
    "PluginAuthorizationError",
    "Principal",
    "RbacAuthorizationProvider",
    "aenforce_plugin_action",
    "aenforce_plugin_management",
    "afilter_plugin_management",
    "afilter_plugin_pages",
    "apply_tool_authorization",
    "authorize_sandbox_execution",
    "build_principal_from_context",
    "enforce_plugin_action",
    "enforce_plugin_management",
    "filter_available_skills_by_authorization",
    "filter_resources_by_authorization",
    "filter_tools_by_authorization",
    "normalize_authz_attributes",
    "plugin_action_target",
    "plugin_management_target",
    "plugin_page_target",
    "resolve_authorization_provider",
]
