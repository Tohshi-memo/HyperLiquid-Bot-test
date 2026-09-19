# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-19T04:07:29.062181+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8282`

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

- `news_risk_high->crypto_major_24h` score `61.4575` n `53` status `ready` deltaP `34.9875` edge `4.9774` maxDD `-5.8019`
- `news_risk_high->crypto_alt_24h` score `55.6786` n `53` status `ready` deltaP `37.0938` edge `4.5305` maxDD `-9.3661`
- `market_context_high->unknown_4h` score `36.2795` n `149` status `ready` deltaP `-1.3781` edge `3.0558` maxDD `-0.5326`
- `news_risk_high->equity_24h` score `14.7732` n `53` status `ready` deltaP `49.3056` edge `0.9024` maxDD `0.0`
- `risk_on_high->unknown_4h` score `10.1581` n `52` status `ready` deltaP `-8.6187` edge `0.9265` maxDD `-0.4694`
- `risk_on_and_context->unknown_4h` score `10.1581` n `52` status `ready` deltaP `-8.6187` edge `0.9265` maxDD `-0.4694`
- `news_risk_high->crypto_alt_4h` score `8.8468` n `72` status `ready` deltaP `28.3706` edge `0.6607` maxDD `-7.675`
- `risk_on_high->commodity_24h` score `8.2911` n `52` status `ready` deltaP `45.1389` edge `0.39` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `8.2911` n `52` status `ready` deltaP `45.1389` edge `0.39` maxDD `0.0`
- `market_context_high->commodity_24h` score `6.992` n `149` status `ready` deltaP `38.4275` edge `0.379` maxDD `-0.8682`
- `news_risk_high->crypto_major_4h` score `6.0042` n `72` status `ready` deltaP `24.6443` edge `0.4535` maxDD `-8.0625`
- `news_risk_high->metal_24h` score `4.757` n `53` status `ready` deltaP `37.441` edge `0.1626` maxDD `-0.2629`
- `news_risk_high->crypto_alt_1h` score `3.229` n `81` status `ready` deltaP `17.0012` edge `0.2023` maxDD `-2.058`
- `news_risk_high->crypto_major_1h` score `2.6017` n `81` status `ready` deltaP `19.9194` edge `0.1363` maxDD `-2.8494`
- `risk_on_high->commodity_4h` score `2.5224` n `52` status `ready` deltaP `30.1008` edge `0.0445` maxDD `-0.1313`
- `risk_on_and_context->commodity_4h` score `2.5224` n `52` status `ready` deltaP `30.1008` edge `0.0445` maxDD `-0.1313`
- `market_context_high->commodity_4h` score `2.4221` n `149` status `ready` deltaP `26.6031` edge `0.0663` maxDD `-0.345`
- `news_risk_high->fx_4h` score `1.5507` n `72` status `ready` deltaP `16.9207` edge `0.0383` maxDD `-0.084`
- `news_risk_high->equity_4h` score `1.5463` n `72` status `ready` deltaP `12.3984` edge `0.1362` maxDD `-4.1995`
- `news_risk_high->fx_24h` score `1.4913` n `53` status `ready` deltaP `7.6618` edge `0.0774` maxDD `-0.0029`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
