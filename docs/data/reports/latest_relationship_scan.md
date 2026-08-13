# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-13T18:22:37.780795+00:00`
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

- `market_context_high->unknown_24h` score `79.2114` n `157` status `ready` deltaP `-25.0354` edge `7.0591` maxDD `-9.6329`
- `risk_on_high->unknown_24h` score `33.6756` n `32` status `ready` deltaP `-42.0139` edge `4.6725` maxDD `-1.6689`
- `risk_on_and_context->unknown_24h` score `33.6756` n `32` status `ready` deltaP `-42.0139` edge `4.6725` maxDD `-1.6689`
- `news_risk_high->equity_24h` score `9.4558` n `36` status `ready` deltaP `10.0694` edge `0.7588` maxDD `-1.0358`
- `news_risk_high->equity_4h` score `6.5085` n `36` status `ready` deltaP `35.3659` edge `0.3066` maxDD `0.0`
- `risk_on_high->commodity_24h` score `4.2544` n `32` status `ready` deltaP `30.0347` edge `0.1543` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `4.2544` n `32` status `ready` deltaP `30.0347` edge `0.1543` maxDD `0.0`
- `risk_on_high->commodity_4h` score `2.6878` n `32` status `ready` deltaP `18.9787` edge `0.1157` maxDD `-0.1258`
- `risk_on_and_context->commodity_4h` score `2.6878` n `32` status `ready` deltaP `18.9787` edge `0.1157` maxDD `-0.1258`
- `news_risk_high->index_24h` score `2.5076` n `36` status `ready` deltaP `15.625` edge `0.1048` maxDD `0.0`
- `market_context_high->commodity_24h` score `2.3047` n `157` status `ready` deltaP `19.8436` edge `0.1401` maxDD `-2.4263`
- `risk_on_high->fx_24h` score `1.8462` n `32` status `ready` deltaP `20.8333` edge `0.0334` maxDD `-0.1418`
- `risk_on_and_context->fx_24h` score `1.8462` n `32` status `ready` deltaP `20.8333` edge `0.0334` maxDD `-0.1418`
- `news_risk_high->index_4h` score `1.6349` n `36` status `ready` deltaP `19.3089` edge `0.0207` maxDD `-0.0546`
- `market_context_high->commodity_4h` score `1.5306` n `157` status `ready` deltaP `16.6499` edge `0.0804` maxDD `-2.1077`
- `news_risk_high->equity_1h` score `1.3593` n `36` status `ready` deltaP `6.9362` edge `0.0989` maxDD `-0.5496`
- `risk_on_high->commodity_1h` score `1.2707` n `32` status `ready` deltaP `13.6602` edge `0.0381` maxDD `-0.1957`
- `risk_on_and_context->commodity_1h` score `1.2707` n `32` status `ready` deltaP `13.6602` edge `0.0381` maxDD `-0.1957`
- `risk_on_high->crypto_major_24h` score `1.2671` n `32` status `ready` deltaP `12.8472` edge `0.1924` maxDD `-6.2481`
- `risk_on_and_context->crypto_major_24h` score `1.2671` n `32` status `ready` deltaP `12.8472` edge `0.1924` maxDD `-6.2481`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
