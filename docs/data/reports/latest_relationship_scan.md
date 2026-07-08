# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-08T18:51:18.665693+00:00`
- Price records: `672`
- Market context records: `6114`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11131`

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

- `news_risk_high->crypto_alt_24h` score `9.1332` n `30` status `ready` deltaP `36.5625` edge `0.5321` maxDD `-0.5131`
- `news_risk_high->fx_24h` score `7.964` n `30` status `ready` deltaP `70.6597` edge `0.1926` maxDD `0.0`
- `news_risk_high->fx_4h` score `4.1873` n `32` status `ready` deltaP `43.5213` edge `0.0634` maxDD `-0.0345`
- `news_risk_high->fx_1h` score `2.3284` n `32` status `ready` deltaP `27.994` edge `0.0213` maxDD `-0.1113`
- `news_risk_high->crypto_major_1h` score `1.2628` n `32` status `ready` deltaP `13.6789` edge `0.1174` maxDD `-2.0691`
- `market_context_high->equity_4h` score `0.9441` n `195` status `ready` deltaP `6.4939` edge `0.1271` maxDD `-2.671`
- `news_risk_high->crypto_alt_1h` score `0.6385` n `32` status `ready` deltaP `8.7762` edge `0.0695` maxDD `-1.6923`
- `news_risk_high->index_24h` score `0.022` n `30` status `ready` deltaP `9.2361` edge `0.0284` maxDD `-2.3058`
- `market_context_high->fx_1h` score `-0.3167` n `195` status `ready` deltaP `0.6863` edge `-0.0006` maxDD `-0.5659`
- `news_risk_high->commodity_24h` score `-0.4464` n `30` status `ready` deltaP `14.2709` edge `-0.1118` maxDD `-0.3101`
- `market_context_high->metal_4h` score `-0.6509` n `195` status `ready` deltaP `3.3896` edge `0.0127` maxDD `-3.4996`
- `market_context_high->commodity_1h` score `-0.6828` n `195` status `ready` deltaP `-1.3903` edge `-0.003` maxDD `-0.5708`
- `market_context_high->equity_1h` score `-0.7074` n `195` status `ready` deltaP `0.3393` edge `0.0186` maxDD `-4.2573`
- `news_risk_high->metal_1h` score `-0.7738` n `32` status `ready` deltaP `-2.994` edge `-0.0295` maxDD `-1.6464`
- `market_context_high->metal_1h` score `-0.8248` n `195` status `ready` deltaP `2.3906` edge `-0.0048` maxDD `-2.0564`
- `market_context_high->index_4h` score `-0.909` n `195` status `ready` deltaP `1.3938` edge `0.0206` maxDD `-1.381`
- `market_context_high->crypto_major_1h` score `-0.9352` n `195` status `ready` deltaP `4.4642` edge `0.0271` maxDD `-9.807`
- `market_context_high->crypto_alt_1h` score `-0.9374` n `195` status `ready` deltaP `3.7602` edge `0.03` maxDD `-9.3536`
- `news_risk_high->index_1h` score `-1.1342` n `32` status `ready` deltaP `-10.2732` edge `-0.0206` maxDD `-1.1725`
- `market_context_high->index_1h` score `-1.2718` n `195` status `ready` deltaP `-3.2059` edge `0.0023` maxDD `-0.9531`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
