# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-06T15:22:25.280096+00:00`
- Price records: `672`
- Market context records: `3085`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `6911`

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

- `market_context_high->crypto_alt_24h` score `16.9645` n `86` status `ready` deltaP `12.7664` edge `2.531` maxDD `-26.6275`
- `market_context_high->commodity_24h` score `15.0438` n `86` status `ready` deltaP `45.6113` edge `0.9924` maxDD `-2.0927`
- `market_context_high->unknown_24h` score `14.1286` n `86` status `ready` deltaP `20.9626` edge `1.0841` maxDD `-1.7175`
- `market_context_high->index_24h` score `11.7764` n `86` status `ready` deltaP `34.5203` edge `0.9326` maxDD `-11.5093`
- `market_context_high->equity_24h` score `9.1242` n `86` status `ready` deltaP `22.097` edge `1.4569` maxDD `-30.0893`
- `market_context_high->commodity_4h` score `3.0104` n `120` status `ready` deltaP `18.4451` edge `0.1737` maxDD `-1.9973`
- `market_context_high->unknown_4h` score `0.0312` n `120` status `ready` deltaP `3.4553` edge `0.0849` maxDD `-3.7602`
- `market_context_high->commodity_1h` score `-0.1081` n `124` status `ready` deltaP `0.9224` edge `0.0271` maxDD `-1.7142`
- `market_context_high->index_1h` score `-0.5005` n `124` status `ready` deltaP `3.9164` edge `0.016` maxDD `-4.5023`
- `market_context_high->crypto_alt_1h` score `-0.732` n `124` status `ready` deltaP `3.9164` edge `0.093` maxDD `-14.7034`
- `market_context_high->fx_24h` score `-1.0301` n `86` status `ready` deltaP `0.8277` edge `-0.0055` maxDD `-0.5357`
- `market_context_high->unknown_1h` score `-1.0655` n `124` status `ready` deltaP `1.3039` edge `-0.0244` maxDD `-3.1801`
- `market_context_high->fx_1h` score `-1.1926` n `124` status `ready` deltaP `-8.9869` edge `-0.0022` maxDD `-0.3147`
- `market_context_high->equity_1h` score `-1.2034` n `124` status `ready` deltaP `-1.1059` edge `0.0004` maxDD `-8.7845`
- `market_context_high->fx_4h` score `-1.306` n `120` status `ready` deltaP `-11.5752` edge `-0.0059` maxDD `-1.0829`
- `market_context_high->index_4h` score `-1.3936` n `120` status `ready` deltaP `9.7866` edge `0.047` maxDD `-17.6057`
- `market_context_high->crypto_major_1h` score `-1.9908` n `124` status `ready` deltaP `0.0434` edge `0.0601` maxDD `-15.1032`
- `market_context_high->metal_1h` score `-2.3937` n `124` status `ready` deltaP `-7.3064` edge `-0.0114` maxDD `-7.4828`
- `market_context_high->crypto_alt_4h` score `-3.2952` n `120` status `ready` deltaP `16.4431` edge `0.2724` maxDD `-58.6918`
- `market_context_high->equity_4h` score `-3.8043` n `120` status `ready` deltaP `8.0284` edge `-0.0174` maxDD `-36.242`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
