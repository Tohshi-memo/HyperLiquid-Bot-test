# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-01T23:48:56.603235+00:00`
- Price records: `672`
- Market context records: `5400`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11510`

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

- `market_context_high->crypto_major_24h` score `4.9325` n `194` status `ready` deltaP `21.6709` edge `0.7206` maxDD `-29.6555`
- `market_context_high->crypto_major_4h` score `3.6039` n `205` status `ready` deltaP `15.7012` edge `0.4249` maxDD `-14.0065`
- `market_context_high->crypto_alt_4h` score `2.9311` n `205` status `ready` deltaP `11.6159` edge `0.3309` maxDD `-9.46`
- `market_context_high->equity_4h` score `2.3151` n `205` status `ready` deltaP `11.1281` edge `0.2826` maxDD `-7.4425`
- `market_context_high->equity_1h` score `0.4464` n `205` status `ready` deltaP `7.7596` edge `0.082` maxDD `-5.0555`
- `market_context_high->crypto_major_1h` score `0.1545` n `205` status `ready` deltaP `5.073` edge `0.1036` maxDD `-6.9639`
- `market_context_high->crypto_alt_1h` score `0.096` n `205` status `ready` deltaP `2.6778` edge `0.0863` maxDD `-5.0257`
- `market_context_high->equity_24h` score `0.0832` n `194` status `ready` deltaP `8.0327` edge `0.5371` maxDD `-40.0306`
- `market_context_high->index_1h` score `0.0412` n `205` status `ready` deltaP `5.5762` edge `0.0156` maxDD `-0.9472`
- `market_context_high->fx_24h` score `-0.1671` n `194` status `ready` deltaP `6.991` edge `0.029` maxDD `-0.8294`
- `market_context_high->metal_1h` score `-0.452` n `205` status `ready` deltaP `2.3784` edge `0.014` maxDD `-2.0682`
- `market_context_high->fx_1h` score `-0.4563` n `205` status `ready` deltaP `-1.2531` edge `-0.0012` maxDD `-0.5823`
- `market_context_high->index_4h` score `-1.0297` n `205` status `ready` deltaP `5.7926` edge `0.0365` maxDD `-2.874`
- `market_context_high->fx_4h` score `-1.1939` n `205` status `ready` deltaP `0.2439` edge `0.0018` maxDD `-1.567`
- `market_context_high->commodity_1h` score `-1.4519` n `205` status `ready` deltaP `-3.021` edge `-0.0064` maxDD `-3.5563`
- `market_context_high->index_24h` score `-1.6679` n `194` status `ready` deltaP `12.8275` edge `0.0741` maxDD `-12.5551`
- `market_context_high->metal_4h` score `-2.4479` n `205` status `ready` deltaP `-5.4573` edge `-0.025` maxDD `-12.8631`
- `market_context_high->commodity_4h` score `-4.3228` n `205` status `ready` deltaP `-7.5914` edge `-0.0458` maxDD `-14.1062`
- `market_context_high->crypto_alt_24h` score `-5.0926` n `194` status `ready` deltaP `12.9349` edge `0.3591` maxDD `-54.2437`
- `market_context_high->metal_24h` score `-6.9704` n `194` status `ready` deltaP `-4.4226` edge `-0.1264` maxDD `-33.021`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
