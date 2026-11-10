# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-10T02:07:26.355193+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `104`

- Symbol pattern count: `9966`

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

- `market_context_high->unknown_4h` score `37.4917` n `88` status `ready` deltaP `7.6774` edge `3.1179` maxDD `-0.9153`
- `market_context_high->equity_24h` score `21.2302` n `68` status `ready` deltaP `30.6275` edge `2.7581` maxDD `-16.9034`
- `market_context_high->index_24h` score `3.5305` n `68` status `ready` deltaP `24.9872` edge `0.3323` maxDD `-2.3671`
- `market_context_high->crypto_alt_24h` score `2.3732` n `68` status `ready` deltaP `16.2733` edge `0.7052` maxDD `-33.4213`
- `market_context_high->metal_24h` score `0.2387` n `68` status `ready` deltaP `13.9948` edge `-0.0181` maxDD `-1.4245`
- `market_context_high->metal_1h` score `-0.388` n `88` status `ready` deltaP `3.4976` edge `0.012` maxDD `-1.4122`
- `market_context_high->commodity_1h` score `-0.5343` n `88` status `ready` deltaP `-0.0068` edge `-0.0002` maxDD `-1.7935`
- `market_context_high->commodity_4h` score `-0.7954` n `88` status `ready` deltaP `-1.1641` edge `0.0164` maxDD `-4.182`
- `market_context_high->index_4h` score `-0.8256` n `88` status `ready` deltaP `0.3464` edge `-0.0104` maxDD `-2.4871`
- `market_context_high->index_1h` score `-1.0571` n `88` status `ready` deltaP `-8.5533` edge `0.0046` maxDD `-0.9814`
- `market_context_high->metal_4h` score `-1.1867` n `88` status `ready` deltaP `-2.5776` edge `0.0034` maxDD `-4.0688`
- `market_context_high->fx_1h` score `-1.3856` n `88` status `ready` deltaP `-15.4055` edge `-0.0065` maxDD `-0.8088`
- `market_context_high->equity_1h` score `-1.7375` n `88` status `ready` deltaP `-8.4036` edge `0.0179` maxDD `-8.1039`
- `market_context_high->crypto_alt_1h` score `-1.9257` n `88` status `ready` deltaP `0.7825` edge `-0.0542` maxDD `-10.8319`
- `market_context_high->fx_4h` score `-2.2197` n `88` status `ready` deltaP `-8.2871` edge `-0.0112` maxDD `-2.4506`
- `market_context_high->fx_24h` score `-2.4641` n `68` status `ready` deltaP `-16.4466` edge `-0.0463` maxDD `-3.4642`
- `market_context_high->crypto_major_1h` score `-3.1916` n `88` status `ready` deltaP `-5.2599` edge `-0.1118` maxDD `-15.9848`
- `market_context_high->commodity_24h` score `-3.192` n `68` status `ready` deltaP `-18.3326` edge `0.0219` maxDD `-12.7126`
- `market_context_high->equity_4h` score `-7.4067` n `88` status `ready` deltaP `-2.439` edge `-0.2198` maxDD `-25.16`
- `market_context_high->crypto_alt_4h` score `-9.1134` n `88` status `ready` deltaP `2.245` edge `-0.2626` maxDD `-34.2787`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
