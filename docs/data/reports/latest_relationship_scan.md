# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-12T16:37:23.649683+00:00`
- Price records: `672`
- Market context records: `6518`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `64`

- Symbol pattern count: `7848`

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

- `news_risk_high->crypto_alt_24h` score `13.2367` n `32` status `ready` deltaP `36.211` edge `0.8764` maxDD `-0.5131`
- `market_context_high->unknown_24h` score `6.5312` n `139` status `ready` deltaP `10.5445` edge `0.804` maxDD `-15.0689`
- `news_risk_high->fx_24h` score `6.5152` n `32` status `ready` deltaP `53.8995` edge `0.1836` maxDD `0.0`
- `news_risk_high->crypto_major_24h` score `4.93` n `32` status `ready` deltaP `20.911` edge `0.5706` maxDD `-4.2368`
- `news_risk_high->fx_4h` score `3.7255` n `38` status `ready` deltaP `39.4737` edge `0.0519` maxDD `-0.0345`
- `market_context_high->unknown_1h` score `2.7411` n `180` status `ready` deltaP `-5.3659` edge `0.3543` maxDD `-3.2083`
- `news_risk_high->commodity_24h` score `2.2875` n `32` status `ready` deltaP `23.8897` edge `0.0519` maxDD `-0.3101`
- `news_risk_high->fx_1h` score `1.8167` n `38` status `ready` deltaP `22.7624` edge `0.0177` maxDD `-0.1113`
- `market_context_high->commodity_24h` score `1.6937` n `139` status `ready` deltaP `15.0543` edge `0.2276` maxDD `-5.2791`
- `market_context_high->index_4h` score `0.5956` n `169` status `ready` deltaP `13.2857` edge `0.0287` maxDD `-0.4108`
- `news_risk_high->crypto_major_1h` score `0.5559` n `38` status `ready` deltaP `4.9007` edge `0.0923` maxDD `-2.6299`
- `market_context_high->crypto_alt_4h` score `0.3131` n `169` status `ready` deltaP `9.6551` edge `0.1171` maxDD `-6.7632`
- `news_risk_high->crypto_alt_1h` score `0.0758` n `38` status `ready` deltaP `1.5837` edge `0.0501` maxDD `-2.0756`
- `market_context_high->unknown_4h` score `0.0023` n `169` status `ready` deltaP `-20.0913` edge `0.3747` maxDD `-10.5788`
- `market_context_high->equity_4h` score `-0.3328` n `169` status `ready` deltaP `10.3369` edge `0.0583` maxDD `-8.2573`
- `news_risk_high->index_24h` score `-0.3398` n `32` status `ready` deltaP `6.1633` edge `0.0025` maxDD `-2.3058`
- `market_context_high->fx_1h` score `-0.4416` n `180` status `ready` deltaP `-0.6587` edge `-0.0015` maxDD `-0.7249`
- `market_context_high->crypto_major_1h` score `-0.5185` n `180` status `ready` deltaP `7.006` edge `0.0134` maxDD `-6.7936`
- `market_context_high->crypto_alt_1h` score `-0.5189` n `180` status `ready` deltaP `6.7299` edge `0.0199` maxDD `-5.8368`
- `market_context_high->commodity_1h` score `-0.5293` n `180` status `ready` deltaP `0.5323` edge `-0.0031` maxDD `-2.1314`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
