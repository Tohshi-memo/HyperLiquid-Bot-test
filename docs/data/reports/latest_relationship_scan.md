# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-31T05:37:23.512060+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `7631`

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

- `market_context_high->unknown_24h` score `1587.1323` n `134` status `ready` deltaP `-4.8741` edge `132.3365` maxDD `-1.1049`
- `news_risk_high->unknown_1h` score `115.8163` n `97` status `ready` deltaP `-4.6515` edge `9.711` maxDD `-0.9571`
- `market_context_high->unknown_4h` score `40.3334` n `134` status `ready` deltaP `1.6359` edge `3.3635` maxDD `-0.3966`
- `market_context_high->equity_24h` score `7.9288` n `134` status `ready` deltaP `19.9575` edge `0.8034` maxDD `-14.0571`
- `news_risk_high->crypto_alt_4h` score `7.1745` n `92` status `ready` deltaP `23.3629` edge `0.5082` maxDD `-3.6198`
- `market_context_high->index_24h` score `4.0582` n `134` status `ready` deltaP `38.9096` edge `0.0971` maxDD `-0.1315`
- `news_risk_high->crypto_alt_1h` score `1.1045` n `97` status `ready` deltaP `9.4126` edge `0.1122` maxDD `-3.9659`
- `market_context_high->metal_1h` score `0.3938` n `134` status `ready` deltaP `11.0533` edge `0.0147` maxDD `-0.3659`
- `market_context_high->commodity_4h` score `0.3587` n `134` status `ready` deltaP `14.3952` edge `0.0558` maxDD `-1.0837`
- `market_context_high->metal_4h` score `0.3256` n `134` status `ready` deltaP `14.9163` edge `0.0319` maxDD `-1.8344`
- `market_context_high->equity_1h` score `0.203` n `134` status `ready` deltaP `4.3324` edge `0.0756` maxDD `-2.3383`
- `market_context_high->crypto_major_1h` score `-0.0036` n `134` status `ready` deltaP `7.4649` edge `0.0527` maxDD `-5.2213`
- `market_context_high->fx_1h` score `-0.1003` n `134` status `ready` deltaP `3.5794` edge `-0.0009` maxDD `-0.1986`
- `market_context_high->equity_4h` score `-0.1087` n `134` status `ready` deltaP `1.0193` edge `0.1377` maxDD `-6.008`
- `market_context_high->commodity_1h` score `-0.211` n `134` status `ready` deltaP `2.8421` edge `0.0149` maxDD `-0.4475`
- `market_context_high->fx_4h` score `-0.4808` n `134` status `ready` deltaP `0.1365` edge `-0.0027` maxDD `-0.4545`
- `market_context_high->metal_24h` score `-0.5587` n `134` status `ready` deltaP `3.9257` edge `0.1669` maxDD `-10.5088`
- `market_context_high->index_1h` score `-0.7312` n `134` status `ready` deltaP `-0.8982` edge `0.0009` maxDD `-1.1344`
- `news_risk_high->index_1h` score `-0.871` n `97` status `ready` deltaP `1.6791` edge `-0.0038` maxDD `-1.3981`
- `news_risk_high->fx_1h` score `-0.9248` n `97` status `ready` deltaP `-6.5683` edge `-0.0047` maxDD `-0.6065`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
