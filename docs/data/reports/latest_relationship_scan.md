# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-11T14:37:30.582473+00:00`
- Price records: `672`
- Market context records: `3593`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `13114`

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

- `risk_on_high->crypto_major_24h` score `47.2293` n `32` status `ready` deltaP `50.6012` edge `3.6027` maxDD `-0.0083`
- `risk_on_and_context->crypto_major_24h` score `47.2293` n `32` status `ready` deltaP `50.6012` edge `3.6027` maxDD `-0.0083`
- `risk_on_high->equity_24h` score `43.3789` n `32` status `ready` deltaP `51.6464` edge `3.2706` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `43.3789` n `32` status `ready` deltaP `51.6464` edge `3.2706` maxDD `0.0`
- `risk_on_high->crypto_alt_24h` score `40.8412` n `32` status `ready` deltaP `50.0812` edge `3.0847` maxDD `-0.8779`
- `risk_on_and_context->crypto_alt_24h` score `40.8412` n `32` status `ready` deltaP `50.0812` edge `3.0847` maxDD `-0.8779`
- `risk_on_high->index_24h` score `25.3493` n `32` status `ready` deltaP `52.6863` edge `1.7612` maxDD `0.0`
- `risk_on_and_context->index_24h` score `25.3493` n `32` status `ready` deltaP `52.6863` edge `1.7612` maxDD `0.0`
- `risk_on_high->metal_24h` score `18.4297` n `32` status `ready` deltaP `36.8609` edge `1.3162` maxDD `-0.7574`
- `risk_on_and_context->metal_24h` score `18.4297` n `32` status `ready` deltaP `36.8609` edge `1.3162` maxDD `-0.7574`
- `market_context_high->equity_24h` score `17.735` n `156` status `ready` deltaP `28.5695` edge `1.9287` maxDD `-40.9667`
- `market_context_high->index_24h` score `13.9646` n `156` status `ready` deltaP `37.3017` edge `1.1367` maxDD `-15.0661`
- `risk_on_high->crypto_major_4h` score `13.4083` n `32` status `ready` deltaP `25.1524` edge `1.0619` maxDD `-5.9781`
- `risk_on_and_context->crypto_major_4h` score `13.4083` n `32` status `ready` deltaP `25.1524` edge `1.0619` maxDD `-5.9781`
- `market_context_high->crypto_major_24h` score `11.7952` n `156` status `ready` deltaP `15.9057` edge `1.65` maxDD `-54.8486`
- `market_context_high->metal_24h` score `7.4708` n `156` status `ready` deltaP `30.9314` edge `1.2056` maxDD `-25.9879`
- `market_context_high->crypto_alt_24h` score `6.7541` n `156` status `ready` deltaP `10.2575` edge `1.2987` maxDD `-56.6728`
- `risk_on_high->crypto_alt_4h` score `5.2634` n `32` status `ready` deltaP `6.0213` edge `0.5829` maxDD `-11.7537`
- `risk_on_and_context->crypto_alt_4h` score `5.2634` n `32` status `ready` deltaP `6.0213` edge `0.5829` maxDD `-11.7537`
- `risk_on_high->equity_4h` score `3.7079` n `32` status `ready` deltaP `15.1677` edge `0.4877` maxDD `-5.7426`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
