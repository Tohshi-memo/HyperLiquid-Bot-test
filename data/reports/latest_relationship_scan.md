# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-24T19:37:32.936524+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4092`

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

- `market_context_high->unknown_1h` score `32268.3578` n `45` status `ready` deltaP `1.4171` edge `2689.0298` maxDD `-0.4209`
- `market_context_high->unknown_4h` score `22079.0065` n `45` status `ready` deltaP `3.1776` edge `1839.9099` maxDD `-0.7765`
- `news_risk_high->unknown_1h` score `1033.4029` n `31` status `ready` deltaP `1.6322` edge `86.1236` maxDD `-0.7395`
- `news_risk_high->unknown_4h` score `826.059` n `31` status `ready` deltaP `4.3962` edge `68.8146` maxDD `-0.1191`
- `news_risk_high->crypto_major_24h` score `38.3483` n `31` status `ready` deltaP `50.1736` edge `2.8612` maxDD `0.0`
- `news_risk_high->equity_24h` score `36.5603` n `31` status `ready` deltaP `43.2292` edge `2.7585` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `33.8015` n `31` status `ready` deltaP `48.9583` edge `2.4904` maxDD `0.0`
- `news_risk_high->crypto_alt_4h` score `11.5969` n `31` status `ready` deltaP `26.1506` edge `0.8791` maxDD `-5.2957`
- `news_risk_high->metal_24h` score `11.1002` n `31` status `ready` deltaP `41.2355` edge `0.6776` maxDD `-0.1986`
- `news_risk_high->equity_4h` score `10.1812` n `31` status `ready` deltaP `34.6332` edge `0.6656` maxDD `-2.178`
- `news_risk_high->crypto_major_4h` score `7.1961` n `31` status `ready` deltaP `17.2354` edge `0.9494` maxDD `-7.6714`
- `news_risk_high->fx_24h` score `6.1107` n `31` status `ready` deltaP `51.6073` edge `0.178` maxDD `-0.0262`
- `news_risk_high->index_24h` score `5.4606` n `31` status `ready` deltaP `40.9722` edge `0.1819` maxDD `0.0`
- `news_risk_high->equity_1h` score `3.4341` n `31` status `ready` deltaP `18.3407` edge `0.1826` maxDD `-0.1621`
- `news_risk_high->index_4h` score `3.0479` n `31` status `ready` deltaP `32.9564` edge `0.0603` maxDD `-0.4146`
- `market_context_high->fx_4h` score `2.7549` n `45` status `ready` deltaP `33.4417` edge `0.0351` maxDD `-0.2774`
- `news_risk_high->crypto_major_1h` score `2.6301` n `31` status `ready` deltaP `11.807` edge `0.3046` maxDD `-1.6897`
- `news_risk_high->index_1h` score `2.4985` n `31` status `ready` deltaP `29.747` edge `0.0184` maxDD `-0.0136`
- `news_risk_high->crypto_alt_1h` score `2.2824` n `31` status `ready` deltaP `11.5076` edge `0.2516` maxDD `-1.5232`
- `news_risk_high->metal_4h` score `1.6328` n `31` status `ready` deltaP `21.5037` edge `0.1217` maxDD `-0.7918`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
