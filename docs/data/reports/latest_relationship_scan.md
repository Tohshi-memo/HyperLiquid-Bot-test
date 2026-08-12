# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-12T09:52:31.084119+00:00`
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

- `risk_on_high->equity_24h` score `3.4898` n `32` status `ready` deltaP `9.2014` edge `0.564` maxDD `-11.2348`
- `risk_on_and_context->equity_24h` score `3.4898` n `32` status `ready` deltaP `9.2014` edge `0.564` maxDD `-11.2348`
- `risk_on_high->crypto_major_24h` score `3.233` n `32` status `ready` deltaP `22.0486` edge `0.3831` maxDD `-6.2481`
- `risk_on_and_context->crypto_major_24h` score `3.233` n `32` status `ready` deltaP `22.0486` edge `0.3831` maxDD `-6.2481`
- `risk_on_high->commodity_24h` score `2.2531` n `32` status `ready` deltaP `20.1389` edge `0.0535` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `2.2531` n `32` status `ready` deltaP `20.1389` edge `0.0535` maxDD `0.0`
- `risk_on_high->commodity_4h` score `2.1518` n `32` status `ready` deltaP `14.5579` edge `0.1005` maxDD `-0.1258`
- `risk_on_and_context->commodity_4h` score `2.1518` n `32` status `ready` deltaP `14.5579` edge `0.1005` maxDD `-0.1258`
- `risk_on_high->index_24h` score `1.9554` n `32` status `ready` deltaP `16.3194` edge `0.0846` maxDD `-0.4355`
- `risk_on_and_context->index_24h` score `1.9554` n `32` status `ready` deltaP `16.3194` edge `0.0846` maxDD `-0.4355`
- `risk_on_high->fx_24h` score `1.9179` n `32` status `ready` deltaP `21.3542` edge `0.0359` maxDD `-0.1418`
- `risk_on_and_context->fx_24h` score `1.9179` n `32` status `ready` deltaP `21.3542` edge `0.0359` maxDD `-0.1418`
- `risk_on_high->commodity_1h` score `1.0885` n `32` status `ready` deltaP `12.0135` edge `0.0339` maxDD `-0.1957`
- `risk_on_and_context->commodity_1h` score `1.0885` n `32` status `ready` deltaP `12.0135` edge `0.0339` maxDD `-0.1957`
- `risk_on_high->fx_4h` score `0.8525` n `32` status `ready` deltaP `9.8323` edge `0.0196` maxDD `-0.1285`
- `risk_on_and_context->fx_4h` score `0.8525` n `32` status `ready` deltaP `9.8323` edge `0.0196` maxDD `-0.1285`
- `market_context_high->commodity_1h` score `0.6817` n `180` status `ready` deltaP `9.9302` edge `0.0228` maxDD `-0.5752`
- `market_context_high->commodity_4h` score `0.4182` n `180` status `ready` deltaP `8.0996` edge `0.0447` maxDD `-2.1077`
- `risk_on_high->index_1h` score `0.3381` n `32` status `ready` deltaP `10.5539` edge `0.0105` maxDD `-0.3343`
- `risk_on_and_context->index_1h` score `0.3381` n `32` status `ready` deltaP `10.5539` edge `0.0105` maxDD `-0.3343`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
