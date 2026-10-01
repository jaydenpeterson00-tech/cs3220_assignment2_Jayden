import streamlit as st
from src.CompanyEnvironmentClass import CompanyEnvironment
from src.Task1_YourRecipientsClasses import OfficeManager, Student, ITStaff
from src.agents import ReflexAgentA2pro
from src.locations import loc_A, loc_B, loc_C

import io
from contextlib import redirect_stdout

from src.catFriendlyHouse_envClass import catFriendlyHouse_env
from src.catFriendlyHouse_membersClass import Milk, Sausage, Mouse
from src.agents import ReflexAgentA3pro

from src.catFriendlyHouse_envClass import catFriendlyHouse2_env
from src.agents import RandomMouseAgent, ReflexAgentA4pro

st.title("Assignment 2 - Simple Intelligent Agents")

tab1, tab2, tab3 = st.tabs([
    "Task 1 - Delivery Agent",
    "Task 2 - Cat Agent",
    "Task 3 - Cat vs Mouse"
])

with tab1:
    st.header("Task 1 - Reflex Delivery Agent")

    if st.button("Run Task 1"):
        output = io.StringIO()

        with redirect_stdout(output):
            ce = CompanyEnvironment()

            student = Student()
            staff = ITStaff()
            manager = OfficeManager()

            ce.add_thing(student)
            ce.add_thing(staff)
            ce.add_thing(manager)

            agent = ReflexAgentA2pro()
            ce.add_thing(agent)

            ce.run()

        st.code(output.getvalue())

with tab2:
    st.header("Task 2 - Reflex Cat Agent")

    if st.button("Run Task 2"):
        output = io.StringIO()

        with redirect_stdout(output):
            e = catFriendlyHouse_env()

            milk = Milk(weight=200, calories=50)
            sausage = Sausage(weight=150, calories=505)
            mouse = Mouse(size=2)

            e.add_thing(milk)
            e.add_thing(sausage)
            e.add_thing(mouse)

            cat = ReflexAgentA3pro()
            e.add_thing(cat)

            e.run()

        st.code(output.getvalue())

with tab3:
    st.header("Task 3 - Cat vs Mouse")

    if st.button("Run Task 3"):
        output = io.StringIO()

        with redirect_stdout(output):
            e2 = catFriendlyHouse2_env()

            mouseAgent = RandomMouseAgent()
            e2.add_thing(mouseAgent)
            print("Mouse Agent is located at {}.".format(mouseAgent.location))

            catAgent = ReflexAgentA4pro()
            e2.add_thing(catAgent)
            print("Cat Agent is located at {}.".format(catAgent.location))

            print("State of the House Environment: {}.".format(e2.locations))
            print("N of agents: {}.".format(len(e2.agents)))
            for a in e2.agents:
                print(f"loc: {a.location}, perf: {a.performance}")

            e2.run()

        st.code(output.getvalue())
