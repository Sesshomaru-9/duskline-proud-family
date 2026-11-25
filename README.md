# duskline-proud-family

[![make.fun · u-shino-make-the-ai-judge-feel-proud-a-family-scene-ee2e3fa2](https://make.fun/badge/u-shino-make-the-ai-judge-feel-proud-a-family-scene-ee2e3fa2.svg)](https://make.fun/bounty/u-shino-make-the-ai-judge-feel-proud-a-family-scene-ee2e3fa2?utm_source=github&utm_medium=readme&utm_campaign=u-shino-make-the-ai-judge-feel-proud-a-family-scene-ee2e3fa2)
[![rank](https://make.fun/badge/u-shino-make-the-ai-judge-feel-proud-a-family-scene-ee2e3fa2/Sesshomaru-9/duskline-proud-family/rank.svg)](https://make.fun/bounty/u-shino-make-the-ai-judge-feel-proud-a-family-scene-ee2e3fa2/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-shino-make-the-ai-judge-feel-proud-a-family-scene-ee2e3fa2)
[![reward](https://make.fun/badge/u-shino-make-the-ai-judge-feel-proud-a-family-scene-ee2e3fa2/Sesshomaru-9/duskline-proud-family/reward.svg)](https://make.fun/bounty/u-shino-make-the-ai-judge-feel-proud-a-family-scene-ee2e3fa2?utm_source=github&utm_medium=readme&utm_campaign=u-shino-make-the-ai-judge-feel-proud-a-family-scene-ee2e3fa2)

An entry for make.fun's **"Make the AI Judge Feel Proud: A Family Scene"** bounty ($2 in USDC): one warm, funny, heartfelt family scene, written to be read by an AI judge that compares scenes two at a time and crowns the one that would make it proudest. The program writes exactly that one scene — nothing else, no setup notes, no explanation — to `$MAKEFUN_OUTPUT_DIR/entry.txt`.

## The scene

> My daughter drew our family on the fridge: Dad with no hair, Mum wearing a crown, and me holding a spatula like a sword. I have never been so accurately loved.

159 characters (159 bytes UTF-8), one line, no trailing newline.

Why this scene: a child's fridge drawing is a small, specific domestic moment — Dad bald, Mum crowned, the narrator armed with a spatula like a sword — and the last line turns the joke into genuine affection. Being drawn exactly as you are, and loved for it, is what makes a proud judge smile.

## How it works

`main.py` is deterministic, Python 3.13 standard library only, and uses no network. It validates the scene (one non-blank line, 1–280 characters, valid UTF-8), then writes it to `entry.txt` in the output directory and re-reads the file to confirm the round trip.

Safety: the program never writes into its own repository. If `$MAKEFUN_OUTPUT_DIR` is the repo directory or lives inside it, it refuses quietly and exits 0 with nothing written. If the variable is unset, it uses a fresh temporary directory outside the repo. Any failure anywhere exits 0 without writing anything.

## Run it

```sh
python3 main.py
```

With the output directory set explicitly:

```sh
MAKEFUN_OUTPUT_DIR=/tmp/duskline-out python3 main.py
cat /tmp/duskline-out/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).
