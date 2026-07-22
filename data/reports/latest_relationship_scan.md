# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-22T16:37:28.619972+00:00`
- Price records: `672`
- Market context records: `7583`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `14534`

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

- `market_context_high->commodity_4h` score `0.2069` n `159` status `ready` deltaP `9.5321` edge `0.0297` maxDD `-2.4139`
- `market_context_high->index_1h` score `0.005` n `159` status `ready` deltaP `5.7114` edge `0.0114` maxDD `-0.9072`
- `market_context_high->commodity_24h` score `-0.0714` n `151` status `ready` deltaP `12.57` edge `0.0686` maxDD `-7.0012`
- `market_context_high->commodity_1h` score `-0.1169` n `159` status `ready` deltaP `6.2666` edge `0.0057` maxDD `-1.5775`
- `market_context_high->unknown_24h` score `-0.4904` n `152` status `ready` deltaP `9.0643` edge `0.0972` maxDD `-8.6405`
- `market_context_high->fx_1h` score `-0.5136` n `159` status `ready` deltaP `1.1304` edge `-0.0004` maxDD `-0.6615`
- `market_context_high->index_4h` score `-0.5214` n `159` status `ready` deltaP `10.6486` edge `0.0348` maxDD `-3.4775`
- `market_context_high->crypto_alt_1h` score `-0.5598` n `159` status `ready` deltaP `0.3145` edge `0.0066` maxDD `-4.1042`
- `market_context_high->crypto_major_1h` score `-0.6338` n `159` status `ready` deltaP `5.8553` edge `0.0055` maxDD `-6.3969`
- `market_context_high->metal_1h` score `-0.6425` n `159` status `ready` deltaP `1.1223` edge `0.0147` maxDD `-1.0307`
- `market_context_high->equity_1h` score `-0.6509` n `159` status `ready` deltaP `5.3828` edge `0.0502` maxDD `-8.8965`
- `market_context_high->fx_24h` score `-0.7164` n `151` status `ready` deltaP `7.4717` edge `0.0149` maxDD `-3.6195`
- `market_context_high->unknown_1h` score `-0.9482` n `159` status `ready` deltaP `0.2542` edge `-0.0609` maxDD `-1.3217`
- `market_context_high->crypto_alt_4h` score `-1.2438` n `159` status `ready` deltaP `1.4199` edge `0.0445` maxDD `-10.4077`
- `market_context_high->equity_4h` score `-1.5444` n `159` status `ready` deltaP `3.4072` edge `0.216` maxDD `-21.9375`
- `market_context_high->metal_4h` score `-1.5644` n `159` status `ready` deltaP `-0.372` edge `0.0501` maxDD `-4.8549`
- `market_context_high->crypto_major_4h` score `-1.8856` n `159` status `ready` deltaP `5.6508` edge `0.0478` maxDD `-18.5102`
- `market_context_high->fx_4h` score `-2.2228` n `159` status `ready` deltaP `-2.2907` edge `-0.0015` maxDD `-2.1439`
- `market_context_high->unknown_4h` score `-2.5075` n `159` status `ready` deltaP `10.014` edge `-0.1537` maxDD `-6.0958`
- `market_context_high->metal_24h` score `-3.1485` n `152` status `ready` deltaP `-4.3859` edge `0.0851` maxDD `-13.7607`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
