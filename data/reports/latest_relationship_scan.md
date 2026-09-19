# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-19T03:07:26.750133+00:00`
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

- `news_risk_high->crypto_major_24h` score `62.3994` n `49` status `ready` deltaP `34.3714` edge `5.06` maxDD `-5.8019`
- `news_risk_high->crypto_alt_24h` score `56.931` n `49` status `ready` deltaP `36.3237` edge `4.64` maxDD `-9.3661`
- `market_context_high->unknown_4h` score `36.1535` n `149` status `ready` deltaP `-1.3781` edge `3.0453` maxDD `-0.5326`
- `news_risk_high->equity_24h` score `15.2212` n `49` status `ready` deltaP `50.0` edge `0.9351` maxDD `0.0`
- `risk_on_high->unknown_4h` score `10.0321` n `52` status `ready` deltaP `-8.6187` edge `0.916` maxDD `-0.4694`
- `risk_on_and_context->unknown_4h` score `10.0321` n `52` status `ready` deltaP `-8.6187` edge `0.916` maxDD `-0.4694`
- `news_risk_high->crypto_alt_4h` score `8.878` n `72` status `ready` deltaP `28.3706` edge `0.6633` maxDD `-7.675`
- `risk_on_high->commodity_24h` score `8.346` n `52` status `ready` deltaP `45.6597` edge `0.3911` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `8.346` n `52` status `ready` deltaP `45.6597` edge `0.3911` maxDD `0.0`
- `market_context_high->commodity_24h` score `7.0468` n `149` status `ready` deltaP `38.9483` edge `0.3801` maxDD `-0.8682`
- `news_risk_high->crypto_major_4h` score `6.0682` n `72` status `ready` deltaP `24.9492` edge `0.4568` maxDD `-8.0625`
- `news_risk_high->metal_24h` score `4.801` n `49` status `ready` deltaP `36.6709` edge `0.1714` maxDD `-0.2629`
- `news_risk_high->crypto_alt_1h` score `3.6654` n `77` status `ready` deltaP `19.6361` edge `0.2211` maxDD `-2.058`
- `news_risk_high->crypto_major_1h` score `3.126` n `77` status `ready` deltaP `23.5322` edge `0.1559` maxDD `-2.8494`
- `risk_on_high->commodity_4h` score `2.5588` n `52` status `ready` deltaP `30.4057` edge `0.0455` maxDD `-0.1313`
- `risk_on_and_context->commodity_4h` score `2.5588` n `52` status `ready` deltaP `30.4057` edge `0.0455` maxDD `-0.1313`
- `market_context_high->commodity_4h` score `2.4585` n `149` status `ready` deltaP `26.908` edge `0.0673` maxDD `-0.345`
- `news_risk_high->fx_24h` score `1.6725` n `49` status `ready` deltaP `8.2023` edge `0.0889` maxDD `-0.0029`
- `news_risk_high->equity_4h` score `1.5463` n `72` status `ready` deltaP `12.3984` edge `0.1362` maxDD `-4.1995`
- `news_risk_high->fx_4h` score `1.5385` n `72` status `ready` deltaP `16.7683` edge `0.0383` maxDD `-0.084`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
