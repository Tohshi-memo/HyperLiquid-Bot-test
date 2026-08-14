# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-14T05:52:30.260669+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11712`

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

- `market_context_high->unknown_24h` score `90.3439` n `150` status `ready` deltaP `-29.625` edge `8.0174` maxDD `-9.6329`
- `risk_on_high->unknown_24h` score `33.1828` n `32` status `ready` deltaP `-43.75` edge `4.6209` maxDD `-1.6689`
- `risk_on_and_context->unknown_24h` score `33.1828` n `32` status `ready` deltaP `-43.75` edge `4.6209` maxDD `-1.6689`
- `news_risk_high->equity_24h` score `10.0006` n `36` status `ready` deltaP `10.0694` edge `0.8042` maxDD `-1.0358`
- `news_risk_high->equity_4h` score `7.0988` n `36` status `ready` deltaP `38.1098` edge `0.3375` maxDD `0.0`
- `risk_on_high->commodity_24h` score `4.7841` n `32` status `ready` deltaP `32.2917` edge `0.1834` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `4.7841` n `32` status `ready` deltaP `32.2917` edge `0.1834` maxDD `0.0`
- `risk_on_high->commodity_4h` score `2.9152` n `32` status `ready` deltaP `20.3506` edge `0.1255` maxDD `-0.1258`
- `risk_on_and_context->commodity_4h` score `2.9152` n `32` status `ready` deltaP `20.3506` edge `0.1255` maxDD `-0.1258`
- `market_context_high->commodity_24h` score `2.857` n `150` status `ready` deltaP `22.2917` edge `0.1698` maxDD `-2.4263`
- `news_risk_high->index_24h` score `2.2899` n `36` status `ready` deltaP `14.5833` edge `0.0936` maxDD `0.0`
- `news_risk_high->index_4h` score `1.7031` n `36` status `ready` deltaP `20.0711` edge `0.0213` maxDD `-0.0546`
- `news_risk_high->equity_1h` score `1.6122` n `36` status `ready` deltaP `8.2835` edge `0.111` maxDD `-0.5496`
- `market_context_high->commodity_4h` score `1.5536` n `150` status `ready` deltaP `16.8923` edge `0.0807` maxDD `-2.1077`
- `risk_on_high->commodity_1h` score `1.3198` n `32` status `ready` deltaP `13.9596` edge `0.0402` maxDD `-0.1957`
- `risk_on_and_context->commodity_1h` score `1.3198` n `32` status `ready` deltaP `13.9596` edge `0.0402` maxDD `-0.1957`
- `risk_on_high->fx_24h` score `1.1996` n `32` status `ready` deltaP `14.2361` edge `0.0235` maxDD `-0.1418`
- `risk_on_and_context->fx_24h` score `1.1996` n `32` status `ready` deltaP `14.2361` edge `0.0235` maxDD `-0.1418`
- `risk_on_high->crypto_major_24h` score `1.1878` n `32` status `ready` deltaP `11.4583` edge `0.1915` maxDD `-6.2481`
- `risk_on_and_context->crypto_major_24h` score `1.1878` n `32` status `ready` deltaP `11.4583` edge `0.1915` maxDD `-6.2481`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
