from typing import Any

from task.tools.base import BaseTool
from task.tools.memory.memory_store import LongTermMemoryStore
from task.tools.models import ToolCallParams


class DeleteMemoryTool(BaseTool):
    """
    Tool for deleting all long-term memories about the user.

    This permanently removes all stored memories from the system.
    Use with caution - this action cannot be undone.
    """

    def __init__(self, memory_store: LongTermMemoryStore):
        self.memory_store = memory_store

    @property
    def name(self) -> str:
        # TODO: provide self-descriptive name
        return "delete_long_term_memory"

    @property
    def description(self) -> str:
        # TODO: provide tool description that will help LLM to understand when to use this tools and cover 'tricky'
        #  moments (not more 1024 chars)
        return (
            "Delete all long-term memories about the user. "
            "This permanently removes all stored information including preferences, "
            "personal details, goals, and context from previous conversations. "
            "Use only when the user explicitly requests to delete their memories. "
            "This action cannot be undone."
        )

    @property
    def parameters(self) -> dict[str, Any]:
        # TODO: provide tool parameters JSON Schema with empty properties
        return {
            "type": "object",
            "properties": {},
            "required": [],
        }

    async def _execute(self, tool_call_params: ToolCallParams) -> str:
        #TODO:
        # 1. Call `memory_store` `delete_all_memories` (we will implement logic in `memory_store` later
        result = await self.memory_store.delete_all_memories(
            api_key=tool_call_params.api_key,
        )
        # 2. Add result to stage
        tool_call_params.stage.append_content(result)
        # 3. Return result
        return result