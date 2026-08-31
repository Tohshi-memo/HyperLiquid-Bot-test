# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-31T03:52:30.246662+00:00`
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

- `risk_on_high->crypto_alt_24h` score `21.1392` n `55` status `ready` deltaP `46.5372` edge `1.4994` maxDD `-3.1772`
- `risk_on_and_context->crypto_alt_24h` score `21.1392` n `55` status `ready` deltaP `46.5372` edge `1.4994` maxDD `-3.1772`
- `risk_on_high->unknown_4h` score `10.231` n `93` status `ready` deltaP `30.2452` edge `0.6938` maxDD `-1.0945`
- `risk_on_and_context->unknown_4h` score `10.231` n `93` status `ready` deltaP `30.2452` edge `0.6938` maxDD `-1.0945`
- `risk_on_high->crypto_major_24h` score `8.7846` n `55` status `ready` deltaP `27.6515` edge `0.6895` maxDD `-9.0103`
- `risk_on_and_context->crypto_major_24h` score `8.7846` n `55` status `ready` deltaP `27.6515` edge `0.6895` maxDD `-9.0103`
- `market_context_high->unknown_4h` score `7.4626` n `149` status `ready` deltaP `22.6101` edge `0.514` maxDD `-1.0945`
- `risk_on_high->fx_24h` score `6.1523` n `55` status `ready` deltaP `68.9236` edge `0.0532` maxDD `0.0`
- `risk_on_and_context->fx_24h` score `6.1523` n `55` status `ready` deltaP `68.9236` edge `0.0532` maxDD `0.0`
- `market_context_high->crypto_alt_24h` score `4.737` n `101` status `ready` deltaP `22.4508` edge `0.8766` maxDD `-27.517`
- `market_context_high->crypto_major_24h` score `4.539` n `101` status `ready` deltaP `20.0907` edge `0.4934` maxDD `-17.2607`
- `market_context_high->metal_24h` score `4.4488` n `101` status `ready` deltaP `33.182` edge `0.2295` maxDD `-2.732`
- `risk_on_high->metal_24h` score `4.3804` n `55` status `ready` deltaP `40.5808` edge `0.1417` maxDD `-0.7767`
- `risk_on_and_context->metal_24h` score `4.3804` n `55` status `ready` deltaP `40.5808` edge `0.1417` maxDD `-0.7767`
- `risk_on_high->unknown_1h` score `2.8894` n `104` status `ready` deltaP `8.7345` edge `0.2402` maxDD `-1.9453`
- `risk_on_and_context->unknown_1h` score `2.8894` n `104` status `ready` deltaP `8.7345` edge `0.2402` maxDD `-1.9453`
- `market_context_high->unknown_1h` score `2.3502` n `161` status `ready` deltaP `7.0443` edge `0.2119` maxDD `-2.041`
- `market_context_high->fx_24h` score `1.0383` n `101` status `ready` deltaP `37.2404` edge `0.0307` maxDD `-1.6688`
- `risk_on_high->commodity_24h` score `0.8483` n `55` status `ready` deltaP `9.6528` edge `0.1432` maxDD `-0.5706`
- `risk_on_and_context->commodity_24h` score `0.8483` n `55` status `ready` deltaP `9.6528` edge `0.1432` maxDD `-0.5706`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
