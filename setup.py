from setuptools import setup, find_packages

setup(
    name="xmmersia-agentcore",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[
        "pydantic>=2.0.0",
        "typing-extensions>=4.0.0",
    ],
    python_requires=">=3.8",
    author="Marc Santugini",
    author_email="marc@xmmersia.com",
    description="Immutable foundation for all Xmmersia agents",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/Ayahualulco/Xmmersia-AgentCore",
)