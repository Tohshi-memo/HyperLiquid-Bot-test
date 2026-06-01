# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-01T14:22:28.183038+00:00`
- Price records: `672`
- Market context records: `2569`
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

- `market_context_high->crypto_alt_4h` score `5.9163` n `146` status `ready` deltaP `25.6536` edge `0.5899` maxDD `-15.4319`
- `market_context_high->crypto_major_24h` score `5.4931` n `115` status `ready` deltaP `13.8285` edge `0.6309` maxDD `-15.2264`
- `market_context_high->unknown_24h` score `4.6854` n `115` status `ready` deltaP `19.7811` edge `0.2914` maxDD `-1.626`
- `market_context_high->crypto_major_4h` score `4.0888` n `146` status `ready` deltaP `17.66` edge `0.404` maxDD `-10.1468`
- `market_context_high->equity_24h` score `1.799` n `115` status `ready` deltaP `21.3406` edge `0.066` maxDD `-2.0014`
- `market_context_high->crypto_alt_1h` score `1.5104` n `146` status `ready` deltaP `11.73` edge `0.1664` maxDD `-6.1656`
- `market_context_high->unknown_4h` score `1.4136` n `146` status `ready` deltaP `9.9712` edge `0.1563` maxDD `-3.7312`
- `market_context_high->crypto_major_1h` score `0.9655` n `146` status `ready` deltaP `10.0607` edge `0.1328` maxDD `-4.2199`
- `market_context_high->index_24h` score `0.6374` n `115` status `ready` deltaP `5.8635` edge `0.1121` maxDD `-2.5127`
- `market_context_high->crypto_alt_24h` score `0.3427` n `115` status `ready` deltaP `-0.4408` edge `0.6847` maxDD `-39.0265`
- `market_context_high->index_4h` score `0.1677` n `146` status `ready` deltaP `7.9081` edge `0.0454` maxDD `-2.3986`
- `market_context_high->index_1h` score `-0.1143` n `146` status `ready` deltaP `4.0911` edge `0.0126` maxDD `-1.2855`
- `market_context_high->unknown_1h` score `-0.4344` n `146` status `ready` deltaP `1.6508` edge `0.0191` maxDD `-2.6375`
- `market_context_high->commodity_1h` score `-0.4446` n `146` status `ready` deltaP `5.3523` edge `0.0151` maxDD `-4.3601`
- `market_context_high->fx_1h` score `-0.5587` n `146` status `ready` deltaP `0.363` edge `0.0045` maxDD `-0.278`
- `market_context_high->fx_24h` score `-0.5649` n `115` status `ready` deltaP `1.9958` edge `0.0053` maxDD `-1.6157`
- `market_context_high->metal_1h` score `-0.6068` n `146` status `ready` deltaP `1.2612` edge `0.0158` maxDD `-2.9823`
- `market_context_high->equity_1h` score `-0.7197` n `146` status `ready` deltaP `0.0718` edge `0.0234` maxDD `-2.7085`
- `market_context_high->fx_4h` score `-0.8268` n `146` status `ready` deltaP `0.5367` edge `0.0133` maxDD `-0.8621`
- `market_context_high->metal_4h` score `-0.8334` n `146` status `ready` deltaP `3.4351` edge `0.0464` maxDD `-4.7664`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
