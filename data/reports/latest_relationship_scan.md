# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-31T00:07:26.806221+00:00`
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

- `market_context_high->unknown_24h` score `1585.6335` n `134` status `ready` deltaP `-6.0894` edge `132.2197` maxDD `-1.1049`
- `news_risk_high->unknown_1h` score `151.5866` n `90` status `ready` deltaP `-0.0333` edge `12.645` maxDD `-0.3382`
- `market_context_high->unknown_4h` score `40.3294` n `134` status `ready` deltaP `0.4163` edge `3.3713` maxDD `-0.3966`
- `news_risk_high->crypto_alt_4h` score `6.9426` n `78` status `ready` deltaP `22.7447` edge `0.493` maxDD `-3.6198`
- `market_context_high->equity_24h` score `6.6964` n `134` status `ready` deltaP `17.527` edge `0.7169` maxDD `-14.0571`
- `market_context_high->index_24h` score `3.7712` n `134` status `ready` deltaP `36.1318` edge `0.0917` maxDD `-0.1315`
- `news_risk_high->crypto_alt_1h` score `1.3463` n `90` status `ready` deltaP `9.9601` edge `0.1287` maxDD `-3.9659`
- `market_context_high->commodity_4h` score `0.4534` n `134` status `ready` deltaP `15.3099` edge `0.0576` maxDD `-1.0837`
- `market_context_high->metal_1h` score `0.3618` n `134` status `ready` deltaP `10.4545` edge `0.0146` maxDD `-0.3659`
- `market_context_high->metal_4h` score `0.3367` n `134` status `ready` deltaP `15.0688` edge `0.0323` maxDD `-1.8344`
- `market_context_high->equity_1h` score `0.1922` n `134` status `ready` deltaP `4.3324` edge `0.0747` maxDD `-2.3383`
- `market_context_high->equity_4h` score `-0.0072` n `134` status `ready` deltaP `2.0864` edge `0.1436` maxDD `-6.008`
- `market_context_high->fx_1h` score `-0.0847` n `134` status `ready` deltaP `3.8788` edge `-0.0009` maxDD `-0.1986`
- `market_context_high->crypto_major_1h` score `-0.1019` n `134` status `ready` deltaP `6.7164` edge `0.0495` maxDD `-5.2213`
- `market_context_high->commodity_1h` score `-0.1439` n `134` status `ready` deltaP `3.4409` edge `0.0165` maxDD `-0.4475`
- `market_context_high->fx_4h` score `-0.4808` n `134` status `ready` deltaP `0.1365` edge `-0.0027` maxDD `-0.4545`
- `market_context_high->metal_24h` score `-0.7404` n `134` status `ready` deltaP `3.9257` edge `0.1436` maxDD `-10.5088`
- `news_risk_high->commodity_1h` score `-0.7781` n `90` status `ready` deltaP `-6.1943` edge `0.0035` maxDD `-1.624`
- `market_context_high->index_1h` score `-0.8678` n `134` status `ready` deltaP `-2.5449` edge `0.0005` maxDD `-1.1344`
- `news_risk_high->index_1h` score `-0.947` n `90` status `ready` deltaP `0.7884` edge `-0.0042` maxDD `-1.3981`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
