# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-26T16:37:18.716002+00:00`
- Price records: `672`
- Market context records: `1955`
- Flow alert records: `7525`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `7565`

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

- `market_context_high->crypto_alt_4h` score `7.0152` n `232` status `ready` deltaP `21.7147` edge `0.5543` maxDD `-5.1574`
- `market_context_high->crypto_major_4h` score `6.4747` n `232` status `ready` deltaP `25.389` edge `0.4949` maxDD `-4.9684`
- `market_context_high->unknown_4h` score `2.3633` n `232` status `ready` deltaP `13.3253` edge `0.3105` maxDD `-9.8581`
- `market_context_high->equity_4h` score `2.1416` n `232` status `ready` deltaP `14.2977` edge `0.1926` maxDD `-5.0894`
- `market_context_high->unknown_24h` score `1.1247` n `199` status `ready` deltaP `16.4203` edge `0.5163` maxDD `-35.8966`
- `market_context_high->crypto_major_1h` score `0.8026` n `234` status `ready` deltaP `8.2041` edge `0.1108` maxDD `-3.2225`
- `market_context_high->crypto_alt_1h` score `0.642` n `234` status `ready` deltaP `7.6463` edge `0.1139` maxDD `-4.9097`
- `market_context_high->metal_24h` score `0.39` n `199` status `ready` deltaP `12.3296` edge `0.1929` maxDD `-12.7414`
- `market_context_high->index_4h` score `0.1696` n `232` status `ready` deltaP `8.4946` edge `0.0664` maxDD `-3.7119`
- `market_context_high->index_24h` score `0.1513` n `199` status `ready` deltaP `4.1922` edge `0.1075` maxDD `-4.1604`
- `market_context_high->equity_24h` score `-0.1327` n `199` status `ready` deltaP `11.008` edge `0.4054` maxDD `-33.1875`
- `market_context_high->equity_1h` score `-0.2482` n `234` status `ready` deltaP `4.6497` edge `0.0277` maxDD `-2.6836`
- `market_context_high->fx_24h` score `-0.2579` n `199` status `ready` deltaP `9.9323` edge `0.0172` maxDD `-1.3925`
- `market_context_high->fx_1h` score `-0.6428` n `234` status `ready` deltaP `-2.8635` edge `-0.0001` maxDD `-0.3914`
- `market_context_high->index_1h` score `-0.6617` n `234` status `ready` deltaP `0.485` edge `0.0048` maxDD `-1.7205`
- `market_context_high->fx_4h` score `-1.08` n `232` status `ready` deltaP `-6.9806` edge `-0.0031` maxDD `-1.1056`
- `market_context_high->metal_1h` score `-1.264` n `234` status `ready` deltaP `3.3971` edge `0.0056` maxDD `-6.3532`
- `market_context_high->crypto_major_24h` score `-1.5698` n `199` status `ready` deltaP `15.5495` edge `0.6241` maxDD `-62.3533`
- `market_context_high->unknown_1h` score `-1.5923` n `234` status `ready` deltaP `0.2099` edge `-0.0389` maxDD `-3.6151`
- `market_context_high->metal_4h` score `-1.8381` n `232` status `ready` deltaP `6.7967` edge `0.0707` maxDD `-12.5349`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
