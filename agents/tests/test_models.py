
from agents.models import *
from agents.tests.build_test_data import Build
from django.test import TestCase


class TestModels(TestCase):
    def setUp(self):
        Build().build_data()
        self.user_agent = Agent.objects.get(name="user_proxy")
        self.assistant = Agent.objects.get(name="assistant")
        self.rag_user_proxy = Agent.objects.get(name="retrieval_user_proxy")
        self.rag_assistant = Agent.objects.get(name="retrieval_assistant")
        self.teacher = Agent.objects.get(name="teachable")

    def test_agents(self):
        user_proxy_agent = self.user_agent.get_agent()
        assistant_agent = self.assistant.get_agent()

        user_proxy_agent.initiate_chat(assistant_agent, message="Plot a chart of NVDA and TESLA stock price change YTD.")

    def test_rag_agents(self):
        rag_proxy_agent = self.rag_user_proxy.get_agent(
            task="qa",
            docs_path="https://raw.githubusercontent.com/microsoft/autogen/main/README.md"
        )
        rag_assistant = self.rag_assistant.get_agent()

        rag_proxy_agent.initiate_chat(rag_assistant, problem="What is Autogen")

    def test_teachable_agent(self):
        user = self.user_agent.get_agent()
        teacher_agent = self.teacher.get_agent(reset_db=True)

        teacher_agent.initiate_chat(user, message="Greetings, I'm a teachable user assistant! What's on your mind today?")












