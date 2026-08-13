# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-13T03:22:25.526972+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11840`

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

- `news_risk_high->equity_4h` score `7.0146` n `36` status `ready` deltaP `37.9573` edge `0.3315` maxDD `0.0`
- `risk_on_high->commodity_24h` score `2.3885` n `32` status `ready` deltaP `19.7917` edge `0.0671` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `2.3885` n `32` status `ready` deltaP `19.7917` edge `0.0671` maxDD `0.0`
- `risk_on_high->commodity_4h` score `2.2901` n `32` status `ready` deltaP `15.7774` edge `0.1039` maxDD `-0.1258`
- `risk_on_and_context->commodity_4h` score `2.2901` n `32` status `ready` deltaP `15.7774` edge `0.1039` maxDD `-0.1258`
- `news_risk_high->index_4h` score `2.0318` n `36` status `ready` deltaP `22.815` edge `0.0304` maxDD `-0.0546`
- `risk_on_high->crypto_major_24h` score `1.9873` n `32` status `ready` deltaP `15.9722` edge `0.2639` maxDD `-6.2481`
- `risk_on_and_context->crypto_major_24h` score `1.9873` n `32` status `ready` deltaP `15.9722` edge `0.2639` maxDD `-6.2481`
- `risk_on_high->fx_24h` score `1.8539` n `32` status `ready` deltaP `20.6597` edge `0.0352` maxDD `-0.1418`
- `risk_on_and_context->fx_24h` score `1.8539` n `32` status `ready` deltaP `20.6597` edge `0.0352` maxDD `-0.1418`
- `news_risk_high->equity_1h` score `1.5607` n `36` status `ready` deltaP `7.8344` edge `0.1097` maxDD `-0.5496`
- `risk_on_high->commodity_1h` score `1.1904` n `32` status `ready` deltaP `13.0614` edge `0.0354` maxDD `-0.1957`
- `risk_on_and_context->commodity_1h` score `1.1904` n `32` status `ready` deltaP `13.0614` edge `0.0354` maxDD `-0.1957`
- `market_context_high->commodity_4h` score `1.1085` n `161` status `ready` deltaP `13.4288` edge `0.0667` maxDD `-2.1077`
- `risk_on_high->fx_4h` score `1.0802` n `32` status `ready` deltaP `12.4238` edge `0.0213` maxDD `-0.1285`
- `risk_on_and_context->fx_4h` score `1.0802` n `32` status `ready` deltaP `12.4238` edge `0.0213` maxDD `-0.1285`
- `market_context_high->commodity_1h` score `0.9164` n `161` status `ready` deltaP `11.3921` edge `0.0301` maxDD `-0.3742`
- `market_context_high->commodity_24h` score `0.4196` n `161` status `ready` deltaP `9.8538` edge `0.0496` maxDD `-2.4263`
- `news_risk_high->fx_4h` score `0.2357` n `36` status `ready` deltaP `7.9099` edge `-0.0006` maxDD `-0.0863`
- `risk_on_high->index_1h` score `0.2182` n `32` status `ready` deltaP `8.6078` edge `0.0081` maxDD `-0.3343`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
