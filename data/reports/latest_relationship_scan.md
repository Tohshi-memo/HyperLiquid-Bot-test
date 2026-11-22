# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-22T07:07:36.605556+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `40`

- Symbol pattern count: `4560`

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

- `market_context_high->unknown_1h` score `10893.8599` n `115` status `ready` deltaP `1.0921` edge `907.8342` maxDD `-0.9188`
- `market_context_high->unknown_4h` score `6704.8893` n `115` status `ready` deltaP `-1.3786` edge `558.7805` maxDD `-0.7759`
- `market_context_high->metal_1h` score `-0.1267` n `115` status `ready` deltaP `5.6456` edge `0.0126` maxDD `-2.6517`
- `market_context_high->index_1h` score `-0.2548` n `115` status `ready` deltaP `3.6709` edge `0.003` maxDD `-1.2295`
- `market_context_high->fx_1h` score `-1.3669` n `115` status `ready` deltaP `-10.3059` edge `-0.0018` maxDD `-0.4719`
- `market_context_high->metal_4h` score `-1.5316` n `115` status `ready` deltaP `6.193` edge `0.0117` maxDD `-10.1161`
- `market_context_high->crypto_major_1h` score `-1.5515` n `115` status `ready` deltaP `2.951` edge `-0.0076` maxDD `-13.8788`
- `market_context_high->fx_4h` score `-1.6954` n `115` status `ready` deltaP `-2.96` edge `0.0023` maxDD `-1.6606`
- `market_context_high->equity_1h` score `-1.7656` n `115` status `ready` deltaP `6.6076` edge `0.0064` maxDD `-13.1399`
- `market_context_high->commodity_1h` score `-2.5329` n `115` status `ready` deltaP `-10.9334` edge `-0.0251` maxDD `-4.3803`
- `market_context_high->index_4h` score `-2.927` n `115` status `ready` deltaP `-8.5379` edge `-0.0237` maxDD `-7.0639`
- `market_context_high->crypto_alt_1h` score `-3.6102` n `115` status `ready` deltaP `-5.7732` edge `-0.0513` maxDD `-13.8848`
- `market_context_high->fx_24h` score `-5.3555` n `115` status `ready` deltaP `-7.6148` edge `-0.0018` maxDD `-6.4982`
- `market_context_high->crypto_major_4h` score `-5.8397` n `115` status `ready` deltaP `-4.5572` edge `-0.0254` maxDD `-47.4317`
- `market_context_high->crypto_alt_4h` score `-6.3451` n `115` status `ready` deltaP `-4.7097` edge `-0.1008` maxDD `-46.5016`
- `market_context_high->commodity_4h` score `-6.8243` n `115` status `ready` deltaP `-17.895` edge `-0.0844` maxDD `-15.1996`
- `market_context_high->metal_24h` score `-9.1484` n `115` status `ready` deltaP `-2.2297` edge `0.0621` maxDD `-52.1012`
- `market_context_high->crypto_major_24h` score `-14.1165` n `115` status `ready` deltaP `10.8605` edge `0.1778` maxDD `-152.134`
- `market_context_high->index_24h` score `-15.5554` n `115` status `ready` deltaP `-30.379` edge `-0.1524` maxDD `-39.9754`
- `market_context_high->crypto_alt_24h` score `-16.5638` n `115` status `ready` deltaP `4.0731` edge `-0.0325` maxDD `-156.7906`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
