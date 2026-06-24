# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-24T02:52:29.739981+00:00`
- Price records: `672`
- Market context records: `4580`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9993`

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

- `market_context_high->unknown_1h` score `69.9402` n `157` status `ready` deltaP `6.7347` edge `5.8335` maxDD `-2.3371`
- `market_context_high->unknown_4h` score `3.5401` n `157` status `ready` deltaP `7.9122` edge `0.3633` maxDD `-4.6834`
- `market_context_high->fx_4h` score `-0.584` n `157` status `ready` deltaP `4.7664` edge `0.0016` maxDD `-1.9927`
- `market_context_high->commodity_1h` score `-0.6296` n `157` status `ready` deltaP `1.0994` edge `0.0198` maxDD `-2.0345`
- `market_context_high->fx_1h` score `-0.749` n `157` status `ready` deltaP `-0.5473` edge `-0.0033` maxDD `-1.1038`
- `market_context_high->index_4h` score `-0.8309` n `157` status `ready` deltaP `2.3487` edge `-0.0099` maxDD `-5.9823`
- `market_context_high->equity_1h` score `-0.9093` n `157` status `ready` deltaP `-2.4877` edge `-0.0013` maxDD `-5.5624`
- `market_context_high->equity_4h` score `-0.9159` n `157` status `ready` deltaP `2.1147` edge `0.0454` maxDD `-8.8203`
- `market_context_high->commodity_4h` score `-1.1915` n `157` status `ready` deltaP `3.6614` edge `0.0336` maxDD `-9.1941`
- `market_context_high->index_1h` score `-1.6151` n `157` status `ready` deltaP `-3.2743` edge `-0.0119` maxDD `-2.7358`
- `market_context_high->unknown_24h` score `-2.577` n `155` status `ready` deltaP `1.5278` edge `-0.1326` maxDD `-4.7201`
- `market_context_high->metal_1h` score `-2.9135` n `157` status `ready` deltaP `-3.9552` edge `-0.082` maxDD `-17.8795`
- `market_context_high->index_24h` score `-5.2668` n `155` status `ready` deltaP `-7.192` edge `-0.0898` maxDD `-29.3321`
- `market_context_high->fx_24h` score `-5.3114` n `155` status `ready` deltaP `-12.1629` edge `-0.0103` maxDD `-6.0982`
- `market_context_high->crypto_alt_1h` score `-5.492` n `157` status `ready` deltaP `-2.5258` edge `-0.1121` maxDD `-22.2982`
- `market_context_high->commodity_24h` score `-5.8893` n `155` status `ready` deltaP `8.3815` edge `0.0378` maxDD `-34.0892`
- `market_context_high->crypto_major_1h` score `-6.7351` n `157` status `ready` deltaP `-6.0862` edge `-0.1454` maxDD `-27.356`
- `market_context_high->crypto_alt_4h` score `-9.0301` n `157` status `ready` deltaP `-3.4925` edge `-0.2687` maxDD `-63.9243`
- `market_context_high->metal_4h` score `-10.1917` n `157` status `ready` deltaP `-7.5151` edge `-0.3348` maxDD `-67.4051`
- `market_context_high->crypto_major_4h` score `-11.9262` n `157` status `ready` deltaP `-3.5741` edge `-0.4108` maxDD `-82.2164`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
