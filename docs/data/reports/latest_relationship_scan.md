# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-10T16:37:38.310221+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `11440`

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

- `market_context_high->unknown_4h` score `53.4019` n `88` status `ready` deltaP `7.2201` edge `4.4468` maxDD `-0.9153`
- `market_context_high->equity_24h` score `34.8694` n `88` status `ready` deltaP `33.5611` edge `2.9225` maxDD `-16.9034`
- `market_context_high->index_24h` score `5.5289` n `88` status `ready` deltaP `26.7449` edge `0.3287` maxDD `-2.3671`
- `market_context_high->crypto_alt_24h` score `5.3565` n `88` status `ready` deltaP `25.3742` edge `1.027` maxDD `-33.4213`
- `market_context_high->metal_24h` score `0.9696` n `88` status `ready` deltaP `20.7165` edge `-0.002` maxDD `-1.4245`
- `market_context_high->metal_1h` score `-0.3077` n `88` status `ready` deltaP `4.2461` edge `0.0137` maxDD `-1.4122`
- `market_context_high->commodity_1h` score `-0.4183` n `88` status `ready` deltaP `2.089` edge `0.0007` maxDD `-1.7935`
- `market_context_high->commodity_4h` score `-0.4615` n `88` status `ready` deltaP `3.5615` edge `0.0277` maxDD `-4.182`
- `market_context_high->index_4h` score `-0.591` n `88` status `ready` deltaP `3.8525` edge `-0.0037` maxDD `-2.4871`
- `market_context_high->index_1h` score `-0.9769` n `88` status `ready` deltaP `-7.206` edge `0.0059` maxDD `-0.9814`
- `market_context_high->metal_4h` score `-1.0353` n `88` status `ready` deltaP `-0.5959` edge `0.0096` maxDD `-4.0688`
- `market_context_high->fx_1h` score `-1.272` n `88` status `ready` deltaP `-13.4594` edge `-0.0049` maxDD `-0.8088`
- `market_context_high->equity_1h` score `-1.5535` n `88` status `ready` deltaP `-7.206` edge `0.0335` maxDD `-8.1039`
- `market_context_high->crypto_alt_1h` score `-1.7916` n `88` status `ready` deltaP `1.531` edge `-0.042` maxDD `-10.8319`
- `market_context_high->fx_4h` score `-1.8725` n `88` status `ready` deltaP `-2.4945` edge `-0.0053` maxDD `-2.4506`
- `market_context_high->fx_24h` score `-2.0806` n `88` status `ready` deltaP `0.4333` edge `-0.0163` maxDD `-3.4642`
- `market_context_high->crypto_major_1h` score `-2.865` n `88` status `ready` deltaP `-3.0144` edge `-0.0849` maxDD `-15.9848`
- `market_context_high->equity_4h` score `-6.32` n `88` status `ready` deltaP `0.9146` edge `-0.1516` maxDD `-25.16`
- `market_context_high->crypto_alt_4h` score `-8.5053` n `88` status `ready` deltaP `3.9219` edge `-0.2231` maxDD `-34.2787`
- `market_context_high->commodity_24h` score `-9.2272` n `88` status `ready` deltaP `-23.4698` edge `-0.0601` maxDD `-25.5228`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
