# Agent Skills — .claude

This directory exposes repository-local skills to compatible coding agents. Each skill is in a `<name>/SKILL.md` directory with portable `name` and `description` YAML frontmatter.

The workflows use the repository's canonical `wiki/`, `docs/` and `stages/` paths; they do not override agent safety or permissions. `.agents/` is included for tools recognizing the plural Agent Skills convention, while `.agent/` is retained per repository specification.

See [Agent Skills guide](../docs/AGENT_SKILLS.md).
