# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-05T01:07:23.629457+00:00`
- Price records: `672`
- Market context records: `2921`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `6927`

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

- `market_context_high->crypto_alt_24h` score `13.7746` n `142` status `ready` deltaP `13.1187` edge `1.4521` maxDD `-22.6673`
- `market_context_high->equity_24h` score `6.7901` n `142` status `ready` deltaP `15.3315` edge `0.664` maxDD `-12.6963`
- `market_context_high->unknown_24h` score `6.0755` n `142` status `ready` deltaP `13.5392` edge `0.4625` maxDD `-1.7175`
- `market_context_high->index_24h` score `2.3168` n `142` status `ready` deltaP `11.1062` edge `0.2171` maxDD `-2.5127`
- `market_context_high->commodity_24h` score `1.8372` n `142` status `ready` deltaP `15.5516` edge `0.3588` maxDD `-12.4171`
- `market_context_high->index_4h` score `0.5644` n `142` status `ready` deltaP `13.6057` edge `0.0658` maxDD `-2.3986`
- `market_context_high->equity_4h` score `0.5303` n `142` status `ready` deltaP `7.2977` edge `0.1335` maxDD `-5.7037`
- `market_context_high->unknown_4h` score `0.0753` n `142` status `ready` deltaP `4.0514` edge `0.0846` maxDD `-3.7602`
- `market_context_high->crypto_alt_4h` score `-0.0333` n `142` status `ready` deltaP `15.4049` edge `0.3286` maxDD `-28.7261`
- `market_context_high->index_1h` score `-0.0435` n `143` status `ready` deltaP `3.9488` edge `0.0175` maxDD `-1.2855`
- `market_context_high->unknown_1h` score `-0.3492` n `143` status `ready` deltaP `4.0472` edge `0.017` maxDD `-3.1801`
- `market_context_high->equity_1h` score `-0.4256` n `143` status `ready` deltaP `0.4544` edge `0.0448` maxDD `-2.6634`
- `market_context_high->fx_1h` score `-0.5183` n `143` status `ready` deltaP `-0.3475` edge `0.0035` maxDD `-0.2164`
- `market_context_high->crypto_alt_1h` score `-0.5366` n `143` status `ready` deltaP `5.5955` edge `0.0699` maxDD `-10.747`
- `market_context_high->commodity_1h` score `-0.6446` n `143` status `ready` deltaP `-1.096` edge `0.0` maxDD `-4.3601`
- `market_context_high->metal_1h` score `-0.6481` n `143` status `ready` deltaP `0.3967` edge `0.003` maxDD `-3.4325`
- `market_context_high->crypto_major_1h` score `-0.6952` n `143` status `ready` deltaP `5.4929` edge `0.0612` maxDD `-9.622`
- `market_context_high->fx_4h` score `-1.002` n `142` status `ready` deltaP `-1.9237` edge `0.0072` maxDD `-0.5631`
- `market_context_high->commodity_4h` score `-1.2607` n `142` status `ready` deltaP `2.1427` edge `0.0161` maxDD `-10.0279`
- `market_context_high->fx_24h` score `-1.2756` n `142` status `ready` deltaP `-1.7116` edge `-0.0077` maxDD `-0.6418`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
