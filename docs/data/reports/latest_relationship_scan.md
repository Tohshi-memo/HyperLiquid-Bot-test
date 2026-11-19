# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-19T11:07:24.486300+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `24`

- Symbol pattern count: `2572`

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

- `market_context_high->unknown_1h` score `11728.5689` n `110` status `ready` deltaP `0.9064` edge `977.3945` maxDD `-0.9174`
- `market_context_high->unknown_4h` score `7276.7147` n `110` status `ready` deltaP `0.1968` edge `606.42` maxDD `-0.6067`
- `market_context_high->crypto_major_24h` score `13.3611` n `96` status `ready` deltaP `41.1459` edge `1.6825` maxDD `-16.8411`
- `market_context_high->crypto_alt_24h` score `10.7922` n `96` status `ready` deltaP `22.2222` edge `1.4219` maxDD `-11.2484`
- `market_context_high->crypto_major_4h` score `0.152` n `110` status `ready` deltaP `1.8459` edge `0.327` maxDD `-19.2526`
- `market_context_high->metal_24h` score `-0.1141` n `96` status `ready` deltaP `15.9722` edge `0.1964` maxDD `-14.9915`
- `market_context_high->crypto_alt_4h` score `-0.127` n `110` status `ready` deltaP `2.3032` edge `0.211` maxDD `-14.7439`
- `market_context_high->metal_4h` score `-0.1442` n `110` status `ready` deltaP `14.4706` edge `0.0205` maxDD `-5.9858`
- `market_context_high->metal_1h` score `-0.3002` n `110` status `ready` deltaP `2.3843` edge `0.0121` maxDD `-2.6517`
- `market_context_high->index_1h` score `-0.7962` n `110` status `ready` deltaP `-1.5515` edge `0.0028` maxDD `-1.2295`
- `market_context_high->crypto_major_1h` score `-0.855` n `110` status `ready` deltaP `2.2346` edge `0.0622` maxDD `-10.2705`
- `market_context_high->crypto_alt_1h` score `-1.1055` n `110` status `ready` deltaP `-2.4497` edge `0.0249` maxDD `-7.6911`
- `market_context_high->index_4h` score `-1.2278` n `110` status `ready` deltaP `-3.326` edge `-0.0009` maxDD `-4.7471`
- `market_context_high->fx_1h` score `-1.4767` n `110` status `ready` deltaP `-10.0436` edge `-0.0012` maxDD `-0.392`
- `market_context_high->fx_4h` score `-2.4331` n `110` status `ready` deltaP `-15.5404` edge `-0.0041` maxDD `-2.0058`
- `market_context_high->commodity_1h` score `-2.5327` n `110` status `ready` deltaP `-11.2412` edge `-0.0283` maxDD `-3.9584`
- `market_context_high->equity_1h` score `-2.6963` n `110` status `ready` deltaP `1.1758` edge `-0.0205` maxDD `-10.9626`
- `market_context_high->fx_24h` score `-6.7955` n `96` status `ready` deltaP `-19.6181` edge `-0.0054` maxDD `-5.7418`
- `market_context_high->commodity_4h` score `-7.6059` n `110` status `ready` deltaP `-25.1164` edge `-0.1045` maxDD `-14.9509`
- `market_context_high->index_24h` score `-9.2574` n `96` status `ready` deltaP `-17.0139` edge `-0.1158` maxDD `-20.7114`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
