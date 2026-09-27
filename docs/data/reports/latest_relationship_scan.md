# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-27T08:22:27.085748+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `11908`

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

- `news_risk_high->unknown_24h` score `1478.7756` n `122` status `ready` deltaP `1.2153` edge `123.2232` maxDD `0.0`
- `market_context_high->unknown_1h` score `126.9182` n `44` status `ready` deltaP `10.7513` edge `10.5095` maxDD `-0.0395`
- `market_context_high->crypto_major_24h` score `55.1443` n `40` status `ready` deltaP `29.9653` edge `4.4307` maxDD `-2.4756`
- `market_context_high->equity_24h` score `29.3259` n `40` status `ready` deltaP `35.8681` edge `2.2361` maxDD `-2.1786`
- `market_context_high->crypto_alt_24h` score `28.8928` n `40` status `ready` deltaP `14.6875` edge `2.3478` maxDD `-2.7051`
- `market_context_high->index_24h` score `8.1823` n `40` status `ready` deltaP `33.2639` edge `0.4689` maxDD `-0.3705`
- `market_context_high->metal_24h` score `4.3515` n `40` status `ready` deltaP `39.4444` edge `0.1235` maxDD `-0.2401`
- `market_context_high->equity_4h` score `3.6057` n `42` status `ready` deltaP `23.0619` edge `0.1802` maxDD `-1.3444`
- `market_context_high->index_4h` score `3.1281` n `42` status `ready` deltaP `34.5674` edge `0.0373` maxDD `-0.2323`
- `market_context_high->crypto_alt_4h` score `2.8568` n `42` status `ready` deltaP `14.9463` edge `0.1927` maxDD `-3.3417`
- `market_context_high->equity_1h` score `1.518` n `44` status `ready` deltaP `17.1884` edge `0.0522` maxDD `-1.5564`
- `market_context_high->crypto_major_4h` score `1.4321` n `42` status `ready` deltaP `7.063` edge `0.1627` maxDD `-5.2359`
- `market_context_high->crypto_major_1h` score `1.2595` n `44` status `ready` deltaP `10.4927` edge `0.1208` maxDD `-4.8632`
- `market_context_high->crypto_alt_1h` score `1.0947` n `44` status `ready` deltaP `9.9211` edge `0.114` maxDD `-5.7799`
- `market_context_high->index_1h` score `1.0468` n `44` status `ready` deltaP `14.6162` edge `0.0093` maxDD `-0.2275`
- `news_risk_high->index_24h` score `0.6303` n `122` status `ready` deltaP `14.4524` edge `0.0257` maxDD `-2.2287`
- `news_risk_high->metal_24h` score `0.4566` n `122` status `ready` deltaP `15.1411` edge `0.1226` maxDD `-6.8392`
- `market_context_high->fx_1h` score `0.3212` n `44` status `ready` deltaP `10.3838` edge `0.0076` maxDD `-0.1854`
- `market_context_high->metal_1h` score `-0.0294` n `44` status `ready` deltaP `2.6674` edge `0.0103` maxDD `-0.215`
- `news_risk_high->index_1h` score `-0.175` n `139` status `ready` deltaP `1.7157` edge `0.003` maxDD `-0.3214`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
