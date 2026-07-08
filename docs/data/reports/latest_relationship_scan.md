# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-08T12:22:38.512344+00:00`
- Price records: `672`
- Market context records: `6086`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11095`

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

- `news_risk_high->fx_24h` score `8.1582` n `30` status `ready` deltaP `72.7431` edge `0.1949` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `5.8021` n `30` status `ready` deltaP `32.0486` edge `0.2846` maxDD `-0.5131`
- `news_risk_high->fx_4h` score `4.3005` n `32` status `ready` deltaP `44.7409` edge `0.0647` maxDD `-0.0345`
- `news_risk_high->fx_1h` score `2.4195` n `32` status `ready` deltaP `29.0419` edge `0.0219` maxDD `-0.1113`
- `market_context_high->equity_4h` score `2.0686` n `200` status `ready` deltaP `10.6951` edge `0.1928` maxDD `-2.671`
- `news_risk_high->crypto_major_1h` score `1.1108` n `32` status `ready` deltaP `12.9304` edge `0.1029` maxDD `-2.0691`
- `news_risk_high->crypto_alt_1h` score `0.5854` n `32` status `ready` deltaP `8.6265` edge `0.0637` maxDD `-1.6923`
- `news_risk_high->commodity_24h` score `0.5409` n `30` status `ready` deltaP `18.4375` edge `-0.0573` maxDD `-0.3101`
- `news_risk_high->index_24h` score `0.1039` n `30` status `ready` deltaP `9.2361` edge `0.0389` maxDD `-2.3058`
- `market_context_high->fx_1h` score `-0.2683` n `200` status `ready` deltaP `1.5419` edge `-0.0001` maxDD `-0.5659`
- `market_context_high->metal_1h` score `-0.3043` n `200` status `ready` deltaP `4.5539` edge `0.0105` maxDD `-2.0564`
- `market_context_high->equity_1h` score `-0.4131` n `200` status `ready` deltaP `2.6527` edge `0.0409` maxDD `-4.2573`
- `market_context_high->metal_4h` score `-0.671` n `200` status `ready` deltaP `5.1646` edge `0.0284` maxDD `-3.4996`
- `market_context_high->index_4h` score `-0.7002` n `200` status `ready` deltaP `3.9085` edge `0.0306` maxDD `-1.381`
- `market_context_high->commodity_1h` score `-0.7034` n `200` status `ready` deltaP `-1.497` edge `-0.004` maxDD `-0.5708`
- `news_risk_high->metal_1h` score `-0.7334` n `32` status `ready` deltaP `-1.9461` edge `-0.0313` maxDD `-1.6464`
- `market_context_high->crypto_alt_1h` score `-0.7642` n `200` status `ready` deltaP `4.7515` edge `0.0456` maxDD `-9.3536`
- `market_context_high->crypto_major_1h` score `-0.8191` n `200` status `ready` deltaP `4.8054` edge `0.0397` maxDD `-9.807`
- `news_risk_high->index_1h` score `-1.0073` n `32` status `ready` deltaP `-8.3271` edge `-0.0173` maxDD `-1.1725`
- `market_context_high->index_1h` score `-1.1003` n `200` status `ready` deltaP `-1.4521` edge `0.0049` maxDD `-0.9531`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
