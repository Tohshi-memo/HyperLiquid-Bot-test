# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-25T22:07:29.757510+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5062`

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

- `market_context_high->unknown_4h` score `29.7465` n `113` status `ready` deltaP `-0.7487` edge `2.5174` maxDD `-1.016`
- `market_context_high->crypto_major_24h` score `0.5583` n `79` status `ready` deltaP `5.5006` edge `0.1124` maxDD `-4.5369`
- `market_context_high->fx_4h` score `-0.0974` n `113` status `ready` deltaP `6.5441` edge `0.0081` maxDD `-0.4545`
- `market_context_high->fx_1h` score `-0.0988` n `113` status `ready` deltaP `2.9609` edge `0.0025` maxDD `-0.1258`
- `market_context_high->fx_24h` score `-0.3864` n `79` status `ready` deltaP `13.3791` edge `0.0185` maxDD `-1.2451`
- `market_context_high->commodity_1h` score `-0.4727` n `113` status `ready` deltaP `0.1166` edge `0.0099` maxDD `-1.0053`
- `market_context_high->index_1h` score `-0.669` n `113` status `ready` deltaP `-2.1859` edge `-0.006` maxDD `-1.2155`
- `market_context_high->metal_1h` score `-0.6814` n `113` status `ready` deltaP `4.185` edge `-0.0055` maxDD `-1.6682`
- `market_context_high->commodity_4h` score `-0.7764` n `113` status `ready` deltaP `-1.4759` edge `0.0332` maxDD `-1.165`
- `market_context_high->metal_24h` score `-0.9537` n `79` status `ready` deltaP `8.2586` edge `0.0897` maxDD `-7.3625`
- `market_context_high->index_24h` score `-1.1436` n `79` status `ready` deltaP `7.7862` edge `-0.0703` maxDD `-4.925`
- `market_context_high->crypto_major_1h` score `-1.3208` n `113` status `ready` deltaP `3.3967` edge `-0.0339` maxDD `-9.3126`
- `market_context_high->commodity_24h` score `-1.8048` n `79` status `ready` deltaP `-4.9007` edge `-0.0159` maxDD `-5.2916`
- `market_context_high->metal_4h` score `-2.0218` n `113` status `ready` deltaP `3.3941` edge `-0.0201` maxDD `-5.3474`
- `market_context_high->index_4h` score `-2.1783` n `113` status `ready` deltaP `-8.2249` edge `-0.037` maxDD `-4.3282`
- `market_context_high->crypto_alt_1h` score `-3.1703` n `113` status `ready` deltaP `-1.4109` edge `-0.0674` maxDD `-11.3243`
- `market_context_high->equity_1h` score `-3.9075` n `113` status `ready` deltaP `-0.8386` edge `-0.0927` maxDD `-12.1865`
- `market_context_high->crypto_alt_24h` score `-6.7791` n `79` status `ready` deltaP `-2.2459` edge `-0.2085` maxDD `-42.3182`
- `market_context_high->equity_24h` score `-8.4164` n `79` status `ready` deltaP `-4.1051` edge `-0.5233` maxDD `-36.6024`
- `market_context_high->crypto_major_4h` score `-10.1735` n `113` status `ready` deltaP `-13.9623` edge `-0.2549` maxDD `-32.9851`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
