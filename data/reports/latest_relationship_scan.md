# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-03T23:37:24.041523+00:00`
- Price records: `672`
- Market context records: `2811`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9237`

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

- `market_context_high->unknown_24h` score `2.5206` n `142` status `ready` deltaP `3.1225` edge `0.2357` maxDD `-1.7175`
- `market_context_high->unknown_4h` score `1.0016` n `142` status `ready` deltaP `6.7953` edge `0.1435` maxDD `-3.7602`
- `market_context_high->commodity_24h` score `0.6823` n `142` status `ready` deltaP `11.2114` edge `0.2915` maxDD `-12.4171`
- `market_context_high->crypto_alt_24h` score `0.5116` n `142` status `ready` deltaP `0.2715` edge `0.4325` maxDD `-22.6673`
- `market_context_high->index_4h` score `0.3434` n `142` status `ready` deltaP `13.3009` edge `0.0395` maxDD `-2.3986`
- `market_context_high->unknown_1h` score `0.0706` n `142` status `ready` deltaP `4.7799` edge `0.0471` maxDD `-3.1801`
- `market_context_high->index_1h` score `-0.0579` n `142` status `ready` deltaP `4.4974` edge `0.012` maxDD `-1.2855`
- `market_context_high->fx_1h` score `-0.5239` n `142` status `ready` deltaP `-0.3879` edge `0.0033` maxDD `-0.2164`
- `market_context_high->metal_1h` score `-0.6037` n `142` status `ready` deltaP `0.8813` edge `0.0013` maxDD `-3.0996`
- `market_context_high->commodity_1h` score `-0.6265` n `142` status `ready` deltaP `-0.1328` edge `-0.0041` maxDD `-4.3601`
- `market_context_high->crypto_alt_1h` score `-0.7677` n `142` status `ready` deltaP `4.9465` edge `0.0446` maxDD `-10.747`
- `market_context_high->equity_1h` score `-0.8547` n `142` status `ready` deltaP `-2.45` edge `0.0284` maxDD `-2.6634`
- `market_context_high->crypto_major_1h` score `-0.9591` n `142` status `ready` deltaP `3.7763` edge `0.0388` maxDD `-9.622`
- `market_context_high->equity_4h` score `-0.9894` n `142` status `ready` deltaP `2.2673` edge `0.0404` maxDD `-5.7037`
- `market_context_high->fx_4h` score `-1.1703` n `142` status `ready` deltaP `-4.0579` edge `0.0074` maxDD `-0.5631`
- `market_context_high->commodity_4h` score `-1.5406` n `142` status `ready` deltaP `0.4659` edge `-0.0086` maxDD `-10.0279`
- `market_context_high->fx_24h` score `-1.7514` n `142` status `ready` deltaP `-5.1838` edge `-0.0242` maxDD `-0.6418`
- `market_context_high->crypto_alt_4h` score `-1.7795` n `142` status `ready` deltaP `13.4232` edge `0.1963` maxDD `-28.7261`
- `market_context_high->index_24h` score `-1.808` n `142` status `ready` deltaP `-0.1785` edge `-0.0514` maxDD `-2.5127`
- `market_context_high->metal_4h` score `-2.1293` n `142` status `ready` deltaP `0.1439` edge `-0.0189` maxDD `-11.4038`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
