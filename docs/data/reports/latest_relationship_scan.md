# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-12T09:22:32.844390+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11792`

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

- `risk_on_high->equity_24h` score `3.628` n `32` status `ready` deltaP `9.5486` edge `0.5794` maxDD `-11.2348`
- `risk_on_and_context->equity_24h` score `3.628` n `32` status `ready` deltaP `9.5486` edge `0.5794` maxDD `-11.2348`
- `risk_on_high->crypto_major_24h` score `3.2768` n `32` status `ready` deltaP `22.3958` edge `0.3864` maxDD `-6.2481`
- `risk_on_and_context->crypto_major_24h` score `3.2768` n `32` status `ready` deltaP `22.3958` edge `0.3864` maxDD `-6.2481`
- `risk_on_high->commodity_24h` score `2.2109` n `32` status `ready` deltaP `19.7917` edge `0.0523` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `2.2109` n `32` status `ready` deltaP `19.7917` edge `0.0523` maxDD `0.0`
- `risk_on_high->commodity_4h` score `2.1094` n `32` status `ready` deltaP `14.253` edge `0.099` maxDD `-0.1258`
- `risk_on_and_context->commodity_4h` score `2.1094` n `32` status `ready` deltaP `14.253` edge `0.099` maxDD `-0.1258`
- `risk_on_high->index_24h` score `2.0096` n `32` status `ready` deltaP `16.6667` edge `0.0868` maxDD `-0.4355`
- `risk_on_and_context->index_24h` score `2.0096` n `32` status `ready` deltaP `16.6667` edge `0.0868` maxDD `-0.4355`
- `risk_on_high->fx_24h` score `1.9028` n `32` status `ready` deltaP `21.1806` edge `0.0358` maxDD `-0.1418`
- `risk_on_and_context->fx_24h` score `1.9028` n `32` status `ready` deltaP `21.1806` edge `0.0358` maxDD `-0.1418`
- `risk_on_high->commodity_1h` score `1.0562` n `32` status `ready` deltaP `11.7141` edge `0.0332` maxDD `-0.1957`
- `risk_on_and_context->commodity_1h` score `1.0562` n `32` status `ready` deltaP `11.7141` edge `0.0332` maxDD `-0.1957`
- `risk_on_high->fx_4h` score `0.8257` n `32` status `ready` deltaP `9.5274` edge `0.0194` maxDD `-0.1285`
- `risk_on_and_context->fx_4h` score `0.8257` n `32` status `ready` deltaP `9.5274` edge `0.0194` maxDD `-0.1285`
- `market_context_high->commodity_1h` score `0.6494` n `180` status `ready` deltaP `9.6308` edge `0.0221` maxDD `-0.5752`
- `market_context_high->commodity_4h` score `0.3758` n `180` status `ready` deltaP `7.7947` edge `0.0432` maxDD `-2.1077`
- `risk_on_high->index_1h` score `0.3467` n `32` status `ready` deltaP `10.7036` edge `0.0106` maxDD `-0.3343`
- `risk_on_and_context->index_1h` score `0.3467` n `32` status `ready` deltaP `10.7036` edge `0.0106` maxDD `-0.3343`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
