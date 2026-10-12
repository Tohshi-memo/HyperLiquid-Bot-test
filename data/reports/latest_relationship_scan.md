# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-12T13:52:37.434674+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `7870`

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

- `market_context_high->crypto_alt_24h` score `30.8834` n `41` status `ready` deltaP `43.2207` edge `2.3029` maxDD `-1.0604`
- `market_context_high->crypto_major_24h` score `28.6373` n `41` status `ready` deltaP `52.5873` edge `2.0533` maxDD `-1.0621`
- `risk_on_high->crypto_alt_4h` score `3.9744` n `48` status `ready` deltaP `18.1911` edge `0.2547` maxDD `-1.9151`
- `risk_on_and_context->crypto_alt_4h` score `3.9744` n `48` status `ready` deltaP `18.1911` edge `0.2547` maxDD `-1.9151`
- `risk_on_high->crypto_major_4h` score `3.5685` n `48` status `ready` deltaP `33.1301` edge `0.3219` maxDD `-4.1548`
- `risk_on_and_context->crypto_major_4h` score `3.5685` n `48` status `ready` deltaP `33.1301` edge `0.3219` maxDD `-4.1548`
- `market_context_high->metal_24h` score `3.4304` n `41` status `ready` deltaP `29.8188` edge `0.1054` maxDD `-0.1328`
- `market_context_high->crypto_alt_4h` score `3.2725` n `100` status `ready` deltaP `13.2744` edge `0.3291` maxDD `-9.2574`
- `market_context_high->crypto_major_4h` score `3.0994` n `100` status `ready` deltaP `16.9634` edge `0.3011` maxDD `-7.4722`
- `market_context_high->crypto_alt_1h` score `1.5801` n `100` status `ready` deltaP `12.2036` edge `0.1454` maxDD `-4.9401`
- `risk_on_high->crypto_alt_1h` score `0.9586` n `48` status `ready` deltaP `6.5369` edge `0.096` maxDD `-2.4421`
- `risk_on_and_context->crypto_alt_1h` score `0.9586` n `48` status `ready` deltaP `6.5369` edge `0.096` maxDD `-2.4421`
- `market_context_high->crypto_major_1h` score `0.662` n `100` status `ready` deltaP `4.3473` edge `0.1025` maxDD `-3.4384`
- `risk_on_high->crypto_major_1h` score `0.4186` n `48` status `ready` deltaP `5.514` edge `0.0822` maxDD `-3.2233`
- `risk_on_and_context->crypto_major_1h` score `0.4186` n `48` status `ready` deltaP `5.514` edge `0.0822` maxDD `-3.2233`
- `market_context_high->index_1h` score `-0.0468` n `100` status `ready` deltaP `3.7006` edge `0.0024` maxDD `-0.3122`
- `market_context_high->metal_1h` score `-0.1045` n `100` status `ready` deltaP `6.4012` edge `0.0047` maxDD `-0.4868`
- `market_context_high->unknown_4h` score `-0.1937` n `100` status `ready` deltaP `-5.1463` edge `0.0828` maxDD `-1.8373`
- `risk_on_high->metal_1h` score `-0.2872` n `48` status `ready` deltaP `3.5679` edge `0.0042` maxDD `-0.4868`
- `risk_on_and_context->metal_1h` score `-0.2872` n `48` status `ready` deltaP `3.5679` edge `0.0042` maxDD `-0.4868`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
