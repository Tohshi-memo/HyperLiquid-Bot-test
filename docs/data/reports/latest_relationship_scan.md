# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-26T07:52:28.032568+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `11878`

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

- `news_risk_high->unknown_24h` score `3313.3684` n `102` status `ready` deltaP `-0.6332` edge `276.1227` maxDD `-0.0226`
- `market_context_high->unknown_1h` score `69.9033` n `47` status `ready` deltaP `8.7687` edge `5.7739` maxDD `-0.2334`
- `market_context_high->crypto_major_24h` score `48.0125` n `47` status `ready` deltaP `23.4781` edge `3.8838` maxDD `-2.4756`
- `market_context_high->crypto_alt_24h` score `29.2884` n `47` status `ready` deltaP `21.657` edge `2.3343` maxDD `-2.7051`
- `market_context_high->equity_24h` score `25.3863` n `47` status `ready` deltaP `33.3739` edge `1.9286` maxDD `-2.1786`
- `market_context_high->index_24h` score `7.1838` n `47` status `ready` deltaP `30.4226` edge `0.4088` maxDD `-0.3705`
- `market_context_high->metal_24h` score `3.4011` n `47` status `ready` deltaP `28.8084` edge `0.1152` maxDD `-0.2401`
- `market_context_high->equity_4h` score `2.7265` n `47` status `ready` deltaP `17.2969` edge `0.1537` maxDD `-1.3444`
- `market_context_high->index_4h` score `2.5298` n `47` status `ready` deltaP `29.1483` edge `0.0319` maxDD `-0.2323`
- `market_context_high->crypto_alt_4h` score `1.3861` n `47` status `ready` deltaP `11.5172` edge `0.1055` maxDD `-3.3417`
- `news_risk_high->metal_24h` score `1.2082` n `102` status `ready` deltaP `27.8697` edge `0.1352` maxDD `-6.9545`
- `market_context_high->equity_1h` score `1.0637` n `47` status `ready` deltaP `12.2149` edge `0.0475` maxDD `-1.5564`
- `market_context_high->index_1h` score `0.7822` n `47` status `ready` deltaP `12.5143` edge `0.0096` maxDD `-0.2275`
- `market_context_high->crypto_major_4h` score `0.569` n `47` status `ready` deltaP `5.6045` edge `0.1005` maxDD `-5.2359`
- `market_context_high->fx_1h` score `0.5081` n `47` status `ready` deltaP `10.5586` edge `0.0076` maxDD `-0.1854`
- `market_context_high->crypto_major_1h` score `0.3422` n `47` status `ready` deltaP `5.2013` edge `0.0756` maxDD `-4.5405`
- `news_risk_high->index_24h` score `0.3249` n `102` status `ready` deltaP `13.2762` edge `0.0387` maxDD `-2.344`
- `news_risk_high->crypto_alt_1h` score `0.1388` n `136` status `ready` deltaP `6.4988` edge `0.0593` maxDD `-4.2849`
- `news_risk_high->index_1h` score `0.0663` n `136` status `ready` deltaP `4.6451` edge `0.0038` maxDD `-0.3395`
- `market_context_high->fx_4h` score `0.0615` n `47` status `ready` deltaP `9.6264` edge `0.0077` maxDD `-0.6736`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
