# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-04T00:22:20.710382+00:00`
- Price records: `672`
- Market context records: `2815`
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

- `market_context_high->unknown_24h` score `2.4606` n `142` status `ready` deltaP `3.1225` edge `0.2307` maxDD `-1.7175`
- `market_context_high->unknown_4h` score `0.9266` n `142` status `ready` deltaP `6.338` edge `0.1403` maxDD `-3.7602`
- `market_context_high->commodity_24h` score `0.6907` n `142` status `ready` deltaP `11.2114` edge `0.2922` maxDD `-12.4171`
- `market_context_high->index_4h` score `0.3403` n `142` status `ready` deltaP `13.3009` edge `0.0391` maxDD `-2.3986`
- `market_context_high->crypto_alt_24h` score `0.2372` n `142` status `ready` deltaP `-0.2494` edge `0.4131` maxDD `-22.6673`
- `market_context_high->unknown_1h` score `0.1545` n `142` status `ready` deltaP `5.229` edge `0.0511` maxDD `-3.1801`
- `market_context_high->index_1h` score `-0.0376` n `142` status `ready` deltaP `4.7968` edge `0.0126` maxDD `-1.2855`
- `market_context_high->fx_1h` score `-0.5239` n `142` status `ready` deltaP `-0.3879` edge `0.0033` maxDD `-0.2164`
- `market_context_high->commodity_1h` score `-0.6273` n `142` status `ready` deltaP `-0.1328` edge `-0.0042` maxDD `-4.3601`
- `market_context_high->metal_1h` score `-0.6318` n `142` status `ready` deltaP `0.5819` edge `-0.0003` maxDD `-3.0996`
- `market_context_high->crypto_alt_1h` score `-0.7794` n `142` status `ready` deltaP `4.7968` edge `0.0441` maxDD `-10.747`
- `market_context_high->equity_1h` score `-0.8319` n `142` status `ready` deltaP `-2.3003` edge `0.0293` maxDD `-2.6634`
- `market_context_high->crypto_major_1h` score `-0.9513` n `142` status `ready` deltaP `3.7763` edge `0.0398` maxDD `-9.622`
- `market_context_high->equity_4h` score `-0.993` n `142` status `ready` deltaP `2.2673` edge `0.0401` maxDD `-5.7037`
- `market_context_high->fx_4h` score `-1.1715` n `142` status `ready` deltaP `-4.0579` edge `0.0073` maxDD `-0.5631`
- `market_context_high->commodity_4h` score `-1.4856` n `142` status `ready` deltaP `0.9232` edge `-0.0046` maxDD `-10.0279`
- `market_context_high->index_24h` score `-1.6403` n `142` status `ready` deltaP `0.3423` edge `-0.0409` maxDD `-2.5127`
- `market_context_high->fx_24h` score `-1.7387` n `142` status `ready` deltaP `-5.0102` edge `-0.0243` maxDD `-0.6418`
- `market_context_high->crypto_alt_4h` score `-1.9503` n `142` status `ready` deltaP `13.1183` edge `0.1841` maxDD `-28.7261`
- `market_context_high->metal_4h` score `-2.2178` n `142` status `ready` deltaP `-0.3134` edge `-0.0272` maxDD `-11.4038`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
