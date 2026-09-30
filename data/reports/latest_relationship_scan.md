# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-30T05:37:24.653628+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `7330`

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

- `news_risk_high->unknown_24h` score `1398.1744` n `135` status `ready` deltaP `1.9097` edge `116.5018` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `18.9256` n `135` status `ready` deltaP `29.2477` edge `1.4031` maxDD `-1.0093`
- `news_risk_high->equity_24h` score `8.6531` n `135` status `ready` deltaP `29.2477` edge `0.761` maxDD `-9.4579`
- `news_risk_high->crypto_major_24h` score `8.1628` n `135` status `ready` deltaP `24.1667` edge `0.8345` maxDD `-15.8971`
- `news_risk_high->index_24h` score `3.9966` n `135` status `ready` deltaP `35.4398` edge `0.1446` maxDD `-0.4916`
- `news_risk_high->metal_24h` score `3.6733` n `135` status `ready` deltaP `27.6157` edge `0.2494` maxDD `-2.192`
- `news_risk_high->equity_4h` score `3.0102` n `135` status `ready` deltaP `30.0858` edge `0.2104` maxDD `-9.143`
- `news_risk_high->crypto_alt_4h` score `1.9662` n `135` status `ready` deltaP `11.4171` edge `0.3537` maxDD `-15.9436`
- `news_risk_high->crypto_alt_1h` score `1.1293` n `135` status `ready` deltaP `9.5509` edge `0.1215` maxDD `-4.2849`
- `news_risk_high->equity_1h` score `0.9439` n `135` status `ready` deltaP `9.7006` edge `0.0763` maxDD `-1.6514`
- `news_risk_high->index_1h` score `0.5329` n `135` status `ready` deltaP `9.267` edge `0.0114` maxDD `-0.302`
- `news_risk_high->index_4h` score `-0.0457` n `135` status `ready` deltaP `7.8636` edge `0.0291` maxDD `-1.493`
- `news_risk_high->metal_1h` score `-0.4838` n `135` status `ready` deltaP `1.1577` edge `0.0149` maxDD `-0.7016`
- `news_risk_high->crypto_major_1h` score `-0.4952` n `135` status `ready` deltaP `2.6391` edge `0.0694` maxDD `-7.2607`
- `news_risk_high->metal_4h` score `-1.2624` n `135` status `ready` deltaP `-7.3893` edge `0.0282` maxDD `-2.9297`
- `news_risk_high->fx_4h` score `-1.3681` n `135` status `ready` deltaP `7.8376` edge `-0.0063` maxDD `-3.0414`
- `news_risk_high->crypto_major_4h` score `-1.5697` n `135` status `ready` deltaP `-3.6833` edge `0.0948` maxDD `-13.719`
- `news_risk_high->commodity_1h` score `-1.8203` n `135` status `ready` deltaP `-8.5185` edge `-0.0091` maxDD `-3.3986`
- `news_risk_high->fx_1h` score `-1.9152` n `135` status `ready` deltaP `-10.1031` edge `-0.0042` maxDD `-1.0436`
- `news_risk_high->commodity_4h` score `-2.2215` n `135` status `ready` deltaP `-8.6924` edge `0.015` maxDD `-8.6825`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
