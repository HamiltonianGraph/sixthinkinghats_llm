# sixthinkinghats_llm
An implementation of de Bono's Six Thinking Hats brainstorming methodology using agentic LLM workflows

## Overview ##

As is well known by now, Large Language Models are capable of exceptional creativity. Properly prompted, they can produce outputs that are competitive with teams of humans. What is less well known is that this capability is even more pronounced when multiple instances of a model are connected together in multiagent workflows. 

Some recent (as of this writing) arXiv papers on this:

[Improving Factuality and Reasoning in Language Models through Multiagent Debate](https://arxiv.org/abs/2305.14325)

[AgentCoder: Multi-Agent Code Generation with Effective Testing and Self-optimisation](https://arxiv.org/abs/2312.13010)

[LLM Discussion: Enhancing the Creativity of Large Language Models via Discussion Framework and Role-Play](https://arxiv.org/abs/2405.06373)

This work is an implementation of the last paper, linking six large-language models together. The agents together implement Edward de Bono's [Six Thinking Hats](https://en.wikipedia.org/wiki/Six_Thinking_Hats) brainstorming methodology. Each 'agent' is an instance of OpenAI's GPT-4o (though other OpenAI models can be used), assigned a specific role in the brainstorming discussion:

![Six Thinking Hats explained](https://i1.wp.com/njdiaries.com/wp-content/uploads/2016/08/Six-Hats-explained.jpg)

(not my graphic)

For convenience, the Python script includes the agent template from my [openai-agent](https://github.com/HamiltonianGraph/openai_agent) repository.


