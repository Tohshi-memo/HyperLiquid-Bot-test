# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-29T09:37:30.313004+00:00`
- Price records: `672`
- Market context records: `8289`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5892`

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

- `news_risk_high->unknown_24h` score `5949.0936` n `54` status `ready` deltaP `33.912` edge `495.5738` maxDD `-2.0332`
- `news_risk_high->equity_4h` score `6.8915` n `54` status `ready` deltaP `25.4686` edge `0.4642` maxDD `-3.4427`
- `news_risk_high->equity_1h` score `2.9431` n `54` status `ready` deltaP `21.2298` edge `0.1346` maxDD `-1.1366`
- `news_risk_high->index_4h` score `2.5961` n `54` status `ready` deltaP `21.81` edge `0.09` maxDD `-0.191`
- `news_risk_high->crypto_major_4h` score `1.9762` n `54` status `ready` deltaP `9.2593` edge `0.261` maxDD `-2.8833`
- `news_risk_high->crypto_alt_1h` score `1.8279` n `54` status `ready` deltaP `14.4045` edge `0.0997` maxDD `-1.1388`
- `news_risk_high->crypto_alt_4h` score `1.5311` n `54` status `ready` deltaP `17.2313` edge `0.2206` maxDD `-5.8012`
- `news_risk_high->crypto_major_1h` score `1.5226` n `54` status `ready` deltaP `10.3072` edge `0.0979` maxDD `-1.1783`
- `news_risk_high->metal_4h` score `1.0138` n `54` status `ready` deltaP `9.2818` edge `0.0694` maxDD `-0.7433`
- `news_risk_high->index_1h` score `0.3992` n `54` status `ready` deltaP `6.3041` edge `0.0201` maxDD `-0.3089`
- `news_risk_high->fx_1h` score `0.1518` n `54` status `ready` deltaP `6.6977` edge `0.0029` maxDD `-0.2475`
- `news_risk_high->metal_1h` score `-0.0832` n `54` status `ready` deltaP `3.2546` edge `0.0117` maxDD `-0.5599`
- `news_risk_high->fx_4h` score `-0.4532` n `54` status `ready` deltaP `4.6127` edge `0.0069` maxDD `-0.6604`
- `news_risk_high->commodity_1h` score `-2.0916` n `54` status `ready` deltaP `-8.3611` edge `-0.04` maxDD `-2.9516`
- `news_risk_high->fx_24h` score `-5.038` n `54` status `ready` deltaP `-20.544` edge `-0.0485` maxDD `-5.4165`
- `news_risk_high->metal_24h` score `-5.6224` n `54` status `ready` deltaP `-20.4283` edge `-0.0553` maxDD `-10.8302`
- `news_risk_high->commodity_4h` score `-8.7202` n `54` status `ready` deltaP `-30.1999` edge `-0.1946` maxDD `-13.1269`
- `news_risk_high->commodity_24h` score `-10.9574` n `54` status `ready` deltaP `-5.9606` edge `-0.2794` maxDD `-33.8515`
- `news_risk_high->index_24h` score `-12.0168` n `54` status `ready` deltaP `-23.9004` edge `-0.2918` maxDD `-28.0214`
- `news_risk_high->crypto_major_24h` score `-31.8658` n `54` status `ready` deltaP `-11.8635` edge `-1.1239` maxDD `-103.8662`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
