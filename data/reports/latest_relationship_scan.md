# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-12T12:52:26.292210+00:00`
- Price records: `672`
- Market context records: `6500`
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

- `news_risk_high->crypto_alt_24h` score `12.8575` n `32` status `ready` deltaP `34.6512` edge `0.8552` maxDD `-0.5131`
- `news_risk_high->fx_24h` score `6.4924` n `32` status `ready` deltaP `53.8995` edge `0.1817` maxDD `0.0`
- `market_context_high->unknown_24h` score `6.2894` n `152` status `ready` deltaP `13.8671` edge `0.7617` maxDD `-15.0689`
- `news_risk_high->crypto_major_24h` score `4.7225` n `32` status `ready` deltaP `19.3512` edge `0.5544` maxDD `-4.2368`
- `news_risk_high->fx_4h` score `3.8945` n `38` status `ready` deltaP `41.3763` edge `0.0533` maxDD `-0.0345`
- `market_context_high->unknown_1h` score `2.8517` n `180` status `ready` deltaP `-4.2981` edge `0.3564` maxDD `-3.2083`
- `news_risk_high->commodity_24h` score `2.6862` n `32` status `ready` deltaP `26.4894` edge `0.0678` maxDD `-0.3101`
- `news_risk_high->fx_1h` score `1.843` n `38` status `ready` deltaP `23.0618` edge `0.0179` maxDD `-0.1113`
- `market_context_high->commodity_24h` score `0.9878` n `152` status `ready` deltaP `10.5355` edge `0.1989` maxDD `-5.2791`
- `market_context_high->index_4h` score `0.6654` n `169` status `ready` deltaP `14.0976` edge `0.0291` maxDD `-0.4108`
- `market_context_high->crypto_alt_4h` score `0.6182` n `169` status `ready` deltaP `10.9031` edge `0.1342` maxDD `-6.7632`
- `market_context_high->unknown_4h` score `0.616` n `169` status `ready` deltaP `-14.8946` edge `0.3912` maxDD `-10.5788`
- `news_risk_high->crypto_major_1h` score `0.5372` n `38` status `ready` deltaP `4.751` edge `0.0909` maxDD `-2.6299`
- `news_risk_high->crypto_alt_1h` score `0.0493` n `38` status `ready` deltaP `1.434` edge `0.0477` maxDD `-2.0756`
- `news_risk_high->index_24h` score `-0.4036` n `32` status `ready` deltaP `5.2968` edge `0.0001` maxDD `-2.3058`
- `market_context_high->equity_4h` score `-0.4351` n `169` status `ready` deltaP `8.656` edge `0.0564` maxDD `-8.2573`
- `market_context_high->crypto_major_1h` score `-0.4694` n `180` status `ready` deltaP `7.4119` edge `0.017` maxDD `-6.7936`
- `market_context_high->metal_4h` score `-0.4895` n `169` status `ready` deltaP `7.6094` edge `0.0423` maxDD `-2.7056`
- `market_context_high->fx_1h` score `-0.5013` n `180` status `ready` deltaP `-1.4704` edge `-0.0021` maxDD `-0.8555`
- `market_context_high->commodity_1h` score `-0.577` n `180` status `ready` deltaP `-0.2794` edge `-0.0038` maxDD `-2.1314`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
