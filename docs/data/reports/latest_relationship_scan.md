# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-01T15:52:25.647762+00:00`
- Price records: `672`
- Market context records: `2575`
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

- `market_context_high->crypto_alt_4h` score `6.1731` n `146` status `ready` deltaP `26.5683` edge `0.6052` maxDD `-15.4319`
- `market_context_high->unknown_24h` score `5.1445` n `118` status `ready` deltaP `19.415` edge `0.3321` maxDD `-1.626`
- `market_context_high->crypto_major_4h` score `4.2982` n `146` status `ready` deltaP `18.1173` edge `0.4184` maxDD `-10.1468`
- `market_context_high->crypto_major_24h` score `3.8567` n `118` status `ready` deltaP `12.1704` edge `0.5815` maxDD `-20.2995`
- `market_context_high->crypto_alt_1h` score `1.5511` n `146` status `ready` deltaP `12.0294` edge `0.1678` maxDD `-6.1656`
- `market_context_high->equity_24h` score `1.351` n `118` status `ready` deltaP `20.3448` edge `0.0435` maxDD `-2.324`
- `market_context_high->unknown_4h` score `1.2936` n `146` status `ready` deltaP `9.9712` edge `0.1463` maxDD `-3.7312`
- `market_context_high->crypto_major_1h` score `1.029` n `146` status `ready` deltaP `10.5098` edge `0.1351` maxDD `-4.2199`
- `market_context_high->index_24h` score `0.6426` n `118` status `ready` deltaP `6.4383` edge `0.1087` maxDD `-2.5127`
- `market_context_high->crypto_alt_24h` score `0.3764` n `118` status `ready` deltaP `0.103` edge `0.6854` maxDD `-39.0265`
- `market_context_high->index_4h` score `0.2864` n `146` status `ready` deltaP `8.8227` edge `0.0492` maxDD `-2.3986`
- `market_context_high->index_1h` score `-0.1287` n `146` status `ready` deltaP `3.9414` edge `0.0124` maxDD `-1.2855`
- `market_context_high->commodity_1h` score `-0.4147` n `146` status `ready` deltaP `5.502` edge `0.0166` maxDD `-4.3601`
- `market_context_high->unknown_1h` score `-0.4248` n `146` status `ready` deltaP `1.6508` edge `0.0199` maxDD `-2.6375`
- `market_context_high->fx_1h` score `-0.5982` n `146` status `ready` deltaP `-0.0861` edge `0.0042` maxDD `-0.278`
- `market_context_high->metal_4h` score `-0.6234` n `146` status `ready` deltaP `4.3497` edge `0.0578` maxDD `-4.7664`
- `market_context_high->metal_1h` score `-0.6716` n `146` status `ready` deltaP `0.8121` edge `0.0134` maxDD `-2.9823`
- `market_context_high->fx_4h` score `-0.8244` n `146` status `ready` deltaP `0.5367` edge `0.0135` maxDD `-0.8621`
- `market_context_high->equity_1h` score `-0.8312` n `146` status `ready` deltaP `-0.527` edge `0.0181` maxDD `-2.7085`
- `market_context_high->fx_24h` score `-1.0463` n `118` status `ready` deltaP `0.7357` edge `0.0031` maxDD `-1.6157`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
