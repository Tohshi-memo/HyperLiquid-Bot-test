# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-25T06:37:32.278537+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `7786`

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

- `market_context_high->unknown_4h` score `48.9855` n `98` status `ready` deltaP `0.4885` edge `4.1124` maxDD `-1.016`
- `market_context_high->unknown_1h` score `15.7287` n `110` status `ready` deltaP `3.963` edge `1.3332` maxDD `-1.5781`
- `market_context_high->crypto_alt_24h` score `11.6133` n `35` status `ready` deltaP `31.7361` edge `0.817` maxDD `-4.1975`
- `market_context_high->crypto_major_24h` score `3.3689` n `35` status `ready` deltaP `20.2926` edge `0.2514` maxDD `-5.8084`
- `market_context_high->commodity_24h` score `0.579` n `35` status `ready` deltaP `11.989` edge `0.0852` maxDD `-3.6055`
- `market_context_high->fx_24h` score `-0.0219` n `35` status `ready` deltaP `9.7917` edge `0.0061` maxDD `-0.9352`
- `market_context_high->fx_1h` score `-0.1103` n `110` status `ready` deltaP `2.6946` edge `0.0028` maxDD `-0.1258`
- `market_context_high->fx_4h` score `-0.1563` n `98` status `ready` deltaP `4.7256` edge `0.0083` maxDD `-0.4545`
- `market_context_high->commodity_1h` score `-0.4365` n `110` status `ready` deltaP `-1.9352` edge `0.007` maxDD `-1.0053`
- `market_context_high->index_1h` score `-0.598` n `110` status `ready` deltaP `-0.9418` edge `-0.0052` maxDD `-1.2155`
- `market_context_high->metal_1h` score `-0.6485` n `110` status `ready` deltaP `4.491` edge `-0.0048` maxDD `-1.6682`
- `market_context_high->commodity_4h` score `-0.9327` n `98` status `ready` deltaP `-4.4674` edge `0.0331` maxDD `-1.165`
- `market_context_high->crypto_major_1h` score `-1.3341` n `110` status `ready` deltaP `2.3` edge `-0.0283` maxDD `-9.3126`
- `market_context_high->metal_4h` score `-1.9411` n `98` status `ready` deltaP `4.7473` edge `-0.0224` maxDD `-5.3474`
- `market_context_high->index_4h` score `-1.9824` n `98` status `ready` deltaP `-4.1874` edge `-0.0388` maxDD `-4.3282`
- `market_context_high->metal_24h` score `-2.3324` n `35` status `ready` deltaP `-2.6637` edge `-0.0373` maxDD `-6.1446`
- `market_context_high->equity_1h` score `-2.3788` n `110` status `ready` deltaP `1.4643` edge `-0.0874` maxDD `-12.1865`
- `market_context_high->crypto_alt_1h` score `-2.8552` n `110` status `ready` deltaP `-0.7921` edge `-0.0536` maxDD `-11.3243`
- `market_context_high->crypto_major_4h` score `-5.7639` n `98` status `ready` deltaP `-8.6797` edge `-0.1814` maxDD `-33.3092`
- `market_context_high->index_24h` score `-6.6254` n `35` status `ready` deltaP `-32.9514` edge `-0.2023` maxDD `-5.078`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
