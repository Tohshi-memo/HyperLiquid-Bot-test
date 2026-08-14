# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-14T12:02:05.810226+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11808`

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

- `market_context_high->unknown_24h` score `91.7048` n `149` status `ready` deltaP `-30.7489` edge `8.1383` maxDD `-9.6329`
- `risk_on_high->unknown_24h` score `32.954` n `32` status `ready` deltaP `-44.4444` edge `4.5962` maxDD `-1.6689`
- `risk_on_and_context->unknown_24h` score `32.954` n `32` status `ready` deltaP `-44.4444` edge `4.5962` maxDD `-1.6689`
- `news_risk_high->equity_24h` score `9.6874` n `36` status `ready` deltaP `10.0694` edge `0.7781` maxDD `-1.0358`
- `news_risk_high->equity_4h` score `7.1854` n `36` status `ready` deltaP `38.2622` edge `0.3437` maxDD `0.0`
- `risk_on_high->commodity_24h` score `4.7841` n `32` status `ready` deltaP `32.2917` edge `0.1834` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `4.7841` n `32` status `ready` deltaP `32.2917` edge `0.1834` maxDD `0.0`
- `market_context_high->commodity_24h` score `2.8624` n `149` status `ready` deltaP `22.2246` edge `0.1707` maxDD `-2.4263`
- `risk_on_high->commodity_4h` score `2.782` n `32` status `ready` deltaP `19.436` edge `0.1205` maxDD `-0.1258`
- `risk_on_and_context->commodity_4h` score `2.782` n `32` status `ready` deltaP `19.436` edge `0.1205` maxDD `-0.1258`
- `news_risk_high->index_24h` score `2.1579` n `36` status `ready` deltaP `14.5833` edge `0.0826` maxDD `0.0`
- `risk_on_high->crypto_major_24h` score `1.8246` n `32` status `ready` deltaP `15.7986` edge `0.2442` maxDD `-6.2481`
- `risk_on_and_context->crypto_major_24h` score `1.8246` n `32` status `ready` deltaP `15.7986` edge `0.2442` maxDD `-6.2481`
- `news_risk_high->index_4h` score `1.6993` n `36` status `ready` deltaP `19.9187` edge `0.022` maxDD `-0.0546`
- `news_risk_high->equity_1h` score `1.6446` n `36` status `ready` deltaP `8.4332` edge `0.1127` maxDD `-0.5496`
- `market_context_high->commodity_4h` score `1.3817` n `149` status `ready` deltaP `15.8076` edge `0.0736` maxDD `-2.1077`
- `risk_on_high->commodity_1h` score `1.2288` n `32` status `ready` deltaP `13.0614` edge `0.0386` maxDD `-0.1957`
- `risk_on_and_context->commodity_1h` score `1.2288` n `32` status `ready` deltaP `13.0614` edge `0.0386` maxDD `-0.1957`
- `risk_on_high->fx_24h` score `1.202` n `32` status `ready` deltaP `14.2361` edge `0.0237` maxDD `-0.1418`
- `risk_on_and_context->fx_24h` score `1.202` n `32` status `ready` deltaP `14.2361` edge `0.0237` maxDD `-0.1418`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
