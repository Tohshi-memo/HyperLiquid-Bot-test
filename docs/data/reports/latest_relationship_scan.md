# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-12T13:52:26.481148+00:00`
- Price records: `672`
- Market context records: `6504`
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

- `news_risk_high->crypto_alt_24h` score `13.0222` n `32` status `ready` deltaP `35.3445` edge `0.8643` maxDD `-0.5131`
- `news_risk_high->fx_24h` score `6.4984` n `32` status `ready` deltaP `53.8995` edge `0.1822` maxDD `0.0`
- `market_context_high->unknown_24h` score `6.311` n `148` status `ready` deltaP `12.9069` edge `0.7699` maxDD `-15.0689`
- `news_risk_high->crypto_major_24h` score `4.8264` n `32` status `ready` deltaP `20.0444` edge `0.5631` maxDD `-4.2368`
- `news_risk_high->fx_4h` score `3.8422` n `38` status `ready` deltaP `40.7675` edge `0.053` maxDD `-0.0345`
- `market_context_high->unknown_1h` score `2.7447` n `180` status `ready` deltaP `-5.5156` edge `0.3556` maxDD `-3.2083`
- `news_risk_high->commodity_24h` score `2.5816` n `32` status `ready` deltaP `25.7961` edge `0.0637` maxDD `-0.3101`
- `news_risk_high->fx_1h` score `1.8191` n `38` status `ready` deltaP `22.7624` edge `0.0179` maxDD `-0.1113`
- `market_context_high->commodity_24h` score `1.1666` n `148` status `ready` deltaP `11.6914` edge `0.2061` maxDD `-5.2791`
- `market_context_high->index_4h` score `0.5915` n `169` status `ready` deltaP `13.2186` edge `0.0288` maxDD `-0.4108`
- `news_risk_high->crypto_major_1h` score `0.5395` n `38` status `ready` deltaP `4.751` edge `0.0912` maxDD `-2.6299`
- `market_context_high->crypto_alt_4h` score `0.5026` n `169` status `ready` deltaP `10.4635` edge `0.1275` maxDD `-6.7632`
- `market_context_high->unknown_4h` score `0.4166` n `169` status `ready` deltaP `-16.6527` edge `0.3863` maxDD `-10.5788`
- `news_risk_high->crypto_alt_1h` score `0.0539` n `38` status `ready` deltaP `1.434` edge `0.0483` maxDD `-2.0756`
- `news_risk_high->index_24h` score `-0.3801` n `32` status `ready` deltaP `5.6434` edge `0.0008` maxDD `-2.3058`
- `market_context_high->equity_4h` score `-0.4351` n `169` status `ready` deltaP `8.656` edge `0.0564` maxDD `-8.2573`
- `market_context_high->fx_1h` score `-0.4588` n `180` status `ready` deltaP `-0.6587` edge `-0.0021` maxDD `-0.8529`
- `market_context_high->crypto_alt_1h` score `-0.4619` n `180` status `ready` deltaP `7.1357` edge `0.0245` maxDD `-5.8368`
- `market_context_high->crypto_major_1h` score `-0.4764` n `180` status `ready` deltaP `7.4119` edge `0.0161` maxDD `-6.7936`
- `market_context_high->crypto_major_4h` score `-0.5491` n `169` status `ready` deltaP `11.2588` edge `0.0836` maxDD `-12.6576`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
