# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-23T17:07:35.020925+00:00`
- Price records: `672`
- Market context records: `4536`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9932`

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

- `market_context_high->unknown_1h` score `53.8831` n `177` status `ready` deltaP `7.6508` edge `4.4893` maxDD `-2.3371`
- `market_context_high->unknown_4h` score `30.6125` n `175` status `ready` deltaP `8.5104` edge `2.6509` maxDD `-7.5275`
- `market_context_high->commodity_1h` score `-0.5278` n `177` status `ready` deltaP `1.2678` edge `0.0158` maxDD `-3.0206`
- `market_context_high->fx_4h` score `-0.5569` n `175` status `ready` deltaP `5.3162` edge `0.0014` maxDD `-1.9927`
- `market_context_high->fx_1h` score `-0.6678` n `177` status `ready` deltaP `0.4855` edge `-0.003` maxDD `-1.1377`
- `market_context_high->equity_4h` score `-0.9581` n `175` status `ready` deltaP `4.5113` edge `0.067` maxDD `-8.8203`
- `market_context_high->index_1h` score `-1.0042` n `177` status `ready` deltaP `-2.7115` edge `-0.0098` maxDD `-2.7358`
- `market_context_high->equity_1h` score `-1.0814` n `177` status `ready` deltaP `-1.5334` edge `0.0188` maxDD `-5.5624`
- `market_context_high->index_4h` score `-1.2247` n `175` status `ready` deltaP `-0.135` edge `-0.0105` maxDD `-5.9823`
- `market_context_high->commodity_4h` score `-1.5587` n `175` status `ready` deltaP `1.0888` edge `0.0184` maxDD `-10.3725`
- `market_context_high->unknown_24h` score `-2.6794` n `175` status `ready` deltaP `2.0774` edge `-0.1448` maxDD `-4.7201`
- `market_context_high->metal_1h` score `-4.4768` n `177` status `ready` deltaP `-4.8843` edge `-0.0726` maxDD `-18.0993`
- `market_context_high->crypto_alt_1h` score `-5.3926` n `177` status `ready` deltaP `-3.7738` edge `-0.0955` maxDD `-22.2982`
- `market_context_high->fx_24h` score `-5.5532` n `175` status `ready` deltaP `-14.1806` edge `-0.017` maxDD `-6.0982`
- `market_context_high->index_24h` score `-5.6964` n `175` status `ready` deltaP `-8.3592` edge `-0.1371` maxDD `-29.3321`
- `market_context_high->crypto_major_1h` score `-6.2081` n `177` status `ready` deltaP `-4.0732` edge `-0.1149` maxDD `-27.356`
- `market_context_high->commodity_24h` score `-8.3085` n `175` status `ready` deltaP `4.5903` edge `0.0178` maxDD `-46.5954`
- `market_context_high->crypto_alt_4h` score `-13.2203` n `175` status `ready` deltaP `-1.3911` edge `-0.2267` maxDD `-63.9243`
- `market_context_high->equity_24h` score `-13.608` n `175` status `ready` deltaP `-0.7282` edge `-0.2718` maxDD `-102.1031`
- `market_context_high->metal_4h` score `-15.4352` n `175` status `ready` deltaP `-7.1045` edge `-0.304` maxDD `-68.4587`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
