# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-26T03:52:23.099070+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `3911`

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

- `market_context_high->unknown_1h` score `38703.5272` n `38` status `ready` deltaP `0.1891` edge `3225.3021` maxDD `-0.4209`
- `news_risk_high->unknown_4h` score `3196.8677` n `31` status `ready` deltaP `3.3291` edge `266.3891` maxDD `-0.1191`
- `news_risk_high->unknown_1h` score `886.8145` n `31` status `ready` deltaP `1.6322` edge `73.9079` maxDD `-0.7395`
- `news_risk_high->equity_24h` score `43.0722` n `31` status `ready` deltaP `49.1319` edge `3.2618` maxDD `0.0`
- `news_risk_high->crypto_major_24h` score `40.486` n `31` status `ready` deltaP `50.0` edge `3.0405` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `35.1096` n `31` status `ready` deltaP `49.3056` edge `2.5971` maxDD `0.0`
- `news_risk_high->crypto_alt_4h` score `10.7923` n `31` status `ready` deltaP `26.6079` edge `0.809` maxDD `-5.2957`
- `news_risk_high->metal_24h` score `10.5982` n `31` status `ready` deltaP `35.6799` edge `0.6728` maxDD `-0.1986`
- `news_risk_high->equity_4h` score `10.1917` n `31` status `ready` deltaP `37.2247` edge `0.6492` maxDD `-2.178`
- `news_risk_high->index_24h` score `7.0405` n `31` status `ready` deltaP `50.5208` edge `0.2499` maxDD `0.0`
- `news_risk_high->crypto_major_4h` score `6.7796` n `31` status `ready` deltaP `17.2354` edge `0.896` maxDD `-7.6714`
- `news_risk_high->fx_24h` score `5.3643` n `31` status `ready` deltaP `45.8782` edge `0.154` maxDD `-0.0262`
- `news_risk_high->equity_1h` score `3.6103` n `31` status `ready` deltaP `19.8377` edge `0.1873` maxDD `-0.1621`
- `news_risk_high->index_4h` score `3.3268` n `31` status `ready` deltaP `36.1576` edge `0.0622` maxDD `-0.4146`
- `news_risk_high->index_1h` score `2.671` n `31` status `ready` deltaP `31.6931` edge `0.0198` maxDD `-0.0136`
- `news_risk_high->crypto_major_1h` score `2.4408` n `31` status `ready` deltaP `9.8609` edge `0.2933` maxDD `-1.6897`
- `market_context_high->fx_4h` score `2.4114` n `38` status `ready` deltaP `29.5972` edge `0.0321` maxDD `-0.2774`
- `news_risk_high->crypto_alt_1h` score `2.2362` n `31` status `ready` deltaP `12.5555` edge `0.2387` maxDD `-1.5232`
- `news_risk_high->metal_1h` score `1.4916` n `31` status `ready` deltaP `29.2833` edge `0.0239` maxDD `-0.2315`
- `news_risk_high->metal_4h` score `1.1297` n `31` status `ready` deltaP `16.9305` edge `0.0877` maxDD `-0.7918`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
