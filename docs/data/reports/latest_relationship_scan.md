# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-12T11:48:13.434505+00:00`
- Price records: `672`
- Market context records: `6494`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5861`

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

- `news_risk_high->crypto_alt_24h` score `12.8215` n `32` status `ready` deltaP `34.6512` edge `0.8522` maxDD `-0.5131`
- `news_risk_high->fx_24h` score `6.4864` n `32` status `ready` deltaP `53.8995` edge `0.1812` maxDD `0.0`
- `market_context_high->unknown_24h` score `6.2267` n `156` status `ready` deltaP `14.778` edge `0.7504` maxDD `-15.0689`
- `news_risk_high->crypto_major_24h` score `4.6373` n `32` status `ready` deltaP `18.6579` edge `0.5481` maxDD `-4.2368`
- `news_risk_high->fx_4h` score `3.9347` n `38` status `ready` deltaP `41.8329` edge `0.0536` maxDD `-0.0345`
- `market_context_high->unknown_1h` score `2.8433` n `180` status `ready` deltaP `-4.2981` edge `0.3557` maxDD `-3.2083`
- `news_risk_high->commodity_24h` score `2.7885` n `32` status `ready` deltaP `27.1826` edge `0.0717` maxDD `-0.3101`
- `news_risk_high->fx_1h` score `1.843` n `38` status `ready` deltaP `23.0618` edge `0.0179` maxDD `-0.1113`
- `market_context_high->commodity_24h` score `0.8153` n `156` status `ready` deltaP `9.4743` edge `0.1916` maxDD `-5.2791`
- `market_context_high->index_4h` score `0.7041` n `169` status `ready` deltaP `14.5371` edge `0.0294` maxDD `-0.4108`
- `market_context_high->crypto_alt_4h` score `0.6266` n `169` status `ready` deltaP `10.9031` edge `0.1349` maxDD `-6.7632`
- `market_context_high->unknown_4h` score `0.6256` n `169` status `ready` deltaP `-14.8946` edge `0.392` maxDD `-10.5788`
- `news_risk_high->crypto_major_1h` score `0.5917` n `38` status `ready` deltaP `5.3498` edge `0.0939` maxDD `-2.6299`
- `news_risk_high->crypto_alt_1h` score `0.103` n `38` status `ready` deltaP `1.8831` edge `0.0516` maxDD `-2.0756`
- `market_context_high->metal_4h` score `-0.3404` n `169` status `ready` deltaP `9.3675` edge `0.043` maxDD `-2.7056`
- `news_risk_high->index_24h` score `-0.4181` n `32` status `ready` deltaP `5.1235` edge `-0.0006` maxDD `-2.3058`
- `market_context_high->equity_4h` score `-0.4358` n `169` status `ready` deltaP `8.656` edge `0.0563` maxDD `-8.2573`
- `market_context_high->fx_1h` score `-0.5013` n `180` status `ready` deltaP `-1.4704` edge `-0.0021` maxDD `-0.8555`
- `market_context_high->commodity_1h` score `-0.5684` n `180` status `ready` deltaP `-0.2794` edge `-0.0027` maxDD `-2.1314`
- `market_context_high->crypto_alt_1h` score `-0.5939` n `180` status `ready` deltaP `5.9182` edge `0.0157` maxDD `-5.8368`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
