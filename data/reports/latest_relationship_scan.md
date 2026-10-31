# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-31T03:37:29.309882+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `7170`

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

- `market_context_high->unknown_24h` score `1586.1675` n `134` status `ready` deltaP `-4.8741` edge `132.2561` maxDD `-1.1049`
- `news_risk_high->unknown_1h` score `135.0331` n `92` status `ready` deltaP `-2.7923` edge `11.3` maxDD `-0.9571`
- `market_context_high->unknown_4h` score `40.4722` n `134` status `ready` deltaP `1.331` edge `3.3771` maxDD `-0.3966`
- `news_risk_high->crypto_alt_4h` score `8.0719` n `88` status `ready` deltaP `26.8708` edge `0.5596` maxDD `-3.6198`
- `market_context_high->equity_24h` score `7.3895` n `134` status `ready` deltaP `18.9159` edge `0.7654` maxDD `-14.0571`
- `market_context_high->index_24h` score `3.9262` n `134` status `ready` deltaP `37.6943` edge `0.0942` maxDD `-0.1315`
- `news_risk_high->crypto_alt_1h` score `1.6346` n `92` status `ready` deltaP `12.2885` edge `0.1372` maxDD `-3.9659`
- `market_context_high->commodity_4h` score `0.4146` n `134` status `ready` deltaP `15.005` edge `0.0564` maxDD `-1.0837`
- `market_context_high->metal_1h` score `0.3938` n `134` status `ready` deltaP `11.0533` edge `0.0147` maxDD `-0.3659`
- `market_context_high->metal_4h` score `0.3256` n `134` status `ready` deltaP `14.9163` edge `0.0319` maxDD `-1.8344`
- `market_context_high->equity_1h` score `0.2042` n `134` status `ready` deltaP `4.3324` edge `0.0757` maxDD `-2.3383`
- `market_context_high->crypto_major_1h` score `-0.0372` n `134` status `ready` deltaP `7.3152` edge `0.0509` maxDD `-5.2213`
- `market_context_high->equity_4h` score `-0.0805` n `134` status `ready` deltaP `1.1717` edge `0.1403` maxDD `-6.008`
- `market_context_high->fx_1h` score `-0.1003` n `134` status `ready` deltaP `3.5794` edge `-0.0009` maxDD `-0.1986`
- `market_context_high->commodity_1h` score `-0.1966` n `134` status `ready` deltaP `2.9918` edge `0.0151` maxDD `-0.4475`
- `market_context_high->fx_4h` score `-0.4808` n `134` status `ready` deltaP `0.1365` edge `-0.0027` maxDD `-0.4545`
- `market_context_high->metal_24h` score `-0.6211` n `134` status `ready` deltaP `3.9257` edge `0.1589` maxDD `-10.5088`
- `news_risk_high->index_1h` score `-0.7892` n `92` status `ready` deltaP `2.7011` edge `-0.0038` maxDD `-1.3981`
- `market_context_high->index_1h` score `-0.7935` n `134` status `ready` deltaP `-1.6467` edge `0.0007` maxDD `-1.1344`
- `news_risk_high->fx_1h` score `-0.8561` n `92` status `ready` deltaP `-5.246` edge `-0.0047` maxDD `-0.6065`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
