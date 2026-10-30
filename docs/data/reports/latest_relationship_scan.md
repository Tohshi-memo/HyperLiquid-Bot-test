# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-30T20:52:38.735986+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `6994`

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

- `market_context_high->unknown_24h` score `1590.0567` n `134` status `ready` deltaP `-6.0894` edge `132.5883` maxDD `-1.1049`
- `news_risk_high->unknown_1h` score `103.7744` n `77` status `ready` deltaP `-0.3111` edge `8.6625` maxDD `-0.3382`
- `market_context_high->unknown_4h` score `36.3154` n `134` status `ready` deltaP `0.4163` edge `3.0368` maxDD `-0.3966`
- `market_context_high->equity_24h` score `5.8841` n `134` status `ready` deltaP `16.6589` edge `0.655` maxDD `-14.0571`
- `news_risk_high->crypto_alt_4h` score `5.1514` n `65` status `ready` deltaP `18.9399` edge `0.3691` maxDD `-3.6198`
- `market_context_high->index_24h` score `3.637` n `134` status `ready` deltaP `35.2638` edge `0.0863` maxDD `-0.1315`
- `news_risk_high->crypto_alt_1h` score `0.5527` n `77` status `ready` deltaP `5.2901` edge `0.0937` maxDD `-3.9659`
- `market_context_high->metal_4h` score `0.4046` n `134` status `ready` deltaP `16.1358` edge `0.0339` maxDD `-1.8344`
- `market_context_high->metal_1h` score `0.3977` n `134` status `ready` deltaP `11.0533` edge `0.0152` maxDD `-0.3659`
- `market_context_high->commodity_4h` score `0.3555` n `134` status `ready` deltaP `14.7001` edge `0.0535` maxDD `-1.0837`
- `market_context_high->equity_1h` score `0.2965` n `134` status `ready` deltaP `5.2306` edge `0.0774` maxDD `-2.3383`
- `news_risk_high->commodity_4h` score `0.2791` n `65` status `ready` deltaP `5.8138` edge `0.0426` maxDD `-1.3132`
- `market_context_high->equity_4h` score `0.1902` n `134` status `ready` deltaP `3.1534` edge `0.1618` maxDD `-6.008`
- `market_context_high->crypto_major_1h` score `0.0732` n `134` status `ready` deltaP `7.6146` edge `0.0581` maxDD `-5.2213`
- `market_context_high->fx_1h` score `-0.0862` n `134` status `ready` deltaP `3.8788` edge `-0.0011` maxDD `-0.1986`
- `market_context_high->commodity_1h` score `-0.2301` n `134` status `ready` deltaP `2.5427` edge `0.0153` maxDD `-0.4475`
- `market_context_high->fx_4h` score `-0.4895` n `134` status `ready` deltaP `-0.0159` edge `-0.0028` maxDD `-0.4545`
- `news_risk_high->commodity_1h` score `-0.7043` n `77` status `ready` deltaP `-5.3465` edge `0.0047` maxDD `-1.4151`
- `market_context_high->index_1h` score `-0.7791` n `134` status `ready` deltaP `-1.497` edge `0.0009` maxDD `-1.1344`
- `news_risk_high->index_1h` score `-0.8474` n `77` status `ready` deltaP `-3.4451` edge `-0.0057` maxDD `-1.3981`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
