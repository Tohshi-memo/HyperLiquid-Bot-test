# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-30T20:22:31.858162+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `6898`

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

- `market_context_high->unknown_24h` score `1590.1107` n `134` status `ready` deltaP `-6.0894` edge `132.5928` maxDD `-1.1049`
- `news_risk_high->unknown_1h` score `112.2598` n `75` status `ready` deltaP `-0.6228` edge `9.3717` maxDD `-0.3382`
- `market_context_high->unknown_4h` score `36.3526` n `134` status `ready` deltaP `0.4163` edge `3.0399` maxDD `-0.3966`
- `market_context_high->equity_24h` score `5.7305` n `134` status `ready` deltaP `16.6589` edge `0.6422` maxDD `-14.0571`
- `news_risk_high->crypto_alt_4h` score `5.409` n `63` status `ready` deltaP `19.7518` edge `0.3827` maxDD `-3.4234`
- `market_context_high->index_24h` score `3.6226` n `134` status `ready` deltaP `35.2638` edge `0.0851` maxDD `-0.1315`
- `news_risk_high->commodity_4h` score `0.7654` n `63` status `ready` deltaP `7.1695` edge `0.0507` maxDD `-0.7773`
- `news_risk_high->crypto_alt_1h` score `0.5301` n `75` status `ready` deltaP `5.1577` edge `0.0927` maxDD `-3.9659`
- `market_context_high->metal_4h` score `0.4031` n `134` status `ready` deltaP `16.1358` edge `0.0337` maxDD `-1.8344`
- `market_context_high->metal_1h` score `0.3891` n `134` status `ready` deltaP `10.9036` edge `0.0151` maxDD `-0.3659`
- `market_context_high->equity_1h` score `0.3217` n `134` status `ready` deltaP `5.3803` edge `0.0785` maxDD `-2.3383`
- `market_context_high->commodity_4h` score `0.3143` n `134` status `ready` deltaP `14.3952` edge `0.0521` maxDD `-1.0837`
- `market_context_high->equity_4h` score `0.2201` n `134` status `ready` deltaP `3.4583` edge `0.1636` maxDD `-6.008`
- `market_context_high->crypto_major_1h` score `0.0564` n `134` status `ready` deltaP `7.4649` edge `0.0577` maxDD `-5.2213`
- `market_context_high->fx_1h` score `-0.1026` n `134` status `ready` deltaP `3.5794` edge `-0.0012` maxDD `-0.1986`
- `market_context_high->commodity_1h` score `-0.2589` n `134` status `ready` deltaP `2.2433` edge `0.0149` maxDD `-0.4475`
- `market_context_high->fx_4h` score `-0.4982` n `134` status `ready` deltaP `-0.1683` edge `-0.0029` maxDD `-0.4545`
- `news_risk_high->commodity_1h` score `-0.6104` n `75` status `ready` deltaP `-4.503` edge `0.0078` maxDD `-1.1492`
- `market_context_high->index_1h` score `-0.7911` n `134` status `ready` deltaP `-1.6467` edge `0.0009` maxDD `-1.1344`
- `news_risk_high->index_1h` score `-0.8641` n `75` status `ready` deltaP `-3.6467` edge `-0.0065` maxDD `-1.3981`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
