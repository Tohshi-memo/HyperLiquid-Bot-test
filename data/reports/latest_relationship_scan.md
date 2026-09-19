# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-19T14:52:25.819294+00:00`
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

- `news_risk_high->crypto_major_24h` score `52.4518` n `72` status `ready` deltaP `31.0763` edge `4.253` maxDD `-5.8019`
- `news_risk_high->crypto_alt_24h` score `46.0202` n `72` status `ready` deltaP `35.7639` edge `3.7345` maxDD `-9.3661`
- `market_context_high->unknown_4h` score `39.5125` n `139` status `ready` deltaP `-2.5597` edge `3.3331` maxDD `-0.5326`
- `risk_on_high->unknown_4h` score `10.6247` n `49` status `ready` deltaP `-10.1356` edge `0.9755` maxDD `-0.4694`
- `risk_on_and_context->unknown_4h` score `10.6247` n `49` status `ready` deltaP `-10.1356` edge `0.9755` maxDD `-0.4694`
- `news_risk_high->equity_24h` score `10.0536` n `72` status `ready` deltaP `40.625` edge `0.5712` maxDD `-0.0053`
- `risk_on_high->commodity_24h` score `8.5131` n `49` status `ready` deltaP `46.3542` edge `0.4004` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `8.5131` n `49` status `ready` deltaP `46.3542` edge `0.4004` maxDD `0.0`
- `market_context_high->commodity_24h` score `7.2366` n `139` status `ready` deltaP `39.16` edge `0.3945` maxDD `-0.8682`
- `news_risk_high->crypto_alt_4h` score `6.5833` n `92` status `ready` deltaP `25.3116` edge `0.5008` maxDD `-7.675`
- `news_risk_high->crypto_major_4h` score `4.5643` n `92` status `ready` deltaP `21.7258` edge `0.3613` maxDD `-8.0625`
- `news_risk_high->crypto_alt_1h` score `3.2819` n `98` status `ready` deltaP `19.0731` edge `0.1929` maxDD `-2.058`
- `risk_on_high->commodity_4h` score `2.5882` n `49` status `ready` deltaP `30.4132` edge `0.0479` maxDD `-0.1313`
- `risk_on_and_context->commodity_4h` score `2.5882` n `49` status `ready` deltaP `30.4132` edge `0.0479` maxDD `-0.1313`
- `market_context_high->commodity_4h` score `2.5213` n `139` status `ready` deltaP `27.1978` edge `0.0706` maxDD `-0.345`
- `news_risk_high->crypto_major_1h` score `2.4737` n `98` status `ready` deltaP `20.8695` edge `0.1193` maxDD `-2.8494`
- `news_risk_high->metal_24h` score `1.8124` n `72` status `ready` deltaP `23.4375` edge `0.0792` maxDD `-2.4203`
- `market_context_high->commodity_1h` score `1.2988` n `139` status `ready` deltaP `16.5198` edge `0.0233` maxDD `-0.3491`
- `risk_on_high->commodity_1h` score `0.9331` n `49` status `ready` deltaP `12.7612` edge `0.0154` maxDD `-0.1507`
- `risk_on_and_context->commodity_1h` score `0.9331` n `49` status `ready` deltaP `12.7612` edge `0.0154` maxDD `-0.1507`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
