# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-01T17:52:26.978671+00:00`
- Price records: `672`
- Market context records: `2583`
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

- `market_context_high->unknown_24h` score `6.7838` n `126` status `ready` deltaP `18.5763` edge `0.4743` maxDD `-1.626`
- `market_context_high->crypto_alt_4h` score `6.1289` n `146` status `ready` deltaP `26.7207` edge `0.6005` maxDD `-15.4319`
- `market_context_high->crypto_major_4h` score `4.3352` n `146` status `ready` deltaP `17.9648` edge `0.4225` maxDD `-10.1468`
- `market_context_high->crypto_alt_1h` score `1.436` n `146` status `ready` deltaP `11.73` edge `0.1602` maxDD `-6.1656`
- `market_context_high->unknown_4h` score `1.2028` n `146` status `ready` deltaP `9.3614` edge `0.1428` maxDD `-3.7312`
- `market_context_high->crypto_major_1h` score `0.9378` n `146` status `ready` deltaP `10.2104` edge `0.1295` maxDD `-4.2199`
- `market_context_high->crypto_alt_24h` score `0.8932` n `126` status `ready` deltaP `2.4058` edge `0.7363` maxDD `-39.0265`
- `market_context_high->crypto_major_24h` score `0.778` n `126` status `ready` deltaP `8.3085` edge `0.4831` maxDD `-28.2259`
- `market_context_high->index_24h` score `0.7389` n `126` status `ready` deltaP `7.8373` edge `0.1074` maxDD `-2.5127`
- `market_context_high->equity_24h` score `0.5873` n `126` status `ready` deltaP `17.6339` edge `-0.0016` maxDD `-2.3615`
- `market_context_high->index_4h` score `0.3364` n `146` status `ready` deltaP `9.4325` edge `0.0493` maxDD `-2.3986`
- `market_context_high->index_1h` score `-0.1743` n `146` status `ready` deltaP `3.642` edge `0.0106` maxDD `-1.2855`
- `market_context_high->commodity_1h` score `-0.4062` n `146` status `ready` deltaP `5.3523` edge `0.0183` maxDD `-4.3601`
- `market_context_high->unknown_1h` score `-0.4116` n `146` status `ready` deltaP `1.8005` edge `0.02` maxDD `-2.6375`
- `market_context_high->metal_4h` score `-0.5206` n `146` status `ready` deltaP `4.9594` edge `0.0623` maxDD `-4.7664`
- `market_context_high->metal_1h` score `-0.6572` n `146` status `ready` deltaP `0.8121` edge `0.0146` maxDD `-2.9823`
- `market_context_high->fx_1h` score `-0.676` n `146` status `ready` deltaP `-0.9843` edge `0.0037` maxDD `-0.278`
- `market_context_high->fx_4h` score `-0.8792` n `146` status `ready` deltaP `-0.0731` edge `0.013` maxDD `-0.8621`
- `market_context_high->equity_1h` score `-0.89` n `146` status `ready` deltaP `-0.8264` edge `0.0152` maxDD `-2.7085`
- `market_context_high->fx_24h` score `-1.0184` n `126` status `ready` deltaP `2.009` edge `0.0011` maxDD `-1.6157`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
