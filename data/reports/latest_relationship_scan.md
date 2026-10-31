# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-31T03:52:29.786317+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `7198`

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

- `market_context_high->unknown_24h` score `1586.2311` n `134` status `ready` deltaP `-4.8741` edge `132.2614` maxDD `-1.1049`
- `news_risk_high->unknown_1h` score `135.0391` n `92` status `ready` deltaP `-2.7923` edge `11.3005` maxDD `-0.9571`
- `market_context_high->unknown_4h` score `40.4952` n `134` status `ready` deltaP `1.4834` edge `3.378` maxDD `-0.3966`
- `news_risk_high->crypto_alt_4h` score `7.8566` n `89` status `ready` deltaP `25.9643` edge `0.5477` maxDD `-3.6198`
- `market_context_high->equity_24h` score `7.4411` n `134` status `ready` deltaP `18.9159` edge `0.7697` maxDD `-14.0571`
- `market_context_high->index_24h` score `3.9286` n `134` status `ready` deltaP `37.6943` edge `0.0944` maxDD `-0.1315`
- `news_risk_high->crypto_alt_1h` score `1.637` n `92` status `ready` deltaP `12.2885` edge `0.1374` maxDD `-3.9659`
- `market_context_high->commodity_4h` score `0.417` n `134` status `ready` deltaP `15.005` edge `0.0566` maxDD `-1.0837`
- `market_context_high->metal_1h` score `0.4015` n `134` status `ready` deltaP `11.203` edge `0.0147` maxDD `-0.3659`
- `market_context_high->metal_4h` score `0.3256` n `134` status `ready` deltaP `14.9163` edge `0.0319` maxDD `-1.8344`
- `market_context_high->equity_1h` score `0.2042` n `134` status `ready` deltaP `4.3324` edge `0.0757` maxDD `-2.3383`
- `market_context_high->crypto_major_1h` score `-0.0312` n `134` status `ready` deltaP `7.3152` edge `0.0514` maxDD `-5.2213`
- `market_context_high->equity_4h` score `-0.0908` n `134` status `ready` deltaP `1.0193` edge `0.14` maxDD `-6.008`
- `market_context_high->fx_1h` score `-0.1088` n `134` status `ready` deltaP `3.4297` edge `-0.001` maxDD `-0.1986`
- `market_context_high->commodity_1h` score `-0.211` n `134` status `ready` deltaP `2.8421` edge `0.0149` maxDD `-0.4475`
- `market_context_high->fx_4h` score `-0.4808` n `134` status `ready` deltaP `0.1365` edge `-0.0027` maxDD `-0.4545`
- `market_context_high->metal_24h` score `-0.6133` n `134` status `ready` deltaP `3.9257` edge `0.1599` maxDD `-10.5088`
- `news_risk_high->index_1h` score `-0.7773` n `92` status `ready` deltaP `2.8508` edge `-0.0038` maxDD `-1.3981`
- `market_context_high->index_1h` score `-0.7815` n `134` status `ready` deltaP `-1.497` edge `0.0007` maxDD `-1.1344`
- `news_risk_high->fx_1h` score `-0.8647` n `92` status `ready` deltaP `-5.3957` edge `-0.0048` maxDD `-0.6065`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
