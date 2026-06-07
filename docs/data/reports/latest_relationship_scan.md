# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-07T20:07:22.122458+00:00`
- Price records: `672`
- Market context records: `3212`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `104`

- Symbol pattern count: `11150`

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

- `market_context_high->commodity_24h` score `13.7922` n `100` status `ready` deltaP `47.7708` edge `0.8737` maxDD `-2.0927`
- `market_context_high->crypto_alt_24h` score `11.596` n `100` status `ready` deltaP `13.8264` edge `2.3921` maxDD `-71.142`
- `market_context_high->index_24h` score `9.3146` n `100` status `ready` deltaP `28.9444` edge `0.8387` maxDD `-16.1026`
- `market_context_high->equity_24h` score `5.0967` n `100` status `ready` deltaP `13.3264` edge `1.4062` maxDD `-53.663`
- `market_context_high->commodity_4h` score `3.4716` n `126` status `ready` deltaP `22.5005` edge `0.1851` maxDD `-1.9973`
- `market_context_high->commodity_1h` score `0.5915` n `138` status `ready` deltaP `7.2225` edge `0.0434` maxDD `-1.7142`
- `market_context_high->fx_24h` score `-0.0717` n `100` status `ready` deltaP `7.5625` edge `-0.0063` maxDD `-1.0074`
- `market_context_high->unknown_4h` score `-0.089` n `126` status `ready` deltaP `10.2014` edge `0.1468` maxDD `-14.7778`
- `market_context_high->index_1h` score `-0.9997` n `138` status `ready` deltaP `2.2455` edge `0.008` maxDD `-4.5023`
- `market_context_high->fx_4h` score `-1.0514` n `126` status `ready` deltaP `-6.2283` edge `-0.0048` maxDD `-1.4115`
- `market_context_high->fx_1h` score `-1.5952` n `138` status `ready` deltaP `-8.9473` edge `-0.0046` maxDD `-0.8278`
- `market_context_high->crypto_alt_1h` score `-1.5999` n `138` status `ready` deltaP `3.6948` edge `0.0675` maxDD `-14.7034`
- `market_context_high->index_4h` score `-1.6654` n `126` status `ready` deltaP `14.1333` edge `0.0579` maxDD `-17.6057`
- `market_context_high->equity_1h` score `-1.7732` n `138` status `ready` deltaP `1.3473` edge `-0.004` maxDD `-8.8863`
- `market_context_high->crypto_major_1h` score `-1.7972` n `138` status `ready` deltaP `3.8141` edge `0.0511` maxDD `-15.1032`
- `market_context_high->metal_1h` score `-2.2498` n `138` status `ready` deltaP `-4.1981` edge `-0.0129` maxDD `-8.0609`
- `market_context_high->unknown_1h` score `-2.8685` n `138` status `ready` deltaP `0.4556` edge `-0.1229` maxDD `-17.8311`
- `market_context_high->crypto_major_24h` score `-4.6486` n `100` status `ready` deltaP `11.4583` edge `1.6315` maxDD `-166.3093`
- `market_context_high->crypto_major_4h` score `-4.7409` n `126` status `ready` deltaP `5.1103` edge `0.1505` maxDD `-54.3896`
- `market_context_high->equity_4h` score `-4.9018` n `126` status `ready` deltaP `12.1468` edge `0.0411` maxDD `-36.7784`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
