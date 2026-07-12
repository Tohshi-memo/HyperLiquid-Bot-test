# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-12T13:22:24.392460+00:00`
- Price records: `672`
- Market context records: `6502`
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

- `news_risk_high->crypto_alt_24h` score `12.9369` n `32` status `ready` deltaP `34.9978` edge `0.8595` maxDD `-0.5131`
- `news_risk_high->fx_24h` score `6.4948` n `32` status `ready` deltaP `53.8995` edge `0.1819` maxDD `0.0`
- `market_context_high->unknown_24h` score `6.3007` n `150` status `ready` deltaP `13.3934` edge `0.7658` maxDD `-15.0689`
- `news_risk_high->crypto_major_24h` score `4.7717` n `32` status `ready` deltaP `19.6978` edge `0.5584` maxDD `-4.2368`
- `news_risk_high->fx_4h` score `3.869` n `38` status `ready` deltaP `41.0719` edge `0.0532` maxDD `-0.0345`
- `market_context_high->unknown_1h` score `2.8168` n `180` status `ready` deltaP `-4.7039` edge `0.3562` maxDD `-3.2083`
- `news_risk_high->commodity_24h` score `2.6357` n `32` status `ready` deltaP `26.1428` edge `0.0659` maxDD `-0.3101`
- `news_risk_high->fx_1h` score `1.843` n `38` status `ready` deltaP `23.0618` edge `0.0179` maxDD `-0.1113`
- `market_context_high->commodity_24h` score `1.0726` n `150` status `ready` deltaP `11.1011` edge `0.2022` maxDD `-5.2791`
- `market_context_high->index_4h` score `0.5915` n `169` status `ready` deltaP `13.2186` edge `0.0288` maxDD `-0.4108`
- `market_context_high->crypto_alt_4h` score `0.5678` n `169` status `ready` deltaP `10.9031` edge `0.13` maxDD `-6.7632`
- `news_risk_high->crypto_major_1h` score `0.5395` n `38` status `ready` deltaP `4.751` edge `0.0912` maxDD `-2.6299`
- `market_context_high->unknown_4h` score `0.5181` n `169` status `ready` deltaP `-15.7737` edge `0.3889` maxDD `-10.5788`
- `news_risk_high->crypto_alt_1h` score `0.0633` n `38` status `ready` deltaP `1.5837` edge `0.0485` maxDD `-2.0756`
- `news_risk_high->index_24h` score `-0.3915` n `32` status `ready` deltaP `5.4701` edge `0.0005` maxDD `-2.3058`
- `market_context_high->equity_4h` score `-0.4382` n `169` status `ready` deltaP `8.656` edge `0.056` maxDD `-8.2573`
- `market_context_high->crypto_major_1h` score `-0.4764` n `180` status `ready` deltaP `7.4119` edge `0.0161` maxDD `-6.7936`
- `market_context_high->crypto_alt_1h` score `-0.4854` n `180` status `ready` deltaP `6.7299` edge `0.0242` maxDD `-5.8368`
- `market_context_high->metal_4h` score `-0.4919` n `169` status `ready` deltaP `7.6094` edge `0.0421` maxDD `-2.7056`
- `market_context_high->fx_1h` score `-0.501` n `180` status `ready` deltaP `-1.4704` edge `-0.0021` maxDD `-0.8529`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
