# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-19T02:22:27.733635+00:00`
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

- `news_risk_high->crypto_major_24h` score `62.4528` n `46` status `ready` deltaP `33.839` edge `5.068` maxDD `-5.8019`
- `news_risk_high->crypto_alt_24h` score `57.0745` n `46` status `ready` deltaP `35.6582` edge `4.6564` maxDD `-9.3661`
- `market_context_high->unknown_4h` score `36.0875` n `149` status `ready` deltaP `-1.3781` edge `3.0398` maxDD `-0.5326`
- `news_risk_high->equity_24h` score `15.3073` n `46` status `ready` deltaP `50.5208` edge `0.9388` maxDD `0.0`
- `risk_on_high->unknown_4h` score `9.9661` n `52` status `ready` deltaP `-8.6187` edge `0.9105` maxDD `-0.4694`
- `risk_on_and_context->unknown_4h` score `9.9661` n `52` status `ready` deltaP `-8.6187` edge `0.9105` maxDD `-0.4694`
- `news_risk_high->crypto_alt_4h` score `8.937` n `72` status `ready` deltaP `28.523` edge `0.6672` maxDD `-7.675`
- `risk_on_high->commodity_24h` score `8.3683` n `52` status `ready` deltaP `45.8333` edge `0.3918` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `8.3683` n `52` status `ready` deltaP `45.8333` edge `0.3918` maxDD `0.0`
- `market_context_high->commodity_24h` score `7.0691` n `149` status `ready` deltaP `39.1219` edge `0.3808` maxDD `-0.8682`
- `news_risk_high->crypto_major_4h` score `6.1273` n `72` status `ready` deltaP `25.254` edge `0.4597` maxDD `-8.0625`
- `news_risk_high->metal_24h` score `4.8246` n `46` status `ready` deltaP `36.0054` edge `0.1778` maxDD `-0.2629`
- `news_risk_high->crypto_alt_1h` score `3.3742` n `74` status `ready` deltaP `18.6357` edge `0.2035` maxDD `-2.058`
- `news_risk_high->crypto_major_1h` score `2.9829` n `74` status `ready` deltaP `22.8395` edge `0.1486` maxDD `-2.8494`
- `risk_on_high->commodity_4h` score `2.6073` n `52` status `ready` deltaP `30.863` edge `0.0465` maxDD `-0.1313`
- `risk_on_and_context->commodity_4h` score `2.6073` n `52` status `ready` deltaP `30.863` edge `0.0465` maxDD `-0.1313`
- `market_context_high->commodity_4h` score `2.5071` n `149` status `ready` deltaP `27.3653` edge `0.0683` maxDD `-0.345`
- `news_risk_high->fx_24h` score `1.7468` n `46` status `ready` deltaP `8.59` edge `0.0925` maxDD `-0.0029`
- `news_risk_high->equity_4h` score `1.5475` n `72` status `ready` deltaP `12.3984` edge `0.1363` maxDD `-4.1995`
- `news_risk_high->fx_4h` score `1.5385` n `72` status `ready` deltaP `16.7683` edge `0.0383` maxDD `-0.084`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
