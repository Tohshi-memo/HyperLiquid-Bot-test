# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-31T00:37:25.037202+00:00`
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

- `market_context_high->unknown_24h` score `1585.3779` n `134` status `ready` deltaP `-6.0894` edge `132.1984` maxDD `-1.1049`
- `news_risk_high->unknown_1h` score `157.6558` n `92` status `ready` deltaP `-0.729` edge `13.1554` maxDD `-0.3382`
- `market_context_high->unknown_4h` score `40.4796` n `134` status `ready` deltaP `0.5688` edge `3.3828` maxDD `-0.3966`
- `news_risk_high->crypto_alt_4h` score `7.3501` n `80` status `ready` deltaP `23.3537` edge `0.5229` maxDD `-3.6198`
- `market_context_high->equity_24h` score `6.8099` n `134` status `ready` deltaP `17.7006` edge `0.7252` maxDD `-14.0571`
- `market_context_high->index_24h` score `3.7923` n `134` status `ready` deltaP `36.3054` edge `0.0923` maxDD `-0.1315`
- `news_risk_high->crypto_alt_1h` score `1.4721` n `92` status `ready` deltaP `10.7524` edge `0.1339` maxDD `-3.9659`
- `market_context_high->commodity_4h` score `0.4534` n `134` status `ready` deltaP `15.3099` edge `0.0576` maxDD `-1.0837`
- `market_context_high->metal_1h` score `0.3541` n `134` status `ready` deltaP `10.3048` edge `0.0146` maxDD `-0.3659`
- `market_context_high->metal_4h` score `0.3272` n `134` status `ready` deltaP `14.9163` edge `0.0321` maxDD `-1.8344`
- `market_context_high->equity_1h` score `0.1791` n `134` status `ready` deltaP `4.1827` edge `0.0746` maxDD `-2.3383`
- `market_context_high->equity_4h` score `-0.0095` n `134` status `ready` deltaP `2.0864` edge `0.1433` maxDD `-6.008`
- `market_context_high->fx_1h` score `-0.1003` n `134` status `ready` deltaP `3.5794` edge `-0.0009` maxDD `-0.1986`
- `market_context_high->crypto_major_1h` score `-0.1271` n `134` status `ready` deltaP `6.5667` edge `0.0484` maxDD `-5.2213`
- `market_context_high->commodity_1h` score `-0.1427` n `134` status `ready` deltaP `3.4409` edge `0.0166` maxDD `-0.4475`
- `market_context_high->fx_4h` score `-0.48` n `134` status `ready` deltaP `0.1365` edge `-0.0026` maxDD `-0.4545`
- `market_context_high->metal_24h` score `-0.7193` n `134` status `ready` deltaP `3.9257` edge `0.1463` maxDD `-10.5088`
- `news_risk_high->commodity_1h` score `-0.8439` n `92` status `ready` deltaP `-7.088` edge `0.0024` maxDD `-1.7333`
- `news_risk_high->index_1h` score `-0.8743` n `92` status `ready` deltaP `1.6532` edge `-0.0039` maxDD `-1.3981`
- `market_context_high->index_1h` score `-0.8809` n `134` status `ready` deltaP `-2.6946` edge `0.0004` maxDD `-1.1344`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
