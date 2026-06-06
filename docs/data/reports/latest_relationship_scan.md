# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-06T17:22:18.818849+00:00`
- Price records: `672`
- Market context records: `3095`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `6921`

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

- `market_context_high->crypto_alt_24h` score `16.364` n `84` status `ready` deltaP `13.5416` edge `2.5353` maxDD `-33.5432`
- `market_context_high->commodity_24h` score `15.1331` n `84` status `ready` deltaP `45.3621` edge `1.0015` maxDD `-2.0927`
- `market_context_high->unknown_24h` score `14.6505` n `84` status `ready` deltaP `22.9911` edge `1.1164` maxDD `-1.9039`
- `market_context_high->index_24h` score `10.7754` n `84` status `ready` deltaP `32.5645` edge `0.9171` maxDD `-14.8998`
- `market_context_high->equity_24h` score `7.6727` n `84` status `ready` deltaP `18.9732` edge `1.3779` maxDD `-35.9896`
- `market_context_high->commodity_4h` score `3.0401` n `117` status `ready` deltaP `18.2015` edge `0.1778` maxDD `-1.9973`
- `market_context_high->unknown_4h` score `0.7164` n `117` status `ready` deltaP `5.1035` edge `0.0996` maxDD `-2.914`
- `market_context_high->commodity_1h` score `-0.0097` n `122` status `ready` deltaP `2.1523` edge `0.0271` maxDD `-1.7142`
- `market_context_high->index_1h` score `-0.5047` n `122` status `ready` deltaP `3.8063` edge `0.0162` maxDD `-4.5023`
- `market_context_high->fx_1h` score `-0.6998` n `122` status `ready` deltaP `-7.5979` edge `-0.0018` maxDD `-0.3147`
- `market_context_high->crypto_alt_1h` score `-0.7882` n `122` status `ready` deltaP `3.4357` edge `0.089` maxDD `-14.7034`
- `market_context_high->fx_24h` score `-0.8311` n `84` status `ready` deltaP `2.4057` edge `-0.0042` maxDD `-0.4876`
- `market_context_high->equity_1h` score `-1.3164` n `122` status `ready` deltaP `-2.7584` edge `-0.0018` maxDD `-8.8863`
- `market_context_high->fx_4h` score `-1.3678` n `117` status `ready` deltaP `-12.8232` edge `-0.0055` maxDD `-1.0829`
- `market_context_high->index_4h` score `-1.4267` n `117` status `ready` deltaP `9.6441` edge `0.0437` maxDD `-17.6057`
- `market_context_high->crypto_major_1h` score `-2.2099` n `122` status `ready` deltaP `-0.9399` edge `0.0484` maxDD `-15.1032`
- `market_context_high->metal_1h` score `-2.3596` n `122` status `ready` deltaP `-6.8347` edge `-0.0117` maxDD `-7.4828`
- `market_context_high->unknown_1h` score `-2.7561` n `122` status `ready` deltaP `2.6652` edge `-0.063` maxDD `-12.7554`
- `market_context_high->crypto_alt_4h` score `-3.5829` n `117` status `ready` deltaP `14.2994` edge `0.2498` maxDD `-58.6918`
- `market_context_high->equity_4h` score `-4.0324` n `117` status `ready` deltaP `6.4103` edge `-0.0343` maxDD `-36.3664`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
