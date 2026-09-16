# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-16T19:37:28.068633+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `11173`

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

- `news_risk_high->unknown_4h` score `368.3952` n `83` status `ready` deltaP `-20.9007` edge `30.9284` maxDD `-4.1571`
- `news_risk_high->crypto_alt_24h` score `18.9833` n `83` status `ready` deltaP `42.518` edge `1.4364` maxDD `-9.3661`
- `news_risk_high->crypto_major_24h` score `17.5261` n `83` status `ready` deltaP `35.6258` edge `1.4225` maxDD `-13.2931`
- `news_risk_high->equity_24h` score `13.7766` n `83` status `ready` deltaP `44.8586` edge `1.0264` maxDD `-6.5262`
- `news_risk_high->index_24h` score `7.1742` n `83` status `ready` deltaP `50.2887` edge `0.2802` maxDD `-0.075`
- `risk_on_high->commodity_24h` score `6.2361` n `52` status `ready` deltaP `38.0208` edge `0.2662` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `6.2361` n `52` status `ready` deltaP `38.0208` edge `0.2662` maxDD `0.0`
- `news_risk_high->metal_24h` score `5.4046` n `83` status `ready` deltaP `32.6849` edge `0.2779` maxDD `-0.6334`
- `market_context_high->commodity_24h` score `4.9369` n `149` status `ready` deltaP `31.3094` edge `0.2552` maxDD `-0.8682`
- `risk_on_high->fx_24h` score `2.412` n `52` status `ready` deltaP `32.1047` edge `-0.0088` maxDD `-0.0054`
- `risk_on_and_context->fx_24h` score `2.412` n `52` status `ready` deltaP `32.1047` edge `-0.0088` maxDD `-0.0054`
- `risk_on_high->commodity_4h` score `2.3752` n `52` status `ready` deltaP `29.4911` edge `0.0363` maxDD `-0.1313`
- `risk_on_and_context->commodity_4h` score `2.3752` n `52` status `ready` deltaP `29.4911` edge `0.0363` maxDD `-0.1313`
- `market_context_high->fx_24h` score `2.2771` n `149` status `ready` deltaP `29.3298` edge `0.0158` maxDD `-0.0593`
- `market_context_high->commodity_4h` score `2.2749` n `149` status `ready` deltaP `25.9934` edge `0.0581` maxDD `-0.345`
- `market_context_high->commodity_1h` score `0.9156` n `149` status `ready` deltaP `14.2648` edge `0.0189` maxDD `-0.3491`
- `news_risk_high->index_4h` score `0.3809` n `83` status `ready` deltaP `12.0408` edge `0.0314` maxDD `-0.6935`
- `risk_on_high->commodity_1h` score `0.2923` n `52` status `ready` deltaP `7.3469` edge `0.0106` maxDD `-0.1507`
- `risk_on_and_context->commodity_1h` score `0.2923` n `52` status `ready` deltaP `7.3469` edge `0.0106` maxDD `-0.1507`
- `risk_on_high->metal_1h` score `0.2066` n `52` status `ready` deltaP `7.1626` edge `0.0093` maxDD `-0.1115`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
