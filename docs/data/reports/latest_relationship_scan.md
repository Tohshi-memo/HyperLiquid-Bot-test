# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-01T21:37:29.329047+00:00`
- Price records: `672`
- Market context records: `5390`
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

- `market_context_high->crypto_major_24h` score `5.3886` n `192` status `ready` deltaP `22.9166` edge `0.7503` maxDD `-29.6555`
- `market_context_high->unknown_24h` score `5.1889` n `192` status `ready` deltaP `17.0139` edge `0.332` maxDD `-0.3748`
- `market_context_high->crypto_major_4h` score `3.5697` n `205` status `ready` deltaP `15.2439` edge `0.4251` maxDD `-14.0065`
- `market_context_high->crypto_alt_4h` score `3.0786` n `205` status `ready` deltaP `12.5305` edge `0.3371` maxDD `-9.46`
- `market_context_high->equity_4h` score `2.3295` n `205` status `ready` deltaP `11.1281` edge `0.2838` maxDD `-7.4425`
- `market_context_high->equity_24h` score `0.6749` n `192` status `ready` deltaP `8.8542` edge `0.5726` maxDD `-40.0306`
- `market_context_high->equity_1h` score `0.4153` n `205` status `ready` deltaP `7.4602` edge `0.0814` maxDD `-5.0555`
- `market_context_high->crypto_major_1h` score `0.0921` n `205` status `ready` deltaP `4.7736` edge `0.1004` maxDD `-6.9639`
- `market_context_high->crypto_alt_1h` score `0.0648` n `205` status `ready` deltaP `2.5281` edge `0.0847` maxDD `-5.0257`
- `market_context_high->index_1h` score `0.0448` n `205` status `ready` deltaP `5.5762` edge `0.0159` maxDD `-0.9472`
- `market_context_high->fx_24h` score `-0.1883` n `192` status `ready` deltaP `6.7708` edge `0.0287` maxDD `-0.8294`
- `market_context_high->metal_1h` score `-0.4196` n `205` status `ready` deltaP `2.6778` edge `0.0147` maxDD `-2.0682`
- `market_context_high->fx_1h` score `-0.4906` n `205` status `ready` deltaP `-1.8519` edge `-0.0016` maxDD `-0.5823`
- `market_context_high->unknown_4h` score `-0.5427` n `205` status `ready` deltaP `7.6829` edge `0.022` maxDD `-6.1421`
- `market_context_high->index_4h` score `-1.0345` n `205` status `ready` deltaP `5.7926` edge `0.0361` maxDD `-2.874`
- `market_context_high->fx_4h` score `-1.2023` n `205` status `ready` deltaP `0.2439` edge `0.0011` maxDD `-1.567`
- `market_context_high->index_24h` score `-1.3575` n `192` status `ready` deltaP `13.5416` edge `0.0744` maxDD `-11.5578`
- `market_context_high->commodity_1h` score `-1.5334` n `205` status `ready` deltaP `-3.9192` edge `-0.0072` maxDD `-3.5563`
- `market_context_high->metal_4h` score `-2.437` n `205` status `ready` deltaP `-5.4573` edge `-0.0236` maxDD `-12.8631`
- `market_context_high->commodity_4h` score `-4.318` n `205` status `ready` deltaP `-7.5914` edge `-0.0454` maxDD `-14.1062`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
