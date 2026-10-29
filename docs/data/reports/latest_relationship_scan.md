# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-29T23:52:28.385951+00:00`
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

- `market_context_high->unknown_24h` score `1628.0402` n `134` status `ready` deltaP `-2.7908` edge `135.7316` maxDD `-1.1049`
- `market_context_high->unknown_4h` score `53.8098` n `134` status `ready` deltaP `5.7517` edge `4.4591` maxDD `-0.3966`
- `market_context_high->index_24h` score `2.5519` n `134` status `ready` deltaP `30.0554` edge `0.0306` maxDD `-0.1315`
- `market_context_high->metal_1h` score `0.28` n `134` status `ready` deltaP `9.5563` edge `0.0101` maxDD `-0.3659`
- `market_context_high->commodity_4h` score `0.0877` n `134` status `ready` deltaP `11.8038` edge `0.0505` maxDD `-1.0837`
- `market_context_high->metal_4h` score `0.0499` n `134` status `ready` deltaP `12.6297` edge `0.0118` maxDD `-1.8344`
- `market_context_high->crypto_major_1h` score `-0.109` n `134` status `ready` deltaP `6.2673` edge `0.0519` maxDD `-5.2213`
- `market_context_high->fx_1h` score `-0.1446` n `134` status `ready` deltaP `2.8309` edge `-0.0016` maxDD `-0.1986`
- `market_context_high->equity_1h` score `-0.2299` n `134` status `ready` deltaP `2.536` edge `0.0515` maxDD `-2.3383`
- `market_context_high->commodity_1h` score `-0.3463` n `134` status `ready` deltaP `1.3451` edge `0.0136` maxDD `-0.4475`
- `market_context_high->fx_4h` score `-0.6073` n `134` status `ready` deltaP `-1.9976` edge `-0.0047` maxDD `-0.4545`
- `market_context_high->crypto_alt_1h` score `-0.868` n `134` status `ready` deltaP `3.1482` edge `0.0542` maxDD `-8.251`
- `market_context_high->equity_4h` score `-0.9262` n `134` status `ready` deltaP `-0.9624` edge `0.0461` maxDD `-6.008`
- `market_context_high->index_1h` score `-0.9409` n `134` status `ready` deltaP `-3.1437` edge `-0.0016` maxDD `-1.1344`
- `market_context_high->equity_24h` score `-1.0828` n `134` status `ready` deltaP `12.4923` edge `0.1022` maxDD `-14.0571`
- `market_context_high->fx_24h` score `-1.2949` n `134` status `ready` deltaP `2.4098` edge `0.0091` maxDD `-0.9792`
- `market_context_high->metal_24h` score `-1.5805` n `134` status `ready` deltaP `3.9257` edge `0.0359` maxDD `-10.5088`
- `market_context_high->crypto_major_4h` score `-1.9863` n `134` status `ready` deltaP `6.6368` edge `0.0306` maxDD `-19.0267`
- `market_context_high->index_4h` score `-2.2855` n `134` status `ready` deltaP `-5.8246` edge `-0.0196` maxDD `-3.5621`
- `market_context_high->commodity_24h` score `-4.1625` n `134` status `ready` deltaP `4.0293` edge `-0.0015` maxDD `-24.0547`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
