# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-12T01:07:30.252170+00:00`
- Price records: `672`
- Market context records: `6448`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5875`

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

- `news_risk_high->crypto_alt_24h` score `11.6089` n `32` status `ready` deltaP `29.5139` edge `0.7854` maxDD `-0.5131`
- `market_context_high->unknown_24h` score `8.6391` n `145` status `ready` deltaP `20.1377` edge `0.9157` maxDD `-15.0689`
- `news_risk_high->fx_24h` score `6.3058` n `32` status `ready` deltaP `52.2569` edge `0.1771` maxDD `0.0`
- `news_risk_high->fx_4h` score `4.1096` n `32` status `ready` deltaP `42.7591` edge `0.062` maxDD `-0.0345`
- `news_risk_high->commodity_24h` score `3.9181` n `32` status `ready` deltaP `34.0278` edge `0.1202` maxDD `-0.3101`
- `news_risk_high->crypto_major_24h` score `3.2641` n `32` status `ready` deltaP `11.2847` edge `0.4212` maxDD `-4.2368`
- `news_risk_high->fx_1h` score `2.4685` n `32` status `ready` deltaP `29.7904` edge `0.021` maxDD `-0.1113`
- `news_risk_high->crypto_major_1h` score `1.5459` n `32` status `ready` deltaP `13.9783` edge `0.1517` maxDD `-2.0691`
- `market_context_high->unknown_1h` score `1.1685` n `181` status `ready` deltaP `-6.0327` edge `0.2277` maxDD `-3.2083`
- `news_risk_high->crypto_alt_1h` score `0.9098` n `32` status `ready` deltaP `9.9738` edge `0.0963` maxDD `-1.6923`
- `market_context_high->index_4h` score `0.0625` n `181` status `ready` deltaP `7.2666` edge `0.0244` maxDD `-0.4108`
- `news_risk_high->unknown_1h` score `-0.166` n `32` status `ready` deltaP `6.381` edge `-0.0219` maxDD `-0.7581`
- `market_context_high->metal_4h` score `-0.1922` n `181` status `ready` deltaP `7.7256` edge `0.0413` maxDD `-2.7056`
- `market_context_high->unknown_4h` score `-0.3921` n `181` status `ready` deltaP `-15.4216` edge `0.3107` maxDD `-10.5788`
- `market_context_high->commodity_24h` score `-0.4716` n `145` status `ready` deltaP `2.0666` edge `0.1388` maxDD `-5.6838`
- `news_risk_high->metal_1h` score `-0.5223` n `32` status `ready` deltaP `1.0479` edge `-0.0242` maxDD `-1.6464`
- `market_context_high->metal_1h` score `-0.5555` n `181` status `ready` deltaP `0.7717` edge `0.0014` maxDD `-1.8877`
- `market_context_high->equity_4h` score `-0.5781` n `181` status `ready` deltaP `6.9246` edge `0.0496` maxDD `-8.2573`
- `market_context_high->crypto_alt_1h` score `-0.5972` n `181` status `ready` deltaP `5.8474` edge `0.0167` maxDD `-5.9134`
- `news_risk_high->index_24h` score `-0.6272` n `32` status `ready` deltaP `2.2569` edge `-0.0083` maxDD `-2.3058`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
