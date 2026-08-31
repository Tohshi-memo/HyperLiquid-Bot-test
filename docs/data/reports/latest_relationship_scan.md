# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-31T03:07:26.061812+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11636`

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

- `risk_on_high->crypto_alt_24h` score `20.9799` n `55` status `ready` deltaP `46.0164` edge `1.4896` maxDD `-3.1772`
- `risk_on_and_context->crypto_alt_24h` score `20.9799` n `55` status `ready` deltaP `46.0164` edge `1.4896` maxDD `-3.1772`
- `risk_on_high->unknown_4h` score `10.5157` n `92` status `ready` deltaP `31.5084` edge `0.7091` maxDD `-1.0945`
- `risk_on_and_context->unknown_4h` score `10.5157` n `92` status `ready` deltaP `31.5084` edge `0.7091` maxDD `-1.0945`
- `risk_on_high->crypto_major_24h` score `8.4777` n `55` status `ready` deltaP `27.1307` edge `0.6674` maxDD `-9.0103`
- `risk_on_and_context->crypto_major_24h` score `8.4777` n `55` status `ready` deltaP `27.1307` edge `0.6674` maxDD `-9.0103`
- `market_context_high->crypto_alt_24h` score `7.544` n `104` status `ready` deltaP `22.7297` edge `0.8961` maxDD `-27.517`
- `market_context_high->unknown_4h` score `7.2` n `149` status `ready` deltaP `21.5726` edge `0.5032` maxDD `-1.0945`
- `risk_on_high->fx_24h` score `6.1058` n `55` status `ready` deltaP `68.4028` edge `0.0528` maxDD `0.0`
- `risk_on_and_context->fx_24h` score `6.1058` n `55` status `ready` deltaP `68.4028` edge `0.0528` maxDD `0.0`
- `market_context_high->crypto_major_24h` score `4.9371` n `104` status `ready` deltaP `20.3125` edge `0.5251` maxDD `-17.2607`
- `risk_on_high->metal_24h` score `4.3648` n `55` status `ready` deltaP `40.5808` edge `0.1404` maxDD `-0.7767`
- `risk_on_and_context->metal_24h` score `4.3648` n `55` status `ready` deltaP `40.5808` edge `0.1404` maxDD `-0.7767`
- `market_context_high->metal_24h` score `3.958` n `104` status `ready` deltaP `30.9829` edge `0.2203` maxDD `-3.0949`
- `risk_on_high->unknown_1h` score `3.1093` n `101` status `ready` deltaP `8.6678` edge `0.2527` maxDD `-1.7768`
- `risk_on_and_context->unknown_1h` score `3.1093` n `101` status `ready` deltaP `8.6678` edge `0.2527` maxDD `-1.7768`
- `market_context_high->unknown_1h` score `2.4291` n `161` status `ready` deltaP `7.0443` edge `0.2122` maxDD `-1.8725`
- `market_context_high->fx_24h` score `1.0634` n `104` status `ready` deltaP `37.6336` edge `0.0313` maxDD `-1.6688`
- `risk_on_high->commodity_24h` score `0.8584` n `55` status `ready` deltaP `9.6528` edge `0.1445` maxDD `-0.5706`
- `risk_on_and_context->commodity_24h` score `0.8584` n `55` status `ready` deltaP `9.6528` edge `0.1445` maxDD `-0.5706`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
