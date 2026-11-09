# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-09T16:52:29.565918+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `104`

- Symbol pattern count: `10094`

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

- `market_context_high->equity_24h` score `5.9493` n `34` status `ready` deltaP `9.8755` edge `0.6704` maxDD `-16.9034`
- `market_context_high->commodity_24h` score `1.938` n `34` status `ready` deltaP `4.1463` edge `0.1926` maxDD `-1.6995`
- `market_context_high->index_24h` score `0.8155` n `34` status `ready` deltaP `9.1503` edge `0.0898` maxDD `-2.3671`
- `market_context_high->fx_24h` score `0.7633` n `34` status `ready` deltaP `11.3766` edge `-0.0016` maxDD `-0.1843`
- `market_context_high->metal_1h` score `-0.2754` n `88` status `ready` deltaP `4.5455` edge `0.0144` maxDD `-1.4122`
- `market_context_high->commodity_1h` score `-0.5545` n `88` status `ready` deltaP `-0.3062` edge `-0.0008` maxDD `-1.7935`
- `market_context_high->index_4h` score `-0.6421` n `88` status `ready` deltaP `2.4806` edge `-0.0011` maxDD `-2.4871`
- `market_context_high->commodity_4h` score `-0.8995` n `88` status `ready` deltaP `-2.536` edge `0.0122` maxDD `-4.182`
- `market_context_high->index_1h` score `-0.9769` n `88` status `ready` deltaP `-7.206` edge `0.0059` maxDD `-0.9814`
- `market_context_high->metal_4h` score `-0.9845` n `88` status `ready` deltaP `-0.4434` edge `0.0151` maxDD `-4.0688`
- `market_context_high->fx_1h` score `-1.2868` n `88` status `ready` deltaP `-13.6091` edge `-0.0058` maxDD `-0.8088`
- `market_context_high->equity_1h` score `-1.5894` n `88` status `ready` deltaP `-7.3557` edge `0.0299` maxDD `-8.1039`
- `market_context_high->crypto_alt_1h` score `-1.9389` n `88` status `ready` deltaP `0.4831` edge `-0.0539` maxDD `-10.8319`
- `market_context_high->fx_4h` score `-2.1099` n `88` status `ready` deltaP `-6.6103` edge `-0.0083` maxDD `-2.4506`
- `market_context_high->metal_24h` score `-2.1961` n `34` status `ready` deltaP `-4.6875` edge `-0.195` maxDD `-1.4245`
- `market_context_high->crypto_major_1h` score `-3.1822` n `88` status `ready` deltaP `-5.2599` edge `-0.1106` maxDD `-15.9848`
- `market_context_high->crypto_major_24h` score `-6.0103` n `34` status `ready` deltaP `-6.1785` edge `0.0034` maxDD `-30.3789`
- `market_context_high->equity_4h` score `-6.3644` n `88` status `ready` deltaP `-0.9146` edge `-0.1431` maxDD `-25.16`
- `market_context_high->crypto_alt_4h` score `-9.201` n `88` status `ready` deltaP `1.3304` edge `-0.2638` maxDD `-34.2787`
- `market_context_high->crypto_alt_24h` score `-11.1175` n `34` status `ready` deltaP `-22.2937` edge `-0.2684` maxDD `-33.4213`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
