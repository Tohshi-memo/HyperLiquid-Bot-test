# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-19T05:12:08.441239+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8352`

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

- `news_risk_high->crypto_major_24h` score `60.2193` n `57` status `ready` deltaP `35.17` edge `4.873` maxDD `-5.8019`
- `news_risk_high->crypto_alt_24h` score `54.18` n `57` status `ready` deltaP `37.7559` edge `4.4012` maxDD `-9.3661`
- `market_context_high->unknown_4h` score `36.3225` n `149` status `ready` deltaP `-1.5305` edge `3.0604` maxDD `-0.5326`
- `news_risk_high->equity_24h` score `14.2413` n `57` status `ready` deltaP `48.6111` edge `0.8627` maxDD `0.0`
- `risk_on_high->unknown_4h` score `10.2011` n `52` status `ready` deltaP `-8.7711` edge `0.9311` maxDD `-0.4694`
- `risk_on_and_context->unknown_4h` score `10.2011` n `52` status `ready` deltaP `-8.7711` edge `0.9311` maxDD `-0.4694`
- `news_risk_high->crypto_alt_4h` score `8.6804` n `73` status `ready` deltaP `27.6102` edge `0.6519` maxDD `-7.675`
- `risk_on_high->commodity_24h` score `8.27` n `52` status `ready` deltaP `44.9653` edge `0.3894` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `8.27` n `52` status `ready` deltaP `44.9653` edge `0.3894` maxDD `0.0`
- `market_context_high->commodity_24h` score `6.9709` n `149` status `ready` deltaP `38.2539` edge `0.3784` maxDD `-0.8682`
- `news_risk_high->crypto_major_4h` score `5.8486` n `73` status `ready` deltaP `23.9601` edge `0.4451` maxDD `-8.0625`
- `news_risk_high->metal_24h` score `4.6768` n `57` status `ready` deltaP `38.1031` edge `0.1515` maxDD `-0.2629`
- `news_risk_high->crypto_alt_1h` score `3.2901` n `81` status `ready` deltaP `17.3006` edge `0.2054` maxDD `-2.058`
- `news_risk_high->crypto_major_1h` score `2.6305` n `81` status `ready` deltaP `20.0691` edge `0.1377` maxDD `-2.8494`
- `risk_on_high->commodity_4h` score `2.5188` n `52` status `ready` deltaP `30.1008` edge `0.0442` maxDD `-0.1313`
- `risk_on_and_context->commodity_4h` score `2.5188` n `52` status `ready` deltaP `30.1008` edge `0.0442` maxDD `-0.1313`
- `market_context_high->commodity_4h` score `2.4185` n `149` status `ready` deltaP `26.6031` edge `0.066` maxDD `-0.345`
- `news_risk_high->fx_4h` score `1.5599` n `73` status `ready` deltaP `17.1108` edge `0.0378` maxDD `-0.084`
- `news_risk_high->equity_4h` score `1.3525` n `73` status `ready` deltaP `11.4851` edge `0.1323` maxDD `-4.3594`
- `news_risk_high->fx_24h` score `1.3234` n `57` status `ready` deltaP `7.2734` edge `0.066` maxDD `-0.0029`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
