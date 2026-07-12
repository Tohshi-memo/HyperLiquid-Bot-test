# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-12T13:07:53.886588+00:00`
- Price records: `672`
- Market context records: `6501`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5862`

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

- `news_risk_high->crypto_alt_24h` score `12.8942` n `32` status `ready` deltaP `34.8245` edge `0.8571` maxDD `-0.5131`
- `news_risk_high->fx_24h` score `6.4936` n `32` status `ready` deltaP `53.8995` edge `0.1818` maxDD `0.0`
- `market_context_high->unknown_24h` score `6.3006` n `151` status `ready` deltaP `13.6318` edge `0.7642` maxDD `-15.0689`
- `news_risk_high->crypto_major_24h` score `4.7463` n `32` status `ready` deltaP `19.5245` edge `0.5563` maxDD `-4.2368`
- `news_risk_high->fx_4h` score `3.8824` n `38` status `ready` deltaP `41.2241` edge `0.0533` maxDD `-0.0345`
- `market_context_high->unknown_1h` score `2.8517` n `180` status `ready` deltaP `-4.2981` edge `0.3564` maxDD `-3.2083`
- `news_risk_high->commodity_24h` score `2.6604` n `32` status `ready` deltaP `26.3161` edge `0.0668` maxDD `-0.3101`
- `news_risk_high->fx_1h` score `1.843` n `38` status `ready` deltaP `23.0618` edge `0.0179` maxDD `-0.1113`
- `market_context_high->commodity_24h` score `1.0306` n `151` status `ready` deltaP `10.8153` edge `0.2006` maxDD `-5.2791`
- `market_context_high->index_4h` score `0.6278` n `169` status `ready` deltaP `13.6581` edge `0.0289` maxDD `-0.4108`
- `market_context_high->crypto_alt_4h` score `0.5822` n `169` status `ready` deltaP `10.9031` edge `0.1312` maxDD `-6.7632`
- `market_context_high->unknown_4h` score `0.5641` n `169` status `ready` deltaP `-15.3341` edge `0.3898` maxDD `-10.5788`
- `news_risk_high->crypto_major_1h` score `0.5387` n `38` status `ready` deltaP `4.751` edge `0.0911` maxDD `-2.6299`
- `news_risk_high->crypto_alt_1h` score `0.0516` n `38` status `ready` deltaP `1.434` edge `0.048` maxDD `-2.0756`
- `news_risk_high->index_24h` score `-0.393` n `32` status `ready` deltaP `5.4701` edge `0.0003` maxDD `-2.3058`
- `market_context_high->equity_4h` score `-0.4382` n `169` status `ready` deltaP `8.656` edge `0.056` maxDD `-8.2573`
- `market_context_high->crypto_alt_1h` score `-0.4549` n `180` status `ready` deltaP `7.1357` edge `0.0254` maxDD `-5.8368`
- `market_context_high->crypto_major_1h` score `-0.4725` n `180` status `ready` deltaP `7.4119` edge `0.0166` maxDD `-6.7936`
- `market_context_high->metal_4h` score `-0.4907` n `169` status `ready` deltaP `7.6094` edge `0.0422` maxDD `-2.7056`
- `market_context_high->fx_1h` score `-0.501` n `180` status `ready` deltaP `-1.4704` edge `-0.0021` maxDD `-0.8529`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
