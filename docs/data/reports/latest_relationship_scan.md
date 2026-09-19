# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-19T00:43:00.451850+00:00`
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

- `news_risk_high->crypto_major_24h` score `62.4472` n `41` status `ready` deltaP `32.7786` edge `5.0746` maxDD `-5.8019`
- `news_risk_high->crypto_alt_24h` score `57.2025` n `41` status `ready` deltaP `34.3327` edge `4.6759` maxDD `-9.3661`
- `market_context_high->unknown_4h` score `37.5803` n `149` status `ready` deltaP `-1.3781` edge `3.1642` maxDD `-0.5326`
- `news_risk_high->equity_24h` score `15.1357` n `41` status `ready` deltaP `51.7361` edge `0.9164` maxDD `0.0`
- `risk_on_high->unknown_4h` score `11.4589` n `52` status `ready` deltaP `-8.6187` edge `1.0349` maxDD `-0.4694`
- `risk_on_and_context->unknown_4h` score `11.4589` n `52` status `ready` deltaP `-8.6187` edge `1.0349` maxDD `-0.4694`
- `news_risk_high->crypto_alt_4h` score `8.8912` n `72` status `ready` deltaP `28.3706` edge `0.6644` maxDD `-7.675`
- `risk_on_high->commodity_24h` score `8.4919` n `52` status `ready` deltaP `47.0486` edge `0.394` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `8.4919` n `52` status `ready` deltaP `47.0486` edge `0.394` maxDD `0.0`
- `market_context_high->commodity_24h` score `7.1927` n `149` status `ready` deltaP `40.3372` edge `0.383` maxDD `-0.8682`
- `news_risk_high->crypto_major_4h` score `6.1357` n `72` status `ready` deltaP `25.254` edge `0.4604` maxDD `-8.0625`
- `news_risk_high->metal_24h` score `4.8656` n `41` status `ready` deltaP `34.8535` edge `0.1889` maxDD `-0.2629`
- `news_risk_high->crypto_alt_1h` score `3.1708` n `72` status `ready` deltaP `17.4734` edge `0.1943` maxDD `-2.058`
- `news_risk_high->crypto_major_1h` score `2.8965` n `72` status `ready` deltaP `22.0892` edge `0.1464` maxDD `-2.8494`
- `risk_on_high->commodity_4h` score `2.7299` n `52` status `ready` deltaP `31.9301` edge `0.0496` maxDD `-0.1313`
- `risk_on_and_context->commodity_4h` score `2.7299` n `52` status `ready` deltaP `31.9301` edge `0.0496` maxDD `-0.1313`
- `market_context_high->commodity_4h` score `2.6296` n `149` status `ready` deltaP `28.4324` edge `0.0714` maxDD `-0.345`
- `news_risk_high->fx_24h` score `1.8658` n `41` status `ready` deltaP `9.1929` edge `0.0984` maxDD `-0.0029`
- `news_risk_high->equity_4h` score `1.5403` n `72` status `ready` deltaP `12.3984` edge `0.1357` maxDD `-4.1995`
- `news_risk_high->fx_4h` score `1.4739` n `72` status `ready` deltaP `16.0061` edge `0.038` maxDD `-0.084`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
