# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-11T11:22:32.092729+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `12406`

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

- `news_risk_high->unknown_1h` score `750.9413` n `59` status `ready` deltaP `-6.2088` edge `62.662` maxDD `-1.7068`
- `risk_on_high->crypto_alt_24h` score `22.5652` n `91` status `ready` deltaP `41.2069` edge `1.6287` maxDD `-0.8386`
- `risk_on_and_context->crypto_alt_24h` score `22.5652` n `91` status `ready` deltaP `41.2069` edge `1.6287` maxDD `-0.8386`
- `market_context_high->crypto_alt_24h` score `20.1931` n `162` status `ready` deltaP `36.8249` edge `1.52` maxDD `-3.9523`
- `market_context_high->equity_24h` score `9.2991` n `162` status `ready` deltaP `35.7639` edge `0.5365` maxDD `0.0`
- `risk_on_high->equity_24h` score `9.2019` n `91` status `ready` deltaP `35.7639` edge `0.5284` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `9.2019` n `91` status `ready` deltaP `35.7639` edge `0.5284` maxDD `0.0`
- `risk_on_high->crypto_alt_4h` score `8.7301` n `91` status `ready` deltaP `41.3361` edge `0.4891` maxDD `-1.9733`
- `risk_on_and_context->crypto_alt_4h` score `8.7301` n `91` status `ready` deltaP `41.3361` edge `0.4891` maxDD `-1.9733`
- `risk_on_high->crypto_major_24h` score `7.3751` n `91` status `ready` deltaP `25.021` edge `1.1855` maxDD `-24.5429`
- `risk_on_and_context->crypto_major_24h` score `7.3751` n `91` status `ready` deltaP `25.021` edge `1.1855` maxDD `-24.5429`
- `risk_on_high->crypto_major_4h` score `7.1979` n `91` status `ready` deltaP `31.4393` edge `0.4761` maxDD `-3.8693`
- `risk_on_and_context->crypto_major_4h` score `7.1979` n `91` status `ready` deltaP `31.4393` edge `0.4761` maxDD `-3.8693`
- `risk_on_high->index_24h` score `5.5588` n `91` status `ready` deltaP `51.5644` edge `0.1237` maxDD `-0.0051`
- `risk_on_and_context->index_24h` score `5.5588` n `91` status `ready` deltaP `51.5644` edge `0.1237` maxDD `-0.0051`
- `market_context_high->index_24h` score `4.4222` n `162` status `ready` deltaP `43.75` edge `0.1162` maxDD `-0.1483`
- `risk_on_high->equity_4h` score `3.535` n `91` status `ready` deltaP `34.2603` edge `0.0755` maxDD `-0.079`
- `risk_on_and_context->equity_4h` score `3.535` n `91` status `ready` deltaP `34.2603` edge `0.0755` maxDD `-0.079`
- `market_context_high->crypto_alt_4h` score `3.3069` n `162` status `ready` deltaP `22.2749` edge `0.2976` maxDD `-7.6417`
- `market_context_high->equity_4h` score `2.3864` n `162` status `ready` deltaP `27.8907` edge `0.0956` maxDD `-2.6138`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
