# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-29T22:37:31.694020+00:00`
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

- `market_context_high->unknown_24h` score `1610.4014` n `134` status `ready` deltaP `-2.7908` edge `134.2617` maxDD `-1.1049`
- `market_context_high->unknown_4h` score `58.815` n `134` status `ready` deltaP `5.7517` edge `4.8762` maxDD `-0.3966`
- `market_context_high->index_24h` score `2.4465` n `134` status `ready` deltaP `29.1874` edge `0.0276` maxDD `-0.1315`
- `market_context_high->metal_1h` score `0.2878` n `134` status `ready` deltaP `9.706` edge `0.0101` maxDD `-0.3659`
- `market_context_high->commodity_4h` score `0.0683` n `134` status `ready` deltaP `11.6513` edge `0.0499` maxDD `-1.0837`
- `market_context_high->metal_4h` score `0.0492` n `134` status `ready` deltaP `12.6297` edge `0.0117` maxDD `-1.8344`
- `market_context_high->fx_1h` score `-0.1189` n `134` status `ready` deltaP `3.28` edge `-0.0013` maxDD `-0.1986`
- `market_context_high->crypto_major_1h` score `-0.2085` n `134` status `ready` deltaP `5.6685` edge `0.0476` maxDD `-5.2213`
- `market_context_high->equity_1h` score `-0.2502` n `134` status `ready` deltaP `2.3863` edge `0.0508` maxDD `-2.3383`
- `market_context_high->commodity_1h` score `-0.3715` n `134` status `ready` deltaP `1.0457` edge `0.0135` maxDD `-0.4475`
- `market_context_high->fx_4h` score `-0.5741` n `134` status `ready` deltaP `-1.3878` edge `-0.0045` maxDD `-0.4545`
- `market_context_high->crypto_alt_1h` score `-0.9218` n `134` status `ready` deltaP `2.6991` edge `0.0503` maxDD `-8.251`
- `market_context_high->index_1h` score `-0.9385` n `134` status `ready` deltaP `-3.1437` edge `-0.0014` maxDD `-1.1344`
- `market_context_high->equity_4h` score `-1.1734` n `134` status `ready` deltaP `-1.7246` edge `0.0195` maxDD `-6.008`
- `market_context_high->fx_24h` score `-1.2122` n `134` status `ready` deltaP `3.2779` edge `0.0102` maxDD `-0.9792`
- `market_context_high->metal_24h` score `-1.6085` n `134` status `ready` deltaP `3.9257` edge `0.0323` maxDD `-10.5088`
- `market_context_high->equity_24h` score `-1.6382` n `134` status `ready` deltaP `11.6242` edge `0.0617` maxDD `-14.0571`
- `market_context_high->crypto_major_4h` score `-2.2748` n `134` status `ready` deltaP `5.8746` edge `-0.0013` maxDD `-19.0267`
- `market_context_high->index_4h` score `-2.3571` n `134` status `ready` deltaP `-6.4343` edge `-0.0215` maxDD `-3.5621`
- `market_context_high->commodity_24h` score `-4.2576` n `134` status `ready` deltaP `3.1613` edge `-0.0079` maxDD `-24.0547`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
