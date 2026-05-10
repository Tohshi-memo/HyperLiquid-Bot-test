# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-10T06:37:14.097342+00:00`
- Price records: `672`
- Market context records: `949`
- Flow alert records: `2657`
- Minimum samples: `30`
- Pattern count: `88`

- Symbol pattern count: `1320`

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

- `market_context_high->crypto_major_24h` score `14.7421` n `166` status `ready` deltaP `31.7102` edge `1.0505` maxDD `-1.3382`
- `market_context_high->crypto_alt_24h` score `8.0933` n `166` status `ready` deltaP `7.9861` edge `0.6212` maxDD `0.0`
- `market_context_high->equity_24h` score `0.9386` n `166` status `ready` deltaP `3.3133` edge `0.3166` maxDD `-10.5047`
- `market_context_high->index_24h` score `0.1736` n `166` status `ready` deltaP `2.0373` edge `0.2004` maxDD `-5.9609`
- `market_context_high->commodity_1h` score `-0.2056` n `204` status `ready` deltaP `3.7425` edge `0.0387` maxDD `-3.7959`
- `market_context_high->fx_1h` score `-0.3919` n `204` status `ready` deltaP `1.0098` edge `0.0011` maxDD `-0.3124`
- `market_context_high->fx_4h` score `-0.6164` n `196` status `ready` deltaP `2.7034` edge `0.0026` maxDD `-1.6381`
- `market_context_high->index_1h` score `-0.6911` n `204` status `ready` deltaP `3.2347` edge `0.0062` maxDD `-2.8282`
- `market_context_high->equity_1h` score `-0.713` n `204` status `ready` deltaP `0.4579` edge `0.0144` maxDD `-4.4826`
- `market_context_high->unknown_1h` score `-1.2665` n `204` status `ready` deltaP `-2.2602` edge `-0.0133` maxDD `-3.5069`
- `market_context_high->equity_4h` score `-1.3356` n `196` status `ready` deltaP `2.0408` edge `0.0903` maxDD `-10.5498`
- `market_context_high->commodity_4h` score `-1.444` n `196` status `ready` deltaP `-1.6146` edge `0.0799` maxDD `-13.0076`
- `market_context_high->index_4h` score `-1.4859` n `196` status `ready` deltaP `0.4573` edge `0.0254` maxDD `-6.5149`
- `market_context_high->crypto_major_1h` score `-1.6438` n `204` status `ready` deltaP `5.7473` edge `-0.003` maxDD `-11.4508`
- `market_context_high->metal_1h` score `-1.7457` n `204` status `ready` deltaP `-0.1321` edge `-0.027` maxDD `-9.0076`
- `market_context_high->crypto_alt_1h` score `-1.8448` n `204` status `ready` deltaP `1.9109` edge `-0.0225` maxDD `-8.1842`
- `market_context_high->crypto_major_4h` score `-2.3501` n `196` status `ready` deltaP `9.7592` edge `0.1097` maxDD `-22.648`
- `market_context_high->crypto_alt_4h` score `-3.2725` n `196` status `ready` deltaP `-1.5151` edge `0.0152` maxDD `-15.2248`
- `market_context_high->unknown_4h` score `-3.3409` n `196` status `ready` deltaP `6.6918` edge `-0.1352` maxDD `-8.3588`
- `market_context_high->unknown_24h` score `-4.6247` n `166` status `ready` deltaP `5.02` edge `-0.0758` maxDD `-33.7129`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
