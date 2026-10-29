# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-29T16:52:35.920496+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `6816`

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

- `market_context_high->unknown_24h` score `1622.7515` n `134` status `ready` deltaP `0.1606` edge `135.2712` maxDD `-1.1049`
- `market_context_high->unknown_4h` score `66.1186` n `134` status `ready` deltaP `6.9712` edge `5.4767` maxDD `-0.3966`
- `market_context_high->index_24h` score `2.0029` n `134` status `ready` deltaP `25.3679` edge `0.0161` maxDD `-0.1315`
- `market_context_high->metal_1h` score `0.3376` n `134` status `ready` deltaP `10.6042` edge `0.0105` maxDD `-0.3659`
- `market_context_high->commodity_4h` score `0.2331` n `134` status `ready` deltaP `12.8708` edge `0.0555` maxDD `-1.0837`
- `market_context_high->metal_4h` score `0.1036` n `134` status `ready` deltaP `13.3919` edge `0.0136` maxDD `-1.8344`
- `market_context_high->fx_1h` score `-0.0855` n `134` status `ready` deltaP `3.8788` edge `-0.001` maxDD `-0.1986`
- `market_context_high->commodity_1h` score `-0.3283` n `134` status `ready` deltaP `1.4948` edge `0.0141` maxDD `-0.4475`
- `market_context_high->fx_4h` score `-0.3906` n `134` status `ready` deltaP `1.6609` edge `-0.0013` maxDD `-0.4545`
- `market_context_high->equity_1h` score `-0.5261` n `134` status `ready` deltaP `1.4881` edge `0.0338` maxDD `-2.3383`
- `market_context_high->crypto_major_1h` score `-0.5923` n `134` status `ready` deltaP `4.6206` edge `0.0226` maxDD `-5.2213`
- `market_context_high->fx_24h` score `-0.8455` n `134` status `ready` deltaP `7.0973` edge `0.0153` maxDD `-0.9792`
- `market_context_high->index_1h` score `-1.0008` n `134` status `ready` deltaP `-3.7425` edge `-0.0026` maxDD `-1.1344`
- `market_context_high->crypto_alt_1h` score `-1.2789` n `134` status `ready` deltaP `1.3518` edge `0.0135` maxDD `-8.251`
- `market_context_high->equity_4h` score `-1.5821` n `134` status `ready` deltaP `-2.6392` edge `-0.0268` maxDD `-6.008`
- `market_context_high->metal_24h` score `-1.7302` n `134` status `ready` deltaP `3.9257` edge `0.0167` maxDD `-10.5088`
- `market_context_high->index_4h` score `-2.4504` n `134` status `ready` deltaP `-7.1965` edge `-0.0242` maxDD `-3.5621`
- `market_context_high->crypto_major_4h` score `-2.7534` n `134` status `ready` deltaP `4.3502` edge `-0.0525` maxDD `-19.0267`
- `market_context_high->equity_24h` score `-3.6089` n `134` status `ready` deltaP `7.6312` edge `-0.0759` maxDD `-14.0571`
- `market_context_high->commodity_24h` score `-4.7015` n `134` status `ready` deltaP `-0.8318` edge `-0.0382` maxDD `-24.0547`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
