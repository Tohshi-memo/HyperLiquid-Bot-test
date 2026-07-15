# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-15T11:37:24.777522+00:00`
- Price records: `672`
- Market context records: `6813`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11680`

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

- `market_context_high->unknown_24h` score `0.8297` n `176` status `ready` deltaP `-1.5467` edge `0.4919` maxDD `-12.3511`
- `market_context_high->commodity_24h` score `0.4091` n `176` status `ready` deltaP `10.9217` edge `0.1481` maxDD `-5.2791`
- `market_context_high->crypto_major_1h` score `-0.4127` n `194` status `ready` deltaP `5.6686` edge `0.0138` maxDD `-4.2122`
- `market_context_high->fx_1h` score `-0.4275` n `194` status `ready` deltaP `-0.9306` edge `-0.0001` maxDD `-0.5468`
- `market_context_high->crypto_alt_1h` score `-0.5257` n `194` status `ready` deltaP `2.9416` edge `0.013` maxDD `-3.7803`
- `market_context_high->commodity_1h` score `-0.6548` n `194` status `ready` deltaP `-1.4306` edge `-0.0061` maxDD `-2.1314`
- `market_context_high->index_1h` score `-0.7597` n `194` status `ready` deltaP `-3.2595` edge `-0.0026` maxDD `-0.8451`
- `market_context_high->metal_1h` score `-1.0156` n `194` status `ready` deltaP `-7.0992` edge `-0.009` maxDD `-1.9098`
- `market_context_high->fx_4h` score `-1.3389` n `185` status `ready` deltaP `5.5224` edge `-0.0021` maxDD `-2.1765`
- `market_context_high->commodity_4h` score `-1.3467` n `185` status `ready` deltaP `-2.1408` edge `-0.0094` maxDD `-5.5853`
- `market_context_high->equity_1h` score `-1.534` n `194` status `ready` deltaP `0.8967` edge `-0.0249` maxDD `-4.3798`
- `market_context_high->index_4h` score `-1.6625` n `185` status `ready` deltaP `1.8375` edge `-0.0294` maxDD `-6.3458`
- `market_context_high->unknown_1h` score `-1.8083` n `194` status `ready` deltaP `-6.7335` edge `-0.0157` maxDD `-3.2083`
- `market_context_high->metal_4h` score `-2.8687` n `185` status `ready` deltaP `-6.0094` edge `-0.0294` maxDD `-5.5324`
- `market_context_high->crypto_major_4h` score `-3.3326` n `185` status `ready` deltaP `-1.1149` edge `-0.0871` maxDD `-16.9508`
- `market_context_high->unknown_4h` score `-3.5001` n `185` status `ready` deltaP `-14.1175` edge `0.039` maxDD `-10.2579`
- `market_context_high->crypto_alt_4h` score `-3.5396` n `185` status `ready` deltaP `-1.8219` edge `-0.0833` maxDD `-20.6678`
- `market_context_high->fx_24h` score `-4.4768` n `176` status `ready` deltaP `-9.7853` edge `-0.0042` maxDD `-5.6237`
- `market_context_high->equity_4h` score `-5.0641` n `185` status `ready` deltaP `-0.81` edge `-0.19` maxDD `-29.3079`
- `market_context_high->metal_24h` score `-9.6363` n `176` status `ready` deltaP `-21.7961` edge `-0.2416` maxDD `-28.2147`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
