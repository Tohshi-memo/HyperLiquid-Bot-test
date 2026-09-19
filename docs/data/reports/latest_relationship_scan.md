# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-19T03:37:26.925328+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8168`

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

- `news_risk_high->crypto_major_24h` score `61.9558` n `51` status `ready` deltaP `34.6916` edge `5.0209` maxDD `-5.8019`
- `news_risk_high->crypto_alt_24h` score `56.3414` n `51` status `ready` deltaP `36.7239` edge `4.5882` maxDD `-9.3661`
- `market_context_high->unknown_4h` score `36.2183` n `149` status `ready` deltaP `-1.3781` edge `3.0507` maxDD `-0.5326`
- `news_risk_high->equity_24h` score `15.0218` n `51` status `ready` deltaP `49.6528` edge `0.9208` maxDD `0.0`
- `risk_on_high->unknown_4h` score `10.0969` n `52` status `ready` deltaP `-8.6187` edge `0.9214` maxDD `-0.4694`
- `risk_on_and_context->unknown_4h` score `10.0969` n `52` status `ready` deltaP `-8.6187` edge `0.9214` maxDD `-0.4694`
- `news_risk_high->crypto_alt_4h` score `8.86` n `72` status `ready` deltaP `28.3706` edge `0.6618` maxDD `-7.675`
- `risk_on_high->commodity_24h` score `8.311` n `52` status `ready` deltaP `45.3125` edge `0.3905` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `8.311` n `52` status `ready` deltaP `45.3125` edge `0.3905` maxDD `0.0`
- `market_context_high->commodity_24h` score `7.0119` n `149` status `ready` deltaP `38.6011` edge `0.3795` maxDD `-0.8682`
- `news_risk_high->crypto_major_4h` score `6.0258` n `72` status `ready` deltaP `24.6443` edge `0.4553` maxDD `-8.0625`
- `news_risk_high->metal_24h` score `4.8019` n `51` status `ready` deltaP `37.0711` edge `0.1688` maxDD `-0.2629`
- `news_risk_high->crypto_alt_1h` score `3.5133` n `79` status `ready` deltaP `18.8452` edge `0.2137` maxDD `-2.058`
- `news_risk_high->crypto_major_1h` score `2.8467` n `79` status `ready` deltaP `21.6763` edge `0.145` maxDD `-2.8494`
- `risk_on_high->commodity_4h` score `2.526` n `52` status `ready` deltaP `30.1008` edge `0.0448` maxDD `-0.1313`
- `risk_on_and_context->commodity_4h` score `2.526` n `52` status `ready` deltaP `30.1008` edge `0.0448` maxDD `-0.1313`
- `market_context_high->commodity_4h` score `2.4257` n `149` status `ready` deltaP `26.6031` edge `0.0666` maxDD `-0.345`
- `news_risk_high->fx_24h` score `1.584` n `51` status `ready` deltaP `7.935` edge `0.0833` maxDD `-0.0029`
- `news_risk_high->equity_4h` score `1.5463` n `72` status `ready` deltaP `12.3984` edge `0.1362` maxDD `-4.1995`
- `news_risk_high->fx_4h` score `1.5385` n `72` status `ready` deltaP `16.7683` edge `0.0383` maxDD `-0.084`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
