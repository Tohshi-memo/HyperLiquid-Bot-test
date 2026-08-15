# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-15T08:22:31.463326+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11700`

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

- `market_context_high->unknown_24h` score `137.1213` n `128` status `ready` deltaP `-27.5821` edge `11.9019` maxDD `-9.6329`
- `risk_on_high->unknown_24h` score `33.4078` n `32` status `ready` deltaP `-40.8633` edge `4.6305` maxDD `-1.6689`
- `risk_on_and_context->unknown_24h` score `33.4078` n `32` status `ready` deltaP `-40.8633` edge `4.6305` maxDD `-1.6689`
- `news_risk_high->equity_24h` score `12.0708` n `36` status `ready` deltaP `21.9815` edge `0.8973` maxDD `-1.0358`
- `news_risk_high->equity_4h` score `7.5696` n `36` status `ready` deltaP `39.2694` edge `0.369` maxDD `0.0`
- `market_context_high->commodity_24h` score `5.1325` n `128` status `ready` deltaP `29.1987` edge `0.2388` maxDD `-0.1266`
- `risk_on_high->commodity_24h` score `4.7086` n `32` status `ready` deltaP `31.5425` edge `0.1821` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `4.7086` n `32` status `ready` deltaP `31.5425` edge `0.1821` maxDD `0.0`
- `risk_on_high->crypto_major_24h` score `4.1417` n `32` status `ready` deltaP `27.5076` edge `0.4632` maxDD `-6.2481`
- `risk_on_and_context->crypto_major_24h` score `4.1417` n `32` status `ready` deltaP `27.5076` edge `0.4632` maxDD `-6.2481`
- `news_risk_high->index_24h` score `3.2252` n `36` status `ready` deltaP `26.1698` edge `0.0943` maxDD `0.0`
- `risk_on_high->commodity_4h` score `2.8698` n `32` status `ready` deltaP `20.743` edge `0.1191` maxDD `-0.1258`
- `risk_on_and_context->commodity_4h` score `2.8698` n `32` status `ready` deltaP `20.743` edge `0.1191` maxDD `-0.1258`
- `market_context_high->commodity_4h` score `1.9219` n `128` status `ready` deltaP `19.1805` edge `0.0794` maxDD `-0.7687`
- `news_risk_high->index_4h` score `1.8137` n `36` status `ready` deltaP `20.9284` edge `0.0248` maxDD `-0.0546`
- `news_risk_high->equity_1h` score `1.6915` n `36` status `ready` deltaP `7.9841` edge `0.1196` maxDD `-0.5496`
- `risk_on_high->commodity_1h` score `1.2743` n `32` status `ready` deltaP `13.5105` edge `0.0394` maxDD `-0.1957`
- `risk_on_and_context->commodity_1h` score `1.2743` n `32` status `ready` deltaP `13.5105` edge `0.0394` maxDD `-0.1957`
- `market_context_high->commodity_1h` score `0.6377` n `128` status `ready` deltaP `8.823` edge `0.024` maxDD `-0.3742`
- `risk_on_high->fx_4h` score `0.5496` n `32` status `ready` deltaP `6.7209` edge `0.0151` maxDD `-0.1285`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
