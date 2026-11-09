# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-09T18:07:31.947482+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `104`

- Symbol pattern count: `10180`

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

- `market_context_high->equity_24h` score `5.3768` n `36` status `ready` deltaP `11.4583` edge `0.8534` maxDD `-16.9034`
- `market_context_high->index_24h` score `1.0376` n `36` status `ready` deltaP `10.2431` edge `0.111` maxDD `-2.3671`
- `market_context_high->commodity_24h` score `0.9766` n `36` status `ready` deltaP `1.0417` edge `0.177` maxDD `-1.6995`
- `market_context_high->fx_24h` score `0.2669` n `36` status `ready` deltaP `8.1597` edge `-0.0093` maxDD `-0.4949`
- `market_context_high->metal_1h` score `-0.2634` n `88` status `ready` deltaP `4.6952` edge `0.0144` maxDD `-1.4122`
- `market_context_high->commodity_1h` score `-0.5904` n `88` status `ready` deltaP `-0.7553` edge `-0.0024` maxDD `-1.7935`
- `market_context_high->index_4h` score `-0.7199` n `88` status `ready` deltaP `1.7184` edge `-0.006` maxDD `-2.4871`
- `market_context_high->commodity_4h` score `-0.9656` n `88` status `ready` deltaP `-3.2982` edge `0.0088` maxDD `-4.182`
- `market_context_high->metal_4h` score `-1.0049` n `88` status `ready` deltaP `-0.5959` edge `0.0135` maxDD `-4.0688`
- `market_context_high->index_1h` score `-1.0127` n `88` status `ready` deltaP `-7.8048` edge `0.0053` maxDD `-0.9814`
- `market_context_high->fx_1h` score `-1.2946` n `88` status `ready` deltaP `-13.7588` edge `-0.0058` maxDD `-0.8088`
- `market_context_high->equity_1h` score `-1.6377` n `88` status `ready` deltaP `-7.6551` edge `0.0257` maxDD `-8.1039`
- `market_context_high->crypto_alt_1h` score `-1.9584` n `88` status `ready` deltaP `0.4831` edge `-0.0564` maxDD `-10.8319`
- `market_context_high->metal_24h` score `-2.0142` n `36` status `ready` deltaP `-2.7778` edge `-0.1844` maxDD `-1.4245`
- `market_context_high->fx_4h` score `-2.102` n `88` status `ready` deltaP `-6.4579` edge `-0.0083` maxDD `-2.4506`
- `market_context_high->crypto_major_1h` score `-3.197` n `88` status `ready` deltaP `-5.2599` edge `-0.1125` maxDD `-15.9848`
- `market_context_high->equity_4h` score `-6.9629` n `88` status `ready` deltaP `-1.6768` edge `-0.1879` maxDD `-25.16`
- `market_context_high->crypto_major_24h` score `-7.5655` n `36` status `ready` deltaP `-6.9444` edge `-0.0535` maxDD `-35.1198`
- `market_context_high->crypto_alt_4h` score `-9.3902` n `88` status `ready` deltaP `0.7206` edge `-0.2755` maxDD `-34.2787`
- `market_context_high->crypto_alt_24h` score `-9.7365` n `36` status `ready` deltaP `-18.5764` edge `-0.1781` maxDD `-33.4213`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
