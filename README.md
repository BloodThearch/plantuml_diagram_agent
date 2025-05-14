
# PlantUML Diagram Agent

Create UML Diagrams using PlantUML and LLM(s).

Note: Project is still WIP.




## Installation

Here are guided installation steps:

### Cloning The Project

```
git clone https://github.com/BloodThearch/plantuml_diagram_agent.git
```

### Installing Requirements

You can choose to install requirements, in your own custom virtual environment.

```
cd plantuml_diagram_agent
pip install -r requirements.txt
```

### OpenAI Supported Models Key Setup

Create a file named `.env` in the root of the project to save your Model API Key and URL as environment variable. Currently meta/llama-3.1-8b-instruct is being used through Nvidia API.

### Download PlantUML JAR file

Download the local jar file for PlantUML through their official website. And place the file in `plantuml_diagram_agent/plantuml directory`, with the name `plantuml.jar`.

### Run Tests

If all the tests are successful then the stable release of the project is correctly installed on your system.

```
python runTests.py
```

## Current Progress

- Pydantic validation setup for 3 diagrams (Sequence, usecase, class).
- Create a driver function for the project
- API based model integration (OpenAI)

## To-do

- ~~Create a driver function for the project~~
- UI
- ~~Model integration (either api based or offloaded here)~~
- Add more UML diagrams for pydantic validation.