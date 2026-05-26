# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-26T09:22:20.706707+00:00`
- Price records: `672`
- Market context records: `1932`
- Flow alert records: `7461`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `7540`

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

- `market_context_high->crypto_alt_4h` score `7.2237` n `211` status `ready` deltaP `23.0162` edge `0.563` maxDD `-5.1574`
- `market_context_high->crypto_major_4h` score `6.6403` n `211` status `ready` deltaP `27.0099` edge `0.4979` maxDD `-4.9684`
- `market_context_high->unknown_4h` score `3.3469` n `211` status `ready` deltaP `16.5002` edge `0.3713` maxDD `-9.8581`
- `market_context_high->equity_4h` score `2.0763` n `211` status `ready` deltaP `13.4818` edge `0.1926` maxDD `-5.0894`
- `market_context_high->unknown_24h` score `0.699` n `196` status `ready` deltaP `14.3389` edge `0.4947` maxDD `-35.8966`
- `market_context_high->crypto_major_1h` score `0.5939` n `223` status `ready` deltaP `7.6965` edge `0.0968` maxDD `-3.2225`
- `market_context_high->crypto_alt_1h` score `0.4659` n `223` status `ready` deltaP `7.2447` edge `0.1019` maxDD `-4.9097`
- `market_context_high->metal_24h` score `0.3138` n `196` status `ready` deltaP `12.2626` edge `0.187` maxDD `-12.7414`
- `market_context_high->index_24h` score `0.1706` n `196` status `ready` deltaP `4.2233` edge `0.1089` maxDD `-4.1604`
- `market_context_high->index_4h` score `0.1045` n `211` status `ready` deltaP `7.7115` edge `0.0662` maxDD `-3.7119`
- `market_context_high->equity_1h` score `-0.2061` n `223` status `ready` deltaP `4.5454` edge `0.0319` maxDD `-2.6836`
- `market_context_high->fx_24h` score `-0.2489` n `196` status `ready` deltaP `10.1793` edge `0.0163` maxDD `-1.3925`
- `market_context_high->fx_1h` score `-0.6409` n `223` status `ready` deltaP `-2.9155` edge `0.0005` maxDD `-0.3914`
- `market_context_high->index_1h` score `-0.6892` n `223` status `ready` deltaP `-0.0846` edge `0.0063` maxDD `-1.7205`
- `market_context_high->metal_1h` score `-0.74` n `223` status `ready` deltaP `3.811` edge `0.0133` maxDD `-6.3532`
- `market_context_high->fx_4h` score `-0.939` n `211` status `ready` deltaP `-4.5551` edge `-0.0012` maxDD `-1.1056`
- `market_context_high->equity_24h` score `-1.1408` n `196` status `ready` deltaP `7.6318` edge `0.3439` maxDD `-33.1875`
- `market_context_high->metal_4h` score `-1.1965` n `211` status `ready` deltaP `8.5322` edge `0.1126` maxDD `-12.5349`
- `market_context_high->unknown_1h` score `-1.3662` n `223` status `ready` deltaP `1.1164` edge `-0.0261` maxDD `-3.6151`
- `market_context_high->commodity_1h` score `-1.92` n `223` status `ready` deltaP `2.0166` edge `-0.0038` maxDD `-15.7972`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
