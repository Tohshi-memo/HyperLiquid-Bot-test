# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-12T09:22:26.511446+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `11799`

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

- `market_context_high->unknown_24h` score `2602.3898` n `118` status `ready` deltaP `13.7565` edge `216.7793` maxDD `-0.082`
- `news_risk_high->unknown_1h` score `383.2608` n `82` status `ready` deltaP `-3.3044` edge `32.0026` maxDD `-1.7068`
- `news_risk_high->crypto_major_24h` score `24.3494` n `59` status `ready` deltaP `54.505` edge `1.7558` maxDD `-5.8705`
- `risk_on_high->crypto_alt_24h` score `21.8086` n `69` status `ready` deltaP `41.3647` edge `1.5646` maxDD `-0.8386`
- `risk_on_and_context->crypto_alt_24h` score `21.8086` n `69` status `ready` deltaP `41.3647` edge `1.5646` maxDD `-0.8386`
- `market_context_high->crypto_alt_24h` score `18.3041` n `118` status `ready` deltaP `35.0518` edge `1.3744` maxDD `-3.9523`
- `news_risk_high->crypto_alt_24h` score `17.6326` n `59` status `ready` deltaP `29.967` edge `1.3184` maxDD `-2.2369`
- `news_risk_high->equity_24h` score `12.1859` n `59` status `ready` deltaP `33.9366` edge `0.7991` maxDD `-0.1212`
- `risk_on_high->equity_24h` score `9.0641` n `69` status `ready` deltaP `37.3264` edge `0.5065` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `9.0641` n `69` status `ready` deltaP `37.3264` edge `0.5065` maxDD `0.0`
- `market_context_high->equity_24h` score `8.7209` n `118` status `ready` deltaP `37.3264` edge `0.4779` maxDD `0.0`
- `news_risk_high->metal_24h` score `8.2991` n `59` status `ready` deltaP `52.6042` edge `0.3409` maxDD `0.0`
- `risk_on_high->crypto_alt_4h` score `8.0517` n `69` status `ready` deltaP `42.8309` edge `0.4226` maxDD `-1.9733`
- `risk_on_and_context->crypto_alt_4h` score `8.0517` n `69` status `ready` deltaP `42.8309` edge `0.4226` maxDD `-1.9733`
- `news_risk_high->index_24h` score `7.9117` n `59` status `ready` deltaP `51.4713` edge `0.3255` maxDD `-0.0797`
- `risk_on_high->crypto_major_4h` score `5.3634` n `69` status `ready` deltaP `26.6569` edge `0.3551` maxDD `-3.8693`
- `risk_on_and_context->crypto_major_4h` score `5.3634` n `69` status `ready` deltaP `26.6569` edge `0.3551` maxDD `-3.8693`
- `risk_on_high->index_24h` score `5.0307` n `69` status `ready` deltaP `50.5133` edge `0.0867` maxDD `-0.0051`
- `risk_on_and_context->index_24h` score `5.0307` n `69` status `ready` deltaP `50.5133` edge `0.0867` maxDD `-0.0051`
- `risk_on_high->equity_4h` score `4.0672` n `69` status `ready` deltaP `37.4182` edge `0.0988` maxDD `-0.079`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
