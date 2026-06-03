# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-03T20:37:28.581588+00:00`
- Price records: `672`
- Market context records: `2798`
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

- `market_context_high->unknown_24h` score `2.9048` n `142` status `ready` deltaP `4.685` edge `0.2573` maxDD `-1.7175`
- `market_context_high->crypto_alt_24h` score `1.5517` n `142` status `ready` deltaP `2.0076` edge `0.5076` maxDD `-22.6673`
- `market_context_high->unknown_4h` score `1.0018` n `142` status `ready` deltaP `6.9478` edge `0.1425` maxDD `-3.7602`
- `market_context_high->commodity_24h` score `0.5881` n `142` status `ready` deltaP `11.0377` edge `0.2848` maxDD `-12.4171`
- `market_context_high->index_4h` score `0.3169` n `142` status `ready` deltaP `13.3009` edge `0.0361` maxDD `-2.3986`
- `market_context_high->unknown_1h` score `0.0526` n `142` status `ready` deltaP `4.7799` edge `0.0456` maxDD `-3.1801`
- `market_context_high->index_1h` score `-0.0579` n `142` status `ready` deltaP `4.6471` edge `0.011` maxDD `-1.2855`
- `market_context_high->fx_1h` score `-0.5395` n `142` status `ready` deltaP `-0.5376` edge `0.003` maxDD `-0.2164`
- `market_context_high->metal_1h` score `-0.5967` n `142` status `ready` deltaP `0.8813` edge `0.0022` maxDD `-3.0996`
- `market_context_high->crypto_alt_1h` score `-0.6749` n `142` status `ready` deltaP `5.0962` edge `0.0555` maxDD `-10.747`
- `market_context_high->commodity_1h` score `-0.6842` n `142` status `ready` deltaP `-0.7316` edge `-0.0075` maxDD `-4.3601`
- `market_context_high->crypto_major_1h` score `-0.8656` n `142` status `ready` deltaP `4.2254` edge `0.0478` maxDD `-9.622`
- `market_context_high->equity_1h` score `-0.9147` n `142` status `ready` deltaP `-2.3003` edge `0.0224` maxDD `-2.6634`
- `market_context_high->fx_4h` score `-1.1581` n `142` status `ready` deltaP `-3.9054` edge `0.0074` maxDD `-0.5631`
- `market_context_high->equity_4h` score `-1.1934` n `142` status `ready` deltaP `2.2673` edge `0.0234` maxDD `-5.7037`
- `market_context_high->crypto_alt_4h` score `-1.5339` n `142` status `ready` deltaP `14.0329` edge `0.2127` maxDD `-28.7261`
- `market_context_high->fx_24h` score `-1.5969` n `142` status `ready` deltaP `-3.4477` edge `-0.0229` maxDD `-0.6418`
- `market_context_high->commodity_4h` score `-1.6381` n `142` status `ready` deltaP `-0.4488` edge `-0.015` maxDD `-10.0279`
- `market_context_high->metal_4h` score `-2.046` n `142` status `ready` deltaP `-0.0086` edge `-0.0072` maxDD `-11.4038`
- `market_context_high->index_24h` score `-2.367` n `142` status `ready` deltaP `-2.2618` edge `-0.0841` maxDD `-2.5127`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
