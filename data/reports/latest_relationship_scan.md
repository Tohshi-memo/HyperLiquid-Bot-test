# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-01T17:07:27.391646+00:00`
- Price records: `672`
- Market context records: `5371`
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

- `market_context_high->unknown_24h` score `9.2335` n `177` status `ready` deltaP `17.0521` edge `0.6688` maxDD `-0.3748`
- `market_context_high->crypto_major_24h` score `5.1577` n `177` status `ready` deltaP `21.875` edge `0.738` maxDD `-29.6555`
- `market_context_high->equity_24h` score `2.9771` n `177` status `ready` deltaP `13.8713` edge `0.7185` maxDD `-40.0306`
- `market_context_high->crypto_major_4h` score `2.7996` n `203` status `ready` deltaP `13.7923` edge `0.3706` maxDD `-14.0065`
- `market_context_high->crypto_alt_4h` score `2.1644` n `203` status `ready` deltaP `10.2975` edge `0.2758` maxDD `-9.46`
- `market_context_high->equity_4h` score `1.3328` n `203` status `ready` deltaP `8.8099` edge `0.2162` maxDD `-7.4425`
- `market_context_high->index_24h` score `0.3112` n `177` status `ready` deltaP `17.1551` edge `0.0961` maxDD `-9.0959`
- `market_context_high->equity_1h` score `0.0268` n `205` status `ready` deltaP `5.8135` edge `0.06` maxDD `-5.0555`
- `market_context_high->fx_24h` score `-0.0089` n `177` status `ready` deltaP `8.354` edge `0.0331` maxDD `-0.8294`
- `market_context_high->index_1h` score `-0.1289` n `205` status `ready` deltaP `4.0792` edge `0.0114` maxDD `-0.9472`
- `market_context_high->crypto_major_1h` score `-0.2365` n `205` status `ready` deltaP `3.4263` edge `0.082` maxDD `-6.9639`
- `market_context_high->crypto_alt_1h` score `-0.2986` n `205` status `ready` deltaP `1.1808` edge `0.0634` maxDD `-5.0257`
- `market_context_high->fx_1h` score `-0.4322` n `205` status `ready` deltaP `-0.804` edge `-0.0011` maxDD `-0.5823`
- `market_context_high->metal_1h` score `-0.6137` n `205` status `ready` deltaP `0.8814` edge `0.0105` maxDD `-2.0682`
- `market_context_high->fx_4h` score `-1.129` n `203` status `ready` deltaP `1.1159` edge `0.0014` maxDD `-1.567`
- `market_context_high->index_4h` score `-1.1982` n `203` status `ready` deltaP `4.1872` edge `0.0227` maxDD `-2.704`
- `market_context_high->unknown_4h` score `-1.3504` n `203` status `ready` deltaP `7.8615` edge `-0.0465` maxDD `-6.1421`
- `market_context_high->commodity_1h` score `-1.531` n `205` status `ready` deltaP `-3.9192` edge `-0.007` maxDD `-3.5563`
- `market_context_high->metal_4h` score `-2.6733` n `203` status `ready` deltaP `-7.7061` edge `-0.0389` maxDD `-12.8631`
- `market_context_high->crypto_alt_24h` score `-3.4968` n `177` status `ready` deltaP `12.5706` edge `0.3376` maxDD `-54.2437`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
