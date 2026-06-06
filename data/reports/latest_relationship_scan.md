# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-06T17:52:26.936103+00:00`
- Price records: `672`
- Market context records: `3097`
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

- `market_context_high->crypto_alt_24h` score `16.5803` n `82` status `ready` deltaP `14.3546` edge `2.5576` maxDD `-33.5432`
- `market_context_high->commodity_24h` score `15.1818` n `82` status `ready` deltaP `45.1008` edge `1.0073` maxDD `-2.0927`
- `market_context_high->unknown_24h` score `14.8901` n `82` status `ready` deltaP `22.6711` edge `1.1385` maxDD `-1.9039`
- `market_context_high->index_24h` score `10.8322` n `82` status `ready` deltaP `32.3891` edge `0.923` maxDD `-14.8998`
- `market_context_high->equity_24h` score `7.4961` n `82` status `ready` deltaP `18.2461` edge `1.3601` maxDD `-35.9896`
- `market_context_high->commodity_4h` score `3.0338` n `116` status `ready` deltaP `17.9878` edge `0.1787` maxDD `-1.9973`
- `market_context_high->unknown_4h` score `0.9634` n `116` status `ready` deltaP `6.1764` edge `0.1047` maxDD `-2.914`
- `market_context_high->commodity_1h` score `-0.0758` n `120` status `ready` deltaP `1.3872` edge `0.0267` maxDD `-1.7142`
- `market_context_high->index_1h` score `-0.4963` n `120` status `ready` deltaP `3.997` edge `0.016` maxDD `-4.5023`
- `market_context_high->fx_24h` score `-0.6229` n `82` status `ready` deltaP `3.7136` edge `-0.0039` maxDD `-0.4876`
- `market_context_high->fx_1h` score `-0.6807` n `120` status `ready` deltaP `-7.2006` edge `-0.002` maxDD `-0.3147`
- `market_context_high->crypto_alt_1h` score `-0.8481` n `120` status `ready` deltaP `2.9291` edge `0.0847` maxDD `-14.7034`
- `market_context_high->equity_1h` score `-1.3549` n `120` status `ready` deltaP `-3.3333` edge `-0.0029` maxDD `-8.8863`
- `market_context_high->fx_4h` score `-1.3977` n `116` status `ready` deltaP `-13.3831` edge `-0.0056` maxDD `-1.0829`
- `market_context_high->index_4h` score `-1.4109` n `116` status `ready` deltaP `9.9927` edge `0.0434` maxDD `-17.6057`
- `market_context_high->crypto_major_1h` score `-2.3212` n `120` status `ready` deltaP `-1.7465` edge `0.0445` maxDD `-15.1032`
- `market_context_high->metal_1h` score `-2.3989` n `120` status `ready` deltaP `-7.1757` edge `-0.0127` maxDD `-7.4828`
- `market_context_high->unknown_1h` score `-2.6566` n `120` status `ready` deltaP `3.3084` edge `-0.059` maxDD `-12.7554`
- `market_context_high->crypto_alt_4h` score `-3.7355` n `116` status `ready` deltaP `13.3147` edge `0.2368` maxDD `-58.6918`
- `market_context_high->equity_4h` score `-4.1378` n `116` status `ready` deltaP `5.4773` edge `-0.0409` maxDD `-36.4212`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
