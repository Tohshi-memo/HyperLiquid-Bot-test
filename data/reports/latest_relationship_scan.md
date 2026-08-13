# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-13T19:52:30.468791+00:00`
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

- `market_context_high->unknown_24h` score `80.8836` n `156` status `ready` deltaP `-25.2538` edge `7.1999` maxDD `-9.6329`
- `risk_on_high->unknown_24h` score `33.7111` n `32` status `ready` deltaP `-41.8403` edge `4.6759` maxDD `-1.6689`
- `risk_on_and_context->unknown_24h` score `33.7111` n `32` status `ready` deltaP `-41.8403` edge `4.6759` maxDD `-1.6689`
- `news_risk_high->equity_24h` score `9.679` n `36` status `ready` deltaP `10.0694` edge `0.7774` maxDD `-1.0358`
- `news_risk_high->equity_4h` score `6.6916` n `36` status `ready` deltaP `35.9756` edge `0.3178` maxDD `0.0`
- `risk_on_high->commodity_24h` score `4.4253` n `32` status `ready` deltaP `31.0764` edge `0.1616` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `4.4253` n `32` status `ready` deltaP `31.0764` edge `0.1616` maxDD `0.0`
- `risk_on_high->commodity_4h` score `2.798` n `32` status `ready` deltaP `19.7409` edge `0.1198` maxDD `-0.1258`
- `risk_on_and_context->commodity_4h` score `2.798` n `32` status `ready` deltaP `19.7409` edge `0.1198` maxDD `-0.1258`
- `news_risk_high->index_24h` score `2.4992` n `36` status `ready` deltaP `15.625` edge `0.1041` maxDD `0.0`
- `market_context_high->commodity_24h` score `2.4777` n `156` status `ready` deltaP `20.82` edge `0.148` maxDD `-2.4263`
- `risk_on_high->fx_24h` score `1.7449` n `32` status `ready` deltaP `19.7917` edge `0.0319` maxDD `-0.1418`
- `risk_on_and_context->fx_24h` score `1.7449` n `32` status `ready` deltaP `19.7917` edge `0.0319` maxDD `-0.1418`
- `news_risk_high->index_4h` score `1.6689` n `36` status `ready` deltaP `19.6138` edge `0.0215` maxDD `-0.0546`
- `market_context_high->commodity_4h` score `1.6128` n `156` status `ready` deltaP `17.2569` edge `0.0832` maxDD `-2.1077`
- `news_risk_high->equity_1h` score `1.4768` n `36` status `ready` deltaP `7.0859` edge `0.1077` maxDD `-0.5496`
- `risk_on_high->crypto_major_24h` score `1.3385` n `32` status `ready` deltaP `13.0208` edge `0.2004` maxDD `-6.2481`
- `risk_on_and_context->crypto_major_24h` score `1.3385` n `32` status `ready` deltaP `13.0208` edge `0.2004` maxDD `-6.2481`
- `risk_on_high->commodity_1h` score `1.2575` n `32` status `ready` deltaP `13.5105` edge `0.038` maxDD `-0.1957`
- `risk_on_and_context->commodity_1h` score `1.2575` n `32` status `ready` deltaP `13.5105` edge `0.038` maxDD `-0.1957`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
