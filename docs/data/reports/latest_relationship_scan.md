# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-24T18:07:31.325290+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4200`

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

- `market_context_high->unknown_1h` score `32287.1498` n `45` status `ready` deltaP `1.4171` edge `2690.5958` maxDD `-0.4209`
- `market_context_high->unknown_4h` score `22097.1647` n `45` status `ready` deltaP `3.0251` edge `1841.4241` maxDD `-0.7765`
- `news_risk_high->unknown_1h` score `1052.1949` n `31` status `ready` deltaP `1.6322` edge `87.6896` maxDD `-0.7395`
- `news_risk_high->unknown_4h` score `844.2172` n `31` status `ready` deltaP `4.2437` edge `70.3288` maxDD `-0.1191`
- `news_risk_high->crypto_major_24h` score `37.9202` n `31` status `ready` deltaP `49.6528` edge `2.829` maxDD `0.0`
- `news_risk_high->equity_24h` score `35.9502` n `31` status `ready` deltaP `42.1875` edge `2.7146` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `33.2165` n `31` status `ready` deltaP `47.9167` edge `2.4486` maxDD `0.0`
- `news_risk_high->crypto_alt_4h` score `11.3259` n `31` status `ready` deltaP `25.3884` edge `0.8616` maxDD `-5.2957`
- `news_risk_high->metal_24h` score `11.1002` n `31` status `ready` deltaP `41.2355` edge `0.6776` maxDD `-0.1986`
- `news_risk_high->equity_4h` score `9.7662` n `31` status `ready` deltaP `33.871` edge `0.6361` maxDD `-2.178`
- `news_risk_high->crypto_major_4h` score `7.0326` n `31` status `ready` deltaP `16.6257` edge `0.9325` maxDD `-7.6714`
- `news_risk_high->fx_24h` score `6.2492` n `31` status `ready` deltaP `52.649` edge `0.1826` maxDD `-0.0262`
- `news_risk_high->index_24h` score `5.3412` n `31` status `ready` deltaP `39.9306` edge `0.1789` maxDD `0.0`
- `news_risk_high->equity_1h` score `3.4713` n `31` status `ready` deltaP `18.6401` edge `0.1837` maxDD `-0.1621`
- `news_risk_high->index_4h` score `2.9849` n `31` status `ready` deltaP `32.499` edge `0.0581` maxDD `-0.4146`
- `market_context_high->fx_4h` score `2.8317` n `45` status `ready` deltaP `34.3563` edge `0.0354` maxDD `-0.2774`
- `news_risk_high->crypto_major_1h` score `2.5919` n `31` status `ready` deltaP `11.5076` edge `0.3017` maxDD `-1.6897`
- `news_risk_high->index_1h` score `2.5249` n `31` status `ready` deltaP `30.0464` edge `0.0186` maxDD `-0.0136`
- `news_risk_high->crypto_alt_1h` score `2.2185` n `31` status `ready` deltaP `10.9088` edge `0.2474` maxDD `-1.5232`
- `news_risk_high->metal_1h` score `1.6443` n `31` status `ready` deltaP `30.7803` edge `0.0335` maxDD `-0.2315`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
