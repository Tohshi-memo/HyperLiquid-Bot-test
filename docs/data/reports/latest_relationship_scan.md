# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-28T13:52:28.397792+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `7396`

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

- `news_risk_high->unknown_1h` score `3406.4232` n `31` status `ready` deltaP `2.231` edge `283.8713` maxDD `-0.7395`
- `news_risk_high->unknown_4h` score `3229.2081` n `31` status `ready` deltaP `3.634` edge `269.0821` maxDD `-0.1191`
- `news_risk_high->crypto_major_24h` score `24.2313` n `31` status `ready` deltaP `36.2218` edge `1.7778` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `17.9894` n `31` status `ready` deltaP `34.1421` edge `1.2715` maxDD `0.0`
- `news_risk_high->equity_24h` score `13.0158` n `31` status `ready` deltaP `28.9428` edge `0.8917` maxDD `0.0`
- `news_risk_high->crypto_alt_4h` score `9.2856` n `31` status `ready` deltaP `24.1689` edge `0.6997` maxDD `-5.2957`
- `news_risk_high->crypto_major_4h` score `5.914` n `31` status `ready` deltaP `18.4549` edge `0.7769` maxDD `-7.6714`
- `news_risk_high->equity_4h` score `5.7954` n `31` status `ready` deltaP `32.0417` edge `0.3174` maxDD `-2.178`
- `news_risk_high->fx_24h` score `5.084` n `31` status `ready` deltaP `41.969` edge `0.1567` maxDD `-0.0262`
- `news_risk_high->metal_24h` score `4.0012` n `31` status `ready` deltaP `17.387` edge `0.245` maxDD `-0.1986`
- `news_risk_high->index_4h` score `2.6048` n `31` status `ready` deltaP `31.7369` edge `0.0315` maxDD `-0.4146`
- `news_risk_high->index_24h` score `2.4513` n `31` status `ready` deltaP `26.5165` edge `0.0275` maxDD `0.0`
- `news_risk_high->index_1h` score `2.3822` n `31` status `ready` deltaP `29.1482` edge `0.0127` maxDD `-0.0136`
- `news_risk_high->equity_1h` score `2.2827` n `31` status `ready` deltaP `15.0473` edge `0.1086` maxDD `-0.1621`
- `news_risk_high->crypto_major_1h` score `2.1298` n `31` status `ready` deltaP `7.4657` edge `0.2694` maxDD `-1.6897`
- `news_risk_high->crypto_alt_1h` score `1.9478` n `31` status `ready` deltaP `10.6094` edge `0.2147` maxDD `-1.5232`
- `news_risk_high->metal_1h` score `1.1543` n `31` status `ready` deltaP `24.942` edge `0.0096` maxDD `-0.2315`
- `market_context_high->metal_4h` score `1.0093` n `48` status `ready` deltaP `14.8882` edge `0.026` maxDD `-0.2914`
- `news_risk_high->commodity_4h` score `0.4655` n `31` status `ready` deltaP `10.8084` edge `0.0274` maxDD `-0.5151`
- `news_risk_high->metal_4h` score `0.3617` n `31` status `ready` deltaP `11.5952` edge `0.0248` maxDD `-0.7918`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
