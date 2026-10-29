# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-29T22:07:28.035244+00:00`
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

- `market_context_high->unknown_24h` score `1611.664` n `134` status `ready` deltaP `-2.4435` edge `134.3646` maxDD `-1.1049`
- `market_context_high->unknown_4h` score `59.6286` n `134` status `ready` deltaP `5.7517` edge `4.944` maxDD `-0.3966`
- `market_context_high->index_24h` score `2.4055` n `134` status `ready` deltaP `28.8402` edge `0.0265` maxDD `-0.1315`
- `market_context_high->metal_1h` score `0.3042` n `134` status `ready` deltaP `10.0054` edge `0.0102` maxDD `-0.3659`
- `market_context_high->metal_4h` score `0.0697` n `134` status `ready` deltaP `12.9346` edge `0.0123` maxDD `-1.8344`
- `market_context_high->commodity_4h` score `0.0502` n `134` status `ready` deltaP `11.4989` edge `0.0494` maxDD `-1.0837`
- `market_context_high->fx_1h` score `-0.1182` n `134` status `ready` deltaP `3.28` edge `-0.0012` maxDD `-0.1986`
- `market_context_high->crypto_major_1h` score `-0.2265` n `134` status `ready` deltaP `5.6685` edge `0.0461` maxDD `-5.2213`
- `market_context_high->equity_1h` score `-0.2538` n `134` status `ready` deltaP `2.3863` edge `0.0505` maxDD `-2.3383`
- `market_context_high->commodity_1h` score `-0.3595` n `134` status `ready` deltaP `1.1954` edge `0.0135` maxDD `-0.4475`
- `market_context_high->fx_4h` score `-0.5567` n `134` status `ready` deltaP `-1.083` edge `-0.0043` maxDD `-0.4545`
- `market_context_high->crypto_alt_1h` score `-0.9382` n `134` status `ready` deltaP `2.6991` edge `0.0482` maxDD `-8.251`
- `market_context_high->index_1h` score `-0.9385` n `134` status `ready` deltaP `-3.1437` edge `-0.0014` maxDD `-1.1344`
- `market_context_high->fx_24h` score `-1.1797` n `134` status `ready` deltaP `3.6251` edge `0.0106` maxDD `-0.9792`
- `market_context_high->equity_4h` score `-1.2516` n `134` status `ready` deltaP `-2.0295` edge `0.0115` maxDD `-6.008`
- `market_context_high->metal_24h` score `-1.6187` n `134` status `ready` deltaP `3.9257` edge `0.031` maxDD `-10.5088`
- `market_context_high->equity_24h` score `-1.8544` n `134` status `ready` deltaP `11.277` edge `0.046` maxDD `-14.0571`
- `market_context_high->index_4h` score `-2.3607` n `134` status `ready` deltaP `-6.4343` edge `-0.0218` maxDD `-3.5621`
- `market_context_high->crypto_major_4h` score `-2.3647` n `134` status `ready` deltaP `5.5698` edge `-0.0108` maxDD `-19.0267`
- `market_context_high->commodity_24h` score `-4.2951` n `134` status `ready` deltaP `2.8141` edge `-0.0104` maxDD `-24.0547`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
