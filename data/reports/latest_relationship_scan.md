# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-26T08:07:39.056665+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4031`

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

- `news_risk_high->unknown_4h` score `3254.1271` n `31` status `ready` deltaP `3.4815` edge `271.1597` maxDD `-0.1191`
- `news_risk_high->unknown_1h` score `3223.8637` n `31` status `ready` deltaP `1.6322` edge `268.662` maxDD `-0.7395`
- `market_context_high->unknown_1h` score `93.5718` n `31` status `ready` deltaP `1.6322` edge `7.7962` maxDD `-0.4209`
- `news_risk_high->equity_24h` score `39.6428` n `31` status `ready` deltaP `46.1806` edge `2.9957` maxDD `0.0`
- `news_risk_high->crypto_major_24h` score `38.2531` n `31` status `ready` deltaP `47.0486` edge `2.8741` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `32.6319` n `31` status `ready` deltaP `46.3542` edge `2.4103` maxDD `0.0`
- `news_risk_high->crypto_alt_4h` score `10.9975` n `31` status `ready` deltaP `27.5226` edge `0.82` maxDD `-5.2957`
- `news_risk_high->equity_4h` score `10.6436` n `31` status `ready` deltaP `38.749` edge `0.6767` maxDD `-2.178`
- `news_risk_high->metal_24h` score `9.5293` n `31` status `ready` deltaP `32.7285` edge `0.6034` maxDD `-0.1986`
- `news_risk_high->crypto_major_4h` score `6.9171` n `31` status `ready` deltaP `18.4549` edge `0.9055` maxDD `-7.6714`
- `news_risk_high->index_24h` score `6.5284` n `31` status `ready` deltaP `47.5694` edge `0.2269` maxDD `0.0`
- `news_risk_high->fx_24h` score `5.2992` n `31` status `ready` deltaP `45.1837` edge `0.1532` maxDD `-0.0262`
- `news_risk_high->equity_1h` score `3.759` n `31` status `ready` deltaP `20.4365` edge `0.1957` maxDD `-0.1621`
- `news_risk_high->index_4h` score `3.5064` n `31` status `ready` deltaP `37.682` edge `0.067` maxDD `-0.4146`
- `news_risk_high->index_1h` score `2.7333` n `31` status `ready` deltaP `32.2919` edge `0.021` maxDD `-0.0136`
- `news_risk_high->crypto_major_1h` score `2.5` n `31` status `ready` deltaP `10.1603` edge `0.2989` maxDD `-1.6897`
- `news_risk_high->crypto_alt_1h` score `2.3071` n `31` status `ready` deltaP `13.4537` edge `0.2418` maxDD `-1.5232`
- `market_context_high->fx_4h` score `2.1372` n `31` status `ready` deltaP `27.1145` edge `0.0258` maxDD `-0.2774`
- `news_risk_high->metal_1h` score `1.5173` n `31` status `ready` deltaP `29.5827` edge `0.0252` maxDD `-0.2315`
- `news_risk_high->metal_4h` score `1.1086` n `31` status `ready` deltaP `16.7781` edge `0.086` maxDD `-0.7918`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
