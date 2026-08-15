# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-15T14:07:31.918224+00:00`
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

- `market_context_high->unknown_24h` score `137.6123` n `128` status `ready` deltaP `-23.7693` edge `11.9174` maxDD `-9.6329`
- `risk_on_high->unknown_24h` score `33.727` n `32` status `ready` deltaP `-37.0505` edge `4.646` maxDD `-1.6689`
- `risk_on_and_context->unknown_24h` score `33.727` n `32` status `ready` deltaP `-37.0505` edge `4.646` maxDD `-1.6689`
- `news_risk_high->equity_24h` score `12.8684` n `36` status `ready` deltaP `25.9676` edge `0.9372` maxDD `-1.0358`
- `news_risk_high->equity_4h` score `7.7329` n `36` status `ready` deltaP `40.3963` edge `0.3751` maxDD `0.0`
- `market_context_high->commodity_24h` score `5.4291` n `128` status `ready` deltaP `31.4517` edge `0.2485` maxDD `-0.1266`
- `risk_on_high->commodity_24h` score `5.0052` n `32` status `ready` deltaP `33.7955` edge `0.1918` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `5.0052` n `32` status `ready` deltaP `33.7955` edge `0.1918` maxDD `0.0`
- `risk_on_high->crypto_major_24h` score `4.2269` n `32` status `ready` deltaP `28.2008` edge `0.4695` maxDD `-6.2481`
- `risk_on_and_context->crypto_major_24h` score `4.2269` n `32` status `ready` deltaP `28.2008` edge `0.4695` maxDD `-6.2481`
- `news_risk_high->index_24h` score `3.6281` n `36` status `ready` deltaP `30.156` edge `0.1013` maxDD `0.0`
- `risk_on_high->commodity_4h` score `2.916` n `32` status `ready` deltaP `20.9604` edge `0.1215` maxDD `-0.1258`
- `risk_on_and_context->commodity_4h` score `2.916` n `32` status `ready` deltaP `20.9604` edge `0.1215` maxDD `-0.1258`
- `market_context_high->commodity_4h` score `1.9681` n `128` status `ready` deltaP `19.3979` edge `0.0818` maxDD `-0.7687`
- `news_risk_high->index_4h` score `1.9388` n `36` status `ready` deltaP `22.3577` edge `0.0257` maxDD `-0.0546`
- `news_risk_high->equity_1h` score `1.7478` n `36` status `ready` deltaP `8.4332` edge `0.1213` maxDD `-0.5496`
- `risk_on_high->commodity_1h` score `1.3617` n `32` status `ready` deltaP `14.5584` edge `0.0397` maxDD `-0.1957`
- `risk_on_and_context->commodity_1h` score `1.3617` n `32` status `ready` deltaP `14.5584` edge `0.0397` maxDD `-0.1957`
- `market_context_high->commodity_1h` score `0.7251` n `128` status `ready` deltaP `9.8709` edge `0.0243` maxDD `-0.3742`
- `risk_on_high->equity_24h` score `0.7183` n `32` status `ready` deltaP `14.5093` edge `0.1733` maxDD `-11.2348`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
