# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-27T08:37:22.527393+00:00`
- Price records: `672`
- Market context records: `2026`
- Flow alert records: `7722`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9091`

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

- `market_context_high->crypto_major_4h` score `8.8847` n `205` status `ready` deltaP `30.7927` edge `0.5881` maxDD `-1.9063`
- `market_context_high->crypto_alt_4h` score `8.373` n `205` status `ready` deltaP `24.5427` edge `0.6486` maxDD `-5.1574`
- `market_context_high->unknown_4h` score `5.9097` n `205` status `ready` deltaP `18.689` edge `0.4428` maxDD `-2.6599`
- `market_context_high->equity_4h` score `3.0191` n `205` status `ready` deltaP `17.2561` edge `0.246` maxDD `-5.0894`
- `market_context_high->crypto_major_1h` score `1.5201` n `205` status `ready` deltaP `12.328` edge `0.1431` maxDD `-3.2225`
- `market_context_high->index_4h` score `1.4342` n `205` status `ready` deltaP `12.9269` edge `0.1017` maxDD `-1.8022`
- `market_context_high->crypto_alt_1h` score `1.2018` n `205` status `ready` deltaP `9.7831` edge `0.1463` maxDD `-4.9097`
- `market_context_high->unknown_24h` score `0.575` n `195` status `ready` deltaP `16.4638` edge `0.4702` maxDD `-35.8966`
- `market_context_high->equity_24h` score `0.3276` n `195` status `ready` deltaP `15.4417` edge `0.4142` maxDD `-33.1875`
- `market_context_high->equity_1h` score `0.2068` n `205` status `ready` deltaP `6.9104` edge `0.05` maxDD `-2.6402`
- `market_context_high->index_24h` score `0.1068` n `195` status `ready` deltaP `3.8005` edge `0.1064` maxDD `-4.1604`
- `market_context_high->unknown_1h` score `0.017` n `205` status `ready` deltaP `3.5965` edge `0.0494` maxDD `-3.0902`
- `market_context_high->index_1h` score `-0.3265` n `205` status `ready` deltaP `2.2543` edge `0.0168` maxDD `-1.3898`
- `market_context_high->fx_24h` score `-0.3288` n `195` status `ready` deltaP `12.0275` edge `0.0241` maxDD `-2.2013`
- `market_context_high->fx_1h` score `-0.8769` n `205` status `ready` deltaP `-1.5912` edge `0.0003` maxDD `-0.3548`
- `market_context_high->metal_1h` score `-0.8958` n `205` status `ready` deltaP `3.6585` edge `0.0197` maxDD `-5.166`
- `market_context_high->metal_24h` score `-0.9558` n `195` status `ready` deltaP `10.8465` edge `0.1498` maxDD `-17.4743`
- `market_context_high->metal_4h` score `-1.3068` n `205` status `ready` deltaP `8.1098` edge `0.0993` maxDD `-11.9812`
- `market_context_high->fx_4h` score `-1.6097` n `205` status `ready` deltaP `-6.5854` edge `-0.0021` maxDD `-1.0513`
- `market_context_high->commodity_1h` score `-1.813` n `205` status `ready` deltaP `3.2043` edge `0.002` maxDD `-15.7972`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
