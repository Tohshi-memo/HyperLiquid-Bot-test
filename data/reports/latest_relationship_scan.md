# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-19T16:07:26.350669+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8582`

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

- `news_risk_high->crypto_major_24h` score `52.0548` n `72` status `ready` deltaP `30.2083` edge `4.2257` maxDD `-5.8019`
- `news_risk_high->crypto_alt_24h` score `45.7056` n `72` status `ready` deltaP `35.4167` edge `3.7106` maxDD `-9.3661`
- `market_context_high->unknown_4h` score `42.2007` n `134` status `ready` deltaP `-2.9623` edge `3.5598` maxDD `-0.5326`
- `risk_on_high->unknown_4h` score `15.5362` n `44` status `ready` deltaP `-12.2228` edge `1.3987` maxDD `-0.4694`
- `risk_on_and_context->unknown_4h` score `15.5362` n `44` status `ready` deltaP `-12.2228` edge `1.3987` maxDD `-0.4694`
- `news_risk_high->equity_24h` score `9.7418` n `72` status `ready` deltaP `39.7569` edge `0.551` maxDD `-0.0053`
- `risk_on_high->commodity_24h` score `8.909` n `44` status `ready` deltaP `47.2222` edge `0.4276` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `8.909` n `44` status `ready` deltaP `47.2222` edge `0.4276` maxDD `0.0`
- `market_context_high->commodity_24h` score `7.4237` n `134` status `ready` deltaP `39.7595` edge `0.4061` maxDD `-0.8682`
- `news_risk_high->crypto_alt_4h` score `5.8888` n `97` status `ready` deltaP `22.1807` edge `0.4638` maxDD `-7.675`
- `news_risk_high->crypto_major_4h` score `4.4097` n `97` status `ready` deltaP `22.0283` edge `0.3464` maxDD `-8.0625`
- `news_risk_high->crypto_alt_1h` score `3.3611` n `98` status `ready` deltaP `19.6719` edge `0.1955` maxDD `-2.058`
- `market_context_high->commodity_4h` score `2.5394` n `134` status `ready` deltaP `27.1546` edge `0.0724` maxDD `-0.345`
- `risk_on_high->commodity_4h` score `2.4882` n `44` status `ready` deltaP `29.0882` edge `0.0484` maxDD `-0.1313`
- `risk_on_and_context->commodity_4h` score `2.4882` n `44` status `ready` deltaP `29.0882` edge `0.0484` maxDD `-0.1313`
- `news_risk_high->crypto_major_1h` score `2.4618` n `98` status `ready` deltaP `20.7198` edge `0.1193` maxDD `-2.8494`
- `news_risk_high->metal_24h` score `1.7285` n `72` status `ready` deltaP `22.5694` edge `0.078` maxDD `-2.4203`
- `risk_on_high->commodity_1h` score `1.6236` n `44` status `ready` deltaP `20.1824` edge `0.0193` maxDD `-0.1507`
- `risk_on_and_context->commodity_1h` score `1.6236` n `44` status `ready` deltaP `20.1824` edge `0.0193` maxDD `-0.1507`
- `market_context_high->commodity_1h` score `1.529` n `134` status `ready` deltaP `19.0969` edge `0.0253` maxDD `-0.3491`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
