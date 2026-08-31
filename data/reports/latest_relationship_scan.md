# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-31T01:37:28.596668+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11748`

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

- `risk_on_high->crypto_alt_24h` score `20.719` n `55` status `ready` deltaP `44.9747` edge `1.4748` maxDD `-3.1772`
- `risk_on_and_context->crypto_alt_24h` score `20.719` n `55` status `ready` deltaP `44.9747` edge `1.4748` maxDD `-3.1772`
- `risk_on_high->unknown_4h` score `10.0442` n `90` status `ready` deltaP `31.4194` edge `0.6704` maxDD `-1.0945`
- `risk_on_and_context->unknown_4h` score `10.0442` n `90` status `ready` deltaP `31.4194` edge `0.6704` maxDD `-1.0945`
- `risk_on_high->crypto_major_24h` score `7.9168` n `55` status `ready` deltaP `26.089` edge `0.6276` maxDD `-9.0103`
- `risk_on_and_context->crypto_major_24h` score `7.9168` n `55` status `ready` deltaP `26.089` edge `0.6276` maxDD `-9.0103`
- `market_context_high->crypto_alt_24h` score `7.535` n `110` status `ready` deltaP `23.1566` edge `0.8925` maxDD `-27.517`
- `market_context_high->unknown_4h` score `6.4457` n `149` status `ready` deltaP `21.054` edge `0.4438` maxDD `-1.0945`
- `risk_on_high->fx_24h` score `6.0606` n `55` status `ready` deltaP `67.8819` edge `0.0525` maxDD `0.0`
- `risk_on_and_context->fx_24h` score `6.0606` n `55` status `ready` deltaP `67.8819` edge `0.0525` maxDD `0.0`
- `market_context_high->crypto_major_24h` score `5.2484` n `110` status `ready` deltaP `20.6344` edge `0.5489` maxDD `-17.2607`
- `risk_on_high->metal_24h` score `4.2173` n `55` status `ready` deltaP `39.7128` edge `0.1339` maxDD `-0.7767`
- `risk_on_and_context->metal_24h` score `4.2173` n `55` status `ready` deltaP `39.7128` edge `0.1339` maxDD `-0.7767`
- `risk_on_high->unknown_1h` score `4.1601` n `95` status `ready` deltaP `12.1337` edge `0.2928` maxDD `-0.4947`
- `risk_on_and_context->unknown_1h` score `4.1601` n `95` status `ready` deltaP `12.1337` edge `0.2928` maxDD `-0.4947`
- `market_context_high->metal_24h` score `3.8451` n `110` status `ready` deltaP `30.6219` edge `0.2182` maxDD `-3.1535`
- `market_context_high->unknown_1h` score `2.9874` n `161` status `ready` deltaP `8.93` edge `0.2303` maxDD `-0.9372`
- `market_context_high->fx_24h` score `0.9786` n `110` status `ready` deltaP `36.0637` edge `0.0309` maxDD `-1.6688`
- `risk_on_high->commodity_24h` score `0.8924` n `55` status `ready` deltaP `9.8264` edge `0.1477` maxDD `-0.5706`
- `risk_on_and_context->commodity_24h` score `0.8924` n `55` status `ready` deltaP `9.8264` edge `0.1477` maxDD `-0.5706`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
