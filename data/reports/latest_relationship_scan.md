# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-15T04:21:56.532584+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11796`

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

- `market_context_high->unknown_24h` score `136.7126` n `128` status `ready` deltaP `-28.3855` edge `11.8732` maxDD `-9.6329`
- `risk_on_high->unknown_24h` score `33.1422` n `32` status `ready` deltaP `-41.6667` edge `4.6018` maxDD `-1.6689`
- `risk_on_and_context->unknown_24h` score `33.1422` n `32` status `ready` deltaP `-41.6667` edge `4.6018` maxDD `-1.6689`
- `news_risk_high->equity_24h` score `11.6429` n `36` status `ready` deltaP `19.618` edge `0.8774` maxDD `-1.0358`
- `news_risk_high->equity_4h` score `7.4602` n `36` status `ready` deltaP `38.2622` edge `0.3666` maxDD `0.0`
- `market_context_high->commodity_24h` score `4.9238` n `128` status `ready` deltaP `27.8645` edge `0.2303` maxDD `-0.1266`
- `risk_on_high->commodity_24h` score `4.4999` n `32` status `ready` deltaP `30.2083` edge `0.1736` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `4.4999` n `32` status `ready` deltaP `30.2083` edge `0.1736` maxDD `0.0`
- `risk_on_high->crypto_major_24h` score `3.9394` n `32` status `ready` deltaP `25.8681` edge `0.4482` maxDD `-6.2481`
- `risk_on_and_context->crypto_major_24h` score `3.9394` n `32` status `ready` deltaP `25.8681` edge `0.4482` maxDD `-6.2481`
- `news_risk_high->index_24h` score `2.9646` n `36` status `ready` deltaP `23.4375` edge `0.0908` maxDD `0.0`
- `risk_on_high->commodity_4h` score `2.7254` n `32` status `ready` deltaP `19.2835` edge `0.1168` maxDD `-0.1258`
- `risk_on_and_context->commodity_4h` score `2.7254` n `32` status `ready` deltaP `19.2835` edge `0.1168` maxDD `-0.1258`
- `market_context_high->commodity_4h` score `1.7776` n `128` status `ready` deltaP `17.721` edge `0.0771` maxDD `-0.7687`
- `news_risk_high->index_4h` score `1.7025` n `36` status `ready` deltaP `19.6138` edge `0.0243` maxDD `-0.0546`
- `news_risk_high->equity_1h` score `1.6819` n `36` status `ready` deltaP `7.8344` edge `0.1198` maxDD `-0.5496`
- `risk_on_high->commodity_1h` score `1.2491` n `32` status `ready` deltaP `13.3608` edge `0.0383` maxDD `-0.1957`
- `risk_on_and_context->commodity_1h` score `1.2491` n `32` status `ready` deltaP `13.3608` edge `0.0383` maxDD `-0.1957`
- `risk_on_high->fx_24h` score `0.7111` n `32` status `ready` deltaP `9.375` edge `0.0152` maxDD `-0.1418`
- `risk_on_and_context->fx_24h` score `0.7111` n `32` status `ready` deltaP `9.375` edge `0.0152` maxDD `-0.1418`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
