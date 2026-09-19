# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-19T15:07:29.337366+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8594`

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

- `news_risk_high->crypto_major_24h` score `52.3659` n `72` status `ready` deltaP `30.9027` edge `4.247` maxDD `-5.8019`
- `news_risk_high->crypto_alt_24h` score `45.9554` n `72` status `ready` deltaP `35.7639` edge `3.7291` maxDD `-9.3661`
- `market_context_high->unknown_4h` score `39.9587` n `138` status `ready` deltaP `-2.6379` edge `3.3708` maxDD `-0.5326`
- `risk_on_high->unknown_4h` score `11.2205` n `48` status `ready` deltaP `-10.5183` edge `1.0277` maxDD `-0.4694`
- `risk_on_and_context->unknown_4h` score `11.2205` n `48` status `ready` deltaP `-10.5183` edge `1.0277` maxDD `-0.4694`
- `news_risk_high->equity_24h` score `9.9893` n `72` status `ready` deltaP `40.4514` edge `0.567` maxDD `-0.0053`
- `risk_on_high->commodity_24h` score `8.5798` n `48` status `ready` deltaP `46.5278` edge `0.4048` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `8.5798` n `48` status `ready` deltaP `46.5278` edge `0.4048` maxDD `0.0`
- `market_context_high->commodity_24h` score `7.2703` n `138` status `ready` deltaP `39.2814` edge `0.3965` maxDD `-0.8682`
- `news_risk_high->crypto_alt_4h` score `6.5541` n `93` status `ready` deltaP `25.4869` edge `0.4972` maxDD `-7.675`
- `news_risk_high->crypto_major_4h` score `4.5663` n `93` status `ready` deltaP `21.7955` edge `0.361` maxDD `-8.0625`
- `news_risk_high->crypto_alt_1h` score `3.2843` n `98` status `ready` deltaP `19.0731` edge `0.1931` maxDD `-2.058`
- `risk_on_high->commodity_4h` score `2.5757` n `48` status `ready` deltaP `30.1829` edge `0.0484` maxDD `-0.1313`
- `risk_on_and_context->commodity_4h` score `2.5757` n `48` status `ready` deltaP `30.1829` edge `0.0484` maxDD `-0.1313`
- `market_context_high->commodity_4h` score `2.5258` n `138` status `ready` deltaP `27.1938` edge `0.071` maxDD `-0.345`
- `news_risk_high->crypto_major_1h` score `2.4726` n `98` status `ready` deltaP `20.8695` edge `0.1192` maxDD `-2.8494`
- `news_risk_high->metal_24h` score `1.7949` n `72` status `ready` deltaP `23.2639` edge `0.0789` maxDD `-2.4203`
- `market_context_high->commodity_1h` score `1.3437` n `138` status `ready` deltaP `17.0203` edge `0.0237` maxDD `-0.3491`
- `risk_on_high->commodity_1h` score `1.1039` n `48` status `ready` deltaP `14.1218` edge `0.0164` maxDD `-0.1507`
- `risk_on_and_context->commodity_1h` score `1.1039` n `48` status `ready` deltaP `14.1218` edge `0.0164` maxDD `-0.1507`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
