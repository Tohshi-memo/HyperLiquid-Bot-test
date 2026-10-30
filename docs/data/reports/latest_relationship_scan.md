# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-30T22:52:32.163144+00:00`
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

- `market_context_high->unknown_24h` score `1585.6676` n `134` status `ready` deltaP `-6.263` edge `132.2237` maxDD `-1.1049`
- `news_risk_high->unknown_1h` score `171.1771` n `85` status `ready` deltaP `-0.5372` edge `14.2809` maxDD `-0.3382`
- `market_context_high->unknown_4h` score `36.9562` n `134` status `ready` deltaP `0.4163` edge `3.0902` maxDD `-0.3966`
- `market_context_high->equity_24h` score `6.3509` n `134` status `ready` deltaP `16.6589` edge `0.6939` maxDD `-14.0571`
- `news_risk_high->crypto_alt_4h` score `5.9367` n `73` status `ready` deltaP `21.0763` edge `0.4203` maxDD `-3.6198`
- `market_context_high->index_24h` score `3.6766` n `134` status `ready` deltaP `35.2638` edge `0.0896` maxDD `-0.1315`
- `news_risk_high->crypto_alt_1h` score `0.9359` n `85` status `ready` deltaP `7.7104` edge `0.1095` maxDD `-3.9659`
- `market_context_high->commodity_4h` score `0.4594` n `134` status `ready` deltaP `15.3099` edge `0.0581` maxDD `-1.0837`
- `market_context_high->metal_1h` score `0.3541` n `134` status `ready` deltaP `10.3048` edge `0.0146` maxDD `-0.3659`
- `market_context_high->metal_4h` score `0.3469` n `134` status `ready` deltaP `15.2212` edge `0.0326` maxDD `-1.8344`
- `market_context_high->equity_1h` score `0.2222` n `134` status `ready` deltaP `4.6318` edge `0.0752` maxDD `-2.3383`
- `market_context_high->equity_4h` score `0.0185` n `134` status `ready` deltaP `2.0864` edge `0.1469` maxDD `-6.008`
- `market_context_high->crypto_major_1h` score `-0.0372` n `134` status `ready` deltaP `7.1655` edge `0.0519` maxDD `-5.2213`
- `market_context_high->fx_1h` score `-0.0606` n `134` status `ready` deltaP `4.3279` edge `-0.0008` maxDD `-0.1986`
- `market_context_high->commodity_1h` score `-0.1714` n `134` status `ready` deltaP `3.1415` edge `0.0162` maxDD `-0.4475`
- `market_context_high->fx_4h` score `-0.4816` n `134` status `ready` deltaP `0.1365` edge `-0.0028` maxDD `-0.4545`
- `news_risk_high->commodity_1h` score `-0.7243` n `85` status `ready` deltaP `-5.2519` edge `0.004` maxDD `-1.6142`
- `market_context_high->metal_24h` score `-0.7958` n `134` status `ready` deltaP `3.9257` edge `0.1365` maxDD `-10.5088`
- `news_risk_high->commodity_4h` score `-0.7974` n `73` status `ready` deltaP `0.6912` edge `0.0064` maxDD `-4.0587`
- `market_context_high->index_1h` score `-0.8558` n `134` status `ready` deltaP `-2.3952` edge `0.0005` maxDD `-1.1344`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
