# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-09T07:22:32.757755+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10224`

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

- `risk_on_high->crypto_alt_24h` score `7.6365` n `117` status `ready` deltaP `19.164` edge `0.5316` maxDD `-0.8386`
- `risk_on_and_context->crypto_alt_24h` score `7.6365` n `117` status `ready` deltaP `19.164` edge `0.5316` maxDD `-0.8386`
- `risk_on_high->crypto_alt_4h` score `5.5636` n `117` status `ready` deltaP `31.2448` edge `0.2925` maxDD `-1.9733`
- `risk_on_and_context->crypto_alt_4h` score `5.5636` n `117` status `ready` deltaP `31.2448` edge `0.2925` maxDD `-1.9733`
- `risk_on_high->crypto_major_24h` score `3.906` n `117` status `ready` deltaP `17.1074` edge `0.7935` maxDD `-24.5429`
- `risk_on_and_context->crypto_major_24h` score `3.906` n `117` status `ready` deltaP `17.1074` edge `0.7935` maxDD `-24.5429`
- `risk_on_high->crypto_major_4h` score `3.5878` n `117` status `ready` deltaP `21.7128` edge `0.2401` maxDD `-3.8693`
- `risk_on_and_context->crypto_major_4h` score `3.5878` n `117` status `ready` deltaP `21.7128` edge `0.2401` maxDD `-3.8693`
- `market_context_high->crypto_alt_24h` score `2.5891` n `241` status `ready` deltaP `11.8192` edge `0.2197` maxDD `-3.9523`
- `risk_on_high->index_24h` score `1.6772` n `117` status `ready` deltaP `18.2692` edge `0.0222` maxDD `-0.0051`
- `risk_on_and_context->index_24h` score `1.6772` n `117` status `ready` deltaP `18.2692` edge `0.0222` maxDD `-0.0051`
- `market_context_high->index_24h` score `0.9557` n `241` status `ready` deltaP `13.3644` edge `0.0299` maxDD `-0.1483`
- `risk_on_high->crypto_alt_1h` score `0.9249` n `117` status `ready` deltaP `4.097` edge `0.085` maxDD `-1.1521`
- `risk_on_and_context->crypto_alt_1h` score `0.9249` n `117` status `ready` deltaP `4.097` edge `0.085` maxDD `-1.1521`
- `risk_on_high->metal_24h` score `0.249` n `117` status `ready` deltaP `17.6549` edge `0.0298` maxDD `-0.9131`
- `risk_on_and_context->metal_24h` score `0.249` n `117` status `ready` deltaP `17.6549` edge `0.0298` maxDD `-0.9131`
- `risk_on_high->metal_1h` score `0.1531` n `117` status `ready` deltaP `8.0327` edge `-0.0009` maxDD `-0.3081`
- `risk_on_and_context->metal_1h` score `0.1531` n `117` status `ready` deltaP `8.0327` edge `-0.0009` maxDD `-0.3081`
- `risk_on_high->index_1h` score `0.1281` n `117` status `ready` deltaP `8.6699` edge `-0.005` maxDD `-0.5764`
- `risk_on_and_context->index_1h` score `0.1281` n `117` status `ready` deltaP `8.6699` edge `-0.005` maxDD `-0.5764`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
