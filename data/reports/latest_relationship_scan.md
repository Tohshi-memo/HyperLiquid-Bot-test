# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-08T12:22:25.846521+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10426`

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

- `risk_on_high->crypto_alt_24h` score `7.5618` n `117` status `ready` deltaP `18.4696` edge `0.53` maxDD `-0.8386`
- `risk_on_and_context->crypto_alt_24h` score `7.5618` n `117` status `ready` deltaP `18.4696` edge `0.53` maxDD `-0.8386`
- `risk_on_high->crypto_alt_4h` score `5.7716` n `117` status `ready` deltaP `31.5497` edge `0.3078` maxDD `-1.9733`
- `risk_on_and_context->crypto_alt_4h` score `5.7716` n `117` status `ready` deltaP `31.5497` edge `0.3078` maxDD `-1.9733`
- `risk_on_high->crypto_major_4h` score `4.7039` n `117` status `ready` deltaP `25.5238` edge `0.3077` maxDD `-3.8693`
- `risk_on_and_context->crypto_major_4h` score `4.7039` n `117` status `ready` deltaP `25.5238` edge `0.3077` maxDD `-3.8693`
- `risk_on_high->crypto_major_24h` score `4.7002` n `117` status `ready` deltaP `21.1005` edge `0.8687` maxDD `-24.5429`
- `risk_on_and_context->crypto_major_24h` score `4.7002` n `117` status `ready` deltaP `21.1005` edge `0.8687` maxDD `-24.5429`
- `market_context_high->crypto_alt_24h` score `2.5143` n `241` status `ready` deltaP `11.1248` edge `0.2181` maxDD `-3.9523`
- `risk_on_high->crypto_alt_1h` score `0.9585` n `117` status `ready` deltaP `4.2467` edge `0.0868` maxDD `-1.1521`
- `risk_on_and_context->crypto_alt_1h` score `0.9585` n `117` status `ready` deltaP `4.2467` edge `0.0868` maxDD `-1.1521`
- `risk_on_high->index_24h` score `0.7242` n `117` status `ready` deltaP `9.7623` edge `-0.0005` maxDD `-0.0051`
- `risk_on_and_context->index_24h` score `0.7242` n `117` status `ready` deltaP `9.7623` edge `-0.0005` maxDD `-0.0051`
- `risk_on_high->equity_1h` score `0.3586` n `117` status `ready` deltaP `13.4744` edge `-0.0068` maxDD `-2.2516`
- `risk_on_and_context->equity_1h` score `0.3586` n `117` status `ready` deltaP `13.4744` edge `-0.0068` maxDD `-2.2516`
- `risk_on_high->crypto_major_1h` score `0.2793` n `117` status `ready` deltaP `4.3337` edge `0.0671` maxDD `-3.1509`
- `risk_on_and_context->crypto_major_1h` score `0.2793` n `117` status `ready` deltaP `4.3337` edge `0.0671` maxDD `-3.1509`
- `risk_on_high->metal_1h` score `0.238` n `117` status `ready` deltaP `9.38` edge `0.001` maxDD `-0.3081`
- `risk_on_and_context->metal_1h` score `0.238` n `117` status `ready` deltaP `9.38` edge `0.001` maxDD `-0.3081`
- `risk_on_high->index_1h` score `0.1593` n `117` status `ready` deltaP `9.119` edge `-0.004` maxDD `-0.5764`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
