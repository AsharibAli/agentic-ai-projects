FROM langchain/langgraph-api:3.11

ADD . /deps/react-agents

RUN pip install --upgrade pip

RUN PYTHONDONTWRITEBYTECODE=1 pip install --no-cache-dir -c /api/constraints.txt -e /deps/*

ENV LANGSERVE_GRAPHS='{"react_agent": "./src/react_agent/graph.py:react_graph"}'

WORKDIR /deps/react-agents