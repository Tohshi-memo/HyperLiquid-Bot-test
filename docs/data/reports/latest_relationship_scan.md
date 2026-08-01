# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-01T18:22:26.701327+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5915`

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

- `news_risk_high->unknown_24h` score `5190.0358` n `60` status `ready` deltaP `33.7146` edge `432.3203` maxDD `-2.0332`
- `market_context_high->crypto_alt_24h` score `17.0996` n `53` status `ready` deltaP `55.3644` edge `1.0956` maxDD `-2.1786`
- `news_risk_high->equity_4h` score `6.5756` n `60` status `ready` deltaP `24.3699` edge `0.4452` maxDD `-3.4427`
- `news_risk_high->index_4h` score `2.7044` n `60` status `ready` deltaP `23.9126` edge `0.085` maxDD `-0.191`
- `market_context_high->commodity_24h` score `2.0018` n `53` status `ready` deltaP `29.5641` edge `0.2454` maxDD `-10.2019`
- `news_risk_high->crypto_major_4h` score `1.3643` n `60` status `ready` deltaP `8.2012` edge `0.1978` maxDD `-3.5385`
- `news_risk_high->crypto_alt_4h` score `0.6056` n `60` status `ready` deltaP `12.439` edge `0.1339` maxDD `-5.8012`
- `market_context_high->crypto_alt_4h` score `0.5911` n `53` status `ready` deltaP `9.0428` edge `0.1112` maxDD `-5.323`
- `news_risk_high->equity_1h` score `0.5762` n `68` status `ready` deltaP `8.2952` edge `0.075` maxDD `-2.916`
- `news_risk_high->fx_4h` score `0.2778` n `60` status `ready` deltaP `14.1463` edge `0.0246` maxDD `-0.6604`
- `market_context_high->fx_4h` score `0.2216` n `53` status `ready` deltaP `13.8633` edge `0.0156` maxDD `-1.3685`
- `news_risk_high->metal_4h` score `0.1867` n `60` status `ready` deltaP `5.437` edge `0.0353` maxDD `-0.8085`
- `news_risk_high->crypto_alt_1h` score `0.1411` n `68` status `ready` deltaP `7.08` edge `0.0391` maxDD `-3.1233`
- `market_context_high->fx_1h` score `-0.0161` n `53` status `ready` deltaP `7.2026` edge `0.0009` maxDD `-0.6874`
- `news_risk_high->index_1h` score `-0.0917` n `68` status `ready` deltaP `1.8669` edge `0.0081` maxDD `-0.5845`
- `market_context_high->commodity_1h` score `-0.1033` n `53` status `ready` deltaP `3.7284` edge `0.016` maxDD `-1.3282`
- `news_risk_high->fx_1h` score `-0.112` n `68` status `ready` deltaP `2.0694` edge `0.0041` maxDD `-0.2475`
- `news_risk_high->metal_1h` score `-0.1255` n `68` status `ready` deltaP `2.6154` edge `0.0068` maxDD `-0.5599`
- `news_risk_high->crypto_major_1h` score `-0.1672` n `68` status `ready` deltaP `2.6682` edge `0.0328` maxDD `-3.762`
- `market_context_high->fx_24h` score `-0.1996` n `53` status `ready` deltaP `4.9802` edge `0.0392` maxDD `-2.506`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
