# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-10T15:37:45.013265+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `11460`

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

- `market_context_high->unknown_4h` score `54.5461` n `88` status `ready` deltaP `7.6774` edge `4.5391` maxDD `-0.9153`
- `market_context_high->equity_24h` score `34.6747` n `88` status `ready` deltaP `32.8678` edge `2.9109` maxDD `-16.9034`
- `market_context_high->index_24h` score `5.4531` n `88` status `ready` deltaP `26.0516` edge `0.327` maxDD `-2.3671`
- `market_context_high->crypto_alt_24h` score `5.0701` n `88` status `ready` deltaP `24.6809` edge `0.9949` maxDD `-33.4213`
- `market_context_high->metal_24h` score `0.8026` n `88` status `ready` deltaP `20.0232` edge `-0.0113` maxDD `-1.4245`
- `market_context_high->metal_1h` score `-0.3125` n `88` status `ready` deltaP `4.2461` edge `0.0133` maxDD `-1.4122`
- `market_context_high->commodity_1h` score `-0.4105` n `88` status `ready` deltaP `2.089` edge `0.0017` maxDD `-1.7935`
- `market_context_high->commodity_4h` score `-0.4766` n `88` status `ready` deltaP `3.2567` edge `0.0278` maxDD `-4.182`
- `market_context_high->index_4h` score `-0.6021` n `88` status `ready` deltaP `3.7001` edge `-0.0041` maxDD `-2.4871`
- `market_context_high->index_1h` score `-0.9979` n `88` status `ready` deltaP `-7.5054` edge `0.0052` maxDD `-0.9814`
- `market_context_high->metal_4h` score `-1.0416` n `88` status `ready` deltaP `-0.5959` edge `0.0088` maxDD `-4.0688`
- `market_context_high->fx_1h` score `-1.2984` n `88` status `ready` deltaP `-13.9085` edge `-0.0053` maxDD `-0.8088`
- `market_context_high->equity_1h` score `-1.6307` n `88` status `ready` deltaP `-7.6551` edge `0.0266` maxDD `-8.1039`
- `market_context_high->crypto_alt_1h` score `-1.882` n `88` status `ready` deltaP `1.2316` edge `-0.0516` maxDD `-10.8319`
- `market_context_high->fx_4h` score `-1.9112` n `88` status `ready` deltaP `-3.1042` edge `-0.0062` maxDD `-2.4506`
- `market_context_high->fx_24h` score `-2.1564` n `88` status `ready` deltaP `-0.26` edge `-0.018` maxDD `-3.4642`
- `market_context_high->crypto_major_1h` score `-2.9625` n `88` status `ready` deltaP `-3.3138` edge `-0.0954` maxDD `-15.9848`
- `market_context_high->equity_4h` score `-6.3814` n `88` status `ready` deltaP `0.7622` edge `-0.1557` maxDD `-25.16`
- `market_context_high->crypto_alt_4h` score `-8.604` n `88` status `ready` deltaP `3.617` edge `-0.2293` maxDD `-34.2787`
- `market_context_high->commodity_24h` score `-9.2236` n `88` status `ready` deltaP `-23.4698` edge `-0.0598` maxDD `-25.5228`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
