# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-09T11:52:27.771988+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9226`

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

- `market_context_high->equity_24h` score `7.801` n `34` status `ready` deltaP `13.0005` edge `0.8007` maxDD `-16.6495`
- `market_context_high->commodity_24h` score `1.9404` n `34` status `ready` deltaP `4.1463` edge `0.1928` maxDD `-1.6995`
- `market_context_high->index_24h` score `1.0876` n `34` status `ready` deltaP `12.449` edge `0.1027` maxDD `-2.3671`
- `market_context_high->fx_24h` score `0.4775` n `34` status `ready` deltaP `8.5988` edge `-0.0069` maxDD `-0.1843`
- `market_context_high->metal_1h` score `-0.3173` n `88` status `ready` deltaP `4.2461` edge `0.0129` maxDD `-1.4122`
- `market_context_high->commodity_1h` score `-0.4556` n `88` status `ready` deltaP `0.8914` edge `0.0039` maxDD `-1.7935`
- `market_context_high->index_4h` score `-0.4744` n `88` status `ready` deltaP `4.3098` edge `0.0082` maxDD `-2.4871`
- `market_context_high->commodity_4h` score `-0.741` n `88` status `ready` deltaP `-1.4689` edge `0.0254` maxDD `-4.182`
- `market_context_high->index_1h` score `-0.8951` n `88` status `ready` deltaP `-6.0084` edge `0.0084` maxDD `-0.9814`
- `market_context_high->metal_4h` score `-0.9549` n `88` status `ready` deltaP `0.4712` edge `0.0128` maxDD `-4.0688`
- `market_context_high->equity_1h` score `-1.261` n `88` status `ready` deltaP `-6.0084` edge `0.062` maxDD `-8.0225`
- `market_context_high->fx_1h` score `-1.272` n `88` status `ready` deltaP `-13.3097` edge `-0.0059` maxDD `-0.8088`
- `market_context_high->crypto_alt_1h` score `-1.7916` n `88` status `ready` deltaP `1.531` edge `-0.042` maxDD `-10.8319`
- `market_context_high->metal_24h` score `-1.8112` n `34` status `ready` deltaP `-1.2153` edge `-0.1688` maxDD `-1.4245`
- `market_context_high->fx_4h` score `-2.1939` n `88` status `ready` deltaP `-8.1347` edge `-0.0089` maxDD `-2.4506`
- `market_context_high->crypto_major_1h` score `-3.063` n `88` status `ready` deltaP `-4.3617` edge `-0.1013` maxDD `-15.9848`
- `market_context_high->equity_4h` score `-4.6915` n `88` status `ready` deltaP `2.1341` edge `-0.0272` maxDD `-24.9053`
- `market_context_high->crypto_major_24h` score `-7.084` n `34` status `ready` deltaP `-6.6993` edge `-0.0826` maxDD `-30.3789`
- `market_context_high->crypto_alt_4h` score `-8.0783` n `88` status `ready` deltaP `3.7694` edge `-0.1865` maxDD `-34.2787`
- `market_context_high->crypto_alt_24h` score `-10.5541` n `34` status `ready` deltaP `-20.0368` edge `-0.2365` maxDD `-33.4213`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
