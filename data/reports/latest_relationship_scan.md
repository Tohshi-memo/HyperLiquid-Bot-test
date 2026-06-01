# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-01T14:08:55.092187+00:00`
- Price records: `672`
- Market context records: `2568`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9200`

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

- `market_context_high->crypto_alt_4h` score `5.8765` n `146` status `ready` deltaP `25.5012` edge `0.5876` maxDD `-15.4319`
- `market_context_high->crypto_major_24h` score `5.4667` n `115` status `ready` deltaP `13.8285` edge `0.6287` maxDD `-15.2264`
- `market_context_high->unknown_24h` score `4.7893` n `115` status `ready` deltaP `19.9547` edge `0.2989` maxDD `-1.626`
- `market_context_high->crypto_major_4h` score `4.049` n `146` status `ready` deltaP `17.5075` edge `0.4017` maxDD `-10.1468`
- `market_context_high->equity_24h` score `1.7906` n `115` status `ready` deltaP `21.3406` edge `0.0653` maxDD `-2.0014`
- `market_context_high->crypto_alt_1h` score `1.4888` n `146` status `ready` deltaP `11.5803` edge `0.1656` maxDD `-6.1656`
- `market_context_high->unknown_4h` score `1.4424` n `146` status `ready` deltaP `9.9712` edge `0.1587` maxDD `-3.7312`
- `market_context_high->crypto_major_1h` score `0.9331` n `146` status `ready` deltaP `9.911` edge `0.1311` maxDD `-4.2199`
- `market_context_high->index_24h` score `0.6398` n `115` status `ready` deltaP `5.8635` edge `0.1123` maxDD `-2.5127`
- `market_context_high->crypto_alt_24h` score `0.3243` n `115` status `ready` deltaP `-0.6144` edge `0.6835` maxDD `-39.0265`
- `market_context_high->index_4h` score `0.1471` n `146` status `ready` deltaP `7.7556` edge `0.0447` maxDD `-2.3986`
- `market_context_high->index_1h` score `-0.1143` n `146` status `ready` deltaP `4.0911` edge `0.0126` maxDD `-1.2855`
- `market_context_high->unknown_1h` score `-0.4416` n `146` status `ready` deltaP `1.6508` edge `0.0185` maxDD `-2.6375`
- `market_context_high->commodity_1h` score `-0.4434` n `146` status `ready` deltaP `5.3523` edge `0.0152` maxDD `-4.3601`
- `market_context_high->fx_24h` score `-0.5641` n `115` status `ready` deltaP `1.9958` edge `0.0054` maxDD `-1.6157`
- `market_context_high->fx_1h` score `-0.5718` n `146` status `ready` deltaP `0.2133` edge `0.0044` maxDD `-0.278`
- `market_context_high->metal_1h` score `-0.6068` n `146` status `ready` deltaP `1.2612` edge `0.0158` maxDD `-2.9823`
- `market_context_high->equity_1h` score `-0.7054` n `146` status `ready` deltaP `0.2215` edge `0.0236` maxDD `-2.7085`
- `market_context_high->fx_4h` score `-0.828` n `146` status `ready` deltaP `0.5367` edge `0.0132` maxDD `-0.8621`
- `market_context_high->metal_4h` score `-0.866` n `146` status `ready` deltaP `3.2826` edge `0.0447` maxDD `-4.7664`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
