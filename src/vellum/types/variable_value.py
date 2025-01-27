# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations

import typing

import typing_extensions

from .array_variable_value import ArrayVariableValue
from .chat_history_variable_value import ChatHistoryVariableValue
from .error_variable_value import ErrorVariableValue
from .function_call_variable_value import FunctionCallVariableValue
from .json_variable_value import JsonVariableValue
from .number_variable_value import NumberVariableValue
from .search_results_variable_value import SearchResultsVariableValue
from .string_variable_value import StringVariableValue


class VariableValue_String(StringVariableValue):
    type: typing_extensions.Literal["STRING"]

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True


class VariableValue_Number(NumberVariableValue):
    type: typing_extensions.Literal["NUMBER"]

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True


class VariableValue_Json(JsonVariableValue):
    type: typing_extensions.Literal["JSON"]

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True


class VariableValue_ChatHistory(ChatHistoryVariableValue):
    type: typing_extensions.Literal["CHAT_HISTORY"]

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True


class VariableValue_SearchResults(SearchResultsVariableValue):
    type: typing_extensions.Literal["SEARCH_RESULTS"]

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True


class VariableValue_Error(ErrorVariableValue):
    type: typing_extensions.Literal["ERROR"]

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True


class VariableValue_Array(ArrayVariableValue):
    type: typing_extensions.Literal["ARRAY"]

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True


class VariableValue_FunctionCall(FunctionCallVariableValue):
    type: typing_extensions.Literal["FUNCTION_CALL"]

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True


VariableValue = typing.Union[
    VariableValue_String,
    VariableValue_Number,
    VariableValue_Json,
    VariableValue_ChatHistory,
    VariableValue_SearchResults,
    VariableValue_Error,
    VariableValue_Array,
    VariableValue_FunctionCall,
]

VariableValue_Array.update_forward_refs()
