import streamlit as st

# --- PAGE CONFIGURATION ---
# First, before every other import: the app's name is the first
# thing this app declares (share-preview lesson, Nov 19, 2026).
st.set_page_config(
    page_title="Fictitious Labs — Document Control",
    page_icon="🗂️",
    layout="wide",
)

import base64
import json
import os

BASE = os.path.dirname(os.path.abspath(__file__))


def logo_bytes():
    """The company logo. The JPEG ships in the repo as base64 text
    (assets/logo.b64) because the snapshot push route carries UTF-8
    files only; a local logo.jpg, when present, wins."""
    jpg = os.path.join(BASE, "assets", "logo.jpg")
    if os.path.exists(jpg):
        with open(jpg, "rb") as f:
            return f.read()
    b64 = os.path.join(BASE, "assets", "logo.b64")
    if os.path.exists(b64):
        with open(b64, encoding="ascii") as f:
            return base64.b64decode(f.read())
    return None

STATUS_GLYPH = {
    "Effective": "🟢 Effective",
    "Superseded": "⚪ Superseded",
    "Draft": "🟡 Draft",
}
STATUS_PILL = {
    "Effective": ("#1a7f37", "#ffffff"),
    "Superseded": ("#6e7781", "#ffffff"),
    "Draft": ("#b54708", "#ffffff"),
}


def load_registry():
    with open(os.path.join(BASE, "registry.json"), encoding="utf-8") as f:
        return json.load(f)


def load_doc(rel_path):
    with open(os.path.join(BASE, rel_path), encoding="utf-8") as f:
        return f.read()


def doc_key(d):
    return f'{d["number"]}|{d["version"]}'


def doc_label(d):
    return f'{d["number"]} — {d["title"]} (v{d["version"]}, {d["status"]})'


registry = load_registry()
docs = registry["documents"]
by_key = {doc_key(d): d for d in docs}

# --- Session state: which view, which document ---
if "view" not in st.session_state:
    st.session_state.view = "library"
if "selected_key" not in st.session_state:
    st.session_state.selected_key = None


def open_selected():
    key = st.session_state.get("open_picker")
    if key:
        st.session_state.selected_key = key
        st.session_state.view = "document"


def back_to_library():
    st.session_state.view = "library"
    st.session_state.open_picker = None


def open_key(key):
    st.session_state.selected_key = key
    st.session_state.view = "document"


# --- Header: branding band + system bar ---
_logo = logo_bytes()
if _logo is not None:
    band = st.columns([1, 2, 1])
    band[1].image(_logo, width="stretch")
else:
    st.title("Fictitious Labs Inc.")

bar = st.columns([3, 2])
bar[0].markdown("**FL-EDMS** · Document Control")
bar[1].markdown(
    '<div style="text-align: right;">M. Whitfield · Quality Assurance '
    "· <b>PROD</b></div>",
    unsafe_allow_html=True,
)
st.divider()


def render_library():
    # --- Sidebar: navigation + filters ---
    st.sidebar.header("Library")
    query = st.sidebar.text_input(
        "Search", placeholder="Number, title, owner…"
    )
    type_filter = st.sidebar.multiselect(
        "Document type", sorted({d["type"] for d in docs}),
        default=sorted({d["type"] for d in docs}),
    )
    status_filter = st.sidebar.multiselect(
        "Lifecycle status", sorted({d["status"] for d in docs}),
        default=sorted({d["status"] for d in docs}),
    )
    owner_filter = st.sidebar.multiselect(
        "Owner", sorted({d["owner"] for d in docs}),
        default=sorted({d["owner"] for d in docs}),
    )
    n_eff = sum(1 for d in docs if d["status"] == "Effective")
    n_sup = sum(1 for d in docs if d["status"] == "Superseded")
    st.sidebar.divider()
    st.sidebar.caption(
        f"{len(docs)} controlled documents · {n_eff} Effective · "
        f"{n_sup} Superseded"
    )

    def matches(d):
        if d["type"] not in type_filter:
            return False
        if d["status"] not in status_filter:
            return False
        if d["owner"] not in owner_filter:
            return False
        if query:
            hay = f'{d["number"]} {d["title"]} {d["owner"]}'.lower()
            if query.lower() not in hay:
                return False
        return True

    visible = [d for d in docs if matches(d)]

    # --- Register grid ---
    st.subheader("Document Library")
    st.caption(f"Showing {len(visible)} of {len(docs)} documents")
    st.dataframe(
        [
            {
                "Number": d["number"],
                "Title": d["title"],
                "Type": d["type"],
                "Version": d["version"],
                "Status": STATUS_GLYPH.get(d["status"], d["status"]),
                "Effective": d["effective_date"],
                "Owner": d["owner"],
            }
            for d in visible
        ],
        width="stretch",
        hide_index=True,
    )

    # --- Open a document ---
    if visible:
        st.selectbox(
            "Open document",
            options=[doc_key(d) for d in visible],
            format_func=lambda k: doc_label(by_key[k]),
            index=None,
            placeholder="Select a document to open…",
            key="open_picker",
            on_change=open_selected,
        )
    else:
        st.info("No documents match the current filters.")


