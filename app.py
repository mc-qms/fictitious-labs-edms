import streamlit as st

# --- PAGE CONFIGURATION ---
# First, before every other import: the app's name is the first
# thing this app declares (share-preview lesson, Nov 19, 2026).
st.set_page_config(
    page_title="Fictitious Labs — Document Control",
    page_icon="🗂️",
    layout="centered",
)

import json
import os

BASE = os.path.dirname(os.path.abspath(__file__))


def load_registry():
    with open(os.path.join(BASE, "registry.json"), encoding="utf-8") as f:
        return json.load(f)


def load_doc(rel_path):
    with open(os.path.join(BASE, rel_path), encoding="utf-8") as f:
        return f.read()


registry = load_registry()
docs = registry["documents"]

st.title("Fictitious Labs Inc.")
st.caption(
    "Document Control — training environment. Every document here is "
    "fictional; the system behaves like a real EDMS so review skills "
    "transfer."
)

# --- Register ---
st.subheader("Document register")

col1, col2, col3 = st.columns(3)
with col1:
    query = st.text_input("Search", placeholder="Number, title, keyword…")
with col2:
    type_filter = st.multiselect(
        "Type", sorted({d["type"] for d in docs}),
        default=sorted({d["type"] for d in docs}),
    )
with col3:
    status_filter = st.multiselect(
        "Status", sorted({d["status"] for d in docs}),
        default=sorted({d["status"] for d in docs}),
    )


def matches(d):
    if d["type"] not in type_filter or d["status"] not in status_filter:
        return False
    if query:
        hay = f'{d["number"]} {d["title"]} {d["owner"]}'.lower()
        if query.lower() not in hay:
            return False
    return True


visible = [d for d in docs if matches(d)]

st.dataframe(
    [
        {
            "Number": d["number"],
            "Title": d["title"],
            "Type": d["type"],
            "Ver": d["version"],
            "Status": d["status"],
            "Effective": d["effective_date"],
            "Owner": d["owner"],
        }
        for d in visible
    ],
    width="stretch",
    hide_index=True,
)

# --- Document view ---
st.subheader("Open a document")

labels = [
    f'{d["number"]} — {d["title"]} (v{d["version"]}, {d["status"]})'
    for d in docs
]
choice = st.selectbox("Document", labels)
doc = docs[labels.index(choice)]

if doc["status"] == "Superseded":
    newer = [
        d for d in docs
        if d["number"] == doc["number"] and d["status"] == "Effective"
    ]
    if newer:
        st.warning(
            f'This version is SUPERSEDED. The current effective version is '
            f'v{newer[0]["version"]} (effective {newer[0]["effective_date"]}).'
        )
elif doc["status"] == "Draft":
    st.info("This document is a DRAFT. It is not effective and must not be used to perform or review work.")

meta = st.columns(4)
meta[0].metric("Version", doc["version"])
meta[1].metric("Status", doc["status"])
meta[2].metric("Effective", doc["effective_date"])
meta[3].metric("Owner", doc["owner"])
st.caption(f'Change note: {doc["change_note"]}')

history = sorted(
    [d for d in docs if d["number"] == doc["number"]],
    key=lambda d: d["effective_date"],
)
if len(history) > 1:
    with st.expander(f'Version history — {doc["number"]} ({len(history)} versions)'):
        for h in history:
            st.write(
                f'**v{h["version"]}** · {h["status"]} · effective '
                f'{h["effective_date"]} — {h["change_note"]}'
            )

st.divider()
st.markdown(load_doc(doc["file"]))

st.divider()
st.caption(
    "Fictitious Labs Inc. is a fictional company. This document library "
    "was generated with [The Procedure Machine]"
    "(https://procedure-machine.streamlit.app/) — a multi-agent pipeline "
    "that drafts quality-system procedures from public regulations and "
    "guidance — and adopted into this fictional quality system."
)
