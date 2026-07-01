# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-01T21:07:31.549633+00:00`
- Price records: `672`
- Market context records: `5388`
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

- `market_context_high->unknown_24h` score `5.6498` n `190` status `ready` deltaP `16.9701` edge `0.3707` maxDD `-0.3748`
- `market_context_high->crypto_major_24h` score `5.3605` n `190` status `ready` deltaP `22.9405` edge `0.7478` maxDD `-29.6555`
- `market_context_high->crypto_major_4h` score `3.5467` n `205` status `ready` deltaP `15.0915` edge `0.4242` maxDD `-14.0065`
- `market_context_high->crypto_alt_4h` score `3.0604` n `205` status `ready` deltaP `12.3781` edge `0.3366` maxDD `-9.46`
- `market_context_high->equity_4h` score `2.2945` n `205` status `ready` deltaP `10.9757` edge `0.2819` maxDD `-7.4425`
- `market_context_high->equity_24h` score `1.1397` n `190` status `ready` deltaP `9.693` edge `0.5974` maxDD `-40.0306`
- `market_context_high->equity_1h` score `0.4117` n `205` status `ready` deltaP `7.4602` edge `0.0811` maxDD `-5.0555`
- `market_context_high->crypto_major_1h` score `0.1113` n `205` status `ready` deltaP `4.7736` edge `0.102` maxDD `-6.9639`
- `market_context_high->crypto_alt_1h` score `0.0804` n `205` status `ready` deltaP `2.5281` edge `0.086` maxDD `-5.0257`
- `market_context_high->index_1h` score `0.0448` n `205` status `ready` deltaP `5.5762` edge `0.0159` maxDD `-0.9472`
- `market_context_high->fx_24h` score `-0.2027` n `190` status `ready` deltaP `6.5461` edge `0.029` maxDD `-0.8294`
- `market_context_high->metal_1h` score `-0.4448` n `205` status `ready` deltaP `2.3784` edge `0.0146` maxDD `-2.0682`
- `market_context_high->fx_1h` score `-0.4734` n `205` status `ready` deltaP `-1.5525` edge `-0.0014` maxDD `-0.5823`
- `market_context_high->unknown_4h` score `-0.4751` n `205` status `ready` deltaP `7.9878` edge `0.0256` maxDD `-6.1421`
- `market_context_high->index_24h` score `-1.0005` n `190` status `ready` deltaP `14.2708` edge `0.0787` maxDD `-10.5768`
- `market_context_high->index_4h` score `-1.0369` n `205` status `ready` deltaP `5.7926` edge `0.0359` maxDD `-2.874`
- `market_context_high->fx_4h` score `-1.2035` n `205` status `ready` deltaP `0.2439` edge `0.001` maxDD `-1.567`
- `market_context_high->commodity_1h` score `-1.5058` n `205` status `ready` deltaP `-3.6198` edge `-0.0069` maxDD `-3.5563`
- `market_context_high->metal_4h` score `-2.4409` n `205` status `ready` deltaP `-5.4573` edge `-0.0241` maxDD `-12.8631`
- `market_context_high->commodity_4h` score `-4.3168` n `205` status `ready` deltaP `-7.5914` edge `-0.0453` maxDD `-14.1062`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
