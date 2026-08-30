# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-30T23:22:25.844121+00:00`
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

- `risk_on_high->crypto_alt_24h` score `22.9041` n `53` status `ready` deltaP `48.6111` edge `1.5846` maxDD `0.0`
- `risk_on_and_context->crypto_alt_24h` score `22.9041` n `53` status `ready` deltaP `48.6111` edge `1.5846` maxDD `0.0`
- `risk_on_high->crypto_major_24h` score `9.9427` n `53` status `ready` deltaP `28.8293` edge `0.713` maxDD `-4.464`
- `risk_on_and_context->crypto_major_24h` score `9.9427` n `53` status `ready` deltaP `28.8293` edge `0.713` maxDD `-4.464`
- `risk_on_high->unknown_4h` score `8.8316` n `83` status `ready` deltaP `30.4823` edge `0.5756` maxDD `-1.0945`
- `risk_on_and_context->unknown_4h` score `8.8316` n `83` status `ready` deltaP `30.4823` edge `0.5756` maxDD `-1.0945`
- `risk_on_high->fx_24h` score `6.1662` n `53` status `ready` deltaP `69.0972` edge `0.0532` maxDD `0.0`
- `risk_on_and_context->fx_24h` score `6.1662` n `53` status `ready` deltaP `69.0972` edge `0.0532` maxDD `0.0`
- `market_context_high->unknown_4h` score `5.0969` n `149` status `ready` deltaP `21.054` edge `0.3314` maxDD `-1.0945`
- `risk_on_high->metal_24h` score `4.5014` n `53` status `ready` deltaP `41.3064` edge `0.1351` maxDD `-0.4952`
- `risk_on_and_context->metal_24h` score `4.5014` n `53` status `ready` deltaP `41.3064` edge `0.1351` maxDD `-0.4952`
- `risk_on_high->unknown_1h` score `4.4428` n `92` status `ready` deltaP `11.8915` edge `0.3154` maxDD `-0.2885`
- `risk_on_and_context->unknown_1h` score `4.4428` n `92` status `ready` deltaP `11.8915` edge `0.3154` maxDD `-0.2885`
- `market_context_high->crypto_major_24h` score `4.3451` n `117` status `ready` deltaP `17.4279` edge `0.495` maxDD `-17.2607`
- `market_context_high->metal_24h` score `4.0639` n `117` status `ready` deltaP `32.2917` edge `0.2253` maxDD `-3.1535`
- `market_context_high->crypto_alt_24h` score `3.8492` n `117` status `ready` deltaP `18.6966` edge `0.7878` maxDD `-27.517`
- `market_context_high->unknown_1h` score `2.9356` n `161` status `ready` deltaP `9.8728` edge `0.2197` maxDD `-0.9372`
- `risk_on_high->equity_24h` score `2.3287` n `53` status `ready` deltaP `21.7342` edge `0.098` maxDD `-1.907`
- `risk_on_and_context->equity_24h` score `2.3287` n `53` status `ready` deltaP `21.7342` edge `0.098` maxDD `-1.907`
- `risk_on_high->index_24h` score `1.2536` n `53` status `ready` deltaP `20.2764` edge `0.0005` maxDD `-0.4968`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
