# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-30T21:37:31.439996+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `7058`

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

- `market_context_high->unknown_24h` score `1589.9811` n `134` status `ready` deltaP `-6.0894` edge `132.582` maxDD `-1.1049`
- `news_risk_high->unknown_1h` score `91.2871` n `80` status `ready` deltaP `-1.2725` edge `7.6283` maxDD `-0.3382`
- `market_context_high->unknown_4h` score `36.4222` n `134` status `ready` deltaP `0.4163` edge `3.0457` maxDD `-0.3966`
- `market_context_high->equity_24h` score `6.0689` n `134` status `ready` deltaP `16.6589` edge `0.6704` maxDD `-14.0571`
- `news_risk_high->crypto_alt_4h` score `5.1976` n `68` status `ready` deltaP `19.7722` edge `0.3674` maxDD `-3.6198`
- `market_context_high->index_24h` score `3.6526` n `134` status `ready` deltaP `35.2638` edge `0.0876` maxDD `-0.1315`
- `news_risk_high->crypto_alt_1h` score `0.7016` n `80` status `ready` deltaP `5.5913` edge `0.1041` maxDD `-3.9659`
- `market_context_high->commodity_4h` score `0.4208` n `134` status `ready` deltaP `15.1574` edge `0.0559` maxDD `-1.0837`
- `market_context_high->metal_1h` score `0.3984` n `134` status `ready` deltaP `11.0533` edge `0.0153` maxDD `-0.3659`
- `market_context_high->metal_4h` score `0.3951` n `134` status `ready` deltaP `15.9834` edge `0.0337` maxDD `-1.8344`
- `market_context_high->equity_1h` score `0.2821` n `134` status `ready` deltaP `5.0809` edge `0.0772` maxDD `-2.3383`
- `market_context_high->equity_4h` score `0.1306` n `134` status `ready` deltaP `2.6961` edge `0.1572` maxDD `-6.008`
- `market_context_high->crypto_major_1h` score `0.042` n `134` status `ready` deltaP `7.3152` edge `0.0575` maxDD `-5.2213`
- `market_context_high->fx_1h` score `-0.0699` n `134` status `ready` deltaP `4.1782` edge `-0.001` maxDD `-0.1986`
- `news_risk_high->commodity_4h` score `-0.1665` n `68` status `ready` deltaP `3.9634` edge `0.0257` maxDD `-2.5439`
- `market_context_high->commodity_1h` score `-0.1846` n `134` status `ready` deltaP `2.9918` edge `0.0161` maxDD `-0.4475`
- `market_context_high->fx_4h` score `-0.4816` n `134` status `ready` deltaP `0.1365` edge `-0.0028` maxDD `-0.4545`
- `market_context_high->index_1h` score `-0.7923` n `134` status `ready` deltaP `-1.6467` edge `0.0008` maxDD `-1.1344`
- `news_risk_high->commodity_1h` score `-0.7972` n `80` status `ready` deltaP `-6.5045` edge `0.003` maxDD `-1.6142`
- `market_context_high->metal_24h` score `-0.8504` n `134` status `ready` deltaP `3.9257` edge `0.1295` maxDD `-10.5088`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
