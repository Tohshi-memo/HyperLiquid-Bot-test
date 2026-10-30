# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-30T01:07:26.887481+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `6714`

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

- `market_context_high->unknown_24h` score `1645.5302` n `134` status `ready` deltaP `-2.7908` edge `137.1891` maxDD `-1.1049`
- `market_context_high->unknown_4h` score `41.4893` n `134` status `ready` deltaP `5.5993` edge `3.4334` maxDD `-0.3966`
- `market_context_high->index_24h` score `2.6718` n `134` status `ready` deltaP `30.9235` edge `0.0348` maxDD `-0.1315`
- `market_context_high->metal_1h` score `0.2808` n `134` status `ready` deltaP `9.5563` edge `0.0102` maxDD `-0.3659`
- `market_context_high->commodity_4h` score `0.1631` n `134` status `ready` deltaP `12.566` edge `0.0517` maxDD `-1.0837`
- `market_context_high->crypto_major_1h` score `0.0733` n `134` status `ready` deltaP `7.0158` edge `0.0621` maxDD `-5.2213`
- `market_context_high->metal_4h` score `0.0546` n `134` status `ready` deltaP `12.6297` edge `0.0124` maxDD `-1.8344`
- `market_context_high->equity_1h` score `-0.092` n `134` status `ready` deltaP `3.1348` edge `0.059` maxDD `-2.3383`
- `market_context_high->fx_1h` score `-0.1532` n `134` status `ready` deltaP `2.6812` edge `-0.0017` maxDD `-0.1986`
- `market_context_high->commodity_1h` score `-0.3271` n `134` status `ready` deltaP `1.4948` edge `0.0142` maxDD `-0.4475`
- `market_context_high->equity_24h` score `-0.4673` n `134` status `ready` deltaP `13.3603` edge `0.1477` maxDD `-14.0571`
- `market_context_high->fx_4h` score `-0.6073` n `134` status `ready` deltaP `-1.9976` edge `-0.0047` maxDD `-0.4545`
- `market_context_high->crypto_alt_1h` score `-0.7027` n `134` status `ready` deltaP `3.8967` edge `0.0704` maxDD `-8.251`
- `market_context_high->equity_4h` score `-0.7306` n `134` status `ready` deltaP `-0.2002` edge `0.0661` maxDD `-6.008`
- `market_context_high->index_1h` score `-0.8941` n `134` status `ready` deltaP `-2.6946` edge `-0.0007` maxDD `-1.1344`
- `market_context_high->fx_24h` score `-1.3696` n `134` status `ready` deltaP `1.7154` edge `0.0075` maxDD `-0.9792`
- `market_context_high->metal_24h` score `-1.5493` n `134` status `ready` deltaP `3.9257` edge `0.0399` maxDD `-10.5088`
- `market_context_high->crypto_major_4h` score `-1.7431` n `134` status `ready` deltaP `7.399` edge `0.0567` maxDD `-19.0267`
- `market_context_high->index_4h` score `-2.2017` n `134` status `ready` deltaP `-5.0624` edge `-0.0177` maxDD `-3.5621`
- `market_context_high->commodity_24h` score `-4.062` n `134` status `ready` deltaP `4.8974` edge `0.0056` maxDD `-24.0547`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
