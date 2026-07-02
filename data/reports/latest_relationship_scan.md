# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-02T00:22:26.295202+00:00`
- Price records: `672`
- Market context records: `5403`
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

- `market_context_high->crypto_major_24h` score `4.8136` n `194` status `ready` deltaP `21.3237` edge `0.713` maxDD `-29.6555`
- `market_context_high->crypto_major_4h` score `3.6003` n `205` status `ready` deltaP `15.7012` edge `0.4246` maxDD `-14.0065`
- `market_context_high->crypto_alt_4h` score `2.8923` n `205` status `ready` deltaP `11.311` edge `0.3297` maxDD `-9.46`
- `market_context_high->equity_4h` score `2.3067` n `205` status `ready` deltaP `11.1281` edge `0.2819` maxDD `-7.4425`
- `market_context_high->equity_1h` score `0.4404` n `205` status `ready` deltaP `7.7596` edge `0.0815` maxDD `-5.0555`
- `market_context_high->crypto_major_1h` score `0.1629` n `205` status `ready` deltaP `5.073` edge `0.1043` maxDD `-6.9639`
- `market_context_high->crypto_alt_1h` score `0.0996` n `205` status `ready` deltaP `2.6778` edge `0.0866` maxDD `-5.0257`
- `market_context_high->equity_24h` score `0.0604` n `194` status `ready` deltaP `8.0327` edge `0.5352` maxDD `-40.0306`
- `market_context_high->index_1h` score `0.0448` n `205` status `ready` deltaP `5.5762` edge `0.0159` maxDD `-0.9472`
- `market_context_high->fx_24h` score `-0.1647` n `194` status `ready` deltaP `6.991` edge `0.0292` maxDD `-0.8294`
- `market_context_high->fx_1h` score `-0.4555` n `205` status `ready` deltaP `-1.2531` edge `-0.0011` maxDD `-0.5823`
- `market_context_high->metal_1h` score `-0.4687` n `205` status `ready` deltaP `2.2287` edge `0.0136` maxDD `-2.0682`
- `market_context_high->index_4h` score `-0.9993` n `205` status `ready` deltaP `6.0975` edge `0.037` maxDD `-2.874`
- `market_context_high->fx_4h` score `-1.1939` n `205` status `ready` deltaP `0.2439` edge `0.0018` maxDD `-1.567`
- `market_context_high->commodity_1h` score `-1.4531` n `205` status `ready` deltaP `-3.021` edge `-0.0065` maxDD `-3.5563`
- `market_context_high->index_24h` score `-1.6463` n `194` status `ready` deltaP `12.8275` edge `0.0759` maxDD `-12.5551`
- `market_context_high->metal_4h` score `-2.4677` n `205` status `ready` deltaP `-5.7622` edge `-0.0255` maxDD `-12.8631`
- `market_context_high->commodity_4h` score `-4.3252` n `205` status `ready` deltaP `-7.5914` edge `-0.046` maxDD `-14.1062`
- `market_context_high->crypto_alt_24h` score `-5.2355` n `194` status `ready` deltaP `12.5877` edge `0.3495` maxDD `-54.2437`
- `market_context_high->metal_24h` score `-6.9767` n `194` status `ready` deltaP `-4.4226` edge `-0.1272` maxDD `-33.021`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
