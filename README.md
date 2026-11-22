# Editorial IG Photos

Midjourney-quality, IG-ready photos from Nano Banana without the AI-slop look: one-light house-style prompts, consistent subjects, vignette and grain finish in code

## Included skills

- `editorial-ig-photos`

## Installation

```bash
npx github:AustineA/editorial-ig-photos
```

This installs the skills separately at:

```text
~/.agents/skills/editorial-ig-photos/
```

It then symlinks them into detected Claude Code, Codex, Cursor, Windsurf, Antigravity, Trae, and Amp installations.

Other commands:

```bash
npx github:AustineA/editorial-ig-photos update     # install the latest version if GitHub has a newer commit
npx github:AustineA/editorial-ig-photos status     # installed commit, where it's installed and linked
npx github:AustineA/editorial-ig-photos uninstall  # remove the copies and their links
```

## Updating

```bash
npx github:AustineA/editorial-ig-photos update
```

It compares the latest commit on GitHub with the one recorded at install time. If yours is older, it clones the latest version and installs it. The installed copy is replaced, not merged, so files removed from a skill don't linger. Restart your agent afterwards.

## Usage

After installation, Needs the Sume MCP connected for generation, and Python 3 with Pillow and numpy for the finish script..

## Package structure

```text
bin/
  install.mjs
skill/
  editorial-ig-photos/
    SKILL.md
package.json
```

## License

MIT
