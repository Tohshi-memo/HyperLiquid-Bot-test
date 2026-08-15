# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-15T22:07:25.771614+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11717`

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

- `market_context_high->unknown_24h` score `183.0416` n `112` status `ready` deltaP `-27.6755` edge `15.7076` maxDD `-7.9034`
- `risk_on_high->unknown_24h` score `33.787` n `32` status `ready` deltaP `-37.0505` edge `4.6537` maxDD `-1.6689`
- `risk_on_and_context->unknown_24h` score `33.787` n `32` status `ready` deltaP `-37.0505` edge `4.6537` maxDD `-1.6689`
- `news_risk_high->equity_24h` score `12.9755` n `36` status `ready` deltaP `26.6609` edge `0.9415` maxDD `-1.0358`
- `news_risk_high->equity_4h` score `7.7395` n `36` status `ready` deltaP `39.939` edge `0.3787` maxDD `0.0`
- `market_context_high->commodity_24h` score `6.5592` n `112` status `ready` deltaP `36.8625` edge `0.3066` maxDD `-0.1266`
- `risk_on_high->commodity_24h` score `5.5087` n `32` status `ready` deltaP `38.6482` edge `0.2014` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `5.5087` n `32` status `ready` deltaP `38.6482` edge `0.2014` maxDD `0.0`
- `risk_on_high->crypto_major_24h` score `4.0399` n `32` status `ready` deltaP `27.6809` edge `0.449` maxDD `-6.2481`
- `risk_on_and_context->crypto_major_24h` score `4.0399` n `32` status `ready` deltaP `27.6809` edge `0.449` maxDD `-6.2481`
- `news_risk_high->index_24h` score `3.7938` n `36` status `ready` deltaP `32.0624` edge `0.1024` maxDD `0.0`
- `risk_on_high->commodity_4h` score `2.8988` n `32` status `ready` deltaP `20.6555` edge `0.1221` maxDD `-0.1258`
- `risk_on_and_context->commodity_4h` score `2.8988` n `32` status `ready` deltaP `20.6555` edge `0.1221` maxDD `-0.1258`
- `market_context_high->commodity_4h` score `2.2436` n `112` status `ready` deltaP `21.1019` edge `0.0934` maxDD `-0.7687`
- `news_risk_high->index_4h` score `2.0156` n `36` status `ready` deltaP `23.2723` edge `0.026` maxDD `-0.0546`
- `news_risk_high->equity_1h` score `1.7742` n `36` status `ready` deltaP `8.5829` edge `0.1225` maxDD `-0.5496`
- `risk_on_high->commodity_1h` score `1.3857` n `32` status `ready` deltaP `14.8578` edge `0.0397` maxDD `-0.1957`
- `risk_on_and_context->commodity_1h` score `1.3857` n `32` status `ready` deltaP `14.8578` edge `0.0397` maxDD `-0.1957`
- `risk_on_high->equity_24h` score `0.7879` n `32` status `ready` deltaP `15.2026` edge `0.1776` maxDD `-11.2348`
- `risk_on_and_context->equity_24h` score `0.7879` n `32` status `ready` deltaP `15.2026` edge `0.1776` maxDD `-11.2348`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
