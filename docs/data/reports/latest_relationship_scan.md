# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-08T14:07:33.549151+00:00`
- Price records: `672`
- Market context records: `6094`
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

- `news_risk_high->fx_24h` score `8.163` n `30` status `ready` deltaP `72.7431` edge `0.1953` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `6.9145` n `30` status `ready` deltaP `33.2639` edge `0.3692` maxDD `-0.5131`
- `news_risk_high->fx_4h` score `4.2603` n `32` status `ready` deltaP `44.2835` edge `0.0644` maxDD `-0.0345`
- `news_risk_high->fx_1h` score `2.3931` n `32` status `ready` deltaP `28.7425` edge `0.0217` maxDD `-0.1113`
- `market_context_high->equity_4h` score `1.6594` n `195` status `ready` deltaP `9.3902` edge `0.1674` maxDD `-2.671`
- `news_risk_high->crypto_major_1h` score `1.2511` n `32` status `ready` deltaP `13.6789` edge `0.1159` maxDD `-2.0691`
- `news_risk_high->crypto_alt_1h` score `0.7008` n `32` status `ready` deltaP `9.375` edge `0.0735` maxDD `-1.6923`
- `news_risk_high->commodity_24h` score `0.2145` n `30` status `ready` deltaP `17.2223` edge `-0.0764` maxDD `-0.3101`
- `news_risk_high->index_24h` score `0.1218` n `30` status `ready` deltaP `9.2361` edge `0.0412` maxDD `-2.3058`
- `market_context_high->fx_1h` score `-0.2746` n `195` status `ready` deltaP `1.4348` edge `-0.0002` maxDD `-0.5659`
- `market_context_high->metal_4h` score `-0.5739` n `195` status `ready` deltaP `3.9994` edge `0.0185` maxDD `-3.4996`
- `market_context_high->equity_1h` score `-0.5967` n `195` status `ready` deltaP `1.6866` edge `0.0238` maxDD `-4.2573`
- `market_context_high->commodity_1h` score `-0.69` n `195` status `ready` deltaP `-1.3903` edge `-0.0036` maxDD `-0.5708`
- `market_context_high->index_4h` score `-0.6905` n `195` status `ready` deltaP `4.2902` edge `0.0293` maxDD `-1.381`
- `news_risk_high->metal_1h` score `-0.6936` n `32` status `ready` deltaP `-1.7964` edge `-0.0272` maxDD `-1.6464`
- `market_context_high->metal_1h` score `-0.7014` n `195` status `ready` deltaP `3.5882` edge `-0.0025` maxDD `-2.0564`
- `market_context_high->crypto_alt_1h` score `-0.8751` n `195` status `ready` deltaP `4.359` edge `0.034` maxDD `-9.3536`
- `market_context_high->crypto_major_1h` score `-0.9469` n `195` status `ready` deltaP `4.4642` edge `0.0256` maxDD `-9.807`
- `news_risk_high->index_1h` score `-1.0587` n `32` status `ready` deltaP `-9.0756` edge `-0.0189` maxDD `-1.1725`
- `market_context_high->index_1h` score `-1.1556` n `195` status `ready` deltaP `-2.0083` edge `0.004` maxDD `-0.9531`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
