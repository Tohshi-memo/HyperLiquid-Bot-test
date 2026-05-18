# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-18T20:07:18.915597+00:00`
- Price records: `672`
- Market context records: `1150`
- Flow alert records: `5213`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8749`

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

- `market_context_high->crypto_major_24h` score `19.8899` n `152` status `ready` deltaP `43.7226` edge `1.4792` maxDD `-8.0553`
- `market_context_high->crypto_alt_24h` score `9.636` n `152` status `ready` deltaP `20.0749` edge `0.8708` maxDD `-15.1306`
- `market_context_high->equity_24h` score `7.9255` n `152` status `ready` deltaP `19.5541` edge `0.6231` maxDD `-6.4404`
- `market_context_high->index_24h` score `6.2798` n `152` status `ready` deltaP `18.1652` edge `0.458` maxDD `-3.4627`
- `market_context_high->metal_24h` score `5.7739` n `152` status `ready` deltaP `-1.6082` edge `0.6586` maxDD `-6.3373`
- `market_context_high->equity_4h` score `2.5825` n `168` status `ready` deltaP `12.471` edge `0.1984` maxDD `-3.6396`
- `market_context_high->index_4h` score `1.2351` n `168` status `ready` deltaP `9.8141` edge `0.1058` maxDD `-2.1308`
- `market_context_high->index_1h` score `0.578` n `168` status `ready` deltaP `8.3939` edge `0.0239` maxDD `-0.5353`
- `market_context_high->equity_1h` score `0.4791` n `168` status `ready` deltaP `3.7781` edge `0.0525` maxDD `-1.3546`
- `market_context_high->crypto_major_4h` score `0.3544` n `168` status `ready` deltaP `10.1336` edge `0.17` maxDD `-8.3693`
- `market_context_high->crypto_major_1h` score `0.1329` n `168` status `ready` deltaP `7.5813` edge `0.0371` maxDD `-4.1256`
- `market_context_high->fx_1h` score `0.0777` n `168` status `ready` deltaP `7.7167` edge `0.0006` maxDD `-0.3124`
- `market_context_high->metal_1h` score `-0.2484` n `168` status `ready` deltaP `6.651` edge `-0.004` maxDD `-2.2164`
- `market_context_high->crypto_alt_1h` score `-0.2538` n `168` status `ready` deltaP `3.0938` edge `0.0425` maxDD `-3.4088`
- `market_context_high->commodity_1h` score `-0.7972` n `168` status `ready` deltaP `-2.6732` edge `-0.0036` maxDD `-3.7959`
- `market_context_high->crypto_alt_4h` score `-0.8323` n `168` status `ready` deltaP `7.063` edge `0.1427` maxDD `-16.7194`
- `market_context_high->fx_4h` score `-0.8677` n `168` status `ready` deltaP `-1.3502` edge `-0.0026` maxDD `-1.6381`
- `market_context_high->metal_4h` score `-2.2877` n `168` status `ready` deltaP `7.6147` edge `-0.046` maxDD `-9.2991`
- `market_context_high->unknown_24h` score `-3.0835` n `152` status `ready` deltaP `4.651` edge `-0.015` maxDD `-10.1706`
- `market_context_high->unknown_4h` score `-3.1546` n `168` status `ready` deltaP `9.1609` edge `-0.2023` maxDD `-6.7322`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
