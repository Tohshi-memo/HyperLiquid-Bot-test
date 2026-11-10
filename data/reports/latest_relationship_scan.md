# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-10T04:52:27.682149+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `11538`

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

- `market_context_high->unknown_4h` score `37.8803` n `88` status `ready` deltaP `7.525` edge `3.1513` maxDD `-0.9153`
- `market_context_high->equity_24h` score `33.7307` n `79` status `ready` deltaP `31.7926` edge `2.8394` maxDD `-16.9034`
- `market_context_high->index_24h` score `5.4204` n `79` status `ready` deltaP `25.538` edge `0.3277` maxDD `-2.3671`
- `market_context_high->crypto_alt_24h` score `2.9179` n `79` status `ready` deltaP `19.323` edge `0.7547` maxDD `-33.4213`
- `market_context_high->metal_24h` score `-0.1093` n `79` status `ready` deltaP `15.5694` edge `-0.0576` maxDD `-1.4245`
- `market_context_high->metal_1h` score `-0.43` n `88` status `ready` deltaP `3.1982` edge `0.0105` maxDD `-1.4122`
- `market_context_high->commodity_1h` score `-0.5031` n `88` status `ready` deltaP `0.4423` edge `0.0008` maxDD `-1.7935`
- `market_context_high->commodity_4h` score `-0.6528` n `88` status `ready` deltaP `0.5128` edge `0.0235` maxDD `-4.182`
- `market_context_high->index_4h` score `-0.8264` n `88` status `ready` deltaP `0.3464` edge `-0.0105` maxDD `-2.4871`
- `market_context_high->index_1h` score `-1.075` n `88` status `ready` deltaP `-8.8527` edge `0.0043` maxDD `-0.9814`
- `market_context_high->metal_4h` score `-1.2416` n `88` status `ready` deltaP `-2.8825` edge `-0.0016` maxDD `-4.0688`
- `market_context_high->fx_1h` score `-1.3872` n `88` status `ready` deltaP `-15.4055` edge `-0.0067` maxDD `-0.8088`
- `market_context_high->equity_1h` score `-1.778` n `88` status `ready` deltaP `-8.8527` edge `0.0157` maxDD `-8.1039`
- `market_context_high->crypto_alt_1h` score `-1.967` n `88` status `ready` deltaP `0.4831` edge `-0.0575` maxDD `-10.8319`
- `market_context_high->fx_4h` score `-2.2228` n `88` status `ready` deltaP `-8.2871` edge `-0.0116` maxDD `-2.4506`
- `market_context_high->fx_24h` score `-2.9825` n `79` status `ready` deltaP `-8.0512` edge `-0.0349` maxDD `-3.4642`
- `market_context_high->crypto_major_1h` score `-3.1916` n `88` status `ready` deltaP `-5.2599` edge `-0.1118` maxDD `-15.9848`
- `market_context_high->commodity_24h` score `-5.0201` n `79` status `ready` deltaP `-21.53` edge `-0.0456` maxDD `-20.6908`
- `market_context_high->equity_4h` score `-7.4967` n `88` status `ready` deltaP `-2.439` edge `-0.2273` maxDD `-25.16`
- `market_context_high->crypto_alt_4h` score `-9.1534` n `88` status `ready` deltaP `1.9402` edge `-0.2639` maxDD `-34.2787`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
