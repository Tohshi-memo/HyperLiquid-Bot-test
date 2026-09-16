# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-16T22:07:34.306444+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `11343`

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

- `news_risk_high->unknown_4h` score `372.0814` n `83` status `ready` deltaP `-21.0531` edge `31.2366` maxDD `-4.1571`
- `news_risk_high->crypto_alt_24h` score `18.1836` n `83` status `ready` deltaP `41.4763` edge `1.3767` maxDD `-9.3661`
- `news_risk_high->crypto_major_24h` score `16.6756` n `83` status `ready` deltaP `33.8897` edge `1.3632` maxDD `-13.2931`
- `news_risk_high->equity_24h` score `13.0293` n `83` status `ready` deltaP `43.1225` edge `0.9757` maxDD `-6.5262`
- `news_risk_high->index_24h` score `6.961` n `83` status `ready` deltaP `48.5526` edge `0.274` maxDD `-0.075`
- `risk_on_high->commodity_24h` score `6.7242` n `52` status `ready` deltaP `39.7569` edge `0.2953` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `6.7242` n `52` status `ready` deltaP `39.7569` edge `0.2953` maxDD `0.0`
- `market_context_high->commodity_24h` score `5.425` n `149` status `ready` deltaP `33.0455` edge `0.2843` maxDD `-0.8682`
- `news_risk_high->metal_24h` score `5.2006` n `83` status `ready` deltaP `32.6849` edge `0.2609` maxDD `-0.6334`
- `risk_on_high->commodity_4h` score `2.4202` n `52` status `ready` deltaP `29.9484` edge `0.037` maxDD `-0.1313`
- `risk_on_and_context->commodity_4h` score `2.4202` n `52` status `ready` deltaP `29.9484` edge `0.037` maxDD `-0.1313`
- `risk_on_high->fx_24h` score `2.4168` n `52` status `ready` deltaP `32.1047` edge `-0.0084` maxDD `-0.0054`
- `risk_on_and_context->fx_24h` score `2.4168` n `52` status `ready` deltaP `32.1047` edge `-0.0084` maxDD `-0.0054`
- `market_context_high->commodity_4h` score `2.3199` n `149` status `ready` deltaP `26.4507` edge `0.0588` maxDD `-0.345`
- `market_context_high->fx_24h` score `2.2819` n `149` status `ready` deltaP `29.3298` edge `0.0162` maxDD `-0.0593`
- `market_context_high->commodity_1h` score `0.9444` n `149` status `ready` deltaP `14.5642` edge `0.0193` maxDD `-0.3491`
- `news_risk_high->index_4h` score `0.444` n `83` status `ready` deltaP `12.803` edge `0.0344` maxDD `-0.6935`
- `risk_on_high->commodity_1h` score `0.3211` n `52` status `ready` deltaP `7.6463` edge `0.011` maxDD `-0.1507`
- `risk_on_and_context->commodity_1h` score `0.3211` n `52` status `ready` deltaP `7.6463` edge `0.011` maxDD `-0.1507`
- `risk_on_high->metal_1h` score `0.1879` n `52` status `ready` deltaP `6.8632` edge `0.0089` maxDD `-0.1115`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
