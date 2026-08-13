# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-13T12:52:27.774003+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11712`

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

- `market_context_high->unknown_24h` score `44.3487` n `161` status `ready` deltaP `-23.6898` edge `4.1449` maxDD `-9.6329`
- `risk_on_high->unknown_24h` score `15.0729` n `32` status `ready` deltaP `-42.1875` edge `2.2887` maxDD `-1.6689`
- `risk_on_and_context->unknown_24h` score `15.0729` n `32` status `ready` deltaP `-42.1875` edge `2.2887` maxDD `-1.6689`
- `news_risk_high->equity_4h` score `6.9774` n `36` status `ready` deltaP `37.0427` edge `0.3345` maxDD `0.0`
- `risk_on_high->commodity_24h` score `3.59` n `32` status `ready` deltaP `26.2153` edge `0.1244` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `3.59` n `32` status `ready` deltaP `26.2153` edge `0.1244` maxDD `0.0`
- `risk_on_high->commodity_4h` score `2.5558` n `32` status `ready` deltaP `18.064` edge `0.1108` maxDD `-0.1258`
- `risk_on_and_context->commodity_4h` score `2.5558` n `32` status `ready` deltaP `18.064` edge `0.1108` maxDD `-0.1258`
- `risk_on_high->fx_24h` score `2.0688` n `32` status `ready` deltaP `23.0903` edge `0.0369` maxDD `-0.1418`
- `risk_on_and_context->fx_24h` score `2.0688` n `32` status `ready` deltaP `23.0903` edge `0.0369` maxDD `-0.1418`
- `news_risk_high->index_4h` score `1.8593` n `36` status `ready` deltaP `21.1382` edge `0.0272` maxDD `-0.0546`
- `market_context_high->commodity_24h` score `1.621` n `161` status `ready` deltaP `16.2774` edge `0.1069` maxDD `-2.4263`
- `news_risk_high->equity_1h` score `1.5895` n `36` status `ready` deltaP `7.8344` edge `0.1121` maxDD `-0.5496`
- `market_context_high->commodity_4h` score `1.3743` n `161` status `ready` deltaP `15.7154` edge `0.0736` maxDD `-2.1077`
- `risk_on_high->crypto_major_24h` score `1.3591` n `32` status `ready` deltaP `12.8472` edge `0.2042` maxDD `-6.2481`
- `risk_on_and_context->crypto_major_24h` score `1.3591` n `32` status `ready` deltaP `12.8472` edge `0.2042` maxDD `-6.2481`
- `risk_on_high->commodity_1h` score `1.17` n `32` status `ready` deltaP `12.6123` edge `0.0367` maxDD `-0.1957`
- `risk_on_and_context->commodity_1h` score `1.17` n `32` status `ready` deltaP `12.6123` edge `0.0367` maxDD `-0.1957`
- `risk_on_high->fx_4h` score `0.9841` n `32` status `ready` deltaP `11.3567` edge `0.0204` maxDD `-0.1285`
- `risk_on_and_context->fx_4h` score `0.9841` n `32` status `ready` deltaP `11.3567` edge `0.0204` maxDD `-0.1285`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
