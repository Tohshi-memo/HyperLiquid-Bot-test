# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-30T14:36:22.515719+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `7028`

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

- `market_context_high->unknown_24h` score `1615.7587` n `134` status `ready` deltaP `-2.9644` edge `134.7093` maxDD `-1.1049`
- `news_risk_high->unknown_1h` score `189.5463` n `52` status `ready` deltaP `-0.5872` edge `15.812` maxDD `-0.3382`
- `market_context_high->unknown_4h` score `31.9356` n `134` status `ready` deltaP `1.4834` edge `2.6647` maxDD `-0.3966`
- `news_risk_high->crypto_alt_4h` score `7.9404` n `40` status `ready` deltaP `23.1098` edge `0.5423` maxDD `-1.4402`
- `market_context_high->index_24h` score `3.4258` n `134` status `ready` deltaP `35.2638` edge `0.0687` maxDD `-0.1315`
- `market_context_high->equity_24h` score `3.3281` n `134` status `ready` deltaP `16.6589` edge `0.442` maxDD `-14.0571`
- `market_context_high->metal_1h` score `0.4047` n `134` status `ready` deltaP `11.203` edge `0.0151` maxDD `-0.3659`
- `market_context_high->metal_4h` score `0.3568` n `134` status `ready` deltaP `15.831` edge `0.0298` maxDD `-1.8344`
- `market_context_high->equity_1h` score `0.2509` n `134` status `ready` deltaP `5.0809` edge `0.0746` maxDD `-2.3383`
- `news_risk_high->commodity_4h` score `0.2508` n `40` status `ready` deltaP `1.9817` edge `0.0527` maxDD `-0.7008`
- `news_risk_high->crypto_alt_1h` score `0.2288` n `52` status `ready` deltaP `4.9401` edge `0.0675` maxDD `-3.3547`
- `market_context_high->commodity_4h` score `0.1687` n `134` status `ready` deltaP `13.1757` edge `0.0481` maxDD `-1.0837`
- `market_context_high->crypto_major_1h` score `0.1571` n `134` status `ready` deltaP `7.914` edge `0.0631` maxDD `-5.2213`
- `market_context_high->fx_1h` score `-0.0512` n `134` status `ready` deltaP `4.4776` edge `-0.0006` maxDD `-0.1986`
- `market_context_high->equity_4h` score `-0.0742` n `134` status `ready` deltaP `3.1534` edge `0.1279` maxDD `-6.008`
- `market_context_high->commodity_1h` score `-0.3595` n `134` status `ready` deltaP `1.3451` edge `0.0125` maxDD `-0.4475`
- `news_risk_high->index_1h` score `-0.3876` n `52` status `ready` deltaP `3.6734` edge `-0.0043` maxDD `-0.5909`
- `market_context_high->fx_4h` score `-0.5077` n `134` status `ready` deltaP `-0.3208` edge `-0.0031` maxDD `-0.4545`
- `market_context_high->crypto_alt_1h` score `-0.7978` n `134` status `ready` deltaP `3.4476` edge `0.0612` maxDD `-8.251`
- `market_context_high->index_1h` score `-0.8306` n `134` status `ready` deltaP `-2.0958` edge `0.0006` maxDD `-1.1344`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
