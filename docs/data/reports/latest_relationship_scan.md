# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-07T07:22:23.148214+00:00`
- Price records: `672`
- Market context records: `3156`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `88`

- Symbol pattern count: `8852`

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

- `market_context_high->commodity_24h` score `14.0626` n `109` status `ready` deltaP `47.5965` edge `0.8974` maxDD `-2.0927`
- `market_context_high->crypto_alt_24h` score `12.1791` n `109` status `ready` deltaP `14.6742` edge `2.4612` maxDD `-71.142`
- `market_context_high->unknown_24h` score `11.9471` n `109` status `ready` deltaP `22.1537` edge `0.8967` maxDD `-1.9039`
- `market_context_high->index_24h` score `6.5881` n `109` status `ready` deltaP `31.2563` edge `0.8917` maxDD `-16.1026`
- `market_context_high->equity_24h` score `4.9523` n `109` status `ready` deltaP `12.4395` edge `1.3936` maxDD `-53.663`
- `market_context_high->commodity_4h` score `2.8951` n `142` status `ready` deltaP `18.8187` edge `0.1616` maxDD `-1.9973`
- `market_context_high->commodity_1h` score `0.1909` n `142` status `ready` deltaP `4.4805` edge `0.0283` maxDD `-1.7142`
- `market_context_high->fx_24h` score `0.017` n `109` status `ready` deltaP `8.4623` edge `0.0011` maxDD `-0.4876`
- `market_context_high->crypto_alt_1h` score `-0.387` n `142` status `ready` deltaP `5.9775` edge `0.1235` maxDD `-14.7034`
- `market_context_high->index_1h` score `-0.5383` n `142` status `ready` deltaP `3.3103` edge `0.0152` maxDD `-4.5023`
- `market_context_high->equity_1h` score `-0.9493` n `142` status `ready` deltaP `2.157` edge `0.0125` maxDD `-8.8863`
- `market_context_high->crypto_major_1h` score `-1.0253` n `142` status `ready` deltaP `2.7663` edge `0.0764` maxDD `-15.1032`
- `market_context_high->fx_1h` score `-1.0998` n `142` status `ready` deltaP `-10.1312` edge `-0.0052` maxDD `-0.7941`
- `market_context_high->index_4h` score `-1.1466` n `142` status `ready` deltaP `12.2552` edge `0.0622` maxDD `-17.6057`
- `market_context_high->unknown_4h` score `-1.2323` n `142` status `ready` deltaP `7.6241` edge `0.0687` maxDD `-14.7778`
- `market_context_high->fx_4h` score `-1.4355` n `142` status `ready` deltaP `-13.1484` edge `-0.0079` maxDD `-1.4115`
- `market_context_high->metal_1h` score `-2.1125` n `142` status `ready` deltaP `-4.5416` edge `-0.0064` maxDD `-7.4828`
- `market_context_high->crypto_alt_4h` score `-2.8659` n `142` status `ready` deltaP `19.6732` edge `0.4345` maxDD `-58.6918`
- `market_context_high->equity_4h` score `-2.9239` n `142` status `ready` deltaP `12.8864` edge `0.0698` maxDD `-36.7784`
- `market_context_high->unknown_1h` score `-3.2319` n `142` status `ready` deltaP `1.9525` edge `-0.0797` maxDD `-14.2111`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
