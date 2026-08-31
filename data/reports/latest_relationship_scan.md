# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-31T02:52:31.599435+00:00`
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

- `risk_on_high->crypto_alt_24h` score `20.9216` n `55` status `ready` deltaP `45.8428` edge `1.4859` maxDD `-3.1772`
- `risk_on_and_context->crypto_alt_24h` score `20.9216` n `55` status `ready` deltaP `45.8428` edge `1.4859` maxDD `-3.1772`
- `risk_on_high->unknown_4h` score `10.5589` n `92` status `ready` deltaP `31.5084` edge `0.7127` maxDD `-1.0945`
- `risk_on_and_context->unknown_4h` score `10.5589` n `92` status `ready` deltaP `31.5084` edge `0.7127` maxDD `-1.0945`
- `risk_on_high->crypto_major_24h` score `8.3726` n `55` status `ready` deltaP `26.9571` edge `0.6598` maxDD `-9.0103`
- `risk_on_and_context->crypto_major_24h` score `8.3726` n `55` status `ready` deltaP `26.9571` edge `0.6598` maxDD `-9.0103`
- `market_context_high->crypto_alt_24h` score `7.6118` n `105` status `ready` deltaP `22.8125` edge `0.9012` maxDD `-27.517`
- `market_context_high->unknown_4h` score `7.0548` n `149` status `ready` deltaP `21.5726` edge `0.4911` maxDD `-1.0945`
- `risk_on_high->fx_24h` score `6.0907` n `55` status `ready` deltaP `68.2292` edge `0.0527` maxDD `0.0`
- `risk_on_and_context->fx_24h` score `6.0907` n `55` status `ready` deltaP `68.2292` edge `0.0527` maxDD `0.0`
- `market_context_high->crypto_major_24h` score `5.0419` n `105` status `ready` deltaP `20.377` edge `0.5334` maxDD `-17.2607`
- `risk_on_high->metal_24h` score `4.3588` n `55` status `ready` deltaP `40.5808` edge `0.1399` maxDD `-0.7767`
- `risk_on_and_context->metal_24h` score `4.3588` n `55` status `ready` deltaP `40.5808` edge `0.1399` maxDD `-0.7767`
- `market_context_high->metal_24h` score `3.8128` n `105` status `ready` deltaP `30.2777` edge `0.2178` maxDD `-3.1535`
- `risk_on_high->unknown_1h` score `3.2835` n `100` status `ready` deltaP `9.3114` edge `0.2583` maxDD `-1.7399`
- `risk_on_and_context->unknown_1h` score `3.2835` n `100` status `ready` deltaP `9.3114` edge `0.2583` maxDD `-1.7399`
- `market_context_high->unknown_1h` score `2.481` n `161` status `ready` deltaP `7.0443` edge `0.2119` maxDD `-1.8356`
- `market_context_high->fx_24h` score `1.0704` n `105` status `ready` deltaP `37.753` edge `0.0314` maxDD `-1.6688`
- `risk_on_high->commodity_24h` score `0.8608` n `55` status `ready` deltaP `9.6528` edge `0.1448` maxDD `-0.5706`
- `risk_on_and_context->commodity_24h` score `0.8608` n `55` status `ready` deltaP `9.6528` edge `0.1448` maxDD `-0.5706`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
