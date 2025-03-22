# Agent Components Index

This agent configuration has been split into modular components for better context loading. Reference the specific component needed for your current context.

## Available Agent Components

1. [Agent Identity](agent/identity.md) - Core identity of the dev0 agent
2. [Agent Capabilities](agent/capabilities.md) - What the agent can do
3. [Agent Limitations](agent/limitations.md) - What the agent will not do

## Using The Agent Components

Load only the relevant components when needed to optimize context usage:

```
// Example: Load agent identity
!include agent/identity.md

// Example: Load agent capabilities
!include agent/capabilities.md
```
