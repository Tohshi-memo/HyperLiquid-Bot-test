# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-06T15:37:25.150314+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9991`

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

- `risk_on_high->unknown_24h` score `130.6627` n `108` status `ready` deltaP `23.8426` edge `10.7406` maxDD `-0.2126`
- `risk_on_and_context->unknown_24h` score `130.6627` n `108` status `ready` deltaP `23.8426` edge `10.7406` maxDD `-0.2126`
- `risk_on_high->crypto_major_24h` score `11.9719` n `108` status `ready` deltaP `25.0` edge `1.2156` maxDD `-24.4356`
- `risk_on_and_context->crypto_major_24h` score `11.9719` n `108` status `ready` deltaP `25.0` edge `1.2156` maxDD `-24.4356`
- `market_context_high->equity_24h` score `3.4526` n `196` status `ready` deltaP `16.695` edge `0.3618` maxDD `-8.4976`
- `risk_on_high->crypto_alt_24h` score `3.3219` n `108` status `ready` deltaP `13.2523` edge `0.5566` maxDD `-22.1168`
- `risk_on_and_context->crypto_alt_24h` score `3.3219` n `108` status `ready` deltaP `13.2523` edge `0.5566` maxDD `-22.1168`
- `market_context_high->crypto_alt_24h` score `1.6178` n `196` status `ready` deltaP `15.1608` edge `0.4272` maxDD `-23.4762`
- `risk_on_high->equity_24h` score `1.1131` n `108` status `ready` deltaP `8.7963` edge `0.2195` maxDD `-8.4976`
- `risk_on_and_context->equity_24h` score `1.1131` n `108` status `ready` deltaP `8.7963` edge `0.2195` maxDD `-8.4976`
- `risk_on_high->index_1h` score `-0.0801` n `132` status `ready` deltaP `5.6297` edge `-0.0031` maxDD `-0.5764`
- `risk_on_and_context->index_1h` score `-0.0801` n `132` status `ready` deltaP `5.6297` edge `-0.0031` maxDD `-0.5764`
- `risk_on_high->crypto_alt_1h` score `-0.1975` n `132` status `ready` deltaP `2.9441` edge `0.0656` maxDD `-5.4685`
- `risk_on_and_context->crypto_alt_1h` score `-0.1975` n `132` status `ready` deltaP `2.9441` edge `0.0656` maxDD `-5.4685`
- `market_context_high->index_24h` score `-0.2233` n `196` status `ready` deltaP `14.2184` edge `0.077` maxDD `-5.232`
- `risk_on_high->metal_1h` score `-0.2603` n `132` status `ready` deltaP `6.0243` edge `-0.0023` maxDD `-1.699`
- `risk_on_and_context->metal_1h` score `-0.2603` n `132` status `ready` deltaP `6.0243` edge `-0.0023` maxDD `-1.699`
- `risk_on_high->equity_1h` score `-0.4236` n `132` status `ready` deltaP `6.9089` edge `-0.0129` maxDD `-2.6638`
- `risk_on_and_context->equity_1h` score `-0.4236` n `132` status `ready` deltaP `6.9089` edge `-0.0129` maxDD `-2.6638`
- `risk_on_high->commodity_1h` score `-0.5287` n `132` status `ready` deltaP `0.8393` edge `0.0007` maxDD `-1.0281`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
