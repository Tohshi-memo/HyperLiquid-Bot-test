# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-31T02:07:28.321137+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `7072`

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

- `market_context_high->unknown_24h` score `1585.1218` n `134` status `ready` deltaP `-5.9158` edge `132.1759` maxDD `-1.1049`
- `news_risk_high->unknown_1h` score `141.5111` n `96` status `ready` deltaP `-2.757` edge `11.8396` maxDD `-0.9571`
- `market_context_high->unknown_4h` score `40.35` n `134` status `ready` deltaP `0.5688` edge `3.372` maxDD `-0.3966`
- `news_risk_high->crypto_alt_4h` score `7.8603` n `86` status `ready` deltaP `24.7058` edge `0.5564` maxDD `-3.6198`
- `market_context_high->equity_24h` score `7.1188` n `134` status `ready` deltaP `18.7423` edge `0.744` maxDD `-14.0571`
- `market_context_high->index_24h` score `3.8864` n `134` status `ready` deltaP `37.3471` edge `0.0932` maxDD `-0.1315`
- `news_risk_high->crypto_alt_1h` score `1.4371` n `96` status `ready` deltaP `10.7348` edge `0.1311` maxDD `-3.9659`
- `market_context_high->commodity_4h` score `0.4414` n `134` status `ready` deltaP `15.3099` edge `0.0566` maxDD `-1.0837`
- `market_context_high->metal_1h` score `0.386` n `134` status `ready` deltaP `10.9036` edge `0.0147` maxDD `-0.3659`
- `market_context_high->metal_4h` score `0.3177` n `134` status `ready` deltaP `14.7639` edge `0.0319` maxDD `-1.8344`
- `market_context_high->equity_1h` score `0.2018` n `134` status `ready` deltaP `4.3324` edge `0.0755` maxDD `-2.3383`
- `market_context_high->equity_4h` score `-0.0181` n `134` status `ready` deltaP `2.0864` edge `0.1422` maxDD `-6.008`
- `market_context_high->crypto_major_1h` score `-0.0671` n `134` status `ready` deltaP `7.0158` edge `0.0504` maxDD `-5.2213`
- `market_context_high->fx_1h` score `-0.1088` n `134` status `ready` deltaP `3.4297` edge `-0.001` maxDD `-0.1986`
- `market_context_high->commodity_1h` score `-0.1439` n `134` status `ready` deltaP `3.4409` edge `0.0165` maxDD `-0.4475`
- `market_context_high->fx_4h` score `-0.4641` n `134` status `ready` deltaP `0.4414` edge `-0.0026` maxDD `-0.4545`
- `market_context_high->metal_24h` score `-0.6671` n `134` status `ready` deltaP `3.9257` edge `0.153` maxDD `-10.5088`
- `market_context_high->index_1h` score `-0.8438` n `134` status `ready` deltaP `-2.2455` edge `0.0005` maxDD `-1.1344`
- `news_risk_high->index_1h` score `-0.8504` n `96` status `ready` deltaP `1.9212` edge `-0.0037` maxDD `-1.3981`
- `news_risk_high->commodity_1h` score `-0.9744` n `96` status `ready` deltaP `-8.7637` edge `-0.0001` maxDD `-1.9789`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
