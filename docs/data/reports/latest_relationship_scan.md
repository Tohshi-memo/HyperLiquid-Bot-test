# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-15T06:37:30.874771+00:00`
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

- `market_context_high->unknown_24h` score `136.7246` n `128` status `ready` deltaP `-28.3855` edge `11.8742` maxDD `-9.6329`
- `risk_on_high->unknown_24h` score `33.15` n `32` status `ready` deltaP `-41.6667` edge `4.6028` maxDD `-1.6689`
- `risk_on_and_context->unknown_24h` score `33.15` n `32` status `ready` deltaP `-41.6667` edge `4.6028` maxDD `-1.6689`
- `news_risk_high->equity_24h` score `11.8541` n `36` status `ready` deltaP `20.8333` edge `0.8869` maxDD `-1.0358`
- `news_risk_high->equity_4h` score `7.4736` n `36` status `ready` deltaP `38.4146` edge `0.3667` maxDD `0.0`
- `market_context_high->commodity_24h` score `4.9677` n `128` status `ready` deltaP `28.0381` edge `0.2328` maxDD `-0.1266`
- `risk_on_high->commodity_24h` score `4.5438` n `32` status `ready` deltaP `30.3819` edge `0.1761` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `4.5438` n `32` status `ready` deltaP `30.3819` edge `0.1761` maxDD `0.0`
- `risk_on_high->crypto_major_24h` score `4.1033` n `32` status `ready` deltaP `27.4306` edge `0.4588` maxDD `-6.2481`
- `risk_on_and_context->crypto_major_24h` score `4.1033` n `32` status `ready` deltaP `27.4306` edge `0.4588` maxDD `-6.2481`
- `news_risk_high->index_24h` score `3.11` n `36` status `ready` deltaP `25.0` edge `0.0925` maxDD `0.0`
- `risk_on_high->commodity_4h` score `2.7596` n `32` status `ready` deltaP `19.7409` edge `0.1166` maxDD `-0.1258`
- `risk_on_and_context->commodity_4h` score `2.7596` n `32` status `ready` deltaP `19.7409` edge `0.1166` maxDD `-0.1258`
- `market_context_high->commodity_4h` score `1.8118` n `128` status `ready` deltaP `18.1784` edge `0.0769` maxDD `-0.7687`
- `news_risk_high->index_4h` score `1.7403` n `36` status `ready` deltaP `20.0711` edge `0.0244` maxDD `-0.0546`
- `news_risk_high->equity_1h` score `1.6795` n `36` status `ready` deltaP `7.8344` edge `0.1196` maxDD `-0.5496`
- `risk_on_high->commodity_1h` score `1.1988` n `32` status `ready` deltaP `12.762` edge `0.0381` maxDD `-0.1957`
- `risk_on_and_context->commodity_1h` score `1.1988` n `32` status `ready` deltaP `12.762` edge `0.0381` maxDD `-0.1957`
- `risk_on_high->fx_24h` score `0.599` n `32` status `ready` deltaP `8.3333` edge `0.0128` maxDD `-0.1418`
- `risk_on_and_context->fx_24h` score `0.599` n `32` status `ready` deltaP `8.3333` edge `0.0128` maxDD `-0.1418`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
