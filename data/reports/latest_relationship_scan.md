# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-09T11:43:00.261667+00:00`
- Price records: `672`
- Market context records: `3379`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `13080`

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

- `risk_on_high->crypto_major_24h` score `56.0164` n `32` status `ready` deltaP `58.6806` edge `4.2811` maxDD `-0.0083`
- `risk_on_and_context->crypto_major_24h` score `56.0164` n `32` status `ready` deltaP `58.6806` edge `4.2811` maxDD `-0.0083`
- `risk_on_high->crypto_alt_24h` score `53.6057` n `32` status `ready` deltaP `54.6875` edge `4.1177` maxDD `-0.8779`
- `risk_on_and_context->crypto_alt_24h` score `53.6057` n `32` status `ready` deltaP `54.6875` edge `4.1177` maxDD `-0.8779`
- `risk_on_high->equity_24h` score `45.6381` n `32` status `ready` deltaP `56.7708` edge `3.4247` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `45.6381` n `32` status `ready` deltaP `56.7708` edge `3.4247` maxDD `0.0`
- `risk_on_high->index_24h` score `23.1182` n `32` status `ready` deltaP `50.8681` edge `1.5874` maxDD `0.0`
- `risk_on_and_context->index_24h` score `23.1182` n `32` status `ready` deltaP `50.8681` edge `1.5874` maxDD `0.0`
- `market_context_high->crypto_alt_24h` score `22.2085` n `153` status `ready` deltaP `19.904` edge `2.5165` maxDD `-56.8787`
- `risk_on_high->crypto_major_4h` score `15.4056` n `32` status `ready` deltaP `28.3537` edge `1.207` maxDD `-5.9781`
- `risk_on_and_context->crypto_major_4h` score `15.4056` n `32` status `ready` deltaP `28.3537` edge `1.207` maxDD `-5.9781`
- `risk_on_high->metal_24h` score `14.3446` n `32` status `ready` deltaP `30.9028` edge `1.0155` maxDD `-0.7574`
- `risk_on_and_context->metal_24h` score `14.3446` n `32` status `ready` deltaP `30.9028` edge `1.0155` maxDD `-0.7574`
- `market_context_high->index_24h` score `11.754` n `153` status `ready` deltaP `35.1818` edge `1.0004` maxDD `-16.1026`
- `market_context_high->equity_24h` score `10.8912` n `153` status `ready` deltaP `29.9734` edge `2.0381` maxDD `-53.663`
- `market_context_high->crypto_major_24h` score `8.9767` n `153` status `ready` deltaP `23.8971` edge `2.2747` maxDD `-95.3189`
- `risk_on_high->crypto_alt_4h` score `7.3494` n `32` status `ready` deltaP `9.0701` edge `0.7364` maxDD `-11.7537`
- `risk_on_and_context->crypto_alt_4h` score `7.3494` n `32` status `ready` deltaP `9.0701` edge `0.7364` maxDD `-11.7537`
- `risk_on_high->equity_4h` score `3.5645` n `32` status `ready` deltaP `14.4055` edge `0.4744` maxDD `-5.7426`
- `risk_on_and_context->equity_4h` score `3.5645` n `32` status `ready` deltaP `14.4055` edge `0.4744` maxDD `-5.7426`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
