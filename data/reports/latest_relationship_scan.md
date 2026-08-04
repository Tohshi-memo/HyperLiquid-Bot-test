# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-04T02:22:25.024170+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `64`

- Symbol pattern count: `7932`

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

- `market_context_high->unknown_24h` score `37.3839` n `46` status `ready` deltaP `26.2983` edge `2.9443` maxDD `-0.0103`
- `market_context_high->crypto_alt_24h` score `10.1942` n `46` status `ready` deltaP `47.4714` edge `0.5504` maxDD `-0.3889`
- `market_context_high->unknown_4h` score `9.2332` n `78` status `ready` deltaP `8.0128` edge `0.7634` maxDD `-1.4578`
- `market_context_high->commodity_24h` score `8.4316` n `46` status `ready` deltaP `39.9985` edge `0.4539` maxDD `-0.434`
- `news_risk_high->fx_24h` score `1.0289` n `31` status `ready` deltaP `12.192` edge `0.0697` maxDD `-1.5526`
- `market_context_high->commodity_4h` score `0.9825` n `78` status `ready` deltaP `13.1254` edge `0.079` maxDD `-2.7703`
- `news_risk_high->commodity_1h` score `0.8298` n `31` status `ready` deltaP `18.3407` edge `0.0053` maxDD `-0.6947`
- `market_context_high->fx_1h` score `0.3137` n `88` status `ready` deltaP `9.4788` edge `-0.0022` maxDD `-0.7878`
- `market_context_high->commodity_1h` score `0.2948` n `88` status `ready` deltaP `6.2806` edge `0.0243` maxDD `-1.3282`
- `market_context_high->fx_4h` score `0.2654` n `78` status `ready` deltaP `16.7136` edge `0.0086` maxDD `-1.8797`
- `news_risk_high->fx_4h` score `0.0584` n `31` status `ready` deltaP `3.5209` edge `0.0343` maxDD `-0.356`
- `news_risk_high->index_1h` score `-0.2089` n `31` status `ready` deltaP `0.198` edge `-0.0083` maxDD `-0.5845`
- `news_risk_high->crypto_alt_1h` score `-0.2227` n `31` status `ready` deltaP `9.943` edge `-0.0308` maxDD `-3.1233`
- `news_risk_high->commodity_4h` score `-0.283` n `31` status `ready` deltaP `8.3694` edge `-0.0293` maxDD `-1.6728`
- `news_risk_high->index_4h` score `-0.2925` n `31` status `ready` deltaP `-3.7225` edge `0.0385` maxDD `-0.3783`
- `news_risk_high->fx_1h` score `-0.3478` n `31` status `ready` deltaP `-2.3614` edge `0.0023` maxDD `-0.1588`
- `market_context_high->index_1h` score `-0.4281` n `88` status `ready` deltaP `2.1775` edge `-0.016` maxDD `-1.6054`
- `news_risk_high->unknown_4h` score `-0.4761` n `31` status `ready` deltaP `-1.2097` edge `-0.0041` maxDD `-1.5766`
- `market_context_high->metal_1h` score `-0.4903` n `88` status `ready` deltaP `-0.871` edge `-0.0076` maxDD `-1.6224`
- `news_risk_high->equity_4h` score `-0.7878` n `31` status `ready` deltaP `-16.9305` edge `0.1168` maxDD `-2.8999`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
