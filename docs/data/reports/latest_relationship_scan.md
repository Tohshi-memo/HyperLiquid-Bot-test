# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-14T17:07:32.198381+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11796`

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

- `market_context_high->unknown_24h` score `133.6753` n `129` status `ready` deltaP `-32.9175` edge `11.6503` maxDD `-9.6329`
- `risk_on_high->unknown_24h` score `32.7431` n `32` status `ready` deltaP `-46.7014` edge `4.5842` maxDD `-1.6689`
- `risk_on_and_context->unknown_24h` score `32.7431` n `32` status `ready` deltaP `-46.7014` edge `4.5842` maxDD `-1.6689`
- `news_risk_high->equity_24h` score `10.0003` n `36` status `ready` deltaP `11.8055` edge `0.7926` maxDD `-1.0358`
- `news_risk_high->equity_4h` score `7.4096` n `36` status `ready` deltaP `39.0244` edge `0.3573` maxDD `0.0`
- `market_context_high->commodity_24h` score `5.0206` n `129` status `ready` deltaP `28.67` edge `0.233` maxDD `-0.1266`
- `risk_on_high->commodity_24h` score `4.7053` n `32` status `ready` deltaP `31.7708` edge `0.1803` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `4.7053` n `32` status `ready` deltaP `31.7708` edge `0.1803` maxDD `0.0`
- `risk_on_high->commodity_4h` score `2.8182` n `32` status `ready` deltaP `19.5884` edge `0.1225` maxDD `-0.1258`
- `risk_on_and_context->commodity_4h` score `2.8182` n `32` status `ready` deltaP `19.5884` edge `0.1225` maxDD `-0.1258`
- `risk_on_high->crypto_major_24h` score `2.3366` n `32` status `ready` deltaP `18.0556` edge `0.2948` maxDD `-6.2481`
- `risk_on_and_context->crypto_major_24h` score `2.3366` n `32` status `ready` deltaP `18.0556` edge `0.2948` maxDD `-6.2481`
- `news_risk_high->index_24h` score `2.2256` n `36` status `ready` deltaP `15.625` edge `0.0813` maxDD `0.0`
- `market_context_high->commodity_4h` score `1.7941` n `129` status `ready` deltaP `17.4324` edge `0.0804` maxDD `-0.7687`
- `news_risk_high->index_4h` score `1.7941` n `36` status `ready` deltaP `20.8333` edge `0.0238` maxDD `-0.0546`
- `news_risk_high->equity_1h` score `1.7238` n `36` status `ready` deltaP `8.5829` edge `0.1183` maxDD `-0.5496`
- `risk_on_high->commodity_1h` score `1.2935` n `32` status `ready` deltaP `13.6602` edge `0.04` maxDD `-0.1957`
- `risk_on_and_context->commodity_1h` score `1.2935` n `32` status `ready` deltaP `13.6602` edge `0.04` maxDD `-0.1957`
- `risk_on_high->fx_24h` score `1.1067` n `32` status `ready` deltaP `13.1944` edge `0.0227` maxDD `-0.1418`
- `risk_on_and_context->fx_24h` score `1.1067` n `32` status `ready` deltaP `13.1944` edge `0.0227` maxDD `-0.1418`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
