# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-11T23:23:03.890192+00:00`
- Price records: `672`
- Market context records: `3631`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `13163`

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

- `risk_on_high->crypto_major_24h` score `40.1808` n `32` status `ready` deltaP `44.9653` edge `3.0529` maxDD `-0.0083`
- `risk_on_and_context->crypto_major_24h` score `40.1808` n `32` status `ready` deltaP `44.9653` edge `3.0529` maxDD `-0.0083`
- `risk_on_high->equity_24h` score `37.0279` n `32` status `ready` deltaP `47.0486` edge `2.772` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `37.0279` n `32` status `ready` deltaP `47.0486` edge `2.772` maxDD `0.0`
- `risk_on_high->crypto_alt_24h` score `32.6033` n `32` status `ready` deltaP `44.0972` edge `2.4381` maxDD `-0.8779`
- `risk_on_and_context->crypto_alt_24h` score `32.6033` n `32` status `ready` deltaP `44.0972` edge `2.4381` maxDD `-0.8779`
- `risk_on_high->index_24h` score `21.2395` n `32` status `ready` deltaP `47.0486` edge `1.4563` maxDD `0.0`
- `risk_on_and_context->index_24h` score `21.2395` n `32` status `ready` deltaP `47.0486` edge `1.4563` maxDD `0.0`
- `risk_on_high->metal_24h` score `13.6243` n `32` status `ready` deltaP `32.6389` edge `0.9439` maxDD `-0.7574`
- `risk_on_and_context->metal_24h` score `13.6243` n `32` status `ready` deltaP `32.6389` edge `0.9439` maxDD `-0.7574`
- `risk_on_high->crypto_major_4h` score `12.2872` n `32` status `ready` deltaP `22.1037` edge `0.9888` maxDD `-5.9781`
- `risk_on_and_context->crypto_major_4h` score `12.2872` n `32` status `ready` deltaP `22.1037` edge `0.9888` maxDD `-5.9781`
- `market_context_high->equity_24h` score `11.2979` n `158` status `ready` deltaP `23.6309` edge `1.4252` maxDD `-40.9667`
- `market_context_high->index_24h` score `9.8896` n `158` status `ready` deltaP `31.8587` edge `0.8334` maxDD `-15.0661`
- `market_context_high->crypto_major_24h` score `4.8582` n `158` status `ready` deltaP `10.7485` edge `1.1063` maxDD `-54.8486`
- `market_context_high->metal_24h` score `4.3802` n `158` status `ready` deltaP `26.5471` edge `0.8386` maxDD `-25.9879`
- `risk_on_high->crypto_alt_4h` score `3.8166` n `32` status `ready` deltaP `2.5152` edge `0.4857` maxDD `-11.7537`
- `risk_on_and_context->crypto_alt_4h` score `3.8166` n `32` status `ready` deltaP `2.5152` edge `0.4857` maxDD `-11.7537`
- `risk_on_high->equity_4h` score `2.7196` n `32` status `ready` deltaP `11.3567` edge `0.3864` maxDD `-5.7426`
- `risk_on_and_context->equity_4h` score `2.7196` n `32` status `ready` deltaP `11.3567` edge `0.3864` maxDD `-5.7426`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
