# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-09T01:37:28.788398+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10176`

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

- `risk_on_high->crypto_alt_24h` score `7.1008` n `117` status `ready` deltaP `16.9071` edge `0.502` maxDD `-0.8386`
- `risk_on_and_context->crypto_alt_24h` score `7.1008` n `117` status `ready` deltaP `16.9071` edge `0.502` maxDD `-0.8386`
- `risk_on_high->crypto_alt_4h` score `5.8052` n `117` status `ready` deltaP `31.5497` edge `0.3106` maxDD `-1.9733`
- `risk_on_and_context->crypto_alt_4h` score `5.8052` n `117` status `ready` deltaP `31.5497` edge `0.3106` maxDD `-1.9733`
- `risk_on_high->crypto_major_4h` score `4.11` n `117` status `ready` deltaP `23.6945` edge `0.2704` maxDD `-3.8693`
- `risk_on_and_context->crypto_major_4h` score `4.11` n `117` status `ready` deltaP `23.6945` edge `0.2704` maxDD `-3.8693`
- `risk_on_high->crypto_major_24h` score `4.0632` n `117` status `ready` deltaP `17.281` edge `0.8125` maxDD `-24.5429`
- `risk_on_and_context->crypto_major_24h` score `4.0632` n `117` status `ready` deltaP `17.281` edge `0.8125` maxDD `-24.5429`
- `market_context_high->crypto_alt_24h` score `2.0533` n `241` status `ready` deltaP `9.5623` edge `0.1901` maxDD `-3.9523`
- `risk_on_high->index_24h` score `1.3163` n `117` status `ready` deltaP `15.3178` edge `0.0118` maxDD `-0.0051`
- `risk_on_and_context->index_24h` score `1.3163` n `117` status `ready` deltaP `15.3178` edge `0.0118` maxDD `-0.0051`
- `risk_on_high->crypto_alt_1h` score `0.8782` n `117` status `ready` deltaP `3.6479` edge `0.0841` maxDD `-1.1521`
- `risk_on_and_context->crypto_alt_1h` score `0.8782` n `117` status `ready` deltaP `3.6479` edge `0.0841` maxDD `-1.1521`
- `market_context_high->index_24h` score `0.5948` n `241` status `ready` deltaP `10.413` edge `0.0195` maxDD `-0.1483`
- `risk_on_high->metal_1h` score `0.1625` n `117` status `ready` deltaP `8.1824` edge `-0.0007` maxDD `-0.3081`
- `risk_on_and_context->metal_1h` score `0.1625` n `117` status `ready` deltaP `8.1824` edge `-0.0007` maxDD `-0.3081`
- `risk_on_high->index_1h` score `0.1281` n `117` status `ready` deltaP `8.6699` edge `-0.005` maxDD `-0.5764`
- `risk_on_and_context->index_1h` score `0.1281` n `117` status `ready` deltaP `8.6699` edge `-0.005` maxDD `-0.5764`
- `risk_on_high->equity_1h` score `0.1164` n `117` status `ready` deltaP `12.1271` edge `-0.018` maxDD `-2.2516`
- `risk_on_and_context->equity_1h` score `0.1164` n `117` status `ready` deltaP `12.1271` edge `-0.018` maxDD `-2.2516`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
