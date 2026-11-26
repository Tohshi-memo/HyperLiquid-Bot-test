# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-26T06:22:32.338089+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `3983`

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

- `news_risk_high->unknown_1h` score `3223.3165` n `31` status `ready` deltaP `1.6322` edge `268.6164` maxDD `-0.7395`
- `news_risk_high->unknown_4h` score `3218.2627` n `31` status `ready` deltaP `3.4815` edge `268.171` maxDD `-0.1191`
- `market_context_high->unknown_1h` score `93.0246` n `31` status `ready` deltaP `1.6322` edge `7.7506` maxDD `-0.4209`
- `news_risk_high->equity_24h` score `41.1429` n `31` status `ready` deltaP `47.3958` edge `3.1126` maxDD `0.0`
- `news_risk_high->crypto_major_24h` score `39.1399` n `31` status `ready` deltaP `48.2639` edge `2.9399` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `33.5848` n `31` status `ready` deltaP `47.5694` edge `2.4816` maxDD `0.0`
- `news_risk_high->crypto_alt_4h` score `10.8379` n `31` status `ready` deltaP `26.6079` edge `0.8128` maxDD `-5.2957`
- `news_risk_high->equity_4h` score `10.3987` n `31` status `ready` deltaP `37.682` edge `0.6634` maxDD `-2.178`
- `news_risk_high->metal_24h` score `9.9481` n `31` status `ready` deltaP `33.9438` edge `0.6302` maxDD `-0.1986`
- `news_risk_high->crypto_major_4h` score `6.8157` n `31` status `ready` deltaP `17.5403` edge `0.8986` maxDD `-7.6714`
- `news_risk_high->index_24h` score `6.7492` n `31` status `ready` deltaP `48.7847` edge `0.2372` maxDD `0.0`
- `news_risk_high->fx_24h` score `5.3655` n `31` status `ready` deltaP `45.8782` edge `0.1541` maxDD `-0.0262`
- `news_risk_high->equity_1h` score `3.7122` n `31` status `ready` deltaP `20.2868` edge `0.1928` maxDD `-0.1621`
- `news_risk_high->index_4h` score `3.3958` n `31` status `ready` deltaP `36.6149` edge `0.0649` maxDD `-0.4146`
- `news_risk_high->index_1h` score `2.6914` n `31` status `ready` deltaP `31.8428` edge `0.0205` maxDD `-0.0136`
- `news_risk_high->crypto_major_1h` score `2.486` n `31` status `ready` deltaP `10.1603` edge `0.2971` maxDD `-1.6897`
- `news_risk_high->crypto_alt_1h` score `2.2596` n `31` status `ready` deltaP `12.8549` edge `0.2397` maxDD `-1.5232`
- `market_context_high->fx_4h` score `2.0922` n `31` status `ready` deltaP `26.6572` edge `0.0251` maxDD `-0.2774`
- `news_risk_high->metal_1h` score `1.5118` n `31` status `ready` deltaP `29.5827` edge `0.0245` maxDD `-0.2315`
- `news_risk_high->metal_4h` score `1.0889` n `31` status `ready` deltaP `16.6257` edge `0.0845` maxDD `-0.7918`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
