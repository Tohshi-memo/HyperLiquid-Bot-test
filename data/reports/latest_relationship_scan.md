# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-19T16:37:25.564450+00:00`
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

- `news_risk_high->crypto_major_24h` score `51.9058` n `72` status `ready` deltaP `29.8611` edge `4.2156` maxDD `-5.8019`
- `news_risk_high->crypto_alt_24h` score `45.5434` n `72` status `ready` deltaP `35.0695` edge `3.6994` maxDD `-9.3661`
- `market_context_high->unknown_4h` score `43.4112` n `132` status `ready` deltaP `-3.1319` edge `3.6618` maxDD `-0.5326`
- `risk_on_high->unknown_4h` score `18.427` n `42` status `ready` deltaP `-13.1969` edge `1.6461` maxDD `-0.4694`
- `risk_on_and_context->unknown_4h` score `18.427` n `42` status `ready` deltaP `-13.1969` edge `1.6461` maxDD `-0.4694`
- `news_risk_high->equity_24h` score `9.612` n `72` status `ready` deltaP `39.4097` edge `0.5425` maxDD `-0.0053`
- `risk_on_high->commodity_24h` score `9.0352` n `42` status `ready` deltaP `47.5694` edge `0.4358` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `9.0352` n `42` status `ready` deltaP `47.5694` edge `0.4358` maxDD `0.0`
- `market_context_high->commodity_24h` score `7.4845` n `132` status `ready` deltaP `39.9936` edge `0.4096` maxDD `-0.8682`
- `news_risk_high->crypto_alt_4h` score `5.7892` n `98` status `ready` deltaP `22.0756` edge `0.4562` maxDD `-7.675`
- `news_risk_high->crypto_major_4h` score `4.3485` n `98` status `ready` deltaP `21.9232` edge `0.342` maxDD `-8.0625`
- `news_risk_high->crypto_alt_1h` score `3.3539` n `98` status `ready` deltaP `19.6719` edge `0.1949` maxDD `-2.058`
- `market_context_high->commodity_4h` score `2.5463` n `132` status `ready` deltaP `27.1203` edge `0.0732` maxDD `-0.345`
- `news_risk_high->crypto_major_1h` score `2.4318` n `98` status `ready` deltaP `20.4204` edge `0.1188` maxDD `-2.8494`
- `risk_on_high->commodity_4h` score `2.431` n `42` status `ready` deltaP `28.419` edge `0.0481` maxDD `-0.1313`
- `risk_on_and_context->commodity_4h` score `2.431` n `42` status `ready` deltaP `28.419` edge `0.0481` maxDD `-0.1313`
- `news_risk_high->metal_24h` score `1.7261` n `72` status `ready` deltaP `22.5694` edge `0.0778` maxDD `-2.4203`
- `risk_on_high->commodity_1h` score `1.546` n `42` status `ready` deltaP `19.1831` edge `0.0195` maxDD `-0.1507`
- `risk_on_and_context->commodity_1h` score `1.546` n `42` status `ready` deltaP `19.1831` edge `0.0195` maxDD `-0.1507`
- `market_context_high->commodity_1h` score `1.5222` n `132` status `ready` deltaP `18.9666` edge `0.0256` maxDD `-0.3491`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
