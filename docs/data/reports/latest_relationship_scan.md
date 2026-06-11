# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-11T22:22:29.556143+00:00`
- Price records: `672`
- Market context records: `3626`
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

- `risk_on_high->crypto_major_24h` score `41.0199` n `32` status `ready` deltaP `45.6597` edge `3.1182` maxDD `-0.0083`
- `risk_on_and_context->crypto_major_24h` score `41.0199` n `32` status `ready` deltaP `45.6597` edge `3.1182` maxDD `-0.0083`
- `risk_on_high->equity_24h` score `38.0026` n `32` status `ready` deltaP `47.7431` edge `2.8486` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `38.0026` n `32` status `ready` deltaP `47.7431` edge `2.8486` maxDD `0.0`
- `risk_on_high->crypto_alt_24h` score `33.5037` n `32` status `ready` deltaP `44.7917` edge `2.5085` maxDD `-0.8779`
- `risk_on_and_context->crypto_alt_24h` score `33.5037` n `32` status `ready` deltaP `44.7917` edge `2.5085` maxDD `-0.8779`
- `risk_on_high->index_24h` score `21.877` n `32` status `ready` deltaP `47.7431` edge `1.5048` maxDD `0.0`
- `risk_on_and_context->index_24h` score `21.877` n `32` status `ready` deltaP `47.7431` edge `1.5048` maxDD `0.0`
- `risk_on_high->metal_24h` score `14.4059` n `32` status `ready` deltaP `33.3333` edge `1.0044` maxDD `-0.7574`
- `risk_on_and_context->metal_24h` score `14.4059` n `32` status `ready` deltaP `33.3333` edge `1.0044` maxDD `-0.7574`
- `risk_on_high->crypto_major_4h` score `12.3946` n `32` status `ready` deltaP `22.561` edge `0.9947` maxDD `-5.9781`
- `risk_on_and_context->crypto_major_4h` score `12.3946` n `32` status `ready` deltaP `22.561` edge `0.9947` maxDD `-5.9781`
- `market_context_high->equity_24h` score `12.2726` n `158` status `ready` deltaP `24.3254` edge `1.5018` maxDD `-40.9667`
- `market_context_high->index_24h` score `10.5271` n `158` status `ready` deltaP `32.5532` edge `0.8819` maxDD `-15.0661`
- `market_context_high->crypto_major_24h` score `5.6973` n `158` status `ready` deltaP `11.4429` edge `1.1716` maxDD `-54.8486`
- `market_context_high->metal_24h` score `4.8882` n `158` status `ready` deltaP `27.2415` edge `0.8991` maxDD `-25.9879`
- `risk_on_high->crypto_alt_4h` score `3.9697` n `32` status `ready` deltaP `3.125` edge `0.4944` maxDD `-11.7537`
- `risk_on_and_context->crypto_alt_4h` score `3.9697` n `32` status `ready` deltaP `3.125` edge `0.4944` maxDD `-11.7537`
- `risk_on_high->equity_4h` score `2.8379` n `32` status `ready` deltaP `11.9665` edge `0.3975` maxDD `-5.7426`
- `risk_on_and_context->equity_4h` score `2.8379` n `32` status `ready` deltaP `11.9665` edge `0.3975` maxDD `-5.7426`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
