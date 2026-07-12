# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-12T14:19:21.047809+00:00`
- Price records: `672`
- Market context records: `6506`
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

- `news_risk_high->crypto_alt_24h` score `13.1219` n `32` status `ready` deltaP `35.6911` edge `0.8703` maxDD `-0.5131`
- `news_risk_high->fx_24h` score `6.5008` n `32` status `ready` deltaP `53.8995` edge `0.1824` maxDD `0.0`
- `market_context_high->unknown_24h` score `6.3454` n `146` status `ready` deltaP `12.4071` edge `0.7761` maxDD `-15.0689`
- `news_risk_high->crypto_major_24h` score `4.8865` n `32` status `ready` deltaP `20.391` edge `0.5685` maxDD `-4.2368`
- `news_risk_high->fx_4h` score `3.8143` n `38` status `ready` deltaP `40.463` edge `0.0527` maxDD `-0.0345`
- `market_context_high->unknown_1h` score `2.7772` n `180` status `ready` deltaP `-5.1098` edge `0.3556` maxDD `-3.2083`
- `news_risk_high->commodity_24h` score `2.5262` n `32` status `ready` deltaP `25.4495` edge `0.0614` maxDD `-0.3101`
- `news_risk_high->fx_1h` score `1.8191` n `38` status `ready` deltaP `22.7624` edge `0.0179` maxDD `-0.1113`
- `market_context_high->commodity_24h` score `1.2675` n `146` status `ready` deltaP `12.3074` edge `0.2104` maxDD `-5.2791`
- `market_context_high->index_4h` score `0.5879` n `169` status `ready` deltaP `13.2186` edge `0.0285` maxDD `-0.4108`
- `news_risk_high->crypto_major_1h` score `0.5512` n `38` status `ready` deltaP `4.9007` edge `0.0917` maxDD `-2.6299`
- `market_context_high->crypto_alt_4h` score `0.3555` n `169` status `ready` deltaP `9.5845` edge `0.1211` maxDD `-6.7632`
- `market_context_high->unknown_4h` score `0.309` n `169` status `ready` deltaP `-17.5317` edge `0.3832` maxDD `-10.5788`
- `news_risk_high->crypto_alt_1h` score `0.0571` n `38` status `ready` deltaP `1.434` edge `0.0487` maxDD `-2.0756`
- `news_risk_high->index_24h` score `-0.3778` n `32` status `ready` deltaP `5.6434` edge `0.0011` maxDD `-2.3058`
- `market_context_high->equity_4h` score `-0.4083` n `169` status `ready` deltaP `9.0955` edge `0.0569` maxDD `-8.2573`
- `market_context_high->fx_1h` score `-0.458` n `180` status `ready` deltaP `-0.6587` edge `-0.002` maxDD `-0.8529`
- `market_context_high->crypto_alt_1h` score `-0.4697` n `180` status `ready` deltaP `7.1357` edge `0.0235` maxDD `-5.8368`
- `market_context_high->crypto_major_1h` score `-0.5084` n `180` status `ready` deltaP `7.006` edge `0.0147` maxDD `-6.7936`
- `market_context_high->commodity_1h` score `-0.5309` n `180` status `ready` deltaP `0.5323` edge `-0.0033` maxDD `-2.1314`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
