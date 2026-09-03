# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-03T05:22:24.319891+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11707`

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

- `risk_on_high->unknown_4h` score `40.851` n `111` status `ready` deltaP `18.3875` edge `3.3435` maxDD `-2.2797`
- `risk_on_and_context->unknown_4h` score `40.851` n `111` status `ready` deltaP `18.3875` edge `3.3435` maxDD `-2.2797`
- `market_context_high->unknown_4h` score `28.0197` n `153` status `ready` deltaP `14.3423` edge `2.3089` maxDD `-2.563`
- `risk_on_high->unknown_1h` score `17.8679` n `123` status `ready` deltaP `0.5403` edge `1.5431` maxDD `-1.95`
- `risk_on_and_context->unknown_1h` score `17.8679` n `123` status `ready` deltaP `0.5403` edge `1.5431` maxDD `-1.95`
- `market_context_high->unknown_1h` score `11.6993` n `165` status `ready` deltaP `-0.4501` edge `1.041` maxDD `-2.0446`
- `risk_on_high->equity_24h` score `5.1094` n `107` status `ready` deltaP `23.3548` edge `0.6846` maxDD `-19.828`
- `risk_on_and_context->equity_24h` score `5.1094` n `107` status `ready` deltaP `23.3548` edge `0.6846` maxDD `-19.828`
- `risk_on_high->crypto_alt_24h` score `2.3354` n `107` status `ready` deltaP `21.4304` edge `0.8469` maxDD `-42.8959`
- `risk_on_and_context->crypto_alt_24h` score `2.3354` n `107` status `ready` deltaP `21.4304` edge `0.8469` maxDD `-42.8959`
- `news_risk_high->crypto_alt_24h` score `2.3064` n `59` status `ready` deltaP `21.3512` edge `0.4468` maxDD `-19.4761`
- `news_risk_high->equity_24h` score `2.1095` n `59` status `ready` deltaP `9.3044` edge `0.3605` maxDD `-15.4056`
- `market_context_high->equity_24h` score `1.6665` n `147` status `ready` deltaP `19.324` edge `0.5657` maxDD `-24.4698`
- `news_risk_high->crypto_major_24h` score `1.4026` n `59` status `ready` deltaP `14.5216` edge `0.4584` maxDD `-30.7329`
- `risk_on_high->crypto_major_24h` score `0.7594` n `107` status `ready` deltaP `20.8577` edge `0.8327` maxDD `-56.9519`
- `risk_on_and_context->crypto_major_24h` score `0.7594` n `107` status `ready` deltaP `20.8577` edge `0.8327` maxDD `-56.9519`
- `market_context_high->crypto_major_24h` score `0.5968` n `147` status `ready` deltaP `23.884` edge `0.8637` maxDD `-61.3797`
- `market_context_high->crypto_alt_24h` score `0.4821` n `147` status `ready` deltaP `15.4478` edge `0.7087` maxDD `-46.3234`
- `risk_on_high->metal_1h` score `0.1165` n `123` status `ready` deltaP `12.2815` edge `0.0043` maxDD `-1.699`
- `risk_on_and_context->metal_1h` score `0.1165` n `123` status `ready` deltaP `12.2815` edge `0.0043` maxDD `-1.699`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
