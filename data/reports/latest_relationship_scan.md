# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-12T00:52:30.643868+00:00`
- Price records: `672`
- Market context records: `3637`
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

- `risk_on_high->crypto_major_24h` score `38.8782` n `32` status `ready` deltaP `43.9236` edge `2.9513` maxDD `-0.0083`
- `risk_on_and_context->crypto_major_24h` score `38.8782` n `32` status `ready` deltaP `43.9236` edge `2.9513` maxDD `-0.0083`
- `risk_on_high->equity_24h` score `35.5958` n `32` status `ready` deltaP `46.0069` edge `2.6596` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `35.5958` n `32` status `ready` deltaP `46.0069` edge `2.6596` maxDD `0.0`
- `risk_on_high->crypto_alt_24h` score `31.2144` n `32` status `ready` deltaP `43.0556` edge `2.3293` maxDD `-0.8779`
- `risk_on_and_context->crypto_alt_24h` score `31.2144` n `32` status `ready` deltaP `43.0556` edge `2.3293` maxDD `-0.8779`
- `risk_on_high->index_24h` score `20.3438` n `32` status `ready` deltaP `46.0069` edge `1.3886` maxDD `0.0`
- `risk_on_and_context->index_24h` score `20.3438` n `32` status `ready` deltaP `46.0069` edge `1.3886` maxDD `0.0`
- `risk_on_high->metal_24h` score `12.4874` n `32` status `ready` deltaP `31.5972` edge `0.8561` maxDD `-0.7574`
- `risk_on_and_context->metal_24h` score `12.4874` n `32` status `ready` deltaP `31.5972` edge `0.8561` maxDD `-0.7574`
- `risk_on_high->crypto_major_4h` score `12.0452` n `32` status `ready` deltaP `21.4939` edge `0.9727` maxDD `-5.9781`
- `risk_on_and_context->crypto_major_4h` score `12.0452` n `32` status `ready` deltaP `21.4939` edge `0.9727` maxDD `-5.9781`
- `market_context_high->equity_24h` score `11.3078` n `157` status `ready` deltaP `23.077` edge `1.3549` maxDD `-35.3144`
- `market_context_high->index_24h` score `9.9477` n `157` status `ready` deltaP `31.3572` edge `0.7915` maxDD `-11.3924`
- `market_context_high->crypto_major_24h` score `4.8732` n `157` status `ready` deltaP `10.1059` edge `1.0454` maxDD `-49.5335`
- `market_context_high->metal_24h` score `4.3359` n `157` status `ready` deltaP `25.9045` edge `0.7784` maxDD `-21.6171`
- `risk_on_high->crypto_alt_4h` score `3.5074` n `32` status `ready` deltaP `1.9055` edge `0.464` maxDD `-11.7537`
- `risk_on_and_context->crypto_alt_4h` score `3.5074` n `32` status `ready` deltaP `1.9055` edge `0.464` maxDD `-11.7537`
- `risk_on_high->equity_4h` score `2.587` n `32` status `ready` deltaP `10.4421` edge `0.3755` maxDD `-5.7426`
- `risk_on_and_context->equity_4h` score `2.587` n `32` status `ready` deltaP `10.4421` edge `0.3755` maxDD `-5.7426`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
