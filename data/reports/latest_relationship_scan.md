# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-10T18:55:22.084378+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `11724`

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

- `market_context_high->unknown_4h` score `52.3387` n `88` status `ready` deltaP `7.2201` edge `4.3582` maxDD `-0.9153`
- `market_context_high->equity_24h` score `35.0804` n `88` status `ready` deltaP `33.6489` edge `2.9395` maxDD `-16.9034`
- `market_context_high->crypto_alt_24h` score `5.9666` n `88` status `ready` deltaP `26.8624` edge `1.0953` maxDD `-33.4213`
- `market_context_high->index_24h` score `5.6858` n `88` status `ready` deltaP `28.0303` edge `0.3332` maxDD `-2.3671`
- `market_context_high->metal_24h` score `1.3599` n `88` status `ready` deltaP `22.1749` edge `0.0208` maxDD `-1.4245`
- `market_context_high->metal_1h` score `-0.3089` n `88` status `ready` deltaP `4.2461` edge `0.0136` maxDD `-1.4122`
- `market_context_high->commodity_1h` score `-0.4004` n `88` status `ready` deltaP `2.5381` edge `0.0` maxDD `-1.7935`
- `market_context_high->commodity_4h` score `-0.4942` n `88` status `ready` deltaP `3.5615` edge `0.0235` maxDD `-4.182`
- `market_context_high->index_4h` score `-0.565` n `88` status `ready` deltaP `4.1574` edge `-0.0024` maxDD `-2.4871`
- `market_context_high->index_1h` score `-0.9496` n `88` status `ready` deltaP `-6.7569` edge `0.0064` maxDD `-0.9814`
- `market_context_high->metal_4h` score `-1.011` n `88` status `ready` deltaP `-0.4434` edge `0.0117` maxDD `-4.0688`
- `market_context_high->fx_1h` score `-1.2478` n `88` status `ready` deltaP `-13.0103` edge `-0.0048` maxDD `-0.8088`
- `market_context_high->equity_1h` score `-1.4966` n `88` status `ready` deltaP `-6.7569` edge `0.0378` maxDD `-8.1039`
- `market_context_high->fx_4h` score `-1.7902` n `88` status `ready` deltaP `-1.1225` edge `-0.0039` maxDD `-2.4506`
- `market_context_high->crypto_alt_1h` score `-1.8017` n `88` status `ready` deltaP `1.3813` edge `-0.0423` maxDD `-10.8319`
- `market_context_high->fx_24h` score `-1.9277` n `88` status `ready` deltaP `1.9097` edge `-0.0134` maxDD `-3.4642`
- `market_context_high->crypto_major_1h` score `-2.8751` n `88` status `ready` deltaP `-3.0144` edge `-0.0862` maxDD `-15.9848`
- `market_context_high->equity_4h` score `-6.1055` n `88` status `ready` deltaP `1.6768` edge `-0.1388` maxDD `-25.16`
- `market_context_high->crypto_alt_4h` score `-8.2601` n `88` status `ready` deltaP `4.2267` edge `-0.2047` maxDD `-34.2787`
- `market_context_high->crypto_major_24h` score `-8.7552` n `88` status `ready` deltaP `3.6774` edge `0.4084` maxDD `-80.6681`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
