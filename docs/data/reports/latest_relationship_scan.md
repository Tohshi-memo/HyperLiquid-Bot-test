# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-26T23:52:27.276329+00:00`
- Price records: `672`
- Market context records: `8037`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11848`

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

- `market_context_high->equity_24h` score `16.7877` n `84` status `ready` deltaP `26.7516` edge `1.3312` maxDD `-5.512`
- `market_context_high->metal_24h` score `7.9652` n `84` status `ready` deltaP `35.8752` edge `0.4246` maxDD `0.0`
- `market_context_high->equity_4h` score `6.4904` n `97` status `ready` deltaP `25.462` edge `0.4604` maxDD `-5.1426`
- `market_context_high->commodity_24h` score `3.6518` n `84` status `ready` deltaP `26.6011` edge `0.2466` maxDD `-6.2367`
- `market_context_high->metal_4h` score `2.5744` n `97` status `ready` deltaP `23.0953` edge `0.1228` maxDD `-0.979`
- `market_context_high->index_4h` score `2.5151` n `97` status `ready` deltaP `26.232` edge `0.0707` maxDD `-0.8791`
- `market_context_high->index_24h` score `1.8402` n `84` status `ready` deltaP `9.6559` edge `0.156` maxDD `-1.3621`
- `market_context_high->equity_1h` score `1.5972` n `97` status `ready` deltaP `13.1181` edge `0.1274` maxDD `-4.2072`
- `market_context_high->fx_24h` score `1.453` n `84` status `ready` deltaP `25.3446` edge `0.038` maxDD `-1.8703`
- `market_context_high->index_1h` score `0.7651` n `97` status `ready` deltaP `12.9854` edge `0.0202` maxDD `-0.7743`
- `market_context_high->metal_1h` score `0.7225` n `97` status `ready` deltaP `10.192` edge `0.0301` maxDD `-0.6936`
- `market_context_high->crypto_major_1h` score `0.4394` n `97` status `ready` deltaP `10.0762` edge `0.0302` maxDD `-1.6171`
- `market_context_high->crypto_major_4h` score `0.3751` n `97` status `ready` deltaP `8.3496` edge `0.1474` maxDD `-6.7444`
- `market_context_high->crypto_alt_4h` score `0.3683` n `97` status `ready` deltaP `4.9519` edge `0.1094` maxDD `-3.9374`
- `market_context_high->crypto_alt_1h` score `-0.1443` n `97` status `ready` deltaP `0.0833` edge `0.0242` maxDD `-1.4603`
- `market_context_high->fx_4h` score `-0.3729` n `97` status `ready` deltaP `4.5795` edge `0.0032` maxDD `-0.8511`
- `market_context_high->fx_1h` score `-0.546` n `97` status `ready` deltaP `-1.3458` edge `0.0002` maxDD `-0.2715`
- `market_context_high->commodity_1h` score `-0.6252` n `97` status `ready` deltaP `-2.0294` edge `-0.0043` maxDD `-1.9855`
- `market_context_high->commodity_4h` score `-1.1572` n `97` status `ready` deltaP `0.8282` edge `-0.0037` maxDD `-5.3478`
- `market_context_high->unknown_1h` score `-1.7829` n `97` status `ready` deltaP `7.9156` edge `-0.159` maxDD `-1.054`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
