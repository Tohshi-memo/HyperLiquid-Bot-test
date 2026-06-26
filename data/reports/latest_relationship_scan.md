# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-26T09:37:35.115779+00:00`
- Price records: `672`
- Market context records: `4814`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `7588`

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

- `market_context_high->unknown_1h` score `11.6927` n `117` status `ready` deltaP `11.5577` edge `0.9391` maxDD `-1.674`
- `market_context_high->unknown_4h` score `7.8306` n `117` status `ready` deltaP `18.1038` edge `0.6529` maxDD `-4.6834`
- `market_context_high->unknown_24h` score `2.2088` n `110` status `ready` deltaP `12.5758` edge `0.1914` maxDD `-4.6272`
- `market_context_high->equity_4h` score `0.3109` n `117` status `ready` deltaP `9.7366` edge `0.1131` maxDD `-6.3852`
- `market_context_high->commodity_1h` score `0.1527` n `117` status `ready` deltaP `6.3284` edge `0.0293` maxDD `-2.0345`
- `market_context_high->commodity_4h` score `0.1285` n `117` status `ready` deltaP `12.6277` edge `0.0495` maxDD `-4.377`
- `market_context_high->index_4h` score `-0.2395` n `117` status `ready` deltaP `7.6897` edge `0.0146` maxDD `-4.7259`
- `market_context_high->fx_4h` score `-0.3156` n `117` status `ready` deltaP `5.0657` edge `0.0034` maxDD `-1.5439`
- `market_context_high->equity_1h` score `-0.6013` n `117` status `ready` deltaP `2.5859` edge `0.0094` maxDD `-4.1397`
- `market_context_high->fx_1h` score `-1.0371` n `117` status `ready` deltaP `-2.7113` edge `-0.0034` maxDD `-0.8626`
- `market_context_high->index_1h` score `-1.3386` n `117` status `ready` deltaP `-0.7702` edge `-0.006` maxDD `-2.6999`
- `market_context_high->commodity_24h` score `-2.1453` n `110` status `ready` deltaP `19.8958` edge `0.1032` maxDD `-27.5371`
- `market_context_high->metal_1h` score `-2.3444` n `117` status `ready` deltaP `-1.7696` edge `-0.0712` maxDD `-14.0715`
- `market_context_high->fx_24h` score `-2.7461` n `110` status `ready` deltaP `-12.5221` edge `-0.0191` maxDD `-3.1009`
- `market_context_high->crypto_major_1h` score `-3.0079` n `117` status `ready` deltaP `0.1957` edge `-0.0779` maxDD `-22.0555`
- `market_context_high->crypto_alt_1h` score `-3.0126` n `117` status `ready` deltaP `1.9244` edge `-0.0479` maxDD `-14.945`
- `market_context_high->index_24h` score `-4.3235` n `110` status `ready` deltaP `-6.6067` edge `-0.1194` maxDD `-23.2678`
- `market_context_high->crypto_alt_4h` score `-4.3802` n `117` status `ready` deltaP `6.6227` edge `-0.0149` maxDD `-41.9318`
- `market_context_high->crypto_major_4h` score `-8.1981` n `117` status `ready` deltaP `3.7211` edge `-0.1755` maxDD `-66.6939`
- `market_context_high->metal_4h` score `-8.5932` n `117` status `ready` deltaP `4.8428` edge `-0.3123` maxDD `-61.0675`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
