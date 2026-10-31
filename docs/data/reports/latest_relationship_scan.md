# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-31T07:07:25.826372+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `7605`

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

- `market_context_high->unknown_24h` score `1588.0551` n `134` status `ready` deltaP `-4.8741` edge `132.4134` maxDD `-1.1049`
- `news_risk_high->unknown_1h` score `112.4789` n `98` status `ready` deltaP `-5.0439` edge `9.4355` maxDD `-0.9571`
- `market_context_high->unknown_4h` score `43.2538` n `134` status `ready` deltaP `2.2456` edge `3.6028` maxDD `-0.3966`
- `market_context_high->equity_24h` score `8.2427` n `134` status `ready` deltaP `20.1312` edge `0.8284` maxDD `-14.0571`
- `news_risk_high->crypto_alt_4h` score `7.1697` n `92` status `ready` deltaP `23.3629` edge `0.5078` maxDD `-3.6198`
- `market_context_high->index_24h` score `4.1251` n `134` status `ready` deltaP `39.4304` edge `0.0992` maxDD `-0.1315`
- `news_risk_high->crypto_alt_1h` score `0.926` n `98` status `ready` deltaP `8.2457` edge `0.1051` maxDD `-3.9659`
- `market_context_high->commodity_4h` score `0.3733` n `134` status `ready` deltaP `14.5477` edge `0.056` maxDD `-1.0837`
- `market_context_high->metal_1h` score `0.3696` n `134` status `ready` deltaP `10.6042` edge `0.0146` maxDD `-0.3659`
- `market_context_high->metal_4h` score `0.2821` n `134` status `ready` deltaP `14.1541` edge `0.0314` maxDD `-1.8344`
- `market_context_high->equity_1h` score `0.1479` n `134` status `ready` deltaP `3.7336` edge `0.075` maxDD `-2.3383`
- `market_context_high->crypto_major_1h` score `-0.0647` n `134` status `ready` deltaP `6.8661` edge `0.0516` maxDD `-5.2213`
- `market_context_high->fx_1h` score `-0.1166` n `134` status `ready` deltaP `3.28` edge `-0.001` maxDD `-0.1986`
- `market_context_high->equity_4h` score `-0.1417` n `134` status `ready` deltaP `0.7144` edge `0.1355` maxDD `-6.008`
- `market_context_high->commodity_1h` score `-0.1942` n `134` status `ready` deltaP `2.9918` edge `0.0153` maxDD `-0.4475`
- `market_context_high->fx_4h` score `-0.457` n `134` status `ready` deltaP `0.5939` edge `-0.0027` maxDD `-0.4545`
- `market_context_high->metal_24h` score `-0.5228` n `134` status `ready` deltaP `3.9257` edge `0.1715` maxDD `-10.5088`
- `market_context_high->index_1h` score `-0.7564` n `134` status `ready` deltaP `-1.1976` edge `0.0008` maxDD `-1.1344`
- `news_risk_high->index_1h` score `-0.8562` n `98` status `ready` deltaP `1.8636` edge `-0.0038` maxDD `-1.3981`
- `news_risk_high->fx_1h` score `-0.9109` n `98` status `ready` deltaP `-6.2996` edge `-0.0047` maxDD `-0.6065`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
