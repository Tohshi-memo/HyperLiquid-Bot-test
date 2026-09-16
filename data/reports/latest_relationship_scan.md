# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-16T18:22:32.395877+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `11713`

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

- `news_risk_high->unknown_4h` score `366.0802` n `83` status `ready` deltaP `-21.0531` edge `30.7365` maxDD `-4.1571`
- `news_risk_high->crypto_alt_24h` score `19.6049` n `82` status `ready` deltaP `43.5171` edge `1.4766` maxDD `-8.9708`
- `news_risk_high->crypto_major_24h` score `17.9343` n `82` status `ready` deltaP `35.8529` edge `1.455` maxDD `-13.2931`
- `news_risk_high->equity_24h` score `13.9815` n `82` status `ready` deltaP `45.2151` edge `1.0411` maxDD `-6.5262`
- `news_risk_high->index_24h` score `7.2383` n `82` status `ready` deltaP `50.4743` edge `0.2843` maxDD `-0.075`
- `risk_on_high->commodity_24h` score `5.9998` n `52` status `ready` deltaP `37.1528` edge `0.2523` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `5.9998` n `52` status `ready` deltaP `37.1528` edge `0.2523` maxDD `0.0`
- `news_risk_high->metal_24h` score `5.6335` n `82` status `ready` deltaP `33.5959` edge `0.2909` maxDD `-0.6334`
- `market_context_high->commodity_24h` score `4.7007` n `149` status `ready` deltaP `30.4414` edge `0.2413` maxDD `-0.8682`
- `risk_on_high->fx_24h` score `2.406` n `52` status `ready` deltaP `32.1047` edge `-0.0093` maxDD `-0.0054`
- `risk_on_and_context->fx_24h` score `2.406` n `52` status `ready` deltaP `32.1047` edge `-0.0093` maxDD `-0.0054`
- `risk_on_high->commodity_4h` score `2.3194` n `52` status `ready` deltaP `29.0338` edge `0.0347` maxDD `-0.1313`
- `risk_on_and_context->commodity_4h` score `2.3194` n `52` status `ready` deltaP `29.0338` edge `0.0347` maxDD `-0.1313`
- `market_context_high->fx_24h` score `2.2711` n `149` status `ready` deltaP `29.3298` edge `0.0153` maxDD `-0.0593`
- `market_context_high->commodity_4h` score `2.2191` n `149` status `ready` deltaP `25.5361` edge `0.0565` maxDD `-0.345`
- `market_context_high->commodity_1h` score `0.9144` n `149` status `ready` deltaP `14.2648` edge `0.0188` maxDD `-0.3491`
- `news_risk_high->index_4h` score `0.3653` n `83` status `ready` deltaP `12.0408` edge `0.0294` maxDD `-0.6935`
- `risk_on_high->crypto_alt_4h` score `0.3552` n `52` status `ready` deltaP `9.5451` edge `0.1434` maxDD `-6.2526`
- `risk_on_and_context->crypto_alt_4h` score `0.3552` n `52` status `ready` deltaP `9.5451` edge `0.1434` maxDD `-6.2526`
- `risk_on_high->commodity_1h` score `0.2911` n `52` status `ready` deltaP `7.3469` edge `0.0105` maxDD `-0.1507`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
