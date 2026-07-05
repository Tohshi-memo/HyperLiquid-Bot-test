# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-05T12:22:27.668639+00:00`
- Price records: `672`
- Market context records: `5771`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `8674`

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

- `market_context_high->equity_24h` score `0.6907` n `229` status `ready` deltaP `15.3665` edge `0.494` maxDD `-31.6316`
- `market_context_high->equity_4h` score `0.1638` n `286` status `ready` deltaP `7.5921` edge `0.1269` maxDD `-7.4425`
- `market_context_high->fx_1h` score `-0.2366` n `298` status `ready` deltaP `2.4987` edge `0.0011` maxDD `-0.5144`
- `market_context_high->metal_1h` score `-0.4161` n `298` status `ready` deltaP `2.2304` edge `-0.0007` maxDD `-2.0682`
- `market_context_high->equity_1h` score `-0.6126` n `298` status `ready` deltaP `3.3668` edge `0.0272` maxDD `-5.0555`
- `market_context_high->commodity_1h` score `-0.8027` n `298` status `ready` deltaP `-2.4937` edge `-0.0058` maxDD `-3.7721`
- `market_context_high->fx_24h` score `-0.9026` n `229` status `ready` deltaP `15.1231` edge `0.0418` maxDD `-3.6674`
- `market_context_high->crypto_major_1h` score `-0.9052` n `298` status `ready` deltaP `3.3557` edge `0.0343` maxDD `-6.2348`
- `market_context_high->index_1h` score `-0.9733` n `298` status `ready` deltaP `0.2894` edge `0.0038` maxDD `-0.9472`
- `market_context_high->crypto_alt_1h` score `-1.1128` n `298` status `ready` deltaP `1.6367` edge `0.0298` maxDD `-6.6758`
- `market_context_high->index_4h` score `-1.1912` n `286` status `ready` deltaP `0.7974` edge `0.0107` maxDD `-3.165`
- `market_context_high->fx_4h` score `-1.2354` n `286` status `ready` deltaP `3.0211` edge `0.006` maxDD `-1.4288`
- `market_context_high->commodity_4h` score `-2.4582` n `286` status `ready` deltaP `-2.939` edge `-0.028` maxDD `-14.071`
- `market_context_high->metal_4h` score `-2.5412` n `286` status `ready` deltaP `-6.2319` edge `-0.0483` maxDD `-11.5426`
- `market_context_high->crypto_major_4h` score `-2.7886` n `286` status `ready` deltaP `7.8085` edge `0.1528` maxDD `-25.6458`
- `market_context_high->index_24h` score `-2.9193` n `229` status `ready` deltaP `1.6496` edge `0.0292` maxDD `-18.1572`
- `market_context_high->crypto_alt_4h` score `-4.3691` n `286` status `ready` deltaP `5.4686` edge `0.1003` maxDD `-28.7346`
- `market_context_high->crypto_major_24h` score `-5.387` n `229` status `ready` deltaP `4.9968` edge `-0.0282` maxDD `-29.6555`
- `market_context_high->metal_24h` score `-7.0282` n `229` status `ready` deltaP `-7.8936` edge `-0.2415` maxDD `-27.5543`
- `market_context_high->commodity_24h` score `-10.8345` n `229` status `ready` deltaP `-13.224` edge `-0.0771` maxDD `-40.676`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
