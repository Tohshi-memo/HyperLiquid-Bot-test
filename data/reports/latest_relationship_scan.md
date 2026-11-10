# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-10T15:52:33.992766+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `11430`

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

- `market_context_high->unknown_4h` score `54.5221` n `88` status `ready` deltaP `7.6774` edge `4.5371` maxDD `-0.9153`
- `market_context_high->equity_24h` score `34.721` n `88` status `ready` deltaP `33.0412` edge `2.9136` maxDD `-16.9034`
- `market_context_high->index_24h` score `5.4717` n `88` status `ready` deltaP `26.225` edge `0.3274` maxDD `-2.3671`
- `market_context_high->crypto_alt_24h` score `5.1243` n `88` status `ready` deltaP `24.8542` edge `1.0007` maxDD `-33.4213`
- `market_context_high->metal_24h` score `0.8416` n `88` status `ready` deltaP `20.1965` edge `-0.0092` maxDD `-1.4245`
- `market_context_high->metal_1h` score `-0.3281` n `88` status `ready` deltaP `4.0964` edge `0.013` maxDD `-1.4122`
- `market_context_high->commodity_1h` score `-0.4097` n `88` status `ready` deltaP `2.089` edge `0.0018` maxDD `-1.7935`
- `market_context_high->commodity_4h` score `-0.4663` n `88` status `ready` deltaP `3.4091` edge `0.0281` maxDD `-4.182`
- `market_context_high->index_4h` score `-0.5934` n `88` status `ready` deltaP `3.8525` edge `-0.004` maxDD `-2.4871`
- `market_context_high->index_1h` score `-0.9971` n `88` status `ready` deltaP `-7.5054` edge `0.0053` maxDD `-0.9814`
- `market_context_high->metal_4h` score `-1.0416` n `88` status `ready` deltaP `-0.5959` edge `0.0088` maxDD `-4.0688`
- `market_context_high->fx_1h` score `-1.2891` n `88` status `ready` deltaP `-13.7588` edge `-0.0051` maxDD `-0.8088`
- `market_context_high->equity_1h` score `-1.6136` n `88` status `ready` deltaP `-7.5054` edge `0.0278` maxDD `-8.1039`
- `market_context_high->crypto_alt_1h` score `-1.8664` n `88` status `ready` deltaP `1.2316` edge `-0.0496` maxDD `-10.8319`
- `market_context_high->fx_4h` score `-1.9017` n `88` status `ready` deltaP `-2.9518` edge `-0.006` maxDD `-2.4506`
- `market_context_high->fx_24h` score `-2.1378` n `88` status `ready` deltaP `-0.0867` edge `-0.0176` maxDD `-3.4642`
- `market_context_high->crypto_major_1h` score `-2.9445` n `88` status `ready` deltaP `-3.3138` edge `-0.0931` maxDD `-15.9848`
- `market_context_high->equity_4h` score `-6.3476` n `88` status `ready` deltaP `0.9146` edge `-0.1539` maxDD `-25.16`
- `market_context_high->crypto_alt_4h` score `-8.5739` n `88` status `ready` deltaP `3.7694` edge `-0.2278` maxDD `-34.2787`
- `market_context_high->commodity_24h` score `-9.2224` n `88` status `ready` deltaP `-23.4698` edge `-0.0597` maxDD `-25.5228`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
