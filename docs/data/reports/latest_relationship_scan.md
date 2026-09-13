# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-13T03:52:27.459603+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `12599`

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

- `market_context_high->unknown_24h` score `16605.8459` n `59` status `ready` deltaP `12.5824` edge `1383.7418` maxDD `-0.082`
- `news_risk_high->unknown_1h` score `380.2671` n `82` status `ready` deltaP `-4.8014` edge `31.7631` maxDD `-1.7068`
- `news_risk_high->crypto_alt_24h` score `17.9531` n `82` status `ready` deltaP `32.2324` edge `1.33` maxDD `-2.2369`
- `news_risk_high->crypto_major_24h` score `17.9344` n `82` status `ready` deltaP `38.8042` edge `1.3829` maxDD `-9.098`
- `market_context_high->equity_24h` score `10.7105` n `59` status `ready` deltaP `47.9167` edge `0.5731` maxDD `0.0`
- `market_context_high->crypto_alt_24h` score `10.0545` n `59` status `ready` deltaP `22.187` edge `0.7727` maxDD `-3.9523`
- `news_risk_high->equity_24h` score `6.4534` n `82` status `ready` deltaP `17.4289` edge `0.5996` maxDD `-6.5742`
- `news_risk_high->index_24h` score `6.1916` n `82` status `ready` deltaP `43.1741` edge `0.2458` maxDD `-0.0797`
- `news_risk_high->metal_24h` score `4.855` n `82` status `ready` deltaP `26.6557` edge `0.2723` maxDD `-0.6334`
- `market_context_high->commodity_24h` score `4.239` n `59` status `ready` deltaP `42.1875` edge `0.072` maxDD `0.0`
- `market_context_high->index_24h` score `4.0702` n `59` status `ready` deltaP `43.7736` edge `0.0866` maxDD `-0.1391`
- `market_context_high->metal_24h` score `0.2647` n `59` status `ready` deltaP `7.4535` edge `0.104` maxDD `-2.9132`
- `news_risk_high->index_4h` score `0.226` n `82` status `ready` deltaP `9.4512` edge `0.0288` maxDD `-0.6935`
- `risk_on_high->crypto_alt_4h` score `0.0834` n `53` status `ready` deltaP `6.9087` edge `0.1321` maxDD `-6.7304`
- `risk_on_and_context->crypto_alt_4h` score `0.0834` n `53` status `ready` deltaP `6.9087` edge `0.1321` maxDD `-6.7304`
- `risk_on_high->fx_1h` score `-0.0254` n `63` status `ready` deltaP `3.0392` edge `0.0032` maxDD `-0.0464`
- `risk_on_and_context->fx_1h` score `-0.0254` n `63` status `ready` deltaP `3.0392` edge `0.0032` maxDD `-0.0464`
- `market_context_high->fx_1h` score `-0.123` n `121` status `ready` deltaP `2.6587` edge `-0.0019` maxDD `-0.5274`
- `risk_on_high->metal_1h` score `-0.2273` n `63` status `ready` deltaP `1.9009` edge `0.0014` maxDD `-0.3081`
- `risk_on_and_context->metal_1h` score `-0.2273` n `63` status `ready` deltaP `1.9009` edge `0.0014` maxDD `-0.3081`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
