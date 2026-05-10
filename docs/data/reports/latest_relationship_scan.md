# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-10T06:52:12.521841+00:00`
- Price records: `672`
- Market context records: `950`
- Flow alert records: `2661`
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

- `market_context_high->crypto_major_24h` score `14.7377` n `165` status `ready` deltaP `31.8655` edge `1.0491` maxDD `-1.3382`
- `market_context_high->crypto_alt_24h` score `8.1636` n `165` status `ready` deltaP `8.1597` edge `0.6259` maxDD `0.0`
- `market_context_high->equity_24h` score `0.9664` n `165` status `ready` deltaP `3.1818` edge `0.3198` maxDD `-10.5047`
- `market_context_high->index_24h` score `0.2025` n `165` status `ready` deltaP `1.8876` edge `0.2038` maxDD `-5.9609`
- `market_context_high->commodity_1h` score `-0.2032` n `204` status `ready` deltaP `3.7425` edge `0.0389` maxDD `-3.7959`
- `market_context_high->fx_1h` score `-0.3919` n `204` status `ready` deltaP `1.0098` edge `0.0011` maxDD `-0.3124`
- `market_context_high->fx_4h` score `-0.6298` n `195` status `ready` deltaP `2.4601` edge `0.0025` maxDD `-1.6381`
- `market_context_high->equity_1h` score `-0.6785` n `204` status `ready` deltaP `0.7984` edge `0.015` maxDD `-4.4826`
- `market_context_high->index_1h` score `-0.6923` n `204` status `ready` deltaP `3.2347` edge `0.0061` maxDD `-2.8282`
- `market_context_high->equity_4h` score `-1.2946` n `195` status `ready` deltaP `2.2835` edge `0.0921` maxDD `-10.5498`
- `market_context_high->unknown_1h` score `-1.3033` n `204` status `ready` deltaP `-2.6007` edge `-0.0141` maxDD `-3.5069`
- `market_context_high->commodity_4h` score `-1.4278` n `195` status `ready` deltaP `-1.4079` edge `0.0806` maxDD `-13.0076`
- `market_context_high->index_4h` score `-1.4877` n `195` status `ready` deltaP `0.3291` edge `0.0261` maxDD `-6.5149`
- `market_context_high->crypto_major_1h` score `-1.645` n `204` status `ready` deltaP `5.7473` edge `-0.0031` maxDD `-11.4508`
- `market_context_high->metal_1h` score `-1.7728` n `204` status `ready` deltaP `-0.4726` edge `-0.0282` maxDD `-9.0076`
- `market_context_high->crypto_alt_1h` score `-1.8888` n `204` status `ready` deltaP `1.5704` edge `-0.0239` maxDD `-8.1842`
- `market_context_high->crypto_major_4h` score `-2.3723` n `195` status `ready` deltaP `9.5708` edge `0.1091` maxDD `-22.648`
- `market_context_high->crypto_alt_4h` score `-3.2966` n `195` status `ready` deltaP `-1.6956` edge `0.0144` maxDD `-15.2248`
- `market_context_high->unknown_4h` score `-3.3468` n `195` status `ready` deltaP `6.6322` edge `-0.1353` maxDD `-8.3588`
- `market_context_high->unknown_24h` score `-4.5895` n `165` status `ready` deltaP `5.0221` edge `-0.0713` maxDD `-33.7129`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
