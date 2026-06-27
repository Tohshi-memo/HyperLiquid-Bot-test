# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-27T18:07:25.965480+00:00`
- Price records: `672`
- Market context records: `4958`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `88`

- Symbol pattern count: `9520`

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

- `market_context_high->unknown_1h` score `19.8779` n `94` status `ready` deltaP `9.772` edge `1.6331` maxDD `-1.674`
- `market_context_high->unknown_4h` score `12.1359` n `94` status `ready` deltaP `28.8661` edge `0.8703` maxDD `-1.7801`
- `market_context_high->crypto_major_4h` score `7.1599` n `94` status `ready` deltaP `21.1306` edge `0.5782` maxDD `-7.1265`
- `market_context_high->crypto_alt_4h` score `6.9258` n `94` status `ready` deltaP `21.5815` edge `0.5685` maxDD `-7.8181`
- `market_context_high->unknown_24h` score `5.7919` n `91` status `ready` deltaP `26.9727` edge `0.3371` maxDD `-1.4072`
- `market_context_high->equity_4h` score `1.6427` n `94` status `ready` deltaP `13.5216` edge `0.1849` maxDD `-6.3852`
- `market_context_high->metal_4h` score `1.4839` n `94` status `ready` deltaP `11.7184` edge `0.1201` maxDD `-1.9651`
- `market_context_high->crypto_major_1h` score `1.0262` n `94` status `ready` deltaP `9.9758` edge `0.1689` maxDD `-5.6406`
- `market_context_high->equity_1h` score `1.0079` n `94` status `ready` deltaP `9.1254` edge `0.0805` maxDD `-2.5875`
- `market_context_high->index_4h` score `0.8826` n `94` status `ready` deltaP `11.4038` edge `0.0437` maxDD `-0.6938`
- `market_context_high->crypto_alt_1h` score `0.8056` n `94` status `ready` deltaP `10.788` edge `0.1336` maxDD `-5.5126`
- `market_context_high->metal_1h` score `0.2129` n `94` status `ready` deltaP `5.7045` edge `0.0377` maxDD `-1.3057`
- `market_context_high->index_1h` score `-0.3338` n `94` status `ready` deltaP `2.908` edge `0.0133` maxDD `-0.7054`
- `market_context_high->commodity_1h` score `-0.3378` n `94` status `ready` deltaP `2.2296` edge `0.0078` maxDD `-1.278`
- `market_context_high->commodity_4h` score `-1.0487` n `94` status `ready` deltaP `6.5613` edge `-0.0066` maxDD `-4.9624`
- `market_context_high->fx_4h` score `-1.1239` n `94` status `ready` deltaP `-6.383` edge `-0.0045` maxDD `-1.0967`
- `market_context_high->fx_24h` score `-1.457` n `91` status `ready` deltaP `-1.303` edge `-0.0117` maxDD `-2.749`
- `market_context_high->fx_1h` score `-1.5435` n `94` status `ready` deltaP `-9.6382` edge `-0.0044` maxDD `-0.4646`
- `market_context_high->commodity_24h` score `-3.9959` n `91` status `ready` deltaP `19.6485` edge `0.0469` maxDD `-27.5371`
- `market_context_high->metal_24h` score `-6.8933` n `91` status `ready` deltaP `-8.9935` edge `0.031` maxDD `-32.9721`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
