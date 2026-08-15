# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-15T21:32:14.444207+00:00`
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

- `market_context_high->unknown_24h` score `176.484` n `114` status `ready` deltaP `-27.8771` edge `15.1702` maxDD `-8.5217`
- `risk_on_high->unknown_24h` score `33.8167` n `32` status `ready` deltaP `-36.7039` edge `4.6552` maxDD `-1.6689`
- `risk_on_and_context->unknown_24h` score `33.8167` n `32` status `ready` deltaP `-36.7039` edge `4.6552` maxDD `-1.6689`
- `news_risk_high->equity_24h` score `12.9731` n `36` status `ready` deltaP `26.6609` edge `0.9413` maxDD `-1.0358`
- `news_risk_high->equity_4h` score `7.7407` n `36` status `ready` deltaP `39.939` edge `0.3788` maxDD `0.0`
- `market_context_high->commodity_24h` score `6.4584` n `114` status `ready` deltaP `36.5472` edge `0.3003` maxDD `-0.1266`
- `risk_on_high->commodity_24h` score `5.4713` n `32` status `ready` deltaP `38.3016` edge `0.2006` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `5.4713` n `32` status `ready` deltaP `38.3016` edge `0.2006` maxDD `0.0`
- `risk_on_high->crypto_major_24h` score `4.0555` n `32` status `ready` deltaP `27.6809` edge `0.451` maxDD `-6.2481`
- `risk_on_and_context->crypto_major_24h` score `4.0555` n `32` status `ready` deltaP `27.6809` edge `0.451` maxDD `-6.2481`
- `news_risk_high->index_24h` score `3.7649` n `36` status `ready` deltaP `31.7158` edge `0.1023` maxDD `0.0`
- `risk_on_high->commodity_4h` score `2.9122` n `32` status `ready` deltaP `20.8079` edge `0.1222` maxDD `-0.1258`
- `risk_on_and_context->commodity_4h` score `2.9122` n `32` status `ready` deltaP `20.8079` edge `0.1222` maxDD `-0.1258`
- `market_context_high->commodity_4h` score `2.1905` n `114` status `ready` deltaP `20.7531` edge `0.0913` maxDD `-0.7687`
- `news_risk_high->index_4h` score `2.0034` n `36` status `ready` deltaP `23.1199` edge `0.026` maxDD `-0.0546`
- `news_risk_high->equity_1h` score `1.7862` n `36` status `ready` deltaP `8.7326` edge `0.1225` maxDD `-0.5496`
- `risk_on_high->commodity_1h` score `1.3737` n `32` status `ready` deltaP `14.7081` edge `0.0397` maxDD `-0.1957`
- `risk_on_and_context->commodity_1h` score `1.3737` n `32` status `ready` deltaP `14.7081` edge `0.0397` maxDD `-0.1957`
- `risk_on_high->equity_24h` score `0.7864` n `32` status `ready` deltaP `15.2026` edge `0.1774` maxDD `-11.2348`
- `risk_on_and_context->equity_24h` score `0.7864` n `32` status `ready` deltaP `15.2026` edge `0.1774` maxDD `-11.2348`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
