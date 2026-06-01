# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-01T13:52:27.691769+00:00`
- Price records: `672`
- Market context records: `2567`
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

- `market_context_high->crypto_alt_4h` score `5.8415` n `146` status `ready` deltaP `25.3488` edge `0.5857` maxDD `-15.4319`
- `market_context_high->crypto_major_24h` score `5.4379` n `115` status `ready` deltaP `13.8285` edge `0.6263` maxDD `-15.2264`
- `market_context_high->unknown_24h` score `4.898` n `115` status `ready` deltaP `20.1283` edge `0.3068` maxDD `-1.626`
- `market_context_high->crypto_major_4h` score `4.0116` n `146` status `ready` deltaP `17.3551` edge `0.3996` maxDD `-10.1468`
- `market_context_high->equity_24h` score `1.7822` n `115` status `ready` deltaP `21.3406` edge `0.0646` maxDD `-2.0014`
- `market_context_high->crypto_alt_1h` score `1.4876` n `146` status `ready` deltaP `11.5803` edge `0.1655` maxDD `-6.1656`
- `market_context_high->unknown_4h` score `1.4712` n `146` status `ready` deltaP `9.9712` edge `0.1611` maxDD `-3.7312`
- `market_context_high->crypto_major_1h` score `0.9043` n `146` status `ready` deltaP `9.7613` edge `0.1297` maxDD `-4.2199`
- `market_context_high->index_24h` score `0.6422` n `115` status `ready` deltaP `5.8635` edge `0.1125` maxDD `-2.5127`
- `market_context_high->crypto_alt_24h` score `0.2989` n `115` status `ready` deltaP `-0.788` edge `0.6814` maxDD `-39.0265`
- `market_context_high->index_4h` score `0.1289` n `146` status `ready` deltaP `7.6032` edge `0.0442` maxDD `-2.3986`
- `market_context_high->index_1h` score `-0.1299` n `146` status `ready` deltaP `3.9414` edge `0.0123` maxDD `-1.2855`
- `market_context_high->commodity_1h` score `-0.4278` n `146` status `ready` deltaP `5.3523` edge `0.0165` maxDD `-4.3601`
- `market_context_high->unknown_1h` score `-0.4428` n `146` status `ready` deltaP `1.6508` edge `0.0184` maxDD `-2.6375`
- `market_context_high->fx_24h` score `-0.5633` n `115` status `ready` deltaP `1.9958` edge `0.0055` maxDD `-1.6157`
- `market_context_high->fx_1h` score `-0.573` n `146` status `ready` deltaP `0.2133` edge `0.0043` maxDD `-0.278`
- `market_context_high->metal_1h` score `-0.6188` n `146` status `ready` deltaP `1.2612` edge `0.0148` maxDD `-2.9823`
- `market_context_high->equity_1h` score `-0.7102` n `146` status `ready` deltaP `0.2215` edge `0.0232` maxDD `-2.7085`
- `market_context_high->fx_4h` score `-0.8292` n `146` status `ready` deltaP `0.5367` edge `0.0131` maxDD `-0.8621`
- `market_context_high->metal_4h` score `-0.8985` n `146` status `ready` deltaP `3.1302` edge `0.043` maxDD `-4.7664`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
