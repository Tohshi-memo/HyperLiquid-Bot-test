# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-12T14:37:46.381236+00:00`
- Price records: `672`
- Market context records: `6508`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5884`

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

- `news_risk_high->crypto_alt_24h` score `13.1754` n `32` status `ready` deltaP `35.8644` edge `0.8736` maxDD `-0.5131`
- `news_risk_high->fx_24h` score `6.502` n `32` status `ready` deltaP `53.8995` edge `0.1825` maxDD `0.0`
- `market_context_high->unknown_24h` score `6.361` n `145` status `ready` deltaP `12.152` edge `0.7791` maxDD `-15.0689`
- `news_risk_high->crypto_major_24h` score `4.9213` n `32` status `ready` deltaP `20.5643` edge `0.5718` maxDD `-4.2368`
- `news_risk_high->fx_4h` score `3.8009` n `38` status `ready` deltaP `40.3108` edge `0.0526` maxDD `-0.0345`
- `market_context_high->unknown_1h` score `2.7411` n `180` status `ready` deltaP `-5.5156` edge `0.3553` maxDD `-3.2083`
- `news_risk_high->commodity_24h` score `2.4992` n `32` status `ready` deltaP `25.2762` edge `0.0603` maxDD `-0.3101`
- `news_risk_high->fx_1h` score `1.8191` n `38` status `ready` deltaP `22.7624` edge `0.0179` maxDD `-0.1113`
- `market_context_high->commodity_24h` score `1.317` n `145` status `ready` deltaP `12.6253` edge `0.2124` maxDD `-5.2791`
- `market_context_high->index_4h` score `0.5855` n `169` status `ready` deltaP `13.2186` edge `0.0283` maxDD `-0.4108`
- `news_risk_high->crypto_major_1h` score `0.5629` n `38` status `ready` deltaP `5.0504` edge `0.0922` maxDD `-2.6299`
- `market_context_high->crypto_alt_4h` score `0.3315` n `169` status `ready` deltaP `9.5845` edge `0.1191` maxDD `-6.7632`
- `market_context_high->unknown_4h` score `0.2547` n `169` status `ready` deltaP `-17.9712` edge `0.3816` maxDD `-10.5788`
- `news_risk_high->crypto_alt_1h` score `0.0672` n `38` status `ready` deltaP `1.5837` edge `0.049` maxDD `-2.0756`
- `news_risk_high->index_24h` score `-0.3672` n `32` status `ready` deltaP `5.8167` edge `0.0013` maxDD `-2.3058`
- `market_context_high->equity_4h` score `-0.4067` n `169` status `ready` deltaP `9.0955` edge `0.0571` maxDD `-8.2573`
- `market_context_high->fx_1h` score `-0.458` n `180` status `ready` deltaP `-0.6587` edge `-0.002` maxDD `-0.8529`
- `market_context_high->crypto_alt_1h` score `-0.4971` n `180` status `ready` deltaP `6.7299` edge `0.0227` maxDD `-5.8368`
- `market_context_high->commodity_1h` score `-0.5082` n `180` status `ready` deltaP `0.9381` edge `-0.0031` maxDD `-2.1314`
- `market_context_high->crypto_major_1h` score `-0.5381` n `180` status `ready` deltaP `6.6001` edge `0.0136` maxDD `-6.7936`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
