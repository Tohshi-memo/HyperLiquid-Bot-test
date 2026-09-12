# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-12T03:37:31.197388+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `11291`

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

- `market_context_high->unknown_24h` score `572.0167` n `141` status `ready` deltaP `14.033` edge `47.5797` maxDD `-0.082`
- `news_risk_high->unknown_1h` score `383.0713` n `82` status `ready` deltaP `-3.6038` edge `31.9888` maxDD `-1.7068`
- `risk_on_high->crypto_alt_24h` score `24.9245` n `89` status `ready` deltaP `42.9931` edge `1.8134` maxDD `-0.8386`
- `risk_on_and_context->crypto_alt_24h` score `24.9245` n `89` status `ready` deltaP `42.9931` edge `1.8134` maxDD `-0.8386`
- `news_risk_high->crypto_major_24h` score `23.6068` n `55` status `ready` deltaP `54.012` edge `1.6972` maxDD `-5.8705`
- `market_context_high->crypto_alt_24h` score `20.7178` n `141` status `ready` deltaP `37.2636` edge `1.5608` maxDD `-3.9523`
- `news_risk_high->crypto_alt_24h` score `16.7634` n `55` status `ready` deltaP `28.6111` edge `1.255` maxDD `-2.2369`
- `news_risk_high->equity_24h` score `11.8216` n `55` status `ready` deltaP `33.3428` edge `0.7727` maxDD `-0.1212`
- `risk_on_high->equity_24h` score `9.1611` n `89` status `ready` deltaP `36.9792` edge `0.5169` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `9.1611` n `89` status `ready` deltaP `36.9792` edge `0.5169` maxDD `0.0`
- `market_context_high->equity_24h` score `8.8419` n `141` status `ready` deltaP `36.9792` edge `0.4903` maxDD `0.0`
- `risk_on_high->crypto_alt_4h` score `8.7651` n `89` status `ready` deltaP `43.8288` edge `0.4754` maxDD `-1.9733`
- `risk_on_and_context->crypto_alt_4h` score `8.7651` n `89` status `ready` deltaP `43.8288` edge `0.4754` maxDD `-1.9733`
- `news_risk_high->metal_24h` score `8.1657` n `55` status `ready` deltaP `51.0417` edge `0.3402` maxDD `0.0`
- `news_risk_high->index_24h` score `7.9316` n `55` status `ready` deltaP `51.2247` edge `0.3288` maxDD `-0.0797`
- `risk_on_high->crypto_major_24h` score `7.6049` n `89` status `ready` deltaP `24.206` edge `1.2204` maxDD `-24.5429`
- `risk_on_and_context->crypto_major_24h` score `7.6049` n `89` status `ready` deltaP `24.206` edge `1.2204` maxDD `-24.5429`
- `risk_on_high->crypto_major_4h` score `6.73` n `89` status `ready` deltaP `31.6046` edge `0.436` maxDD `-3.8693`
- `risk_on_and_context->crypto_major_4h` score `6.73` n `89` status `ready` deltaP `31.6046` edge `0.436` maxDD `-3.8693`
- `risk_on_high->index_24h` score `5.2589` n `89` status `ready` deltaP `51.4903` edge `0.0992` maxDD `-0.0051`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
