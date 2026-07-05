# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-05T17:22:25.655420+00:00`
- Price records: `672`
- Market context records: `5794`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `8128`

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

- `market_context_high->equity_24h` score `0.6473` n `248` status `ready` deltaP `15.3954` edge `0.4592` maxDD `-31.6316`
- `market_context_high->equity_4h` score `-0.0388` n `304` status `ready` deltaP `6.5147` edge `0.1172` maxDD `-7.4425`
- `market_context_high->fx_1h` score `-0.2643` n `304` status `ready` deltaP `2.0643` edge `0.0009` maxDD `-0.5499`
- `market_context_high->metal_1h` score `-0.6322` n `304` status `ready` deltaP `2.3598` edge `-0.0009` maxDD `-2.0682`
- `market_context_high->equity_1h` score `-0.635` n `304` status `ready` deltaP `3.191` edge `0.0265` maxDD `-5.0555`
- `market_context_high->commodity_1h` score `-0.76` n `304` status `ready` deltaP `-1.7925` edge `-0.005` maxDD `-3.7721`
- `market_context_high->crypto_major_1h` score `-0.9753` n `304` status `ready` deltaP `2.8995` edge `0.0315` maxDD `-6.2348`
- `market_context_high->index_1h` score `-1.0028` n `304` status `ready` deltaP `-0.0335` edge `0.0035` maxDD `-0.9472`
- `market_context_high->fx_24h` score `-1.0951` n `248` status `ready` deltaP `13.5752` edge `0.0384` maxDD `-4.544`
- `market_context_high->crypto_alt_1h` score `-1.1447` n `304` status `ready` deltaP `1.3138` edge `0.0293` maxDD `-6.6758`
- `market_context_high->index_4h` score `-1.1851` n `304` status `ready` deltaP `0.9146` edge `0.0107` maxDD `-3.165`
- `market_context_high->fx_4h` score `-1.5006` n `304` status `ready` deltaP `-0.0562` edge `0.0029` maxDD `-2.2593`
- `market_context_high->commodity_4h` score `-2.4323` n `304` status `ready` deltaP `-3.4258` edge `-0.0259` maxDD `-13.7144`
- `market_context_high->metal_4h` score `-2.4848` n `304` status `ready` deltaP `-5.3113` edge `-0.0472` maxDD `-11.5426`
- `market_context_high->index_24h` score `-2.7948` n `248` status `ready` deltaP `3.7131` edge `0.0314` maxDD `-18.1572`
- `market_context_high->crypto_major_4h` score `-3.0161` n `304` status `ready` deltaP `7.4695` edge `0.1361` maxDD `-25.6458`
- `market_context_high->crypto_alt_4h` score `-4.6105` n `304` status `ready` deltaP `5.2712` edge `0.0815` maxDD `-28.7346`
- `market_context_high->metal_24h` score `-7.0164` n `248` status `ready` deltaP `-7.7509` edge `-0.2533` maxDD `-26.8981`
- `market_context_high->crypto_major_24h` score `-8.1538` n `248` status `ready` deltaP `0.7617` edge `-0.1472` maxDD `-29.6555`
- `market_context_high->commodity_24h` score `-10.8929` n `248` status `ready` deltaP `-14.5274` edge `-0.0838` maxDD `-40.1676`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
