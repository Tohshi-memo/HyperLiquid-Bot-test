# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-28T03:22:11.085035+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `3248`

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

- `news_risk_high->unknown_1h` score `3312.7105` n `31` status `ready` deltaP `1.6322` edge `276.0659` maxDD `-0.7395`
- `news_risk_high->unknown_4h` score `3175.4781` n `31` status `ready` deltaP `3.634` edge `264.6046` maxDD `-0.1191`
- `news_risk_high->crypto_major_24h` score `18.1338` n `31` status `ready` deltaP `28.9428` edge `1.3182` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `12.5134` n `31` status `ready` deltaP `26.8631` edge `0.8637` maxDD `0.0`
- `news_risk_high->equity_24h` score `11.2913` n `31` status `ready` deltaP `23.9168` edge `0.7815` maxDD `0.0`
- `news_risk_high->crypto_alt_4h` score `7.0513` n `31` status `ready` deltaP `18.6811` edge `0.5501` maxDD `-5.2957`
- `news_risk_high->equity_4h` score `4.95` n `31` status `ready` deltaP `27.7734` edge `0.2754` maxDD `-2.178`
- `news_risk_high->fx_24h` score `4.7246` n `31` status `ready` deltaP `38.6762` edge `0.1487` maxDD `-0.0262`
- `news_risk_high->crypto_major_4h` score `4.3504` n `31` status `ready` deltaP `13.1196` edge `0.612` maxDD `-7.6714`
- `news_risk_high->metal_24h` score `3.3452` n `31` status `ready` deltaP `12.1877` edge `0.225` maxDD `-0.1986`
- `news_risk_high->index_1h` score `2.1702` n `31` status `ready` deltaP `26.753` edge `0.011` maxDD `-0.0136`
- `news_risk_high->index_4h` score `2.1631` n `31` status `ready` deltaP `27.0112` edge `0.0262` maxDD `-0.4146`
- `news_risk_high->index_24h` score `2.162` n `31` status `ready` deltaP `24.6101` edge `0.0161` maxDD `0.0`
- `news_risk_high->equity_1h` score `2.0608` n `31` status `ready` deltaP `13.9994` edge `0.0971` maxDD `-0.1621`
- `news_risk_high->crypto_major_1h` score `1.6699` n `31` status `ready` deltaP `4.7711` edge `0.2284` maxDD `-1.6897`
- `news_risk_high->crypto_alt_1h` score `1.5285` n `31` status `ready` deltaP `7.9148` edge `0.1789` maxDD `-1.5232`
- `news_risk_high->metal_1h` score `1.0601` n `31` status `ready` deltaP `23.445` edge `0.0075` maxDD `-0.2315`
- `news_risk_high->commodity_4h` score `0.3523` n `31` status `ready` deltaP `8.8267` edge `0.0261` maxDD `-0.5151`
- `news_risk_high->metal_4h` score `0.2008` n `31` status `ready` deltaP `9.461` edge `0.0184` maxDD `-0.7918`
- `news_risk_high->commodity_1h` score `-0.3986` n `31` status `ready` deltaP `-2.8105` edge `0.0117` maxDD `-0.0947`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
