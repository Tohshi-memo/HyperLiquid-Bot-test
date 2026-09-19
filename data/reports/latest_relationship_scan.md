# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-19T01:22:29.964854+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8098`

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

- `news_risk_high->crypto_major_24h` score `62.7524` n `44` status `ready` deltaP `33.4438` edge `5.0956` maxDD `-5.8019`
- `news_risk_high->crypto_alt_24h` score `57.4682` n `44` status `ready` deltaP `35.1642` edge `4.6925` maxDD `-9.3661`
- `market_context_high->unknown_4h` score `36.5279` n `149` status `ready` deltaP `-1.3781` edge `3.0765` maxDD `-0.5326`
- `news_risk_high->equity_24h` score `15.34` n `44` status `ready` deltaP `51.2153` edge `0.9369` maxDD `0.0`
- `risk_on_high->unknown_4h` score `10.4065` n `52` status `ready` deltaP `-8.6187` edge `0.9472` maxDD `-0.4694`
- `risk_on_and_context->unknown_4h` score `10.4065` n `52` status `ready` deltaP `-8.6187` edge `0.9472` maxDD `-0.4694`
- `news_risk_high->crypto_alt_4h` score `8.931` n `72` status `ready` deltaP `28.523` edge `0.6667` maxDD `-7.675`
- `risk_on_high->commodity_24h` score `8.437` n `52` status `ready` deltaP `46.5278` edge `0.3929` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `8.437` n `52` status `ready` deltaP `46.5278` edge `0.3929` maxDD `0.0`
- `market_context_high->commodity_24h` score `7.1379` n `149` status `ready` deltaP `39.8164` edge `0.3819` maxDD `-0.8682`
- `news_risk_high->crypto_major_4h` score `6.1479` n `72` status `ready` deltaP `25.4065` edge `0.4604` maxDD `-8.0625`
- `news_risk_high->metal_24h` score `4.8482` n `44` status `ready` deltaP `35.685` edge `0.1819` maxDD `-0.2629`
- `news_risk_high->crypto_alt_1h` score `3.2091` n `72` status `ready` deltaP `17.6231` edge `0.1965` maxDD `-2.058`
- `news_risk_high->crypto_major_1h` score `2.8773` n `72` status `ready` deltaP `22.0892` edge `0.1448` maxDD `-2.8494`
- `risk_on_high->commodity_4h` score `2.6777` n `52` status `ready` deltaP `31.4728` edge `0.0483` maxDD `-0.1313`
- `risk_on_and_context->commodity_4h` score `2.6777` n `52` status `ready` deltaP `31.4728` edge `0.0483` maxDD `-0.1313`
- `market_context_high->commodity_4h` score `2.5775` n `149` status `ready` deltaP `27.9751` edge `0.0701` maxDD `-0.345`
- `news_risk_high->fx_24h` score `1.8165` n `44` status `ready` deltaP `9.012` edge `0.0955` maxDD `-0.0029`
- `news_risk_high->equity_4h` score `1.5403` n `72` status `ready` deltaP `12.3984` edge `0.1357` maxDD `-4.1995`
- `news_risk_high->fx_4h` score `1.5007` n `72` status `ready` deltaP `16.311` edge `0.0382` maxDD `-0.084`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
