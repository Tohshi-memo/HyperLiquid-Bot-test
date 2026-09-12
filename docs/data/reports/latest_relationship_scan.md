# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-12T06:22:30.513528+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `11478`

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

- `market_context_high->unknown_24h` score `1570.8319` n `130` status `ready` deltaP `13.9129` edge `130.8151` maxDD `-0.082`
- `news_risk_high->unknown_1h` score `383.3725` n `82` status `ready` deltaP `-3.6038` edge `32.0139` maxDD `-1.7068`
- `news_risk_high->crypto_major_24h` score `24.0554` n `59` status `ready` deltaP `54.505` edge `1.7313` maxDD `-5.8705`
- `risk_on_high->crypto_alt_24h` score `22.7011` n `78` status `ready` deltaP `42.2008` edge `1.6334` maxDD `-0.8386`
- `risk_on_and_context->crypto_alt_24h` score `22.7011` n `78` status `ready` deltaP `42.2008` edge `1.6334` maxDD `-0.8386`
- `market_context_high->crypto_alt_24h` score `19.2742` n `130` status `ready` deltaP `36.3034` edge `1.4469` maxDD `-3.9523`
- `news_risk_high->crypto_alt_24h` score `17.533` n `59` status `ready` deltaP `29.967` edge `1.3101` maxDD `-2.2369`
- `news_risk_high->equity_24h` score `12.0934` n `59` status `ready` deltaP `33.5894` edge `0.7937` maxDD `-0.1212`
- `risk_on_high->equity_24h` score `9.0207` n `78` status `ready` deltaP `36.9792` edge `0.5052` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `9.0207` n `78` status `ready` deltaP `36.9792` edge `0.5052` maxDD `0.0`
- `market_context_high->equity_24h` score `8.6991` n `130` status `ready` deltaP `36.9792` edge `0.4784` maxDD `0.0`
- `news_risk_high->metal_24h` score `8.1911` n `59` status `ready` deltaP `51.3889` edge `0.34` maxDD `0.0`
- `risk_on_high->crypto_alt_4h` score `8.0872` n `78` status `ready` deltaP `43.4998` edge `0.4211` maxDD `-1.9733`
- `risk_on_and_context->crypto_alt_4h` score `8.0872` n `78` status `ready` deltaP `43.4998` edge `0.4211` maxDD `-1.9733`
- `news_risk_high->index_24h` score `7.9273` n `59` status `ready` deltaP `51.4713` edge `0.3268` maxDD `-0.0797`
- `risk_on_high->crypto_major_4h` score `5.8944` n `78` status `ready` deltaP `29.5146` edge `0.3803` maxDD `-3.8693`
- `risk_on_and_context->crypto_major_4h` score `5.8944` n `78` status `ready` deltaP `29.5146` edge `0.3803` maxDD `-3.8693`
- `risk_on_high->index_24h` score `5.1284` n `78` status `ready` deltaP `51.0149` edge `0.0915` maxDD `-0.0051`
- `risk_on_and_context->index_24h` score `5.1284` n `78` status `ready` deltaP `51.0149` edge `0.0915` maxDD `-0.0051`
- `risk_on_high->crypto_major_24h` score `5.0819` n `78` status `ready` deltaP `18.977` edge `0.9318` maxDD `-24.5429`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
