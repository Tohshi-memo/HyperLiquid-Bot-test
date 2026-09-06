# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-06T05:22:25.799707+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10755`

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

- `risk_on_high->unknown_4h` score `13.5215` n `145` status `ready` deltaP `-3.9224` edge `1.3535` maxDD `-7.7112`
- `risk_on_and_context->unknown_4h` score `13.5215` n `145` status `ready` deltaP `-3.9224` edge `1.3535` maxDD `-7.7112`
- `news_risk_high->crypto_alt_24h` score `5.7` n `34` status `ready` deltaP `25.3983` edge `0.3272` maxDD `-0.3881`
- `news_risk_high->commodity_24h` score `4.0327` n `34` status `ready` deltaP `20.1389` edge `0.2018` maxDD `0.0`
- `news_risk_high->crypto_major_4h` score `3.8071` n `34` status `ready` deltaP `19.0011` edge `0.2218` maxDD `-0.8307`
- `news_risk_high->metal_4h` score `2.4387` n `34` status `ready` deltaP `24.2916` edge `0.0634` maxDD `-0.7692`
- `news_risk_high->commodity_4h` score `1.7342` n `34` status `ready` deltaP `7.9358` edge `0.1117` maxDD `-0.2737`
- `risk_on_high->crypto_major_24h` score `1.7005` n `87` status `ready` deltaP `12.482` edge `0.8674` maxDD `-47.9416`
- `risk_on_and_context->crypto_major_24h` score `1.7005` n `87` status `ready` deltaP `12.482` edge `0.8674` maxDD `-47.9416`
- `market_context_high->equity_24h` score `1.5589` n `170` status `ready` deltaP `13.5069` edge `0.3937` maxDD `-16.9737`
- `news_risk_high->fx_24h` score `1.4912` n `34` status `ready` deltaP `25.2043` edge `0.0438` maxDD `-3.0051`
- `news_risk_high->equity_1h` score `1.4648` n `34` status `ready` deltaP `10.6112` edge `0.0904` maxDD `-0.7924`
- `news_risk_high->index_1h` score `1.2569` n `34` status `ready` deltaP `14.9525` edge `0.0143` maxDD `-0.0724`
- `news_risk_high->metal_1h` score `1.1388` n `34` status `ready` deltaP `13.2617` edge `0.0258` maxDD `-0.2118`
- `news_risk_high->crypto_major_1h` score `0.9959` n `34` status `ready` deltaP `4.9313` edge `0.0684` maxDD `-0.4628`
- `news_risk_high->crypto_major_24h` score `0.8099` n `34` status `ready` deltaP `16.2684` edge `0.1913` maxDD `-12.6738`
- `news_risk_high->crypto_alt_1h` score `0.3542` n `34` status `ready` deltaP `5.627` edge `0.0185` maxDD `-0.7867`
- `news_risk_high->commodity_1h` score `0.124` n `34` status `ready` deltaP `8.4185` edge `0.0044` maxDD `-0.9036`
- `market_context_high->unknown_4h` score `0.0544` n `245` status `ready` deltaP `0.6378` edge `0.2471` maxDD `-9.4124`
- `risk_on_high->index_1h` score `-0.0998` n `145` status `ready` deltaP `5.2364` edge `-0.003` maxDD `-0.5764`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
