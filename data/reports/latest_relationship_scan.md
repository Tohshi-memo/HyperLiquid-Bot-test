# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-31T04:07:27.190842+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11624`

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

- `risk_on_high->crypto_alt_24h` score `21.1999` n `55` status `ready` deltaP `46.7108` edge `1.5033` maxDD `-3.1772`
- `risk_on_and_context->crypto_alt_24h` score `21.1999` n `55` status `ready` deltaP `46.7108` edge `1.5033` maxDD `-3.1772`
- `risk_on_high->unknown_4h` score `10.0036` n `94` status `ready` deltaP `29.3072` edge `0.6811` maxDD `-1.0945`
- `risk_on_and_context->unknown_4h` score `10.0036` n `94` status `ready` deltaP `29.3072` edge `0.6811` maxDD `-1.0945`
- `risk_on_high->crypto_major_24h` score `8.9029` n `55` status `ready` deltaP `27.8251` edge `0.6982` maxDD `-9.0103`
- `risk_on_and_context->crypto_major_24h` score `8.9029` n `55` status `ready` deltaP `27.8251` edge `0.6982` maxDD `-9.0103`
- `market_context_high->unknown_4h` score `7.4566` n `149` status `ready` deltaP `22.6101` edge `0.5135` maxDD `-1.0945`
- `risk_on_high->fx_24h` score `6.1686` n `55` status `ready` deltaP `69.0972` edge `0.0534` maxDD `0.0`
- `risk_on_and_context->fx_24h` score `6.1686` n `55` status `ready` deltaP `69.0972` edge `0.0534` maxDD `0.0`
- `market_context_high->crypto_alt_24h` score `4.6443` n `100` status `ready` deltaP `22.3472` edge `0.8654` maxDD `-27.517`
- `market_context_high->metal_24h` score `4.6261` n `100` status `ready` deltaP `33.9444` edge `0.2331` maxDD `-2.5778`
- `risk_on_high->metal_24h` score `4.3864` n `55` status `ready` deltaP `40.5808` edge `0.1422` maxDD `-0.7767`
- `risk_on_and_context->metal_24h` score `4.3864` n `55` status `ready` deltaP `40.5808` edge `0.1422` maxDD `-0.7767`
- `market_context_high->crypto_major_24h` score `4.3318` n `100` status `ready` deltaP `20.0069` edge `0.4767` maxDD `-17.2607`
- `risk_on_high->unknown_1h` score `2.7791` n `105` status `ready` deltaP `8.1209` edge `0.2351` maxDD `-1.9453`
- `risk_on_and_context->unknown_1h` score `2.7791` n `105` status `ready` deltaP `8.1209` edge `0.2351` maxDD `-1.9453`
- `market_context_high->unknown_1h` score `2.355` n `161` status `ready` deltaP `7.0443` edge `0.2123` maxDD `-2.041`
- `market_context_high->fx_24h` score `1.0308` n `100` status `ready` deltaP `37.0972` edge `0.0307` maxDD `-1.6688`
- `risk_on_high->commodity_24h` score `0.8436` n `55` status `ready` deltaP `9.6528` edge `0.1426` maxDD `-0.5706`
- `risk_on_and_context->commodity_24h` score `0.8436` n `55` status `ready` deltaP `9.6528` edge `0.1426` maxDD `-0.5706`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
