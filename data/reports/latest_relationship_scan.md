# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-19T15:37:25.713260+00:00`
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

- `news_risk_high->crypto_major_24h` score `52.211` n `72` status `ready` deltaP `30.5555` edge `4.2364` maxDD `-5.8019`
- `news_risk_high->crypto_alt_24h` score `45.8311` n `72` status `ready` deltaP `35.5903` edge `3.7199` maxDD `-9.3661`
- `market_context_high->unknown_4h` score `41.0031` n `136` status `ready` deltaP `-2.7977` edge `3.4589` maxDD `-0.5326`
- `risk_on_high->unknown_4h` score `12.9637` n `46` status `ready` deltaP `-11.3335` edge `1.1784` maxDD `-0.4694`
- `risk_on_and_context->unknown_4h` score `12.9637` n `46` status `ready` deltaP `-11.3335` edge `1.1784` maxDD `-0.4694`
- `news_risk_high->equity_24h` score `9.8643` n `72` status `ready` deltaP `40.1042` edge `0.5589` maxDD `-0.0053`
- `risk_on_high->commodity_24h` score `8.7516` n `46` status `ready` deltaP `46.875` edge `0.4168` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `8.7516` n `46` status `ready` deltaP `46.875` edge `0.4168` maxDD `0.0`
- `market_context_high->commodity_24h` score `7.3495` n `136` status `ready` deltaP `39.5221` edge `0.4015` maxDD `-0.8682`
- `news_risk_high->crypto_alt_4h` score `6.2438` n `95` status `ready` deltaP `23.8736` edge `0.4821` maxDD `-7.675`
- `news_risk_high->crypto_major_4h` score `4.5043` n `95` status `ready` deltaP `21.9207` edge `0.355` maxDD `-8.0625`
- `news_risk_high->crypto_alt_1h` score `3.3263` n `98` status `ready` deltaP `19.3725` edge `0.1946` maxDD `-2.058`
- `risk_on_high->commodity_4h` score `2.5325` n `46` status `ready` deltaP `29.6726` edge `0.0482` maxDD `-0.1313`
- `risk_on_and_context->commodity_4h` score `2.5325` n `46` status `ready` deltaP `29.6726` edge `0.0482` maxDD `-0.1313`
- `market_context_high->commodity_4h` score `2.5318` n `136` status `ready` deltaP `27.179` edge `0.0716` maxDD `-0.345`
- `news_risk_high->crypto_major_1h` score `2.4749` n `98` status `ready` deltaP `20.8695` edge `0.1194` maxDD `-2.8494`
- `news_risk_high->metal_24h` score `1.7611` n `72` status `ready` deltaP `22.9167` edge `0.0784` maxDD `-2.4203`
- `market_context_high->commodity_1h` score `1.4351` n `136` status `ready` deltaP `18.0433` edge `0.0245` maxDD `-0.3491`
- `risk_on_high->commodity_1h` score `1.3538` n `46` status `ready` deltaP `17.0203` edge `0.0179` maxDD `-0.1507`
- `risk_on_and_context->commodity_1h` score `1.3538` n `46` status `ready` deltaP `17.0203` edge `0.0179` maxDD `-0.1507`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
