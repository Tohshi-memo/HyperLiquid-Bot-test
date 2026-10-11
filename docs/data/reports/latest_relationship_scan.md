# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-11T17:22:30.865409+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `88`

- Symbol pattern count: `8174`

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

- `market_context_high->unknown_24h` score `1381.1923` n `40` status `ready` deltaP `-20.4861` edge `115.2723` maxDD `-1.2425`
- `market_context_high->unknown_4h` score `53.0415` n `78` status `ready` deltaP `-7.0083` edge `4.5249` maxDD `-2.3109`
- `market_context_high->unknown_1h` score `10.5561` n `90` status `ready` deltaP `-3.0605` edge `0.9337` maxDD `-1.0231`
- `market_context_high->equity_24h` score `8.8104` n `40` status `ready` deltaP `27.6736` edge `0.5926` maxDD `-1.0977`
- `market_context_high->index_24h` score `6.3856` n `40` status `ready` deltaP `52.4306` edge `0.1826` maxDD `0.0`
- `market_context_high->fx_24h` score `3.3319` n `40` status `ready` deltaP `37.6389` edge `0.0397` maxDD `-0.0374`
- `market_context_high->crypto_major_24h` score `1.6477` n `40` status `ready` deltaP `-20.5903` edge `0.5894` maxDD `-17.8526`
- `market_context_high->crypto_alt_1h` score `0.7395` n `90` status `ready` deltaP `7.5815` edge `0.1145` maxDD `-4.9401`
- `market_context_high->fx_4h` score `0.7219` n `78` status `ready` deltaP `12.0935` edge `0.0079` maxDD `-0.2692`
- `market_context_high->commodity_4h` score `0.4215` n `78` status `ready` deltaP `11.304` edge `0.0131` maxDD `-1.6002`
- `market_context_high->crypto_major_1h` score `-0.0126` n `90` status `ready` deltaP `1.986` edge `0.0746` maxDD `-3.7778`
- `market_context_high->commodity_1h` score `-0.0584` n `90` status `ready` deltaP `2.7745` edge `0.005` maxDD `-0.6025`
- `market_context_high->fx_1h` score `-0.1249` n `90` status `ready` deltaP `1.8763` edge `0.0013` maxDD `-0.271`
- `market_context_high->metal_1h` score `-0.1499` n `90` status `ready` deltaP `6.344` edge `0.0041` maxDD `-0.7107`
- `market_context_high->metal_4h` score `-0.3658` n `78` status `ready` deltaP `3.2989` edge `0.0198` maxDD `-1.1153`
- `market_context_high->index_1h` score `-0.622` n `90` status `ready` deltaP `-1.9461` edge `-0.0017` maxDD `-0.5392`
- `market_context_high->crypto_major_4h` score `-0.7398` n `78` status `ready` deltaP `-3.0566` edge `0.1361` maxDD `-11.1784`
- `market_context_high->index_4h` score `-0.8639` n `78` status `ready` deltaP `-6.4377` edge `0.0022` maxDD `-0.9364`
- `market_context_high->equity_1h` score `-0.9528` n `90` status `ready` deltaP `-5.6254` edge `0.0023` maxDD `-2.2898`
- `market_context_high->crypto_alt_4h` score `-1.7345` n `78` status `ready` deltaP `-6.465` edge `0.1544` maxDD `-13.8008`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
