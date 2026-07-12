# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-12T14:07:29.031012+00:00`
- Price records: `672`
- Market context records: `6505`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5866`

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

- `news_risk_high->crypto_alt_24h` score `13.0721` n `32` status `ready` deltaP `35.5178` edge `0.8673` maxDD `-0.5131`
- `news_risk_high->fx_24h` score `6.4996` n `32` status `ready` deltaP `53.8995` edge `0.1823` maxDD `0.0`
- `market_context_high->unknown_24h` score `6.3272` n `147` status `ready` deltaP `12.6587` edge `0.7729` maxDD `-15.0689`
- `news_risk_high->crypto_major_24h` score `4.8557` n `32` status `ready` deltaP `20.2177` edge `0.5657` maxDD `-4.2368`
- `news_risk_high->fx_4h` score `3.8288` n `38` status `ready` deltaP `40.6153` edge `0.0529` maxDD `-0.0345`
- `market_context_high->unknown_1h` score `2.7772` n `180` status `ready` deltaP `-5.1098` edge `0.3556` maxDD `-3.2083`
- `news_risk_high->commodity_24h` score `2.5545` n `32` status `ready` deltaP `25.6228` edge `0.0626` maxDD `-0.3101`
- `news_risk_high->fx_1h` score `1.8191` n `38` status `ready` deltaP `22.7624` edge `0.0179` maxDD `-0.1113`
- `market_context_high->commodity_24h` score `1.2186` n `147` status `ready` deltaP `11.9961` edge `0.2084` maxDD `-5.2791`
- `market_context_high->index_4h` score `0.5903` n `169` status `ready` deltaP `13.2186` edge `0.0287` maxDD `-0.4108`
- `news_risk_high->crypto_major_1h` score `0.5496` n `38` status `ready` deltaP `4.9007` edge `0.0915` maxDD `-2.6299`
- `market_context_high->crypto_alt_4h` score `0.441` n `169` status `ready` deltaP `10.024` edge `0.1253` maxDD `-6.7632`
- `market_context_high->unknown_4h` score `0.367` n `169` status `ready` deltaP `-17.0922` edge `0.3851` maxDD `-10.5788`
- `news_risk_high->crypto_alt_1h` score `0.0563` n `38` status `ready` deltaP `1.434` edge `0.0486` maxDD `-2.0756`
- `news_risk_high->index_24h` score `-0.3786` n `32` status `ready` deltaP `5.6434` edge `0.001` maxDD `-2.3058`
- `market_context_high->equity_4h` score `-0.4091` n `169` status `ready` deltaP `9.0955` edge `0.0568` maxDD `-8.2573`
- `market_context_high->fx_1h` score `-0.458` n `180` status `ready` deltaP `-0.6587` edge `-0.002` maxDD `-0.8529`
- `market_context_high->crypto_alt_1h` score `-0.4658` n `180` status `ready` deltaP `7.1357` edge `0.024` maxDD `-5.8368`
- `market_context_high->crypto_major_1h` score `-0.5045` n `180` status `ready` deltaP `7.006` edge `0.0152` maxDD `-6.7936`
- `market_context_high->commodity_1h` score `-0.5528` n `180` status `ready` deltaP `0.1264` edge `-0.0034` maxDD `-2.1314`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
