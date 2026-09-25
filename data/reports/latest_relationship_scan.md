# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-25T11:22:32.251947+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `112`

- Symbol pattern count: `11258`

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

- `market_context_high->unknown_1h` score `84.6802` n `47` status `ready` deltaP `8.1698` edge `7.0093` maxDD `-0.2334`
- `market_context_high->crypto_major_24h` score `50.2513` n `47` status `ready` deltaP `30.9434` edge `4.0206` maxDD `-2.4756`
- `market_context_high->crypto_alt_24h` score `31.9396` n `47` status `ready` deltaP `24.782` edge `2.5344` maxDD `-2.7051`
- `market_context_high->equity_24h` score `25.4319` n `47` status `ready` deltaP `34.5892` edge `1.9243` maxDD `-2.1786`
- `news_risk_high->unknown_1h` score `11.2701` n `111` status `ready` deltaP `3.4161` edge `0.9303` maxDD `-0.4452`
- `market_context_high->index_24h` score `7.8168` n `47` status `ready` deltaP `35.1101` edge `0.4303` maxDD `-0.3705`
- `market_context_high->metal_24h` score `4.4648` n `47` status `ready` deltaP `38.0098` edge `0.1425` maxDD `-0.2401`
- `news_risk_high->commodity_24h` score `3.4552` n `50` status `ready` deltaP `29.1528` edge `0.1284` maxDD `-1.7857`
- `market_context_high->index_4h` score `2.6228` n `47` status `ready` deltaP `30.5202` edge `0.0305` maxDD `-0.2323`
- `market_context_high->equity_4h` score `2.029` n `47` status `ready` deltaP `14.2481` edge `0.1159` maxDD `-1.3444`
- `market_context_high->crypto_alt_4h` score `0.9` n `47` status `ready` deltaP `9.5355` edge `0.0782` maxDD `-3.3417`
- `market_context_high->index_1h` score `0.8888` n `47` status `ready` deltaP `13.8616` edge `0.0095` maxDD `-0.2275`
- `market_context_high->equity_1h` score `0.8467` n `47` status `ready` deltaP `10.8676` edge `0.0384` maxDD `-1.5564`
- `news_risk_high->crypto_alt_1h` score `0.6174` n `111` status `ready` deltaP `7.5323` edge `0.0923` maxDD `-4.2849`
- `market_context_high->fx_1h` score `0.459` n `47` status `ready` deltaP `9.9598` edge `0.0075` maxDD `-0.1854`
- `news_risk_high->index_1h` score `0.012` n `111` status `ready` deltaP `3.7601` edge `0.0063` maxDD `-0.3863`
- `market_context_high->metal_1h` score `-0.0014` n `47` status `ready` deltaP `3.1278` edge `0.0106` maxDD `-0.1976`
- `news_risk_high->metal_1h` score `-0.0248` n `111` status `ready` deltaP `8.2457` edge `0.0059` maxDD `-0.7016`
- `news_risk_high->equity_1h` score `-0.1048` n `111` status `ready` deltaP `1.667` edge `0.0262` maxDD `-2.0595`
- `market_context_high->crypto_major_1h` score `-0.1542` n `47` status `ready` deltaP `2.9558` edge `0.0492` maxDD `-4.5405`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
