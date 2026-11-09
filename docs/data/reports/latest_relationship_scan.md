# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-09T23:07:27.505918+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `104`

- Symbol pattern count: `9892`

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

- `market_context_high->unknown_4h` score `29.6901` n `88` status `ready` deltaP `7.3725` edge `2.4698` maxDD `-0.9153`
- `market_context_high->equity_24h` score `16.9924` n `56` status `ready` deltaP `25.9006` edge `2.2463` maxDD `-16.9034`
- `market_context_high->index_24h` score `2.9607` n `56` status `ready` deltaP `21.379` edge `0.2833` maxDD `-2.3671`
- `market_context_high->crypto_alt_24h` score `0.2671` n `56` status `ready` deltaP `8.1115` edge `0.4896` maxDD `-33.4213`
- `market_context_high->metal_24h` score `-0.0295` n `56` status `ready` deltaP `10.7174` edge `-0.0186` maxDD `-1.4245`
- `market_context_high->metal_1h` score `-0.3772` n `88` status `ready` deltaP `3.6473` edge `0.0119` maxDD `-1.4122`
- `market_context_high->commodity_1h` score `-0.5499` n `88` status `ready` deltaP `-0.1565` edge `-0.0012` maxDD `-1.7935`
- `market_context_high->index_4h` score `-0.8477` n `88` status `ready` deltaP `0.0416` edge `-0.0112` maxDD `-2.4871`
- `market_context_high->commodity_4h` score `-0.8917` n `88` status `ready` deltaP `-2.536` edge `0.0132` maxDD `-4.182`
- `market_context_high->index_1h` score `-1.1054` n `88` status `ready` deltaP `-9.3018` edge `0.0034` maxDD `-0.9814`
- `market_context_high->metal_4h` score `-1.1135` n `88` status `ready` deltaP `-1.8154` edge `0.0077` maxDD `-4.0688`
- `market_context_high->fx_1h` score `-1.3187` n `88` status `ready` deltaP `-14.2079` edge `-0.0059` maxDD `-0.8088`
- `market_context_high->equity_1h` score `-1.7742` n `88` status `ready` deltaP `-8.4036` edge `0.0132` maxDD `-8.1039`
- `market_context_high->commodity_24h` score `-1.846` n `56` status `ready` deltaP `-14.425` edge `0.0594` maxDD `-7.9923`
- `market_context_high->crypto_alt_1h` score `-1.9553` n `88` status `ready` deltaP `0.4831` edge `-0.056` maxDD `-10.8319`
- `market_context_high->fx_4h` score `-2.1059` n `88` status `ready` deltaP `-6.4579` edge `-0.0088` maxDD `-2.4506`
- `market_context_high->fx_24h` score `-2.1776` n `56` status `ready` deltaP `-13.2427` edge `-0.0518` maxDD `-3.1275`
- `market_context_high->crypto_major_1h` score `-3.2298` n `88` status `ready` deltaP `-5.5593` edge `-0.1147` maxDD `-15.9848`
- `market_context_high->equity_4h` score `-7.4045` n `88` status `ready` deltaP `-2.5915` edge `-0.2186` maxDD `-25.16`
- `market_context_high->crypto_alt_4h` score `-9.1194` n `88` status `ready` deltaP `2.245` edge `-0.2631` maxDD `-34.2787`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
