# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-12T09:37:29.343090+00:00`
- Price records: `672`
- Market context records: `6485`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5869`

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

- `news_risk_high->crypto_alt_24h` score `12.6571` n `32` status `ready` deltaP `34.2014` edge `0.8415` maxDD `-0.5131`
- `market_context_high->unknown_24h` score `6.5603` n `159` status `ready` deltaP `16.4275` edge `0.7672` maxDD `-15.0689`
- `news_risk_high->fx_24h` score `6.468` n `32` status `ready` deltaP `53.8194` edge `0.1802` maxDD `0.0`
- `news_risk_high->crypto_major_24h` score `4.3978` n `32` status `ready` deltaP `17.1875` edge `0.5272` maxDD `-4.2368`
- `news_risk_high->fx_4h` score `3.9788` n `38` status `ready` deltaP `42.37` edge `0.0537` maxDD `-0.0345`
- `news_risk_high->commodity_24h` score `3.0315` n `32` status `ready` deltaP `28.6458` edge `0.0822` maxDD `-0.3101`
- `market_context_high->unknown_1h` score `2.8338` n `180` status `ready` deltaP `-3.8922` edge `0.3522` maxDD `-3.2083`
- `news_risk_high->fx_1h` score `1.855` n `38` status `ready` deltaP `23.2115` edge `0.0179` maxDD `-0.1113`
- `news_risk_high->crypto_major_1h` score `0.5761` n `38` status `ready` deltaP `5.0504` edge `0.0939` maxDD `-2.6299`
- `market_context_high->index_4h` score `0.516` n `170` status `ready` deltaP `12.2902` edge `0.0287` maxDD `-0.4108`
- `market_context_high->commodity_24h` score `0.3461` n `159` status `ready` deltaP `6.535` edge `0.1721` maxDD `-5.2791`
- `market_context_high->crypto_alt_4h` score `0.3073` n `170` status `ready` deltaP `8.8468` edge `0.122` maxDD `-6.7632`
- `market_context_high->unknown_4h` score `0.2379` n `170` status `ready` deltaP `-15.7514` edge `0.3654` maxDD `-10.5788`
- `market_context_high->metal_4h` score `0.1865` n `170` status `ready` deltaP `12.0247` edge `0.0442` maxDD `-2.7056`
- `news_risk_high->crypto_alt_1h` score `0.0781` n `38` status `ready` deltaP `1.5837` edge `0.0504` maxDD `-2.0756`
- `market_context_high->equity_4h` score `-0.431` n `170` status `ready` deltaP `8.8235` edge `0.0558` maxDD `-8.2573`
- `news_risk_high->index_24h` score `-0.4548` n `32` status `ready` deltaP `4.6875` edge `-0.0024` maxDD `-2.3058`
- `market_context_high->crypto_alt_1h` score `-0.5252` n `180` status `ready` deltaP `6.7299` edge `0.0191` maxDD `-5.8368`
- `market_context_high->metal_1h` score `-0.553` n `180` status `ready` deltaP `0.835` edge `0.0013` maxDD `-1.8877`
- `market_context_high->index_1h` score `-0.5574` n `180` status `ready` deltaP `-0.5556` edge `0.0042` maxDD `-0.7564`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
