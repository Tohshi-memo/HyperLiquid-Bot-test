# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-16T20:56:05.519389+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11831`

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

- `market_context_high->unknown_24h` score `182.3878` n `83` status `ready` deltaP `-25.1401` edge `23.819` maxDD `-7.8016`
- `market_context_high->commodity_24h` score `7.2474` n `83` status `ready` deltaP `41.3404` edge `0.3341` maxDD `-0.1266`
- `market_context_high->commodity_4h` score `1.1946` n `119` status `ready` deltaP `12.6537` edge `0.0623` maxDD `-0.7687`
- `market_context_high->commodity_1h` score `0.0114` n `121` status `ready` deltaP `3.2823` edge `0.0202` maxDD `-0.624`
- `market_context_high->fx_4h` score `-0.2376` n `119` status `ready` deltaP `5.0945` edge `0.0067` maxDD `-0.504`
- `market_context_high->fx_1h` score `-0.3516` n `121` status `ready` deltaP `0.8685` edge `0.0014` maxDD `-0.2527`
- `market_context_high->metal_1h` score `-0.5739` n `121` status `ready` deltaP `0.7188` edge `-0.0068` maxDD `-1.7257`
- `market_context_high->metal_4h` score `-0.6162` n `119` status `ready` deltaP `10.2032` edge `-0.0063` maxDD `-4.5909`
- `market_context_high->index_1h` score `-0.7264` n `121` status `ready` deltaP `-5.7245` edge `-0.0028` maxDD `-0.5064`
- `market_context_high->index_4h` score `-1.1653` n `119` status `ready` deltaP `-9.3321` edge `-0.0063` maxDD `-0.8045`
- `market_context_high->index_24h` score `-1.448` n `83` status `ready` deltaP `-2.0164` edge `-0.0599` maxDD `-1.6509`
- `market_context_high->fx_24h` score `-1.6811` n `83` status `ready` deltaP `-10.6928` edge `0.0165` maxDD `-1.8596`
- `market_context_high->metal_24h` score `-2.0298` n `83` status `ready` deltaP `-10.8664` edge `0.0634` maxDD `-7.0954`
- `market_context_high->crypto_major_1h` score `-2.1379` n `121` status `ready` deltaP `-5.1443` edge `-0.0352` maxDD `-5.6933`
- `market_context_high->crypto_alt_1h` score `-2.2769` n `121` status `ready` deltaP `-4.3178` edge `-0.027` maxDD `-7.0497`
- `market_context_high->crypto_major_4h` score `-2.5147` n `119` status `ready` deltaP `-0.5726` edge `-0.0436` maxDD `-8.6381`
- `market_context_high->equity_1h` score `-2.691` n `121` status `ready` deltaP `-10.9764` edge `-0.0471` maxDD `-4.9849`
- `market_context_high->crypto_major_24h` score `-3.2254` n `83` status `ready` deltaP `-4.7273` edge `0.0559` maxDD `-26.0318`
- `market_context_high->unknown_1h` score `-6.6368` n `121` status `ready` deltaP `3.1264` edge `-0.5342` maxDD `-0.8437`
- `market_context_high->crypto_alt_4h` score `-6.9398` n `119` status `ready` deltaP `-9.742` edge `-0.0802` maxDD `-21.9871`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
