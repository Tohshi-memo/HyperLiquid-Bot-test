# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-24T03:07:29.760923+00:00`
- Price records: `672`
- Market context records: `4581`
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

- `market_context_high->unknown_1h` score `69.9006` n `157` status `ready` deltaP `6.585` edge `5.8312` maxDD `-2.3371`
- `market_context_high->unknown_4h` score `3.5713` n `157` status `ready` deltaP `7.9122` edge `0.3659` maxDD `-4.6834`
- `market_context_high->fx_4h` score `-0.5927` n `157` status `ready` deltaP `4.6139` edge `0.0015` maxDD `-1.9927`
- `market_context_high->commodity_1h` score `-0.6272` n `157` status `ready` deltaP `1.0994` edge `0.02` maxDD `-2.0345`
- `market_context_high->fx_1h` score `-0.7621` n `157` status `ready` deltaP `-0.697` edge `-0.0034` maxDD `-1.1038`
- `market_context_high->index_4h` score `-0.8214` n `157` status `ready` deltaP `2.5011` edge `-0.0097` maxDD `-5.9823`
- `market_context_high->equity_1h` score `-0.8914` n `157` status `ready` deltaP `-2.338` edge `0.0` maxDD `-5.5624`
- `market_context_high->equity_4h` score `-0.9627` n `157` status `ready` deltaP `2.1147` edge `0.0394` maxDD `-8.8203`
- `market_context_high->commodity_4h` score `-1.1915` n `157` status `ready` deltaP `3.6614` edge `0.0336` maxDD `-9.1941`
- `market_context_high->index_1h` score `-1.6103` n `157` status `ready` deltaP `-3.2743` edge `-0.0115` maxDD `-2.7358`
- `market_context_high->unknown_24h` score `-2.511` n `155` status `ready` deltaP `1.5278` edge `-0.1271` maxDD `-4.7201`
- `market_context_high->metal_1h` score `-2.9026` n `157` status `ready` deltaP `-3.8055` edge `-0.0816` maxDD `-17.8795`
- `market_context_high->index_24h` score `-5.2367` n `155` status `ready` deltaP `-7.0184` edge `-0.0871` maxDD `-29.3321`
- `market_context_high->fx_24h` score `-5.2927` n `155` status `ready` deltaP `-11.9893` edge `-0.0099` maxDD `-6.0982`
- `market_context_high->crypto_alt_1h` score `-5.462` n `157` status `ready` deltaP `-2.3761` edge `-0.1106` maxDD `-22.2982`
- `market_context_high->commodity_24h` score `-5.8965` n `155` status `ready` deltaP `8.3815` edge `0.0372` maxDD `-34.0892`
- `market_context_high->crypto_major_1h` score `-6.7087` n `157` status `ready` deltaP `-5.9365` edge `-0.1442` maxDD `-27.356`
- `market_context_high->crypto_alt_4h` score `-9.019` n `157` status `ready` deltaP `-3.34` edge `-0.2683` maxDD `-63.9243`
- `market_context_high->metal_4h` score `-10.1799` n `157` status `ready` deltaP `-7.3627` edge `-0.3343` maxDD `-67.4051`
- `market_context_high->crypto_major_4h` score `-11.927` n `157` status `ready` deltaP `-3.5741` edge `-0.4109` maxDD `-82.2164`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
