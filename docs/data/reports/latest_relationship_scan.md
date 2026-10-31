# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-31T01:37:30.306612+00:00`
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

- `market_context_high->unknown_24h` score `1585.1199` n `134` status `ready` deltaP `-6.0894` edge `132.1769` maxDD `-1.1049`
- `news_risk_high->unknown_1h` score `141.6143` n `96` status `ready` deltaP `-2.9067` edge `11.8492` maxDD `-0.9571`
- `market_context_high->unknown_4h` score `40.4038` n `134` status `ready` deltaP `0.4163` edge `3.3775` maxDD `-0.3966`
- `news_risk_high->crypto_alt_4h` score `7.7968` n `84` status `ready` deltaP `24.3322` edge `0.5536` maxDD `-3.6198`
- `market_context_high->equity_24h` score `7.0214` n `134` status `ready` deltaP `18.395` edge `0.7382` maxDD `-14.0571`
- `market_context_high->index_24h` score `3.8575` n `134` status `ready` deltaP `36.9999` edge `0.0931` maxDD `-0.1315`
- `news_risk_high->crypto_alt_1h` score `1.4011` n `96` status `ready` deltaP `10.5851` edge `0.1291` maxDD `-3.9659`
- `market_context_high->commodity_4h` score `0.445` n `134` status `ready` deltaP `15.3099` edge `0.0569` maxDD `-1.0837`
- `market_context_high->metal_1h` score `0.3696` n `134` status `ready` deltaP `10.6042` edge `0.0146` maxDD `-0.3659`
- `market_context_high->metal_4h` score `0.3256` n `134` status `ready` deltaP `14.9163` edge `0.0319` maxDD `-1.8344`
- `market_context_high->equity_1h` score `0.1695` n `134` status `ready` deltaP `4.033` edge `0.0748` maxDD `-2.3383`
- `market_context_high->equity_4h` score `-0.0142` n `134` status `ready` deltaP `2.0864` edge `0.1427` maxDD `-6.008`
- `market_context_high->fx_1h` score `-0.101` n `134` status `ready` deltaP `3.5794` edge `-0.001` maxDD `-0.1986`
- `market_context_high->crypto_major_1h` score `-0.1079` n `134` status `ready` deltaP `6.7164` edge `0.049` maxDD `-5.2213`
- `market_context_high->commodity_1h` score `-0.1427` n `134` status `ready` deltaP `3.4409` edge `0.0166` maxDD `-0.4475`
- `market_context_high->fx_4h` score `-0.4634` n `134` status `ready` deltaP `0.4414` edge `-0.0025` maxDD `-0.4545`
- `market_context_high->metal_24h` score `-0.6835` n `134` status `ready` deltaP `3.9257` edge `0.1509` maxDD `-10.5088`
- `market_context_high->index_1h` score `-0.869` n `134` status `ready` deltaP `-2.5449` edge `0.0004` maxDD `-1.1344`
- `news_risk_high->index_1h` score `-0.8756` n `96` status `ready` deltaP `1.6218` edge `-0.0038` maxDD `-1.3981`
- `news_risk_high->commodity_1h` score `-0.9737` n `96` status `ready` deltaP `-8.7637` edge `0.0` maxDD `-1.9789`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
