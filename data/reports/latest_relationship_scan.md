# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-10T21:07:29.110825+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11712`

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

- `market_context_high->fx_24h` score `0.9777` n `145` status `ready` deltaP `20.4064` edge `0.0262` maxDD `-1.4613`
- `market_context_high->commodity_4h` score `0.9041` n `177` status `ready` deltaP `12.2107` edge `0.0654` maxDD `-2.7169`
- `market_context_high->commodity_1h` score `0.6249` n `185` status `ready` deltaP `8.6357` edge `0.0288` maxDD `-0.7439`
- `market_context_high->fx_1h` score `-0.1199` n `185` status `ready` deltaP `4.453` edge `0.0001` maxDD `-0.613`
- `market_context_high->fx_4h` score `-0.1345` n `177` status `ready` deltaP `6.2646` edge `0.007` maxDD `-0.4647`
- `market_context_high->equity_24h` score `-0.4404` n `145` status `ready` deltaP `0.8582` edge `0.3012` maxDD `-21.0709`
- `market_context_high->index_1h` score `-0.6157` n `185` status `ready` deltaP `-4.2207` edge `-0.0029` maxDD `-0.832`
- `market_context_high->index_24h` score `-0.6775` n `145` status `ready` deltaP `0.7028` edge `0.092` maxDD `-5.9181`
- `market_context_high->metal_24h` score `-0.843` n `145` status `ready` deltaP `2.5482` edge `0.0452` maxDD `-2.9283`
- `market_context_high->index_4h` score `-0.8635` n `177` status `ready` deltaP `-3.1875` edge `-0.0104` maxDD `-1.3245`
- `market_context_high->equity_1h` score `-1.038` n `185` status `ready` deltaP `-3.4228` edge `-0.0066` maxDD `-5.9591`
- `market_context_high->metal_1h` score `-1.2359` n `185` status `ready` deltaP `-4.6035` edge `-0.0087` maxDD `-2.0884`
- `market_context_high->crypto_alt_1h` score `-2.7321` n `185` status `ready` deltaP `-9.8592` edge `-0.0422` maxDD `-6.5795`
- `market_context_high->crypto_major_24h` score `-2.8718` n `145` status `ready` deltaP `-2.3989` edge `-0.0717` maxDD `-16.7723`
- `market_context_high->metal_4h` score `-3.0532` n `177` status `ready` deltaP `-6.4868` edge `-0.0348` maxDD `-6.1111`
- `market_context_high->equity_4h` score `-3.473` n `177` status `ready` deltaP `-12.2718` edge `-0.0999` maxDD `-12.0832`
- `market_context_high->crypto_major_1h` score `-3.6965` n `185` status `ready` deltaP `-9.7839` edge `-0.0524` maxDD `-11.9002`
- `market_context_high->crypto_alt_24h` score `-5.6135` n `145` status `ready` deltaP `-12.8226` edge `-0.1684` maxDD `-11.1127`
- `market_context_high->crypto_alt_4h` score `-6.1484` n `177` status `ready` deltaP `-12.3166` edge `-0.1367` maxDD `-16.8181`
- `market_context_high->commodity_24h` score `-7.6638` n `145` status `ready` deltaP `-3.067` edge `-0.1364` maxDD `-49.7223`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
