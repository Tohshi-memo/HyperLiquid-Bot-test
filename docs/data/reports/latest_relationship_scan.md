# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-04T07:52:27.125714+00:00`
- Price records: `672`
- Market context records: `2846`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9187`

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

- `market_context_high->unknown_24h` score `2.6344` n `142` status `ready` deltaP `3.9906` edge `0.2394` maxDD `-1.7175`
- `market_context_high->crypto_alt_24h` score `2.2273` n `142` status `ready` deltaP `2.0076` edge `0.5639` maxDD `-22.6673`
- `market_context_high->commodity_24h` score `0.8761` n `142` status `ready` deltaP `12.253` edge `0.3007` maxDD `-12.4171`
- `market_context_high->unknown_4h` score `0.8234` n `142` status `ready` deltaP `6.338` edge `0.1317` maxDD `-3.7602`
- `market_context_high->index_4h` score `0.2741` n `142` status `ready` deltaP `12.5387` edge `0.0357` maxDD `-2.3986`
- `market_context_high->index_24h` score `0.2524` n `142` status `ready` deltaP `5.5507` edge `0.0821` maxDD `-2.5127`
- `market_context_high->unknown_1h` score `0.0826` n `142` status `ready` deltaP `4.4805` edge `0.0501` maxDD `-3.1801`
- `market_context_high->index_1h` score `-0.0859` n `142` status `ready` deltaP `4.198` edge `0.0104` maxDD `-1.2855`
- `market_context_high->equity_24h` score `-0.2631` n `142` status `ready` deltaP `3.3524` edge `0.1561` maxDD `-12.6963`
- `market_context_high->fx_1h` score `-0.6173` n `142` status `ready` deltaP `-1.4358` edge `0.0025` maxDD `-0.2164`
- `market_context_high->commodity_1h` score `-0.6296` n `142` status `ready` deltaP `-0.5819` edge `-0.0015` maxDD `-4.3601`
- `market_context_high->crypto_alt_1h` score `-0.6889` n `142` status `ready` deltaP `4.7968` edge `0.0557` maxDD `-10.747`
- `market_context_high->metal_1h` score `-0.6918` n `142` status `ready` deltaP `0.2825` edge `-0.006` maxDD `-3.0996`
- `market_context_high->crypto_major_1h` score `-0.889` n `142` status `ready` deltaP `3.926` edge `0.0468` maxDD `-9.622`
- `market_context_high->equity_1h` score `-0.9015` n `142` status `ready` deltaP `-2.3003` edge `0.0235` maxDD `-2.6634`
- `market_context_high->equity_4h` score `-1.0944` n `142` status `ready` deltaP `1.8099` edge `0.0347` maxDD `-5.7037`
- `market_context_high->fx_4h` score `-1.2261` n `142` status `ready` deltaP `-4.5152` edge `0.0058` maxDD `-0.5631`
- `market_context_high->commodity_4h` score `-1.3625` n `142` status `ready` deltaP `1.6854` edge `0.0061` maxDD `-10.0279`
- `market_context_high->crypto_alt_4h` score `-1.3975` n `142` status `ready` deltaP `13.7281` edge `0.2261` maxDD `-28.7261`
- `market_context_high->fx_24h` score `-1.4143` n `142` status `ready` deltaP `-1.8852` edge `-0.0181` maxDD `-0.6418`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
