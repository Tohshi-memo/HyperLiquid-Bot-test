# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-12T04:52:27.025302+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `11383`

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

- `market_context_high->unknown_24h` score `1082.2994` n `136` status `ready` deltaP `13.9808` edge `90.1036` maxDD `-0.082`
- `news_risk_high->unknown_1h` score `383.3125` n `82` status `ready` deltaP `-3.7535` edge `32.0099` maxDD `-1.7068`
- `risk_on_high->crypto_alt_24h` score `23.9377` n `84` status `ready` deltaP `42.6587` edge `1.7334` maxDD `-0.8386`
- `risk_on_and_context->crypto_alt_24h` score `23.9377` n `84` status `ready` deltaP `42.6587` edge `1.7334` maxDD `-0.8386`
- `news_risk_high->crypto_major_24h` score `23.8349` n `58` status `ready` deltaP `54.3881` edge `1.7137` maxDD `-5.8705`
- `market_context_high->crypto_alt_24h` score `20.0593` n `136` status `ready` deltaP `36.8464` edge `1.5087` maxDD `-3.9523`
- `news_risk_high->crypto_alt_24h` score `17.2745` n `58` status `ready` deltaP `29.6456` edge `1.2907` maxDD `-2.2369`
- `news_risk_high->equity_24h` score `12.0731` n `58` status `ready` deltaP `33.5309` edge `0.7924` maxDD `-0.1212`
- `risk_on_high->equity_24h` score `9.0483` n `84` status `ready` deltaP `36.9792` edge `0.5075` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `9.0483` n `84` status `ready` deltaP `36.9792` edge `0.5075` maxDD `0.0`
- `market_context_high->equity_24h` score `8.7387` n `136` status `ready` deltaP `36.9792` edge `0.4817` maxDD `0.0`
- `risk_on_high->crypto_alt_4h` score `8.4449` n `84` status `ready` deltaP `43.5613` edge `0.4505` maxDD `-1.9733`
- `risk_on_and_context->crypto_alt_4h` score `8.4449` n `84` status `ready` deltaP `43.5613` edge `0.4505` maxDD `-1.9733`
- `news_risk_high->metal_24h` score `8.1813` n `58` status `ready` deltaP `51.0417` edge `0.3415` maxDD `0.0`
- `news_risk_high->index_24h` score `7.9479` n `58` status `ready` deltaP `51.4128` edge `0.3289` maxDD `-0.0797`
- `risk_on_high->crypto_major_24h` score `6.5807` n `84` status `ready` deltaP `21.999` edge `1.1038` maxDD `-24.5429`
- `risk_on_and_context->crypto_major_24h` score `6.5807` n `84` status `ready` deltaP `21.999` edge `1.1038` maxDD `-24.5429`
- `risk_on_high->crypto_major_4h` score `6.4213` n `84` status `ready` deltaP `30.4007` edge `0.4183` maxDD `-3.8693`
- `risk_on_and_context->crypto_major_4h` score `6.4213` n `84` status `ready` deltaP `30.4007` edge `0.4183` maxDD `-3.8693`
- `risk_on_high->index_24h` score `5.1924` n `84` status `ready` deltaP `51.2897` edge `0.095` maxDD `-0.0051`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
