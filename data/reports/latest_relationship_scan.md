# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-12T09:37:28.754632+00:00`
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

- `market_context_high->unknown_24h` score `2696.7783` n `117` status `ready` deltaP `13.742` edge `224.6451` maxDD `-0.082`
- `news_risk_high->unknown_1h` score `383.2584` n `82` status `ready` deltaP `-3.3044` edge `32.0024` maxDD `-1.7068`
- `news_risk_high->crypto_major_24h` score `24.3626` n `59` status `ready` deltaP `54.505` edge `1.7569` maxDD `-5.8705`
- `risk_on_high->crypto_alt_24h` score `21.6765` n `68` status `ready` deltaP `41.2582` edge `1.5543` maxDD `-0.8386`
- `risk_on_and_context->crypto_alt_24h` score `21.6765` n `68` status `ready` deltaP `41.2582` edge `1.5543` maxDD `-0.8386`
- `market_context_high->crypto_alt_24h` score `18.2024` n `117` status `ready` deltaP `34.9359` edge `1.3667` maxDD `-3.9523`
- `news_risk_high->crypto_alt_24h` score `17.6302` n `59` status `ready` deltaP `29.967` edge `1.3182` maxDD `-2.2369`
- `news_risk_high->equity_24h` score `12.1931` n `59` status `ready` deltaP `33.9366` edge `0.7997` maxDD `-0.1212`
- `risk_on_high->equity_24h` score `9.0593` n `68` status `ready` deltaP `37.3264` edge `0.5061` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `9.0593` n `68` status `ready` deltaP `37.3264` edge `0.5061` maxDD `0.0`
- `market_context_high->equity_24h` score `8.7185` n `117` status `ready` deltaP `37.3264` edge `0.4777` maxDD `0.0`
- `news_risk_high->metal_24h` score `8.313` n `59` status `ready` deltaP `52.7778` edge `0.3409` maxDD `0.0`
- `risk_on_high->crypto_alt_4h` score `8.0761` n `68` status `ready` deltaP `42.7456` edge `0.4252` maxDD `-1.9733`
- `risk_on_and_context->crypto_alt_4h` score `8.0761` n `68` status `ready` deltaP `42.7456` edge `0.4252` maxDD `-1.9733`
- `news_risk_high->index_24h` score `7.9117` n `59` status `ready` deltaP `51.4713` edge `0.3255` maxDD `-0.0797`
- `risk_on_high->crypto_major_4h` score `5.2679` n `68` status `ready` deltaP `26.2733` edge `0.3497` maxDD `-3.8693`
- `risk_on_and_context->crypto_major_4h` score `5.2679` n `68` status `ready` deltaP `26.2733` edge `0.3497` maxDD `-3.8693`
- `risk_on_high->index_24h` score `5.0196` n `68` status `ready` deltaP `50.4493` edge `0.0862` maxDD `-0.0051`
- `risk_on_and_context->index_24h` score `5.0196` n `68` status `ready` deltaP `50.4493` edge `0.0862` maxDD `-0.0051`
- `risk_on_high->equity_4h` score `4.0745` n `68` status `ready` deltaP `37.4642` edge `0.0991` maxDD `-0.079`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
