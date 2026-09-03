# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-03T03:52:37.727560+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11593`

## Conditions

- `news_risk_high`: News Risk is elevated.
- `macro_risk_high`: Macro Risk is elevated.
- `risk_on_high`: Risk-On score is elevated.
- `market_context_high`: Market Context is supportive.
- `polymarket_volume_spike`: Polymarket 24h volume z-score is elevated.
- `flow_alert_high`: Flow Alert score is elevated.
- `news_and_polymarket`: News Risk and Polymarket volume spike happen together.
- `risk_on_and_context`: Risk-On and Market Context are both supportive.
- `macro_and_flow`: Macro Risk and Flow Alert are elevated together.

## Top Patterns

- `risk_on_high->equity_24h` score `5.3943` n `107` status `ready` deltaP `24.3964` edge `0.7014` maxDD `-19.828`
- `risk_on_and_context->equity_24h` score `5.3943` n `107` status `ready` deltaP `24.3964` edge `0.7014` maxDD `-19.828`
- `risk_on_high->unknown_4h` score `4.5049` n `107` status `ready` deltaP `17.7813` edge `0.3187` maxDD `-2.2797`
- `risk_on_and_context->unknown_4h` score `4.5049` n `107` status `ready` deltaP `17.7813` edge `0.3187` maxDD `-2.2797`
- `market_context_high->unknown_4h` score `2.5856` n `147` status `ready` deltaP `13.5153` edge `0.1949` maxDD `-2.563`
- `news_risk_high->equity_24h` score `2.3944` n `59` status `ready` deltaP `10.346` edge `0.3773` maxDD `-15.4056`
- `risk_on_high->crypto_alt_24h` score `2.3271` n `107` status `ready` deltaP `21.2568` edge `0.847` maxDD `-42.8959`
- `risk_on_and_context->crypto_alt_24h` score `2.3271` n `107` status `ready` deltaP `21.2568` edge `0.847` maxDD `-42.8959`
- `news_risk_high->crypto_alt_24h` score `2.2981` n `59` status `ready` deltaP `21.1776` edge `0.4469` maxDD `-19.4761`
- `risk_on_high->unknown_1h` score `1.9497` n `117` status `ready` deltaP `1.5277` edge `0.21` maxDD `-1.95`
- `risk_on_and_context->unknown_1h` score `1.9497` n `117` status `ready` deltaP `1.5277` edge `0.21` maxDD `-1.95`
- `market_context_high->equity_24h` score `1.8517` n `147` status `ready` deltaP `20.3656` edge `0.5825` maxDD `-24.4698`
- `news_risk_high->crypto_major_24h` score `1.2159` n `59` status `ready` deltaP `14.348` edge `0.444` maxDD `-30.7329`
- `market_context_high->unknown_1h` score `0.752` n `159` status `ready` deltaP `0.3182` edge `0.1236` maxDD `-2.0446`
- `risk_on_high->crypto_major_24h` score `0.638` n `107` status `ready` deltaP `20.6841` edge `0.8183` maxDD `-56.9519`
- `risk_on_and_context->crypto_major_24h` score `0.638` n `107` status `ready` deltaP `20.6841` edge `0.8183` maxDD `-56.9519`
- `market_context_high->crypto_major_24h` score `0.4755` n `147` status `ready` deltaP `23.7104` edge `0.8493` maxDD `-61.3797`
- `market_context_high->crypto_alt_24h` score `0.4739` n `147` status `ready` deltaP `15.2742` edge `0.7088` maxDD `-46.3234`
- `risk_on_high->index_1h` score `0.3063` n `117` status `ready` deltaP `9.6794` edge `0.0055` maxDD `-0.5605`
- `risk_on_and_context->index_1h` score `0.3063` n `117` status `ready` deltaP `9.6794` edge `0.0055` maxDD `-0.5605`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
