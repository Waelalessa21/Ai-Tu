import requests
import streamlit as st

API_URL = "http://127.0.0.1:8000/api/v1/issues"

st.title("Issue Tracker")

tab1, tab2 = st.tabs(["Issues", "Create Issue"])

status_options = ["open", "in_progress", "closed"]
priority_options = ["low", "medium", "high"]


def fetch_issues():
    response = requests.get(f"{API_URL}/", timeout=5)
    response.raise_for_status()
    return response.json()


with tab1:
    try:
        issues = fetch_issues()
    except requests.RequestException:
        st.error("Cannot reach API. Run: fastapi dev main.py")
        st.stop()

    if not issues:
        st.write("No issues yet.")
    for issue in issues:
        with st.expander(f"{issue['title']} [{issue['status']}]"):
            st.write(issue["desc"])
            st.write(f"Priority: {issue['priority']}")
            st.write(f"Created: {issue['created_at']}")

            new_status = st.selectbox(
                "Status",
                status_options,
                index=status_options.index(issue["status"]),
                key=f"status_{issue['id']}",
            )
            new_priority = st.selectbox(
                "Priority",
                priority_options,
                index=priority_options.index(issue["priority"]),
                key=f"priority_{issue['id']}",
            )
            new_title = st.text_input("Title", value=issue["title"], key=f"title_{issue['id']}")
            new_desc = st.text_area("Description", value=issue["desc"], key=f"desc_{issue['id']}")

            col1, col2 = st.columns(2)
            with col1:
                if st.button("Update", key=f"update_{issue['id']}"):
                    response = requests.put(
                        f"{API_URL}/{issue['id']}",
                        json={
                            "title": new_title,
                            "desc": new_desc,
                            "status": new_status,
                            "priority": new_priority,
                        },
                        timeout=5,
                    )
                    if response.ok:
                        st.success("Updated")
                        st.rerun()
                    else:
                        st.error(response.json())
            with col2:
                if st.button("Delete", key=f"delete_{issue['id']}"):
                    response = requests.delete(f"{API_URL}/{issue['id']}", timeout=5)
                    if response.status_code == 204:
                        st.success("Deleted")
                        st.rerun()
                    else:
                        st.error("Delete failed")

with tab2:
    title = st.text_input("Title")
    desc = st.text_area("Description")
    status = st.selectbox("Status", status_options)
    priority = st.selectbox("Priority", priority_options)

    if st.button("Create Issue"):
        if len(title) < 3 or len(desc) < 3:
            st.error("Title and description must be at least 3 characters.")
        else:
            try:
                response = requests.post(
                    f"{API_URL}/",
                    json={
                        "title": title,
                        "desc": desc,
                        "status": status,
                        "priority": priority,
                    },
                    timeout=5,
                )
                if response.status_code == 201:
                    st.success("Issue created")
                    st.rerun()
                else:
                    st.error(response.json())
            except requests.RequestException:
                st.error("Cannot reach API. Run: fastapi dev main.py")
