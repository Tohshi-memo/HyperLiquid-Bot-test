# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-24T18:52:31.422941+00:00`
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

- `market_context_high->unknown_1h` score `32284.3046` n `45` status `ready` deltaP `1.4171` edge `2690.3587` maxDD `-0.4209`
- `market_context_high->unknown_4h` score `22095.1597` n `45` status `ready` deltaP `3.1776` edge `1841.256` maxDD `-0.7765`
- `news_risk_high->unknown_1h` score `1049.3497` n `31` status `ready` deltaP `1.6322` edge `87.4525` maxDD `-0.7395`
- `news_risk_high->unknown_4h` score `842.2122` n `31` status `ready` deltaP `4.3962` edge `70.1607` maxDD `-0.1191`
- `news_risk_high->crypto_major_24h` score `38.1671` n `31` status `ready` deltaP `50.1736` edge `2.8461` maxDD `0.0`
- `news_risk_high->equity_24h` score `36.2691` n `31` status `ready` deltaP `42.7083` edge `2.7377` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `33.521` n `31` status `ready` deltaP `48.4375` edge `2.4705` maxDD `0.0`
- `news_risk_high->crypto_alt_4h` score `11.4693` n `31` status `ready` deltaP `25.8457` edge `0.8705` maxDD `-5.2957`
- `news_risk_high->metal_24h` score `11.1026` n `31` status `ready` deltaP `41.2355` edge `0.6778` maxDD `-0.1986`
- `news_risk_high->equity_4h` score `9.9816` n `31` status `ready` deltaP `34.3283` edge `0.651` maxDD `-2.178`
- `news_risk_high->crypto_major_4h` score `7.1188` n `31` status `ready` deltaP `17.083` edge `0.9405` maxDD `-7.6714`
- `news_risk_high->fx_24h` score `6.1799` n `31` status `ready` deltaP `52.1282` edge `0.1803` maxDD `-0.0262`
- `news_risk_high->index_24h` score `5.4021` n `31` status `ready` deltaP `40.4514` edge `0.1805` maxDD `0.0`
- `news_risk_high->equity_1h` score `3.4329` n `31` status `ready` deltaP `18.3407` edge `0.1825` maxDD `-0.1621`
- `news_risk_high->index_4h` score `3.0213` n `31` status `ready` deltaP `32.8039` edge `0.0591` maxDD `-0.4146`
- `market_context_high->fx_4h` score `2.7927` n `45` status `ready` deltaP `33.899` edge `0.0352` maxDD `-0.2774`
- `news_risk_high->crypto_major_1h` score `2.5779` n `31` status `ready` deltaP `11.3579` edge `0.3009` maxDD `-1.6897`
- `news_risk_high->index_1h` score `2.4985` n `31` status `ready` deltaP `29.747` edge `0.0184` maxDD `-0.0136`
- `news_risk_high->crypto_alt_1h` score `2.2286` n `31` status `ready` deltaP `11.0585` edge `0.2477` maxDD `-1.5232`
- `news_risk_high->metal_1h` score `1.6334` n `31` status `ready` deltaP `30.6306` edge `0.0331` maxDD `-0.2315`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
