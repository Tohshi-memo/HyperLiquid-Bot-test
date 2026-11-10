# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-10T06:22:34.945652+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `11442`

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

- `market_context_high->unknown_4h` score `37.9165` n `88` status `ready` deltaP `7.6774` edge `3.1533` maxDD `-0.9153`
- `market_context_high->equity_24h` score `34.9021` n `85` status `ready` deltaP `32.4396` edge `2.9327` maxDD `-16.9034`
- `market_context_high->index_24h` score `5.5022` n `85` status `ready` deltaP `25.5704` edge `0.3343` maxDD `-2.3671`
- `market_context_high->crypto_alt_24h` score `3.7124` n `85` status `ready` deltaP `21.4782` edge `0.8422` maxDD `-33.4213`
- `market_context_high->metal_24h` score `-0.2042` n `85` status `ready` deltaP `16.0485` edge `-0.0687` maxDD `-1.4245`
- `market_context_high->commodity_1h` score `-0.4868` n `88` status `ready` deltaP `0.7417` edge `0.0009` maxDD `-1.7935`
- `market_context_high->metal_1h` score `-0.5007` n `88` status `ready` deltaP `2.4497` edge `0.0096` maxDD `-1.4122`
- `market_context_high->commodity_4h` score `-0.5899` n `88` status `ready` deltaP `1.1225` edge `0.0275` maxDD `-4.182`
- `market_context_high->index_4h` score `-0.8272` n `88` status `ready` deltaP `0.3464` edge `-0.0106` maxDD `-2.4871`
- `market_context_high->index_1h` score `-1.1124` n `88` status `ready` deltaP `-9.4515` edge `0.0035` maxDD `-0.9814`
- `market_context_high->metal_4h` score `-1.2769` n `88` status `ready` deltaP `-3.1873` edge `-0.0041` maxDD `-4.0688`
- `market_context_high->fx_1h` score `-1.3436` n `88` status `ready` deltaP `-14.657` edge `-0.0061` maxDD `-0.8088`
- `market_context_high->equity_1h` score `-1.8653` n `88` status `ready` deltaP `-9.7509` edge `0.0105` maxDD `-8.1039`
- `market_context_high->crypto_alt_1h` score `-2.0091` n `88` status `ready` deltaP `0.034` edge `-0.0599` maxDD `-10.8319`
- `market_context_high->fx_4h` score `-2.1659` n `88` status `ready` deltaP `-7.3725` edge `-0.0104` maxDD `-2.4506`
- `market_context_high->fx_24h` score `-2.8882` n `85` status `ready` deltaP `-7.3973` edge `-0.0314` maxDD `-3.4642`
- `market_context_high->crypto_major_1h` score `-3.2337` n `88` status `ready` deltaP `-5.5593` edge `-0.1152` maxDD `-15.9848`
- `market_context_high->commodity_24h` score `-5.7704` n `85` status `ready` deltaP `-23.0544` edge `-0.0649` maxDD `-24.029`
- `market_context_high->equity_4h` score `-7.5525` n `88` status `ready` deltaP `-2.8963` edge `-0.2289` maxDD `-25.16`
- `market_context_high->crypto_alt_4h` score `-9.2912` n `88` status `ready` deltaP `1.178` edge `-0.2703` maxDD `-34.2787`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
