# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-10T03:52:24.496040+00:00`
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

- `market_context_high->unknown_4h` score `37.8559` n `88` status `ready` deltaP `7.2201` edge `3.1513` maxDD `-0.9153`
- `market_context_high->equity_24h` score `33.4171` n `75` status `ready` deltaP `31.4731` edge `2.8154` maxDD `-16.9034`
- `market_context_high->index_24h` score `5.4434` n `75` status `ready` deltaP `25.4211` edge `0.3304` maxDD `-2.3671`
- `market_context_high->crypto_alt_24h` score `2.6142` n `75` status `ready` deltaP `17.9527` edge `0.7249` maxDD `-33.4213`
- `market_context_high->metal_24h` score `0.0259` n `75` status `ready` deltaP `15.1149` edge `-0.0433` maxDD `-1.4245`
- `market_context_high->metal_1h` score `-0.3952` n `88` status `ready` deltaP `3.4976` edge `0.0114` maxDD `-1.4122`
- `market_context_high->commodity_1h` score `-0.4961` n `88` status `ready` deltaP `0.592` edge `0.0007` maxDD `-1.7935`
- `market_context_high->commodity_4h` score `-0.7126` n `88` status `ready` deltaP `-0.097` edge `0.0199` maxDD `-4.182`
- `market_context_high->index_4h` score `-0.8256` n `88` status `ready` deltaP `0.3464` edge `-0.0104` maxDD `-2.4871`
- `market_context_high->index_1h` score `-1.0571` n `88` status `ready` deltaP `-8.5533` edge `0.0046` maxDD `-0.9814`
- `market_context_high->metal_4h` score `-1.2093` n `88` status `ready` deltaP `-2.5776` edge `0.0005` maxDD `-4.0688`
- `market_context_high->fx_1h` score `-1.4036` n `88` status `ready` deltaP `-15.7049` edge `-0.0068` maxDD `-0.8088`
- `market_context_high->equity_1h` score `-1.7476` n `88` status `ready` deltaP `-8.5533` edge `0.0176` maxDD `-8.1039`
- `market_context_high->crypto_alt_1h` score `-1.9561` n `88` status `ready` deltaP `0.6328` edge `-0.0571` maxDD `-10.8319`
- `market_context_high->fx_24h` score `-2.1107` n `75` status `ready` deltaP `-10.8192` edge `-0.0385` maxDD `-3.4642`
- `market_context_high->fx_4h` score `-2.2561` n `88` status `ready` deltaP `-8.8969` edge `-0.0118` maxDD `-2.4506`
- `market_context_high->crypto_major_1h` score `-3.1939` n `88` status `ready` deltaP `-5.2599` edge `-0.1121` maxDD `-15.9848`
- `market_context_high->commodity_24h` score `-4.3064` n `75` status `ready` deltaP `-20.2473` edge `-0.0194` maxDD `-17.4845`
- `market_context_high->equity_4h` score `-7.4823` n `88` status `ready` deltaP `-2.439` edge `-0.2261` maxDD `-25.16`
- `market_context_high->crypto_alt_4h` score `-9.111` n `88` status `ready` deltaP `2.245` edge `-0.2624` maxDD `-34.2787`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
