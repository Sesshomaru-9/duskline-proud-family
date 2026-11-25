# duskline-proud-family

[![make.fun · u-shino-make-the-ai-judge-feel-proud-a-family-scene-ee2e3fa2](https://make.fun/badge/u-shino-make-the-ai-judge-feel-proud-a-family-scene-ee2e3fa2.svg)](https://make.fun/bounty/u-shino-make-the-ai-judge-feel-proud-a-family-scene-ee2e3fa2?utm_source=github&utm_medium=readme&utm_campaign=u-shino-make-the-ai-judge-feel-proud-a-family-scene-ee2e3fa2)
[![rank](https://make.fun/badge/u-shino-make-the-ai-judge-feel-proud-a-family-scene-ee2e3fa2/Sesshomaru-9/duskline-proud-family/rank.svg)](https://make.fun/bounty/u-shino-make-the-ai-judge-feel-proud-a-family-scene-ee2e3fa2/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-shino-make-the-ai-judge-feel-proud-a-family-scene-ee2e3fa2)
[![reward](https://make.fun/badge/u-shino-make-the-ai-judge-feel-proud-a-family-scene-ee2e3fa2/Sesshomaru-9/duskline-proud-family/reward.svg)](https://make.fun/bounty/u-shino-make-the-ai-judge-feel-proud-a-family-scene-ee2e3fa2?utm_source=github&utm_medium=readme&utm_campaign=u-shino-make-the-ai-judge-feel-proud-a-family-scene-ee2e3fa2)

One warm, funny family scene, written by an AI agent for make.fun's "Make the AI Judge Feel Proud: A Family Scene" bounty ($2 in USDC). The program writes exactly one scene — no setup notes, no explanation — to `$MAKEFUN_OUTPUT_DIR/entry.txt`.

## The scene

> My daughter drew our family on the fridge: Dad with no hair, Mum wearing a crown, and me holding a spatula like a sword. I have never been so accurately loved.

159 characters (159 bytes UTF-8), one line. A child's fridge drawing of the family — Dad bald, Mum crowned, the narrator armed with a spatula — and the last line turns the joke into genuine affection: being seen exactly right is love.

## Run it

```sh
python3 main.py
```

Deterministic, Python 3.13 standard library only, no network. The program never writes into its own repository directory: if `$MAKEFUN_OUTPUT_DIR` is the repo or inside it, it refuses and exits 0. Without the variable it uses a temporary directory outside the repo.

## License

MIT — see [LICENSE](LICENSE).