def pill_html(status):
    bg, fg = STATUS_PILL.get(status, ("#57606a", "#ffffff"))
    return (
        f'<span style="background-color:{bg};color:{fg};'
        f'padding:2px 10px;border-radius:10px;font-size:0.85em;'
        f'font-weight:600;">{status}</span>'
    )


def render_document(doc):
    st.button("← Back to Library", on_click=back_to_library)

    st.header(f'{doc["number"]} — {doc["title"]}')
    st.markdown(
        f'{pill_html(doc["status"])} &nbsp; Version {doc["version"]} '
        f'&nbsp;·&nbsp; Effective {doc["effective_date"]} '
        f'&nbsp;·&nbsp; Owner: {doc["owner"]}',
        unsafe_allow_html=True,
    )

    history = sorted(
        [d for d in docs if d["number"] == doc["number"]],
        key=lambda d: (d["effective_date"], d["version"]),
    )

    if doc["status"] == "Superseded":
        newer = [
            d for d in docs
            if d["number"] == doc["number"] and d["status"] == "Effective"
        ]
        if newer:
            current = newer[0]
            st.warning(
                f'This version is SUPERSEDED. The current effective '
                f'version is v{current["version"]} '
                f'(effective {current["effective_date"]}).'
            )
            st.button(
                f'Open current effective version — {doc["number"]} '
                f'v{current["version"]}',
                on_click=open_key,
                args=(doc_key(current),),
            )
    elif doc["status"] == "Draft":
        st.info(
            "This document is a DRAFT. It is not effective and must "
            "not be used to perform or review work."
        )

    # --- Properties panel ---
    with st.container(border=True):
        meta = st.columns(4)
        meta[0].metric("Version", doc["version"])
        meta[1].metric("Status", doc["status"])
        meta[2].metric("Effective", doc["effective_date"])
        meta[3].metric("Owner", doc["owner"])
        st.caption(f'Change note: {doc["change_note"]}')

    tab_content, tab_props, tab_audit = st.tabs(
        ["Content", "Properties", "Audit Trail"]
    )

    with tab_content:
        st.markdown(load_doc(doc["file"]))

    with tab_props:
        rows = [
            ("Document number", doc["number"]),
            ("Title", doc["title"]),
            ("Type", doc["type"]),
            ("Version", doc["version"]),
            ("Lifecycle status", doc["status"]),
            ("Effective date", doc["effective_date"]),
            ("Owner", doc["owner"]),
            ("Source file", doc["file"]),
            ("Change note", doc["change_note"]),
        ]
        st.markdown(
            "| Property | Value |\n|---|---|\n"
            + "\n".join(f"| {k} | {v} |" for k, v in rows)
        )
        if len(history) > 1:
            st.subheader(f'Version history — {doc["number"]}')
            for h in history:
                st.write(
                    f'**v{h["version"]}** · {h["status"]} · effective '
                    f'{h["effective_date"]} — {h["change_note"]}'
                )
        st.subheader("Change history")
        for h in history:
            st.write(
                f'**v{h["version"]}** ({h["effective_date"]}): '
                f'{h["change_note"]}'
            )

    with tab_audit:
        st.caption(
            "Audit trail derived from the document register "
            "(version events only)."
        )
        for i, h in enumerate(history):
            st.write(
                f'**{h["effective_date"]}** — {h["number"]} '
                f'v{h["version"]} became Effective. '
                f'Change: {h["change_note"]}'
            )
            if h["status"] == "Superseded" and i + 1 < len(history):
                nxt = history[i + 1]
                st.write(
                    f'**{nxt["effective_date"]}** — {h["number"]} '
                    f'v{h["version"]} Superseded by v{nxt["version"]}.'
                )


if st.session_state.view == "document" and st.session_state.selected_key:
    render_document(by_key[st.session_state.selected_key])
else:
    render_library()

st.divider()
st.caption(
    "Fictitious Labs Inc. is a fictional company. This document library "
    "was generated with [The Procedure Machine]"
    "(https://procedure-machine.streamlit.app/) — a multi-agent pipeline "
    "that drafts quality-system procedures from public regulations and "
    "guidance — and adopted into this fictional quality system."
)
