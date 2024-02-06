import autogen
from agents.models import *


class Build:

    def build_data(self):
        self.build_api_keys()
        self.build_llm_configs()
        self.build_user_proxy_agents()

    @staticmethod
    def build_api_keys():
        keys = [
            APIKey(
                model_name="openai",
                _value="OPEN_AI_SECRET_KEY",
            ),
        ]

        APIKey.objects.bulk_create(keys)

    @staticmethod
    def build_llm_configs():
        api_key = APIKey.objects.get(model_name="openai")

        config1 = LLMConfig.objects.create(
            name="standard",
            timeout=600,
            cache_seed=42,
            temperature=25,
        )
        config1.save()
        config1.api_keys.add(api_key)

    @staticmethod
    def build_user_proxy_agents() -> None:
        config = LLMConfig.objects.get(name="standard")

        agents = [
            Agent(
                name="summarization_agent",
                agent_type="user_proxy_agent",
                _code_execution_config=True,
                system_message="Summarize the given article. Give it the title 'TL;DR'",
                llm_config=config,
            )
        ]

        Agent.objects.bulk_create(agents)



