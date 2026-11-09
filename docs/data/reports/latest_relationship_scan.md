# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-09T21:37:35.996782+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `104`

- Symbol pattern count: `9954`

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

- `market_context_high->unknown_4h` score `18.2157` n `88` status `ready` deltaP `7.043` edge `1.5158` maxDD `-0.9153`
- `market_context_high->equity_24h` score `13.6795` n `50` status `ready` deltaP `22.6863` edge `1.843` maxDD `-16.9034`
- `market_context_high->index_24h` score `2.4416` n `50` status `ready` deltaP `18.8076` edge `0.2339` maxDD `-2.3671`
- `market_context_high->metal_1h` score `-0.4156` n `88` status `ready` deltaP `3.1982` edge `0.0117` maxDD `-1.4122`
- `market_context_high->commodity_1h` score `-0.5942` n `88` status `ready` deltaP `-0.905` edge `-0.0019` maxDD `-1.7935`
- `market_context_high->metal_24h` score `-0.7885` n `50` status `ready` deltaP `8.1144` edge `-0.0645` maxDD `-1.4245`
- `market_context_high->index_4h` score `-0.8512` n `88` status `ready` deltaP `-0.026` edge `-0.0112` maxDD `-2.4871`
- `market_context_high->commodity_24h` score `-0.9205` n `50` status `ready` deltaP `-11.3934` edge `0.0967` maxDD `-5.1002`
- `market_context_high->commodity_4h` score `-0.9589` n `88` status `ready` deltaP `-3.3641` edge `0.0101` maxDD `-4.182`
- `market_context_high->metal_4h` score `-1.0877` n `88` status `ready` deltaP `-1.5878` edge `0.0095` maxDD `-4.0688`
- `market_context_high->index_1h` score `-1.1054` n `88` status `ready` deltaP `-9.3018` edge `0.0034` maxDD `-0.9814`
- `market_context_high->fx_1h` score `-1.3023` n `88` status `ready` deltaP `-13.9085` edge `-0.0058` maxDD `-0.8088`
- `market_context_high->fx_24h` score `-1.6558` n `50` status `ready` deltaP `-8.9255` edge `-0.0464` maxDD `-2.5102`
- `market_context_high->equity_1h` score `-1.7749` n `88` status `ready` deltaP `-8.4036` edge `0.0131` maxDD `-8.1039`
- `market_context_high->crypto_alt_1h` score `-1.9997` n `88` status `ready` deltaP `0.034` edge `-0.0587` maxDD `-10.8319`
- `market_context_high->fx_4h` score `-2.0748` n `88` status `ready` deltaP `-5.9205` edge `-0.0084` maxDD `-2.4506`
- `market_context_high->crypto_major_1h` score `-3.2414` n `88` status `ready` deltaP `-5.709` edge `-0.1152` maxDD `-15.9848`
- `market_context_high->crypto_alt_24h` score `-3.4779` n `50` status `ready` deltaP `2.3258` edge `0.2041` maxDD `-33.4213`
- `market_context_high->equity_4h` score `-7.4199` n `88` status `ready` deltaP `-2.6636` edge `-0.2194` maxDD `-25.16`
- `market_context_high->crypto_alt_4h` score `-9.2038` n `88` status `ready` deltaP `1.7002` edge `-0.2665` maxDD `-34.2787`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
