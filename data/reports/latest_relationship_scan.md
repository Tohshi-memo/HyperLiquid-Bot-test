# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-10T03:29:22.839561+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `104`

- Symbol pattern count: `9940`

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

- `market_context_high->unknown_4h` score `37.7911` n `88` status `ready` deltaP `7.2201` edge `3.1459` maxDD `-0.9153`
- `market_context_high->equity_24h` score `21.6896` n `73` status `ready` deltaP `31.2719` edge `2.8127` maxDD `-16.9034`
- `market_context_high->index_24h` score `5.4673` n `73` status `ready` deltaP `25.3294` edge `0.333` maxDD `-2.3671`
- `market_context_high->crypto_alt_24h` score `2.5216` n `73` status `ready` deltaP `17.1031` edge `0.7187` maxDD `-33.4213`
- `market_context_high->metal_24h` score `0.0952` n `73` status `ready` deltaP `14.8405` edge `-0.0357` maxDD `-1.4245`
- `market_context_high->metal_1h` score `-0.3904` n `88` status `ready` deltaP `3.4976` edge `0.0118` maxDD `-1.4122`
- `market_context_high->commodity_1h` score `-0.5148` n `88` status `ready` deltaP `0.2926` edge `0.0003` maxDD `-1.7935`
- `market_context_high->commodity_4h` score `-0.737` n `88` status `ready` deltaP `-0.4019` edge `0.0188` maxDD `-4.182`
- `market_context_high->index_4h` score `-0.8264` n `88` status `ready` deltaP `0.3464` edge `-0.0105` maxDD `-2.4871`
- `market_context_high->index_1h` score `-1.0664` n `88` status `ready` deltaP `-8.703` edge `0.0044` maxDD `-0.9814`
- `market_context_high->metal_4h` score `-1.2039` n `88` status `ready` deltaP `-2.5776` edge `0.0012` maxDD `-4.0688`
- `market_context_high->fx_1h` score `-1.4121` n `88` status `ready` deltaP `-15.8546` edge `-0.0069` maxDD `-0.8088`
- `market_context_high->equity_1h` score `-1.7523` n `88` status `ready` deltaP `-8.5533` edge `0.017` maxDD `-8.1039`
- `market_context_high->crypto_alt_1h` score `-1.9483` n `88` status `ready` deltaP `0.6328` edge `-0.0561` maxDD `-10.8319`
- `market_context_high->fx_24h` score `-2.2018` n `73` status `ready` deltaP `-12.3169` edge `-0.0402` maxDD `-3.4642`
- `market_context_high->fx_4h` score `-2.2561` n `88` status `ready` deltaP `-8.8969` edge `-0.0118` maxDD `-2.4506`
- `market_context_high->crypto_major_1h` score `-3.1916` n `88` status `ready` deltaP `-5.2599` edge `-0.1118` maxDD `-15.9848`
- `market_context_high->commodity_24h` score `-3.9462` n `73` status `ready` deltaP `-19.5532` edge `-0.0056` maxDD `-15.9306`
- `market_context_high->equity_4h` score `-7.4751` n `88` status `ready` deltaP `-2.439` edge `-0.2255` maxDD `-25.16`
- `market_context_high->crypto_alt_4h` score `-9.105` n `88` status `ready` deltaP `2.245` edge `-0.2619` maxDD `-34.2787`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
