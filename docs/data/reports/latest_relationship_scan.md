# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-29T13:22:34.039590+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `7048`

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

- `market_context_high->unknown_24h` score `1362.9168` n `144` status `ready` deltaP `-2.6042` edge `113.6865` maxDD `-4.7527`
- `market_context_high->unknown_4h` score `43.0183` n `144` status `ready` deltaP `5.708` edge `3.5601` maxDD `-0.3966`
- `market_context_high->index_24h` score `1.2719` n `144` status `ready` deltaP `20.8334` edge `0.0012` maxDD `-1.0612`
- `market_context_high->commodity_4h` score `0.147` n `144` status `ready` deltaP `12.5` edge `0.0508` maxDD `-1.0837`
- `market_context_high->fx_1h` score `0.0259` n `144` status `ready` deltaP `5.6512` edge `0.0003` maxDD `-0.1986`
- `market_context_high->metal_1h` score `-0.1207` n `144` status `ready` deltaP `7.5557` edge `0.0061` maxDD `-1.0889`
- `market_context_high->fx_4h` score `-0.1822` n `144` status `ready` deltaP `5.2338` edge `0.0016` maxDD `-0.4545`
- `market_context_high->commodity_1h` score `-0.317` n `144` status `ready` deltaP `0.8982` edge `0.0102` maxDD `-0.8797`
- `market_context_high->metal_4h` score `-0.4224` n `144` status `ready` deltaP `9.6545` edge `0.003` maxDD `-3.7218`
- `market_context_high->index_1h` score `-0.8058` n `144` status `ready` deltaP `-4.5326` edge `-0.0048` maxDD `-1.4631`
- `market_context_high->crypto_major_1h` score `-0.919` n `144` status `ready` deltaP `4.1126` edge `0.0243` maxDD `-6.9306`
- `market_context_high->fx_24h` score `-1.082` n `144` status `ready` deltaP `4.8612` edge `0.0105` maxDD `-0.9792`
- `market_context_high->equity_1h` score `-1.4643` n `144` status `ready` deltaP `-0.5447` edge `-0.0001` maxDD `-8.7199`
- `market_context_high->crypto_alt_1h` score `-1.6681` n `144` status `ready` deltaP `1.4138` edge `0.0075` maxDD `-11.7957`
- `market_context_high->metal_24h` score `-2.2459` n `144` status `ready` deltaP `0.868` edge `-0.0082` maxDD `-10.5088`
- `market_context_high->index_4h` score `-2.9585` n `144` status `ready` deltaP `-9.8577` edge `-0.0312` maxDD `-4.9698`
- `market_context_high->crypto_major_4h` score `-3.446` n `144` status `ready` deltaP `2.2866` edge `-0.0412` maxDD `-25.9342`
- `market_context_high->crypto_major_24h` score `-3.8038` n `144` status `ready` deltaP `-3.4722` edge `0.0212` maxDD `-29.1905`
- `market_context_high->equity_4h` score `-4.1662` n `144` status `ready` deltaP `-4.2852` edge `-0.114` maxDD `-24.6581`
- `market_context_high->commodity_24h` score `-4.6638` n `144` status `ready` deltaP `0.0` edge `-0.0389` maxDD `-24.0547`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
