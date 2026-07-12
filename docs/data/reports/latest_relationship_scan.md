# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-12T13:37:27.760693+00:00`
- Price records: `672`
- Market context records: `6503`
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

- `news_risk_high->crypto_alt_24h` score `12.9759` n `32` status `ready` deltaP `35.1711` edge `0.8616` maxDD `-0.5131`
- `news_risk_high->fx_24h` score `6.4972` n `32` status `ready` deltaP `53.8995` edge `0.1821` maxDD `0.0`
- `market_context_high->unknown_24h` score `6.3066` n `149` status `ready` deltaP `13.1518` edge `0.7679` maxDD `-15.0689`
- `news_risk_high->crypto_major_24h` score `4.7971` n `32` status `ready` deltaP `19.8711` edge `0.5605` maxDD `-4.2368`
- `news_risk_high->fx_4h` score `3.8556` n `38` status `ready` deltaP `40.9197` edge `0.0531` maxDD `-0.0345`
- `market_context_high->unknown_1h` score `2.7808` n `180` status `ready` deltaP `-5.1098` edge `0.3559` maxDD `-3.2083`
- `news_risk_high->commodity_24h` score `2.6098` n `32` status `ready` deltaP `25.9695` edge `0.0649` maxDD `-0.3101`
- `news_risk_high->fx_1h` score `1.8311` n `38` status `ready` deltaP `22.9121` edge `0.0179` maxDD `-0.1113`
- `market_context_high->commodity_24h` score `1.1176` n `149` status `ready` deltaP `11.3932` edge `0.204` maxDD `-5.2791`
- `market_context_high->index_4h` score `0.5927` n `169` status `ready` deltaP `13.2186` edge `0.0289` maxDD `-0.4108`
- `market_context_high->crypto_alt_4h` score `0.557` n `169` status `ready` deltaP `10.9031` edge `0.1291` maxDD `-6.7632`
- `news_risk_high->crypto_major_1h` score `0.5379` n `38` status `ready` deltaP `4.751` edge `0.091` maxDD `-2.6299`
- `market_context_high->unknown_4h` score `0.4649` n `169` status `ready` deltaP `-16.2132` edge `0.3874` maxDD `-10.5788`
- `news_risk_high->crypto_alt_1h` score `0.0539` n `38` status `ready` deltaP `1.434` edge `0.0483` maxDD `-2.0756`
- `news_risk_high->index_24h` score `-0.3907` n `32` status `ready` deltaP `5.4701` edge `0.0006` maxDD `-2.3058`
- `market_context_high->equity_4h` score `-0.4366` n `169` status `ready` deltaP `8.656` edge `0.0562` maxDD `-8.2573`
- `market_context_high->crypto_alt_1h` score `-0.4619` n `180` status `ready` deltaP `7.1357` edge `0.0245` maxDD `-5.8368`
- `market_context_high->crypto_major_1h` score `-0.4717` n `180` status `ready` deltaP `7.4119` edge `0.0167` maxDD `-6.7936`
- `market_context_high->fx_1h` score `-0.4799` n `180` status `ready` deltaP `-1.0646` edge `-0.0021` maxDD `-0.8529`
- `market_context_high->metal_4h` score `-0.5282` n `169` status `ready` deltaP `7.1699` edge `0.042` maxDD `-2.7056`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
