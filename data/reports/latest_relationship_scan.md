# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-31T05:37:25.935898+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11708`

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

- `risk_on_high->crypto_alt_24h` score `21.5417` n `55` status `ready` deltaP `47.5789` edge `1.526` maxDD `-3.1772`
- `risk_on_and_context->crypto_alt_24h` score `21.5417` n `55` status `ready` deltaP `47.5789` edge `1.526` maxDD `-3.1772`
- `risk_on_high->crypto_major_24h` score `9.5754` n `55` status `ready` deltaP `28.8668` edge `0.7473` maxDD `-9.0103`
- `risk_on_and_context->crypto_major_24h` score `9.5754` n `55` status `ready` deltaP `28.8668` edge `0.7473` maxDD `-9.0103`
- `risk_on_high->unknown_4h` score `8.6445` n `99` status `ready` deltaP `24.9015` edge `0.6111` maxDD `-2.2054`
- `risk_on_and_context->unknown_4h` score `8.6445` n `99` status `ready` deltaP `24.9015` edge `0.6111` maxDD `-2.2054`
- `market_context_high->unknown_4h` score `6.8374` n `151` status `ready` deltaP `21.5434` edge `0.4906` maxDD `-2.4887`
- `risk_on_high->fx_24h` score `6.2603` n `55` status `ready` deltaP `70.1389` edge `0.0541` maxDD `0.0`
- `risk_on_and_context->fx_24h` score `6.2603` n `55` status `ready` deltaP `70.1389` edge `0.0541` maxDD `0.0`
- `market_context_high->metal_24h` score `5.2264` n `96` status `ready` deltaP `37.1527` edge `0.2487` maxDD `-1.8678`
- `risk_on_high->metal_24h` score `4.4068` n `55` status `ready` deltaP `40.5808` edge `0.1439` maxDD `-0.7767`
- `risk_on_and_context->metal_24h` score `4.4068` n `55` status `ready` deltaP `40.5808` edge `0.1439` maxDD `-0.7767`
- `market_context_high->crypto_alt_24h` score `4.2918` n `96` status `ready` deltaP `22.0486` edge `0.8222` maxDD `-27.517`
- `market_context_high->crypto_major_24h` score `3.6361` n `96` status `ready` deltaP `19.9653` edge `0.419` maxDD `-17.2607`
- `risk_on_high->unknown_1h` score `2.6744` n `107` status `ready` deltaP `8.0125` edge `0.2271` maxDD `-1.9453`
- `risk_on_and_context->unknown_1h` score `2.6744` n `107` status `ready` deltaP `8.0125` edge `0.2271` maxDD `-1.9453`
- `market_context_high->unknown_1h` score `2.4518` n `159` status `ready` deltaP `7.3542` edge `0.2183` maxDD `-2.041`
- `market_context_high->fx_24h` score `1.0117` n `96` status `ready` deltaP `36.8056` edge `0.0302` maxDD `-1.6688`
- `risk_on_high->commodity_24h` score `0.8108` n `55` status `ready` deltaP `9.6528` edge `0.1384` maxDD `-0.5706`
- `risk_on_and_context->commodity_24h` score `0.8108` n `55` status `ready` deltaP `9.6528` edge `0.1384` maxDD `-0.5706`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
