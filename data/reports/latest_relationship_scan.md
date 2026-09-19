# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-19T00:22:29.858178+00:00`
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

- `news_risk_high->crypto_major_24h` score `62.1901` n `40` status `ready` deltaP `32.5347` edge `5.0548` maxDD `-5.8019`
- `news_risk_high->crypto_alt_24h` score `56.8829` n `40` status `ready` deltaP `34.0278` edge `4.6513` maxDD `-9.3661`
- `market_context_high->unknown_4h` score `37.7663` n `149` status `ready` deltaP `-1.3781` edge `3.1797` maxDD `-0.5326`
- `news_risk_high->equity_24h` score `15.0572` n `40` status `ready` deltaP `51.9097` edge `0.9087` maxDD `0.0`
- `risk_on_high->unknown_4h` score `11.6449` n `52` status `ready` deltaP `-8.6187` edge `1.0504` maxDD `-0.4694`
- `risk_on_and_context->unknown_4h` score `11.6449` n `52` status `ready` deltaP `-8.6187` edge `1.0504` maxDD `-0.4694`
- `news_risk_high->crypto_alt_4h` score `8.8852` n `72` status `ready` deltaP `28.3706` edge `0.6639` maxDD `-7.675`
- `risk_on_high->commodity_24h` score `8.5118` n `52` status `ready` deltaP `47.2222` edge `0.3945` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `8.5118` n `52` status `ready` deltaP `47.2222` edge `0.3945` maxDD `0.0`
- `market_context_high->commodity_24h` score `7.2126` n `149` status `ready` deltaP `40.5108` edge `0.3835` maxDD `-0.8682`
- `news_risk_high->crypto_major_4h` score `6.1405` n `72` status `ready` deltaP `25.254` edge `0.4608` maxDD `-8.0625`
- `news_risk_high->metal_24h` score `4.8521` n `40` status `ready` deltaP `34.5486` edge `0.1898` maxDD `-0.2629`
- `news_risk_high->crypto_alt_1h` score `3.1696` n `72` status `ready` deltaP `17.4734` edge `0.1942` maxDD `-2.058`
- `news_risk_high->crypto_major_1h` score `2.9049` n `72` status `ready` deltaP `22.0892` edge `0.1471` maxDD `-2.8494`
- `risk_on_high->commodity_4h` score `2.7469` n `52` status `ready` deltaP `32.0825` edge `0.05` maxDD `-0.1313`
- `risk_on_and_context->commodity_4h` score `2.7469` n `52` status `ready` deltaP `32.0825` edge `0.05` maxDD `-0.1313`
- `market_context_high->commodity_4h` score `2.6466` n `149` status `ready` deltaP `28.5848` edge `0.0718` maxDD `-0.345`
- `news_risk_high->fx_24h` score `1.8832` n `40` status `ready` deltaP `9.3056` edge `0.0991` maxDD `-0.0029`
- `news_risk_high->equity_4h` score `1.5391` n `72` status `ready` deltaP `12.3984` edge `0.1356` maxDD `-4.1995`
- `news_risk_high->fx_4h` score `1.4861` n `72` status `ready` deltaP `16.1585` edge `0.038` maxDD `-0.084`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
