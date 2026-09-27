# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-27T08:52:26.937144+00:00`
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

- `news_risk_high->unknown_24h` score `1369.6812` n `124` status `ready` deltaP `1.2153` edge `114.132` maxDD `0.0`
- `market_context_high->unknown_1h` score `140.8223` n `42` status `ready` deltaP `10.643` edge `11.6689` maxDD `-0.0395`
- `market_context_high->crypto_major_24h` score `55.5118` n `38` status `ready` deltaP `29.8337` edge `4.4622` maxDD `-2.4756`
- `market_context_high->equity_24h` score `29.7941` n `38` status `ready` deltaP `35.7365` edge `2.276` maxDD `-2.1786`
- `market_context_high->crypto_alt_24h` score `28.1359` n `38` status `ready` deltaP `14.5559` edge `2.2856` maxDD `-2.7051`
- `market_context_high->index_24h` score `8.3014` n `38` status `ready` deltaP `33.1323` edge `0.4797` maxDD `-0.3705`
- `market_context_high->metal_24h` score `4.2977` n `38` status `ready` deltaP `38.697` edge `0.124` maxDD `-0.2401`
- `market_context_high->crypto_alt_4h` score `4.0347` n `42` status `ready` deltaP `17.1748` edge `0.276` maxDD `-3.3417`
- `market_context_high->equity_4h` score `3.8788` n `42` status `ready` deltaP `25.2903` edge `0.1881` maxDD `-1.3444`
- `market_context_high->index_4h` score `3.1389` n `42` status `ready` deltaP `34.5674` edge `0.0382` maxDD `-0.2323`
- `market_context_high->crypto_major_4h` score `2.2403` n `42` status `ready` deltaP `9.2915` edge `0.2152` maxDD `-5.2359`
- `market_context_high->equity_1h` score `1.4369` n `42` status `ready` deltaP `15.8897` edge `0.0541` maxDD `-1.5564`
- `market_context_high->index_1h` score `1.1175` n `42` status `ready` deltaP `15.4406` edge `0.0097` maxDD `-0.2275`
- `market_context_high->crypto_major_1h` score `1.0286` n `42` status `ready` deltaP `8.7611` edge `0.1131` maxDD `-4.8632`
- `market_context_high->crypto_alt_1h` score `0.9264` n `42` status `ready` deltaP `8.4474` edge `0.1098` maxDD `-5.7799`
- `market_context_high->fx_1h` score `0.7043` n `42` status `ready` deltaP `12.9812` edge `0.0078` maxDD `-0.1854`
- `news_risk_high->index_24h` score `0.6602` n `124` status `ready` deltaP `14.7962` edge `0.0259` maxDD `-2.2287`
- `news_risk_high->metal_24h` score `0.4527` n `124` status `ready` deltaP `15.1826` edge `0.122` maxDD `-6.8392`
- `market_context_high->metal_4h` score `0.1597` n `42` status `ready` deltaP `4.7256` edge `0.0197` maxDD `-0.3647`
- `market_context_high->metal_1h` score `-0.148` n `42` status `ready` deltaP `0.4776` edge `0.0097` maxDD `-0.215`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
