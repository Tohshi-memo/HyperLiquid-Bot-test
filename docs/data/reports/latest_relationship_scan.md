# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-19T01:52:28.393747+00:00`
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

- `news_risk_high->crypto_major_24h` score `62.5598` n `45` status `ready` deltaP `33.6458` edge `5.0782` maxDD `-5.8019`
- `news_risk_high->crypto_alt_24h` score `57.2508` n `45` status `ready` deltaP `35.4167` edge `4.6727` maxDD `-9.3661`
- `market_context_high->unknown_4h` score `36.0947` n `149` status `ready` deltaP `-1.3781` edge `3.0404` maxDD `-0.5326`
- `news_risk_high->equity_24h` score `15.3326` n `45` status `ready` deltaP `50.8681` edge `0.9386` maxDD `0.0`
- `risk_on_high->unknown_4h` score `9.9733` n `52` status `ready` deltaP `-8.6187` edge `0.9111` maxDD `-0.4694`
- `risk_on_and_context->unknown_4h` score `9.9733` n `52` status `ready` deltaP `-8.6187` edge `0.9111` maxDD `-0.4694`
- `news_risk_high->crypto_alt_4h` score `8.9624` n `72` status `ready` deltaP `28.6755` edge `0.6683` maxDD `-7.675`
- `risk_on_high->commodity_24h` score `8.402` n `52` status `ready` deltaP `46.1806` edge `0.3923` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `8.402` n `52` status `ready` deltaP `46.1806` edge `0.3923` maxDD `0.0`
- `market_context_high->commodity_24h` score `7.1029` n `149` status `ready` deltaP `39.4692` edge `0.3813` maxDD `-0.8682`
- `news_risk_high->crypto_major_4h` score `6.1649` n `72` status `ready` deltaP `25.5589` edge `0.4608` maxDD `-8.0625`
- `news_risk_high->metal_24h` score `4.8281` n `45` status `ready` deltaP `35.7639` edge `0.1797` maxDD `-0.2629`
- `news_risk_high->crypto_alt_1h` score `3.2571` n `72` status `ready` deltaP `17.9225` edge `0.1985` maxDD `-2.058`
- `news_risk_high->crypto_major_1h` score `2.9001` n `72` status `ready` deltaP `22.2389` edge `0.1457` maxDD `-2.8494`
- `risk_on_high->commodity_4h` score `2.6425` n `52` status `ready` deltaP `31.1679` edge `0.0474` maxDD `-0.1313`
- `risk_on_and_context->commodity_4h` score `2.6425` n `52` status `ready` deltaP `31.1679` edge `0.0474` maxDD `-0.1313`
- `market_context_high->commodity_4h` score `2.5423` n `149` status `ready` deltaP `27.6702` edge `0.0692` maxDD `-0.345`
- `news_risk_high->fx_24h` score `1.7911` n `45` status `ready` deltaP `8.8889` edge `0.0942` maxDD `-0.0029`
- `news_risk_high->equity_4h` score `1.5427` n `72` status `ready` deltaP `12.3984` edge `0.1359` maxDD `-4.1995`
- `news_risk_high->fx_4h` score `1.5251` n `72` status `ready` deltaP `16.6159` edge `0.0382` maxDD `-0.084`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
