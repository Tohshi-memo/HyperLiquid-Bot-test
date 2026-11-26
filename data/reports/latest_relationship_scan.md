# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-26T11:37:28.564558+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `3455`

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

- `news_risk_high->unknown_1h` score `3233.5405` n `31` status `ready` deltaP `1.6322` edge `269.4684` maxDD `-0.7395`
- `news_risk_high->unknown_4h` score `3228.5623` n `31` status `ready` deltaP `3.4815` edge `269.0293` maxDD `-0.1191`
- `market_context_high->unknown_1h` score `103.2486` n `31` status `ready` deltaP `1.6322` edge `8.6026` maxDD `-0.4209`
- `news_risk_high->equity_24h` score `36.278` n `31` status `ready` deltaP `43.75` edge `2.7315` maxDD `0.0`
- `news_risk_high->crypto_major_24h` score `36.195` n `31` status `ready` deltaP `44.6181` edge `2.7188` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `30.4263` n `31` status `ready` deltaP `43.9236` edge `2.2427` maxDD `0.0`
- `news_risk_high->crypto_alt_4h` score `10.9664` n `31` status `ready` deltaP `27.675` edge `0.8164` maxDD `-5.2957`
- `news_risk_high->equity_4h` score `10.8046` n `31` status `ready` deltaP `39.8161` edge `0.683` maxDD `-2.178`
- `news_risk_high->metal_24h` score `8.7444` n `31` status `ready` deltaP `30.298` edge `0.5542` maxDD `-0.1986`
- `news_risk_high->crypto_major_4h` score `7.0525` n `31` status `ready` deltaP `19.9793` edge `0.9127` maxDD `-7.6714`
- `news_risk_high->index_24h` score `6.0399` n `31` status `ready` deltaP `45.1389` edge `0.2024` maxDD `0.0`
- `news_risk_high->fx_24h` score `5.0519` n `31` status `ready` deltaP `42.7532` edge `0.1488` maxDD `-0.0262`
- `news_risk_high->equity_1h` score `3.8645` n `31` status `ready` deltaP `21.185` edge `0.1995` maxDD `-0.1621`
- `news_risk_high->index_4h` score `3.5733` n `31` status `ready` deltaP `38.4442` edge `0.0675` maxDD `-0.4146`
- `news_risk_high->index_1h` score `2.8016` n `31` status `ready` deltaP `33.0404` edge `0.0217` maxDD `-0.0136`
- `news_risk_high->crypto_major_1h` score `2.5148` n `31` status `ready` deltaP `10.1603` edge `0.3008` maxDD `-1.6897`
- `news_risk_high->crypto_alt_1h` score `2.2721` n `31` status `ready` deltaP `13.0046` edge `0.2403` maxDD `-1.5232`
- `market_context_high->fx_4h` score `1.985` n `31` status `ready` deltaP `25.4377` edge `0.0243` maxDD `-0.2774`
- `news_risk_high->metal_1h` score `1.4963` n `31` status `ready` deltaP `29.2833` edge `0.0245` maxDD `-0.2315`
- `news_risk_high->metal_4h` score `1.0566` n `31` status `ready` deltaP `16.1683` edge `0.0834` maxDD `-0.7918`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
