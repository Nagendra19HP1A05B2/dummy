from pathlib import Path
from typing import Any, Callable, Dict, Optional, Tuple

import streamlit as st
import streamlit.components.v1 as components

build_dir = Path(__file__).parent.absolute() / "header"
_component_func = components.declare_component("st_keyup", path=str(build_dir))

build_dir = Path(__file__).parent.absolute() / "search"
_component_footer = components.declare_component("search", path=str(build_dir))

build_dir = Path(__file__).parent.absolute() / "title"
_component_titles = components.declare_component("titles", path=str(build_dir))

build_dir = Path(__file__).parent.absolute() / "card"
_component_cards = components.declare_component("cards", path=str(build_dir))

build_dir = Path(__file__).parent.absolute() / "suites"
_component_suites = components.declare_component("suites", path=str(build_dir))

build_dir = Path(__file__).parent.absolute() / "modal"
_component_modal = components.declare_component("modal", path=str(build_dir))

build_dir = Path(__file__).parent.absolute() / "table"
_component_table = components.declare_component("table", path=str(build_dir))


def st_keyup(
        label: str,
        value: str = "",
        max_chars: Optional[int] = None,
        key: Optional[str] = None,
        type: str = "default",
        debounce: Optional[int] = None,
        on_change: Optional[Callable] = None,
        args: Optional[Tuple[Any, ...]] = None,
        kwargs: Optional[Dict[str, Any]] = None,
        *,
        placeholder: str = "",
        disabled: bool = False,
        label_visibility: str = "visible",
):
    if key is None:
        key = "st_keyup_" + label

    component_value = _component_func(
        label=label,
        value=value,
        key=key,
        debounce=debounce,
        default=value,
        max_chars=max_chars,
        type=type,
        placeholder=placeholder,
        disabled=disabled,
        label_visibility=label_visibility,
    )

    if on_change is not None:
        if "__previous_values__" not in st.session_state:
            st.session_state["__previous_values__"] = {}

        if component_value != st.session_state["__previous_values__"].get(key, value):
            st.session_state["__previous_values__"][key] = component_value

            if on_change:
                if args is None:
                    args = ()
                if kwargs is None:
                    kwargs = {}
                on_change(*args, **kwargs)
    return component_value


def search(label: str):
    component_value = _component_footer(label=label)
    return component_value


def titles(label: str):
    component_value = _component_titles(label=label)
    return component_value


def cards(key: str):
    component_value = _component_cards(key=key)
    return component_value


def suites(label: str):
    component_value = _component_suites(label=label)
    return component_value


def modal(label: str):
    component_value = _component_modal(label=label)
    return component_value

def table(label: str):
    component_value = _component_table(label=label)
    return component_value
