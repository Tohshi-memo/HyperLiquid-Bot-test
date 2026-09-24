# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-24T06:52:26.729578+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9897`

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

- `market_context_high->unknown_1h` score `66.2154` n `47` status `ready` deltaP `10.5651` edge `5.4546` maxDD `-0.2334`
- `market_context_high->crypto_major_24h` score `39.5861` n `46` status `ready` deltaP `26.9022` edge `3.1351` maxDD `-0.5817`
- `market_context_high->crypto_alt_24h` score `24.5236` n `46` status `ready` deltaP `21.875` edge `1.8978` maxDD `0.0`
- `market_context_high->equity_24h` score `22.8975` n `46` status `ready` deltaP `24.298` edge `1.7562` maxDD `-0.1382`
- `market_context_high->index_24h` score `7.6148` n `46` status `ready` deltaP `33.3258` edge `0.4211` maxDD `-0.03`
- `news_risk_high->crypto_major_24h` score `5.845` n `103` status `ready` deltaP `-0.7888` edge `1.3966` maxDD `-63.6743`
- `news_risk_high->crypto_alt_4h` score `4.8639` n `103` status `ready` deltaP `14.6889` edge `0.4072` maxDD `-5.9838`
- `news_risk_high->crypto_major_4h` score `4.7881` n `103` status `ready` deltaP `18.6523` edge `0.3324` maxDD `-2.619`
- `market_context_high->metal_24h` score `2.8` n `46` status `ready` deltaP `27.3023` edge `0.0747` maxDD `-0.2042`
- `market_context_high->index_4h` score `2.7239` n `47` status `ready` deltaP `31.7397` edge `0.0308` maxDD `-0.2323`
- `news_risk_high->crypto_alt_1h` score `2.398` n `109` status `ready` deltaP `13.1957` edge `0.1609` maxDD `-1.5895`
- `news_risk_high->crypto_alt_24h` score `2.2615` n `103` status `ready` deltaP `-3.3677` edge `0.9122` maxDD `-49.7699`
- `news_risk_high->commodity_24h` score `1.9849` n `103` status `ready` deltaP `20.9698` edge `0.1435` maxDD `-2.431`
- `market_context_high->equity_4h` score `1.9634` n `47` status `ready` deltaP `14.553` edge `0.1084` maxDD `-1.3444`
- `news_risk_high->crypto_major_1h` score `1.8602` n `109` status `ready` deltaP `14.5237` edge `0.1017` maxDD `-1.8141`
- `news_risk_high->fx_4h` score `1.605` n `103` status `ready` deltaP `23.3765` edge `0.0415` maxDD `-0.421`
- `news_risk_high->fx_24h` score `1.2335` n `103` status `ready` deltaP `29.6639` edge `0.1235` maxDD `-1.7159`
- `market_context_high->index_1h` score `0.9008` n `47` status `ready` deltaP `14.0113` edge `0.0095` maxDD `-0.2275`
- `market_context_high->equity_1h` score `0.7521` n `47` status `ready` deltaP `9.9694` edge `0.0365` maxDD `-1.5564`
- `news_risk_high->metal_1h` score `0.5095` n `109` status `ready` deltaP `13.6942` edge `0.0105` maxDD `-0.7468`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
