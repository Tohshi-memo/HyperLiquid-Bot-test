# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-12T12:52:25.113299+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `12058`

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

- `market_context_high->unknown_24h` score `4071.4704` n `104` status `ready` deltaP `13.5283` edge `339.2042` maxDD `-0.082`
- `risk_on_high->unknown_24h` score `1093.9837` n `56` status `ready` deltaP `15.4514` edge `91.0623` maxDD `0.0`
- `risk_on_and_context->unknown_24h` score `1093.9837` n `56` status `ready` deltaP `15.4514` edge `91.0623` maxDD `0.0`
- `news_risk_high->unknown_1h` score `383.351` n `82` status `ready` deltaP `-4.6517` edge `32.0191` maxDD `-1.7068`
- `news_risk_high->crypto_major_24h` score `24.4797` n `59` status `ready` deltaP `54.6786` edge `1.7655` maxDD `-5.8705`
- `risk_on_high->crypto_alt_24h` score `18.74` n `56` status `ready` deltaP `39.6825` edge `1.3201` maxDD `-0.8386`
- `risk_on_and_context->crypto_alt_24h` score `18.74` n `56` status `ready` deltaP `39.6825` edge `1.3201` maxDD `-0.8386`
- `news_risk_high->crypto_alt_24h` score `17.5654` n `59` status `ready` deltaP `29.967` edge `1.3128` maxDD `-2.2369`
- `market_context_high->crypto_alt_24h` score `16.1349` n `104` status `ready` deltaP `33.2265` edge `1.2058` maxDD `-3.9523`
- `news_risk_high->equity_24h` score `12.3313` n `59` status `ready` deltaP `34.2838` edge `0.8089` maxDD `-0.1212`
- `risk_on_high->equity_24h` score `8.8903` n `56` status `ready` deltaP `37.6736` edge `0.4897` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `8.8903` n `56` status `ready` deltaP `37.6736` edge `0.4897` maxDD `0.0`
- `risk_on_high->crypto_alt_4h` score `8.6961` n `56` status `ready` deltaP `42.9661` edge `0.4754` maxDD `-1.9733`
- `risk_on_and_context->crypto_alt_4h` score `8.6961` n `56` status `ready` deltaP `42.9661` edge `0.4754` maxDD `-1.9733`
- `market_context_high->equity_24h` score `8.6287` n `104` status `ready` deltaP `37.6736` edge `0.4679` maxDD `0.0`
- `news_risk_high->metal_24h` score `8.4` n `59` status `ready` deltaP `53.8194` edge `0.3412` maxDD `0.0`
- `news_risk_high->index_24h` score `7.9057` n `59` status `ready` deltaP `51.4713` edge `0.325` maxDD `-0.0797`
- `risk_on_high->index_24h` score `4.8672` n `56` status `ready` deltaP `49.504` edge `0.0798` maxDD `-0.0051`
- `risk_on_and_context->index_24h` score `4.8672` n `56` status `ready` deltaP `49.504` edge `0.0798` maxDD `-0.0051`
- `risk_on_high->equity_4h` score `4.2185` n `56` status `ready` deltaP `37.6742` edge `0.1097` maxDD `-0.079`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
