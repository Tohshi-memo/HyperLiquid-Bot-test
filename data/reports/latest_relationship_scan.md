# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-19T02:52:28.127049+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8126`

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

- `news_risk_high->crypto_major_24h` score `62.441` n `48` status `ready` deltaP `34.2014` edge `5.0646` maxDD `-5.8019`
- `news_risk_high->crypto_alt_24h` score `56.9884` n `48` status `ready` deltaP `36.1111` edge `4.6462` maxDD `-9.3661`
- `market_context_high->unknown_4h` score `36.1175` n `149` status `ready` deltaP `-1.3781` edge `3.0423` maxDD `-0.5326`
- `news_risk_high->equity_24h` score `15.2759` n `48` status `ready` deltaP `50.1736` edge `0.9385` maxDD `0.0`
- `risk_on_high->unknown_4h` score `9.9961` n `52` status `ready` deltaP `-8.6187` edge `0.913` maxDD `-0.4694`
- `risk_on_and_context->unknown_4h` score `9.9961` n `52` status `ready` deltaP `-8.6187` edge `0.913` maxDD `-0.4694`
- `news_risk_high->crypto_alt_4h` score `8.9094` n `72` status `ready` deltaP `28.523` edge `0.6649` maxDD `-7.675`
- `risk_on_high->commodity_24h` score `8.3623` n `52` status `ready` deltaP `45.8333` edge `0.3913` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `8.3623` n `52` status `ready` deltaP `45.8333` edge `0.3913` maxDD `0.0`
- `market_context_high->commodity_24h` score `7.0631` n `149` status `ready` deltaP `39.1219` edge `0.3803` maxDD `-0.8682`
- `news_risk_high->crypto_major_4h` score `6.0936` n `72` status `ready` deltaP `25.1016` edge `0.4579` maxDD `-8.0625`
- `news_risk_high->metal_24h` score `4.8068` n `48` status `ready` deltaP `36.4583` edge `0.1733` maxDD `-0.2629`
- `news_risk_high->crypto_alt_1h` score `3.5902` n `76` status `ready` deltaP `19.3114` edge `0.217` maxDD `-2.058`
- `news_risk_high->crypto_major_1h` score `3.1017` n `76` status `ready` deltaP `23.2588` edge `0.1557` maxDD `-2.8494`
- `risk_on_high->commodity_4h` score `2.5746` n `52` status `ready` deltaP `30.5582` edge `0.0458` maxDD `-0.1313`
- `risk_on_and_context->commodity_4h` score `2.5746` n `52` status `ready` deltaP `30.5582` edge `0.0458` maxDD `-0.1313`
- `market_context_high->commodity_4h` score `2.4743` n `149` status `ready` deltaP `27.0605` edge `0.0676` maxDD `-0.345`
- `news_risk_high->fx_24h` score `1.7082` n `48` status `ready` deltaP `8.3334` edge `0.091` maxDD `-0.0029`
- `news_risk_high->equity_4h` score `1.5463` n `72` status `ready` deltaP `12.3984` edge `0.1362` maxDD `-4.1995`
- `news_risk_high->fx_4h` score `1.5385` n `72` status `ready` deltaP `16.7683` edge `0.0383` maxDD `-0.084`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
