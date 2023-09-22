# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations

import typing

import typing_extensions

from .api_node_result import ApiNodeResult
from .conditional_node_result import ConditionalNodeResult
from .prompt_node_result import PromptNodeResult
from .search_node_result import SearchNodeResult
from .templating_node_result import TemplatingNodeResult
from .terminal_node_result import TerminalNodeResult


class WorkflowNodeResultData_Prompt(PromptNodeResult):
    type: typing_extensions.Literal["PROMPT"]

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True


class WorkflowNodeResultData_Search(SearchNodeResult):
    type: typing_extensions.Literal["SEARCH"]

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True


class WorkflowNodeResultData_Templating(TemplatingNodeResult):
    type: typing_extensions.Literal["TEMPLATING"]

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True


class WorkflowNodeResultData_Conditional(ConditionalNodeResult):
    type: typing_extensions.Literal["CONDITIONAL"]

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True


class WorkflowNodeResultData_Api(ApiNodeResult):
    type: typing_extensions.Literal["API"]

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True


class WorkflowNodeResultData_Terminal(TerminalNodeResult):
    type: typing_extensions.Literal["TERMINAL"]

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True


WorkflowNodeResultData = typing.Union[
    WorkflowNodeResultData_Prompt,
    WorkflowNodeResultData_Search,
    WorkflowNodeResultData_Templating,
    WorkflowNodeResultData_Conditional,
    WorkflowNodeResultData_Api,
    WorkflowNodeResultData_Terminal,
]
