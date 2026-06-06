# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-06T02:37:21.057991+00:00`
- Price records: `672`
- Market context records: `3030`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `6987`

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

- `market_context_high->crypto_alt_24h` score `22.656` n `99` status `ready` deltaP `10.8112` edge `2.2076` maxDD `-22.6673`
- `market_context_high->unknown_24h` score `12.9043` n `99` status `ready` deltaP `22.7589` edge `0.9701` maxDD `-1.7175`
- `market_context_high->commodity_24h` score `12.7181` n `99` status `ready` deltaP `42.3769` edge `0.8014` maxDD `-1.2589`
- `market_context_high->equity_24h` score `7.7287` n `99` status `ready` deltaP `21.6383` edge `1.1218` maxDD `-18.3486`
- `market_context_high->index_24h` score `7.5213` n `99` status `ready` deltaP `21.2279` edge `0.6108` maxDD `-4.7103`
- `market_context_high->commodity_4h` score `2.8204` n `120` status `ready` deltaP `19.2073` edge `0.1717` maxDD `-2.8438`
- `market_context_high->commodity_1h` score `0.0553` n `129` status `ready` deltaP `2.5902` edge `0.0296` maxDD `-1.7142`
- `market_context_high->index_4h` score `0.0028` n `120` status `ready` deltaP `15.2439` edge `0.0915` maxDD `-11.0881`
- `market_context_high->crypto_alt_4h` score `-0.1267` n `120` status `ready` deltaP `21.504` edge `0.3952` maxDD `-38.7172`
- `market_context_high->index_1h` score `-0.4107` n `129` status `ready` deltaP `3.7878` edge `0.0235` maxDD `-4.1126`
- `market_context_high->unknown_4h` score `-0.4139` n `120` status `ready` deltaP `1.3415` edge `0.0619` maxDD `-3.7602`
- `market_context_high->equity_1h` score `-0.4785` n `129` status `ready` deltaP `3.7182` edge `0.0354` maxDD `-6.7232`
- `market_context_high->fx_1h` score `-0.533` n `129` status `ready` deltaP `-4.7394` edge `0.0001` maxDD `-0.2801`
- `market_context_high->crypto_alt_1h` score `-0.5638` n `129` status `ready` deltaP `6.3861` edge `0.0981` maxDD `-14.7034`
- `market_context_high->equity_4h` score `-0.5858` n `120` status `ready` deltaP `12.185` edge `0.1241` maxDD `-20.102`
- `market_context_high->unknown_1h` score `-0.8417` n `129` status `ready` deltaP `3.7715` edge `-0.0222` maxDD `-3.1801`
- `market_context_high->crypto_major_1h` score `-0.9957` n `129` status `ready` deltaP `4.2798` edge `0.0701` maxDD `-15.1032`
- `market_context_high->fx_4h` score `-1.038` n `120` status `ready` deltaP `-7.6524` edge `-0.002` maxDD `-0.7382`
- `market_context_high->metal_1h` score `-1.1419` n `129` status `ready` deltaP `-1.7987` edge `-0.0026` maxDD `-6.8783`
- `market_context_high->fx_24h` score `-1.5756` n `99` status `ready` deltaP `-3.3617` edge `-0.0217` maxDD `-0.6418`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
