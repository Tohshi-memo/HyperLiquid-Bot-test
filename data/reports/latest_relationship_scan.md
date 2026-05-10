# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-10T07:07:14.773635+00:00`
- Price records: `672`
- Market context records: `951`
- Flow alert records: `2664`
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

- `market_context_high->crypto_major_24h` score `14.7393` n `164` status `ready` deltaP `32.0206` edge `1.0482` maxDD `-1.3382`
- `market_context_high->crypto_alt_24h` score `8.2375` n `164` status `ready` deltaP `8.3333` edge `0.6309` maxDD `0.0`
- `market_context_high->equity_24h` score `0.9954` n `164` status `ready` deltaP `3.0488` edge `0.3231` maxDD `-10.5047`
- `market_context_high->index_24h` score `0.2324` n `164` status `ready` deltaP `1.7361` edge `0.2073` maxDD `-5.9609`
- `market_context_high->commodity_1h` score `-0.2032` n `204` status `ready` deltaP `3.7425` edge `0.0389` maxDD `-3.7959`
- `market_context_high->fx_1h` score `-0.3919` n `204` status `ready` deltaP `1.0098` edge `0.0011` maxDD `-0.3124`
- `market_context_high->equity_1h` score `-0.6405` n `204` status `ready` deltaP `1.1389` edge `0.0159` maxDD `-4.4826`
- `market_context_high->fx_4h` score `-0.6434` n `194` status `ready` deltaP `2.2143` edge `0.0024` maxDD `-1.6381`
- `market_context_high->index_1h` score `-0.6923` n `204` status `ready` deltaP `3.2347` edge `0.0061` maxDD `-2.8282`
- `market_context_high->equity_4h` score `-1.2509` n `194` status `ready` deltaP `2.5302` edge `0.0941` maxDD `-10.5498`
- `market_context_high->unknown_1h` score `-1.3129` n `204` status `ready` deltaP `-2.6007` edge `-0.0149` maxDD `-3.5069`
- `market_context_high->commodity_4h` score `-1.413` n `194` status `ready` deltaP `-1.1991` edge `0.0811` maxDD `-13.0076`
- `market_context_high->index_4h` score `-1.4618` n `194` status `ready` deltaP `0.5626` edge `0.0267` maxDD `-6.5149`
- `market_context_high->crypto_major_1h` score `-1.651` n `204` status `ready` deltaP `5.7473` edge `-0.0036` maxDD `-11.4508`
- `market_context_high->metal_1h` score `-1.7936` n `204` status `ready` deltaP `-0.8131` edge `-0.0286` maxDD `-9.0076`
- `market_context_high->crypto_alt_1h` score `-1.9316` n `204` status `ready` deltaP `1.2299` edge `-0.0252` maxDD `-8.1842`
- `market_context_high->crypto_major_4h` score `-2.3948` n `194` status `ready` deltaP `9.3805` edge `0.1085` maxDD `-22.648`
- `market_context_high->crypto_alt_4h` score `-3.328` n `194` status `ready` deltaP `-1.878` edge `0.013` maxDD `-15.2248`
- `market_context_high->unknown_4h` score `-3.37` n `194` status `ready` deltaP `6.4181` edge `-0.1358` maxDD `-8.3588`
- `market_context_high->unknown_24h` score `-4.556` n `164` status `ready` deltaP `5.0221` edge `-0.067` maxDD `-33.7129`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
