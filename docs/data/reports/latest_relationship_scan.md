# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-30T23:52:27.072154+00:00`
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

- `market_context_high->unknown_24h` score `1585.6935` n `134` status `ready` deltaP `-6.0894` edge `132.2247` maxDD `-1.1049`
- `news_risk_high->unknown_1h` score `155.8882` n `89` status `ready` deltaP `-0.1582` edge `13.0043` maxDD `-0.3382`
- `market_context_high->unknown_4h` score `40.2274` n `134` status `ready` deltaP `0.4163` edge `3.3628` maxDD `-0.3966`
- `news_risk_high->crypto_alt_4h` score `6.8105` n `77` status `ready` deltaP `22.4284` edge `0.4841` maxDD `-3.6198`
- `market_context_high->equity_24h` score `6.6273` n `134` status `ready` deltaP `17.3534` edge `0.7123` maxDD `-14.0571`
- `market_context_high->index_24h` score `3.7525` n `134` status `ready` deltaP `35.9582` edge `0.0913` maxDD `-0.1315`
- `news_risk_high->crypto_alt_1h` score `1.3073` n `89` status `ready` deltaP `9.6229` edge `0.1277` maxDD `-3.9659`
- `market_context_high->commodity_4h` score `0.4558` n `134` status `ready` deltaP `15.3099` edge `0.0578` maxDD `-1.0837`
- `market_context_high->metal_1h` score `0.3626` n `134` status `ready` deltaP `10.4545` edge `0.0147` maxDD `-0.3659`
- `market_context_high->metal_4h` score `0.3367` n `134` status `ready` deltaP `15.0688` edge `0.0323` maxDD `-1.8344`
- `market_context_high->equity_1h` score `0.209` n `134` status `ready` deltaP `4.4821` edge `0.0751` maxDD `-2.3383`
- `market_context_high->equity_4h` score `-0.0049` n `134` status `ready` deltaP `2.0864` edge `0.1439` maxDD `-6.008`
- `market_context_high->crypto_major_1h` score `-0.0755` n `134` status `ready` deltaP `6.8661` edge `0.0507` maxDD `-5.2213`
- `market_context_high->fx_1h` score `-0.0769` n `134` status `ready` deltaP `4.0285` edge `-0.0009` maxDD `-0.1986`
- `market_context_high->commodity_1h` score `-0.157` n `134` status `ready` deltaP `3.2912` edge `0.0164` maxDD `-0.4475`
- `market_context_high->fx_4h` score `-0.4808` n `134` status `ready` deltaP `0.1365` edge `-0.0027` maxDD `-0.4545`
- `market_context_high->metal_24h` score `-0.7505` n `134` status `ready` deltaP `3.9257` edge `0.1423` maxDD `-10.5088`
- `news_risk_high->commodity_1h` score `-0.7586` n `89` status `ready` deltaP `-5.8821` edge `0.0038` maxDD `-1.6142`
- `market_context_high->index_1h` score `-0.8558` n `134` status `ready` deltaP `-2.3952` edge `0.0005` maxDD `-1.1344`
- `news_risk_high->index_1h` score `-0.9794` n `89` status `ready` deltaP `0.4138` edge `-0.0044` maxDD `-1.3981`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
