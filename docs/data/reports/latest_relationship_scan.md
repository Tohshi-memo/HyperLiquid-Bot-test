# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-01T14:37:29.517712+00:00`
- Price records: `672`
- Market context records: `2570`
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

- `market_context_high->crypto_alt_4h` score `5.9585` n `146` status `ready` deltaP `25.8061` edge `0.5924` maxDD `-15.4319`
- `market_context_high->crypto_major_24h` score `5.5219` n `115` status `ready` deltaP `13.8285` edge `0.6333` maxDD `-15.2264`
- `market_context_high->unknown_24h` score `4.5767` n `115` status `ready` deltaP `19.6074` edge `0.2835` maxDD `-1.626`
- `market_context_high->crypto_major_4h` score `4.1286` n `146` status `ready` deltaP `17.8124` edge `0.4063` maxDD `-10.1468`
- `market_context_high->equity_24h` score `1.8074` n `115` status `ready` deltaP `21.3406` edge `0.0667` maxDD `-2.0014`
- `market_context_high->crypto_alt_1h` score `1.5391` n `146` status `ready` deltaP `11.8797` edge `0.1678` maxDD `-6.1656`
- `market_context_high->unknown_4h` score `1.3764` n `146` status `ready` deltaP `9.9712` edge `0.1532` maxDD `-3.7312`
- `market_context_high->crypto_major_1h` score `0.9954` n `146` status `ready` deltaP `10.2104` edge `0.1343` maxDD `-4.2199`
- `market_context_high->index_24h` score `0.6374` n `115` status `ready` deltaP `5.8635` edge `0.1121` maxDD `-2.5127`
- `market_context_high->crypto_alt_24h` score `0.3673` n `115` status `ready` deltaP `-0.2672` edge `0.6867` maxDD `-39.0265`
- `market_context_high->index_4h` score `0.1895` n `146` status `ready` deltaP `8.0605` edge `0.0462` maxDD `-2.3986`
- `market_context_high->index_1h` score `-0.1275` n `146` status `ready` deltaP `3.9414` edge `0.0125` maxDD `-1.2855`
- `market_context_high->unknown_1h` score `-0.4344` n `146` status `ready` deltaP `1.6508` edge `0.0191` maxDD `-2.6375`
- `market_context_high->commodity_1h` score `-0.447` n `146` status `ready` deltaP `5.3523` edge `0.0149` maxDD `-4.3601`
- `market_context_high->fx_1h` score `-0.5467` n `146` status `ready` deltaP `0.5127` edge `0.0045` maxDD `-0.278`
- `market_context_high->fx_24h` score `-0.5665` n `115` status `ready` deltaP `1.9958` edge `0.0051` maxDD `-1.6157`
- `market_context_high->metal_1h` score `-0.6056` n `146` status `ready` deltaP `1.2612` edge `0.0159` maxDD `-2.9823`
- `market_context_high->equity_1h` score `-0.7377` n `146` status `ready` deltaP `-0.0779` edge `0.0229` maxDD `-2.7085`
- `market_context_high->metal_4h` score `-0.7948` n `146` status `ready` deltaP `3.5875` edge `0.0486` maxDD `-4.7664`
- `market_context_high->fx_4h` score `-0.8268` n `146` status `ready` deltaP `0.5367` edge `0.0133` maxDD `-0.8621`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
