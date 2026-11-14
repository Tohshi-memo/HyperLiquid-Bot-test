# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-14T07:07:30.374066+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `10464`

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

- `market_context_high->unknown_24h` score `445.6589` n `75` status `ready` deltaP `2.1944` edge `37.1377` maxDD `-0.4606`
- `news_risk_high->equity_24h` score `37.2006` n `53` status `ready` deltaP `35.5772` edge `2.9335` maxDD `-3.6503`
- `market_context_high->equity_24h` score `28.967` n `75` status `ready` deltaP `30.118` edge `2.3673` maxDD `-9.0005`
- `market_context_high->crypto_alt_24h` score `16.5774` n `75` status `ready` deltaP `47.5834` edge `1.3157` maxDD `-16.4511`
- `news_risk_high->crypto_major_24h` score `15.5144` n `53` status `ready` deltaP `42.0434` edge `1.9053` maxDD `-12.7247`
- `news_risk_high->equity_4h` score `11.3032` n `53` status `ready` deltaP `36.6975` edge `0.8103` maxDD `-7.0416`
- `news_risk_high->commodity_24h` score `6.5681` n `53` status `ready` deltaP `44.2708` edge `0.2522` maxDD `0.0`
- `market_context_high->index_24h` score `5.8674` n `75` status `ready` deltaP `34.5903` edge `0.2675` maxDD `-0.0653`
- `news_risk_high->index_24h` score `5.1864` n `53` status `ready` deltaP `32.6028` edge `0.2452` maxDD `-0.4279`
- `news_risk_high->metal_4h` score `5.0513` n `53` status `ready` deltaP `47.9205` edge `0.1391` maxDD `-1.0104`
- `market_context_high->metal_24h` score `4.3158` n `75` status `ready` deltaP `41.3334` edge `0.3669` maxDD `-3.7989`
- `news_risk_high->crypto_major_4h` score `4.2432` n `53` status `ready` deltaP `22.2676` edge `0.3539` maxDD `-9.2335`
- `news_risk_high->equity_1h` score `3.5349` n `53` status `ready` deltaP `18.3143` edge `0.2355` maxDD `-3.7082`
- `news_risk_high->commodity_4h` score `3.1189` n `53` status `ready` deltaP `28.3882` edge `0.096` maxDD `-0.3611`
- `news_risk_high->metal_1h` score `2.2445` n `53` status `ready` deltaP `26.1891` edge `0.0379` maxDD `-0.3692`
- `news_risk_high->index_4h` score `2.2065` n `53` status `ready` deltaP `22.5754` edge `0.077` maxDD `-0.8235`
- `news_risk_high->crypto_alt_4h` score `2.0948` n `53` status `ready` deltaP `26.1936` edge `0.2578` maxDD `-10.1088`
- `news_risk_high->crypto_alt_24h` score `1.5695` n `53` status `ready` deltaP `14.4261` edge `0.5556` maxDD `-29.0448`
- `news_risk_high->index_1h` score `1.237` n `53` status `ready` deltaP `16.7269` edge `0.0217` maxDD `-0.4103`
- `news_risk_high->crypto_alt_1h` score `0.7227` n `53` status `ready` deltaP `17.594` edge `0.0733` maxDD `-6.1688`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
