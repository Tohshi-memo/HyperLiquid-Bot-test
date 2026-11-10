# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-10T03:07:30.014061+00:00`
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

- `market_context_high->unknown_4h` score `37.7875` n `88` status `ready` deltaP `7.2201` edge `3.1456` maxDD `-0.9153`
- `market_context_high->equity_24h` score `21.6089` n `72` status `ready` deltaP `31.1598` edge `2.8031` maxDD `-16.9034`
- `market_context_high->index_24h` score `5.4617` n `72` status `ready` deltaP `25.2744` edge `0.3329` maxDD `-2.3671`
- `market_context_high->crypto_alt_24h` score `2.4354` n `72` status `ready` deltaP `16.5704` edge `0.7112` maxDD `-33.4213`
- `market_context_high->metal_24h` score `0.118` n `72` status `ready` deltaP `14.6905` edge `-0.0328` maxDD `-1.4245`
- `market_context_high->metal_1h` score `-0.3892` n `88` status `ready` deltaP `3.4976` edge `0.0119` maxDD `-1.4122`
- `market_context_high->commodity_1h` score `-0.5242` n `88` status `ready` deltaP `0.1429` edge `0.0001` maxDD `-1.7935`
- `market_context_high->commodity_4h` score `-0.7496` n `88` status `ready` deltaP `-0.5543` edge `0.0182` maxDD `-4.182`
- `market_context_high->index_4h` score `-0.8264` n `88` status `ready` deltaP `0.3464` edge `-0.0105` maxDD `-2.4871`
- `market_context_high->index_1h` score `-1.0664` n `88` status `ready` deltaP `-8.703` edge `0.0044` maxDD `-0.9814`
- `market_context_high->metal_4h` score `-1.2008` n `88` status `ready` deltaP `-2.5776` edge `0.0016` maxDD `-4.0688`
- `market_context_high->fx_1h` score `-1.4113` n `88` status `ready` deltaP `-15.8546` edge `-0.0068` maxDD `-0.8088`
- `market_context_high->equity_1h` score `-1.7515` n `88` status `ready` deltaP `-8.5533` edge `0.0171` maxDD `-8.1039`
- `market_context_high->crypto_alt_1h` score `-1.9358` n `88` status `ready` deltaP `0.7825` edge `-0.0555` maxDD `-10.8319`
- `market_context_high->fx_24h` score `-2.2486` n `72` status `ready` deltaP `-13.0969` edge `-0.041` maxDD `-3.4642`
- `market_context_high->fx_4h` score `-2.2561` n `88` status `ready` deltaP `-8.8969` edge `-0.0118` maxDD `-2.4506`
- `market_context_high->crypto_major_1h` score `-3.1916` n `88` status `ready` deltaP `-5.2599` edge `-0.1118` maxDD `-15.9848`
- `market_context_high->commodity_24h` score `-3.7675` n `72` status `ready` deltaP `-19.1917` edge `0.0012` maxDD `-15.1683`
- `market_context_high->equity_4h` score `-7.4607` n `88` status `ready` deltaP `-2.439` edge `-0.2243` maxDD `-25.16`
- `market_context_high->crypto_alt_4h` score `-9.105` n `88` status `ready` deltaP `2.245` edge `-0.2619` maxDD `-34.2787`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
