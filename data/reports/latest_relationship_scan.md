# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-28T01:22:27.292604+00:00`
- Price records: `672`
- Market context records: `8148`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11842`

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

- `market_context_high->equity_24h` score `23.6986` n `81` status `ready` deltaP `44.1166` edge `1.7718` maxDD `-4.9489`
- `market_context_high->equity_4h` score `10.1254` n `82` status `ready` deltaP `37.0426` edge `0.6203` maxDD `-0.5442`
- `market_context_high->metal_24h` score `8.8996` n `81` status `ready` deltaP `38.1944` edge `0.487` maxDD `0.0`
- `news_risk_high->equity_4h` score `8.1246` n `43` status `ready` deltaP `31.5123` edge `0.4875` maxDD `-0.6428`
- `news_risk_high->crypto_major_4h` score `4.8818` n `43` status `ready` deltaP `18.2041` edge `0.346` maxDD `-2.1767`
- `market_context_high->index_24h` score `4.115` n `81` status `ready` deltaP `25.5209` edge `0.2398` maxDD `-1.3621`
- `market_context_high->index_4h` score `3.9635` n `82` status `ready` deltaP `35.3659` edge `0.0988` maxDD `-0.0092`
- `news_risk_high->equity_1h` score `3.7655` n `43` status `ready` deltaP `29.2299` edge `0.1498` maxDD `-1.1366`
- `market_context_high->equity_1h` score `3.262` n `82` status `ready` deltaP `17.4602` edge `0.1857` maxDD `-1.088`
- `market_context_high->metal_4h` score `2.6518` n `82` status `ready` deltaP `24.5427` edge `0.1196` maxDD `-0.979`
- `news_risk_high->index_4h` score `2.5681` n `43` status `ready` deltaP `21.6392` edge `0.0888` maxDD `-0.191`
- `market_context_high->crypto_alt_4h` score `2.556` n `82` status `ready` deltaP `12.3476` edge `0.2424` maxDD `-3.9374`
- `market_context_high->crypto_major_4h` score `2.3065` n `82` status `ready` deltaP `14.1768` edge `0.2695` maxDD `-6.7444`
- `market_context_high->fx_24h` score `2.2187` n `81` status `ready` deltaP `29.9769` edge `0.0554` maxDD `-0.6283`
- `market_context_high->commodity_24h` score `1.839` n `81` status `ready` deltaP `33.2562` edge `0.3026` maxDD `-15.7497`
- `market_context_high->index_1h` score `1.6932` n `82` status `ready` deltaP `19.6838` edge `0.0295` maxDD `-0.2368`
- `news_risk_high->metal_4h` score `1.3831` n `43` status `ready` deltaP `13.8223` edge `0.0699` maxDD `-0.7433`
- `news_risk_high->crypto_major_1h` score `1.3103` n `43` status `ready` deltaP `6.0333` edge `0.1087` maxDD `-1.1783`
- `market_context_high->metal_1h` score `1.0174` n `82` status `ready` deltaP `13.4585` edge `0.0329` maxDD `-0.6936`
- `market_context_high->crypto_major_1h` score `0.8132` n `82` status `ready` deltaP `12.301` edge `0.0633` maxDD `-1.6171`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
