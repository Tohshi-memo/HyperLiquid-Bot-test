# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-31T01:52:27.540742+00:00`
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

- `risk_on_high->crypto_alt_24h` score `20.7521` n `55` status `ready` deltaP `45.1483` edge `1.4764` maxDD `-3.1772`
- `risk_on_and_context->crypto_alt_24h` score `20.7521` n `55` status `ready` deltaP `45.1483` edge `1.4764` maxDD `-3.1772`
- `risk_on_high->unknown_4h` score `10.2531` n `91` status `ready` deltaP `31.5415` edge `0.687` maxDD `-1.0945`
- `risk_on_and_context->unknown_4h` score `10.2531` n `91` status `ready` deltaP `31.5415` edge `0.687` maxDD `-1.0945`
- `risk_on_high->crypto_major_24h` score `8.0015` n `55` status `ready` deltaP `26.2626` edge `0.6335` maxDD `-9.0103`
- `risk_on_and_context->crypto_major_24h` score `8.0015` n `55` status `ready` deltaP `26.2626` edge `0.6335` maxDD `-9.0103`
- `market_context_high->crypto_alt_24h` score `7.577` n `109` status `ready` deltaP `23.0966` edge `0.8964` maxDD `-27.517`
- `market_context_high->unknown_4h` score `6.5909` n `149` status `ready` deltaP `21.054` edge `0.4559` maxDD `-1.0945`
- `risk_on_high->fx_24h` score `6.0756` n `55` status `ready` deltaP `68.0556` edge `0.0526` maxDD `0.0`
- `risk_on_and_context->fx_24h` score `6.0756` n `55` status `ready` deltaP `68.0556` edge `0.0526` maxDD `0.0`
- `market_context_high->crypto_major_24h` score `5.2498` n `109` status `ready` deltaP `20.5912` edge `0.5493` maxDD `-17.2607`
- `risk_on_high->metal_24h` score `4.2456` n `55` status `ready` deltaP `39.8864` edge `0.1351` maxDD `-0.7767`
- `risk_on_and_context->metal_24h` score `4.2456` n `55` status `ready` deltaP `39.8864` edge `0.1351` maxDD `-0.7767`
- `risk_on_high->unknown_1h` score `3.9454` n `96` status `ready` deltaP `11.5706` edge `0.2843` maxDD `-0.9457`
- `risk_on_and_context->unknown_1h` score `3.9454` n `96` status `ready` deltaP `11.5706` edge `0.2843` maxDD `-0.9457`
- `market_context_high->metal_24h` score `3.8355` n `109` status `ready` deltaP `30.5619` edge `0.2178` maxDD `-3.1535`
- `market_context_high->unknown_1h` score `2.8561` n `161` status `ready` deltaP `8.4586` edge `0.2238` maxDD `-1.0414`
- `market_context_high->fx_24h` score `0.9717` n `109` status `ready` deltaP `35.9455` edge `0.0308` maxDD `-1.6688`
- `risk_on_high->commodity_24h` score `0.8771` n `55` status `ready` deltaP `9.6528` edge `0.1469` maxDD `-0.5706`
- `risk_on_and_context->commodity_24h` score `0.8771` n `55` status `ready` deltaP `9.6528` edge `0.1469` maxDD `-0.5706`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
