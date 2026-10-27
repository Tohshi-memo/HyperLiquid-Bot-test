# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-27T05:07:27.081755+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9688`

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

- `market_context_high->unknown_4h` score `79.7681` n `147` status `ready` deltaP `2.999` edge `6.6609` maxDD `-1.0178`
- `market_context_high->unknown_1h` score `14.7319` n `147` status `ready` deltaP `0.9573` edge `1.2702` maxDD `-1.5807`
- `market_context_high->fx_4h` score `0.4413` n `147` status `ready` deltaP `13.0538` edge `0.0096` maxDD `-0.4545`
- `market_context_high->index_24h` score `0.4297` n `122` status `ready` deltaP `20.2645` edge `0.023` maxDD `-2.9075`
- `market_context_high->fx_1h` score `0.3662` n `147` status `ready` deltaP `9.4698` edge `0.0032` maxDD `-0.1986`
- `market_context_high->metal_24h` score `0.1306` n `122` status `ready` deltaP `21.0898` edge `0.1287` maxDD `-6.204`
- `market_context_high->metal_1h` score `0.0325` n `147` status `ready` deltaP `10.3415` edge `0.0099` maxDD `-1.3073`
- `market_context_high->commodity_1h` score `-0.0223` n `147` status `ready` deltaP `4.5165` edge `0.0181` maxDD `-1.0053`
- `market_context_high->fx_24h` score `-0.1761` n `122` status `ready` deltaP `16.4474` edge `0.025` maxDD `-1.2451`
- `market_context_high->commodity_4h` score `-0.3787` n `147` status `ready` deltaP `6.8151` edge `0.0459` maxDD `-1.165`
- `market_context_high->crypto_major_1h` score `-0.5661` n `147` status `ready` deltaP `5.6061` edge `0.0299` maxDD `-7.8544`
- `market_context_high->index_1h` score `-0.598` n `147` status `ready` deltaP `-0.2037` edge `-0.0016` maxDD `-1.8971`
- `market_context_high->metal_4h` score `-0.7615` n `147` status `ready` deltaP `9.7913` edge `0.0013` maxDD `-4.8031`
- `market_context_high->equity_1h` score `-1.6341` n `147` status `ready` deltaP `2.4909` edge `0.0015` maxDD `-12.2088`
- `market_context_high->crypto_alt_1h` score `-1.8424` n `147` status `ready` deltaP `0.2739` edge `0.0064` maxDD `-12.8878`
- `market_context_high->index_4h` score `-3.4036` n `147` status `ready` deltaP `-6.2168` edge `-0.0266` maxDD `-6.5801`
- `market_context_high->equity_24h` score `-3.5271` n `122` status `ready` deltaP `-1.4873` edge `-0.0736` maxDD `-21.4942`
- `market_context_high->crypto_major_24h` score `-3.7836` n `122` status `ready` deltaP `2.7048` edge `-0.0174` maxDD `-29.1905`
- `market_context_high->crypto_major_4h` score `-4.1012` n `147` status `ready` deltaP `0.727` edge `-0.0722` maxDD `-29.3419`
- `market_context_high->equity_4h` score `-6.4308` n `147` status `ready` deltaP `-0.0715` edge `-0.1564` maxDD `-42.74`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
