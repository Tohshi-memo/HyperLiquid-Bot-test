# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-19T12:22:29.649723+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8522`

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

- `news_risk_high->crypto_major_24h` score `53.5915` n `72` status `ready` deltaP `32.8125` edge `4.3364` maxDD `-5.8019`
- `news_risk_high->crypto_alt_24h` score `46.9864` n `72` status `ready` deltaP `37.3264` edge `3.8046` maxDD `-9.3661`
- `market_context_high->unknown_4h` score `37.0057` n `144` status `ready` deltaP `-2.185` edge `3.1217` maxDD `-0.5326`
- `news_risk_high->equity_24h` score `10.7337` n `72` status `ready` deltaP `42.3611` edge `0.6163` maxDD `-0.0053`
- `risk_on_high->unknown_4h` score `8.2531` n `52` status `ready` deltaP `-9.076` edge `0.7708` maxDD `-0.4694`
- `risk_on_and_context->unknown_4h` score `8.2531` n `52` status `ready` deltaP `-9.076` edge `0.7708` maxDD `-0.4694`
- `risk_on_high->commodity_24h` score `8.228` n `52` status `ready` deltaP `44.9653` edge `0.3859` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `8.228` n `52` status `ready` deltaP `44.9653` edge `0.3859` maxDD `0.0`
- `market_context_high->commodity_24h` score `7.0098` n `144` status `ready` deltaP `38.0209` edge `0.3832` maxDD `-0.8682`
- `news_risk_high->crypto_alt_4h` score `6.543` n `82` status `ready` deltaP `23.3232` edge `0.5107` maxDD `-7.675`
- `news_risk_high->crypto_major_4h` score `4.6384` n `82` status `ready` deltaP `20.7317` edge `0.3741` maxDD `-8.0625`
- `news_risk_high->crypto_alt_1h` score `3.5607` n `94` status `ready` deltaP `20.458` edge `0.2069` maxDD `-2.058`
- `risk_on_high->commodity_4h` score `2.6745` n `52` status `ready` deltaP `31.7777` edge `0.046` maxDD `-0.1313`
- `risk_on_and_context->commodity_4h` score `2.6745` n `52` status `ready` deltaP `31.7777` edge `0.046` maxDD `-0.1313`
- `market_context_high->commodity_4h` score `2.5225` n `144` status `ready` deltaP `27.5576` edge `0.0683` maxDD `-0.345`
- `news_risk_high->crypto_major_1h` score `2.4827` n `94` status `ready` deltaP `20.4262` edge `0.123` maxDD `-2.8494`
- `news_risk_high->metal_24h` score `1.9185` n `72` status `ready` deltaP `24.4792` edge `0.0811` maxDD `-2.4203`
- `news_risk_high->fx_4h` score `1.1154` n `82` status `ready` deltaP `12.5` edge `0.0315` maxDD `-0.084`
- `market_context_high->commodity_1h` score `1.0896` n `144` status `ready` deltaP `15.9598` edge `0.0221` maxDD `-0.3491`
- `news_risk_high->equity_1h` score `0.7016` n `94` status `ready` deltaP `9.5585` edge `0.0353` maxDD `-0.9112`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
