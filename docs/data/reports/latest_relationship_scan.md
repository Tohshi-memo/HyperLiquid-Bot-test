# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-12T12:37:24.847578+00:00`
- Price records: `672`
- Market context records: `6498`
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

- `news_risk_high->crypto_alt_24h` score `12.8455` n `32` status `ready` deltaP `34.6512` edge `0.8542` maxDD `-0.5131`
- `news_risk_high->fx_24h` score `6.4912` n `32` status `ready` deltaP `53.8995` edge `0.1816` maxDD `0.0`
- `market_context_high->unknown_24h` score `6.2756` n `153` status `ready` deltaP `14.0993` edge `0.759` maxDD `-15.0689`
- `news_risk_high->crypto_major_24h` score `4.7026` n `32` status `ready` deltaP `19.1779` edge `0.553` maxDD `-4.2368`
- `news_risk_high->fx_4h` score `3.8957` n `38` status `ready` deltaP `41.3763` edge `0.0534` maxDD `-0.0345`
- `market_context_high->unknown_1h` score `2.8469` n `180` status `ready` deltaP `-4.2981` edge `0.356` maxDD `-3.2083`
- `news_risk_high->commodity_24h` score `2.7121` n `32` status `ready` deltaP `26.6627` edge `0.0688` maxDD `-0.3101`
- `news_risk_high->fx_1h` score `1.8311` n `38` status `ready` deltaP `22.9121` edge `0.0179` maxDD `-0.1113`
- `market_context_high->commodity_24h` score `0.9443` n `153` status `ready` deltaP `10.2616` edge `0.1971` maxDD `-5.2791`
- `market_context_high->index_4h` score `0.7041` n `169` status `ready` deltaP `14.5371` edge `0.0294` maxDD `-0.4108`
- `market_context_high->crypto_alt_4h` score `0.6593` n `169` status `ready` deltaP `11.3426` edge `0.1347` maxDD `-6.7632`
- `market_context_high->unknown_4h` score `0.6172` n `169` status `ready` deltaP `-14.8946` edge `0.3913` maxDD `-10.5788`
- `news_risk_high->crypto_major_1h` score `0.5457` n `38` status `ready` deltaP `4.9007` edge `0.091` maxDD `-2.6299`
- `news_risk_high->crypto_alt_1h` score `0.0516` n `38` status `ready` deltaP `1.434` edge `0.048` maxDD `-2.0756`
- `news_risk_high->index_24h` score `-0.4142` n `32` status `ready` deltaP `5.1235` edge `-0.0001` maxDD `-2.3058`
- `market_context_high->equity_4h` score `-0.4319` n `169` status `ready` deltaP `8.656` edge `0.0568` maxDD `-8.2573`
- `market_context_high->metal_4h` score `-0.4519` n `169` status `ready` deltaP `8.0489` edge `0.0425` maxDD `-2.7056`
- `market_context_high->fx_1h` score `-0.4802` n `180` status `ready` deltaP `-1.0646` edge `-0.0021` maxDD `-0.8555`
- `market_context_high->crypto_major_1h` score `-0.4928` n `180` status `ready` deltaP `7.006` edge `0.0167` maxDD `-6.7936`
- `market_context_high->commodity_1h` score `-0.5746` n `180` status `ready` deltaP `-0.2794` edge `-0.0035` maxDD `-2.1314`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
