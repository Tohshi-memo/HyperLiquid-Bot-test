# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-04T15:37:25.575421+00:00`
- Price records: `672`
- Market context records: `5677`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `8758`

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

- `market_context_high->equity_24h` score `1.9908` n `200` status `ready` deltaP `16.1389` edge `0.5662` maxDD `-31.6316`
- `market_context_high->crypto_major_4h` score `0.9338` n `250` status `ready` deltaP `11.7134` edge `0.2225` maxDD `-13.4882`
- `market_context_high->crypto_alt_4h` score `0.4742` n `250` status `ready` deltaP `8.7793` edge `0.162` maxDD `-9.1473`
- `market_context_high->equity_4h` score `0.213` n `250` status `ready` deltaP `5.7317` edge `0.1434` maxDD `-7.4425`
- `market_context_high->fx_1h` score `-0.2465` n `262` status `ready` deltaP `2.2227` edge `0.0012` maxDD `-0.4764`
- `market_context_high->crypto_alt_1h` score `-0.4475` n `262` status `ready` deltaP `2.6489` edge `0.0412` maxDD `-5.0257`
- `market_context_high->equity_1h` score `-0.4754` n `262` status `ready` deltaP `4.6167` edge `0.0303` maxDD `-5.0555`
- `market_context_high->index_1h` score `-0.573` n `262` status `ready` deltaP `1.257` edge `0.005` maxDD `-0.9472`
- `market_context_high->crypto_major_1h` score `-0.6277` n `262` status `ready` deltaP `4.2808` edge `0.0437` maxDD `-6.9639`
- `market_context_high->metal_1h` score `-0.7594` n `262` status `ready` deltaP `0.6959` edge `-0.0004` maxDD `-2.0682`
- `market_context_high->fx_24h` score `-0.8209` n `200` status `ready` deltaP `14.9514` edge `0.0486` maxDD `-3.0011`
- `market_context_high->commodity_1h` score `-0.9193` n `262` status `ready` deltaP `0.5165` edge `-0.0035` maxDD `-3.7906`
- `market_context_high->fx_4h` score `-1.1906` n `250` status `ready` deltaP `3.6` edge `0.0068` maxDD `-1.3415`
- `market_context_high->index_4h` score `-1.2626` n `250` status `ready` deltaP `-0.4207` edge `0.0081` maxDD `-3.04`
- `market_context_high->index_24h` score `-2.5156` n `200` status `ready` deltaP `6.0972` edge `0.0367` maxDD `-16.9893`
- `market_context_high->metal_4h` score `-2.8999` n `250` status `ready` deltaP `-12.0768` edge `-0.0537` maxDD `-11.6719`
- `market_context_high->commodity_4h` score `-3.7553` n `250` status `ready` deltaP `-1.978` edge `-0.0322` maxDD `-14.071`
- `market_context_high->crypto_major_24h` score `-4.7128` n `200` status `ready` deltaP `4.1042` edge `0.0256` maxDD `-29.6555`
- `market_context_high->metal_24h` score `-8.3412` n `200` status `ready` deltaP `-12.7986` edge `-0.2495` maxDD `-32.7652`
- `market_context_high->commodity_24h` score `-12.2188` n `200` status `ready` deltaP `-11.1806` edge `-0.0828` maxDD `-45.8715`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
