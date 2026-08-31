# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-31T04:22:26.190345+00:00`
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

- `risk_on_high->crypto_alt_24h` score `21.2714` n `55` status `ready` deltaP `46.8844` edge `1.5081` maxDD `-3.1772`
- `risk_on_and_context->crypto_alt_24h` score `21.2714` n `55` status `ready` deltaP `46.8844` edge `1.5081` maxDD `-3.1772`
- `risk_on_high->unknown_4h` score `10.0084` n `94` status `ready` deltaP `29.3072` edge `0.6815` maxDD `-1.0945`
- `risk_on_and_context->unknown_4h` score `10.0084` n `94` status `ready` deltaP `29.3072` edge `0.6815` maxDD `-1.0945`
- `risk_on_high->crypto_major_24h` score `9.0296` n `55` status `ready` deltaP `27.9988` edge `0.7076` maxDD `-9.0103`
- `risk_on_and_context->crypto_major_24h` score `9.0296` n `55` status `ready` deltaP `27.9988` edge `0.7076` maxDD `-9.0103`
- `market_context_high->unknown_4h` score `7.4422` n `149` status `ready` deltaP `22.6101` edge `0.5123` maxDD `-1.0945`
- `risk_on_high->fx_24h` score `6.1837` n `55` status `ready` deltaP `69.2708` edge `0.0535` maxDD `0.0`
- `risk_on_and_context->fx_24h` score `6.1837` n `55` status `ready` deltaP `69.2708` edge `0.0535` maxDD `0.0`
- `market_context_high->metal_24h` score `4.8127` n `99` status `ready` deltaP `34.7222` edge `0.2369` maxDD `-2.386`
- `market_context_high->crypto_alt_24h` score `4.5395` n `99` status `ready` deltaP `22.238` edge `0.8527` maxDD `-27.517`
- `risk_on_high->metal_24h` score `4.39` n `55` status `ready` deltaP `40.5808` edge `0.1425` maxDD `-0.7767`
- `risk_on_and_context->metal_24h` score `4.39` n `55` status `ready` deltaP `40.5808` edge `0.1425` maxDD `-0.7767`
- `market_context_high->crypto_major_24h` score `4.1075` n `99` status `ready` deltaP `19.918` edge `0.4586` maxDD `-17.2607`
- `risk_on_high->unknown_1h` score `2.6721` n `106` status `ready` deltaP `7.5189` edge `0.2302` maxDD `-1.9453`
- `risk_on_and_context->unknown_1h` score `2.6721` n `106` status `ready` deltaP `7.5189` edge `0.2302` maxDD `-1.9453`
- `market_context_high->unknown_1h` score `2.3634` n `161` status `ready` deltaP `7.0443` edge `0.213` maxDD `-2.041`
- `market_context_high->fx_24h` score `1.0207` n `99` status `ready` deltaP `36.9476` edge `0.0304` maxDD `-1.6688`
- `risk_on_high->commodity_24h` score `0.8389` n `55` status `ready` deltaP `9.6528` edge `0.142` maxDD `-0.5706`
- `risk_on_and_context->commodity_24h` score `0.8389` n `55` status `ready` deltaP `9.6528` edge `0.142` maxDD `-0.5706`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
