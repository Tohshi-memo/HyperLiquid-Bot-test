# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-09T16:07:32.877598+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10148`

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

- `risk_on_high->crypto_alt_24h` score `9.39` n `117` status `ready` deltaP `21.9418` edge `0.6592` maxDD `-0.8386`
- `risk_on_and_context->crypto_alt_24h` score `9.39` n `117` status `ready` deltaP `21.9418` edge `0.6592` maxDD `-0.8386`
- `risk_on_high->crypto_alt_4h` score `5.6344` n `117` status `ready` deltaP `32.1594` edge `0.2923` maxDD `-1.9733`
- `risk_on_and_context->crypto_alt_4h` score `5.6344` n `117` status `ready` deltaP `32.1594` edge `0.2923` maxDD `-1.9733`
- `risk_on_high->crypto_major_24h` score `4.5848` n `117` status `ready` deltaP `17.8018` edge `0.8759` maxDD `-24.5429`
- `risk_on_and_context->crypto_major_24h` score `4.5848` n `117` status `ready` deltaP `17.8018` edge `0.8759` maxDD `-24.5429`
- `market_context_high->crypto_alt_24h` score `4.3425` n `241` status `ready` deltaP `14.597` edge `0.3473` maxDD `-3.9523`
- `risk_on_high->crypto_major_4h` score `3.839` n `117` status `ready` deltaP `22.9323` edge `0.2529` maxDD `-3.8693`
- `risk_on_and_context->crypto_major_4h` score `3.839` n `117` status `ready` deltaP `22.9323` edge `0.2529` maxDD `-3.8693`
- `risk_on_high->index_24h` score `2.1202` n `117` status `ready` deltaP `22.2623` edge `0.0325` maxDD `-0.0051`
- `risk_on_and_context->index_24h` score `2.1202` n `117` status `ready` deltaP `22.2623` edge `0.0325` maxDD `-0.0051`
- `market_context_high->index_24h` score `1.3988` n `241` status `ready` deltaP `17.3575` edge `0.0402` maxDD `-0.1483`
- `risk_on_high->crypto_alt_1h` score `0.9538` n `117` status `ready` deltaP `3.7976` edge `0.0894` maxDD `-1.1521`
- `risk_on_and_context->crypto_alt_1h` score `0.9538` n `117` status `ready` deltaP `3.7976` edge `0.0894` maxDD `-1.1521`
- `risk_on_high->metal_24h` score `0.6646` n `117` status `ready` deltaP `19.7383` edge `0.0692` maxDD `-0.9131`
- `risk_on_and_context->metal_24h` score `0.6646` n `117` status `ready` deltaP `19.7383` edge `0.0692` maxDD `-0.9131`
- `market_context_high->equity_24h` score `0.3275` n `241` status `ready` deltaP `5.7292` edge `-0.0109` maxDD `0.0`
- `risk_on_high->equity_1h` score `0.2567` n `117` status `ready` deltaP `13.0253` edge `-0.0123` maxDD `-2.2516`
- `risk_on_and_context->equity_1h` score `0.2567` n `117` status `ready` deltaP `13.0253` edge `-0.0123` maxDD `-2.2516`
- `risk_on_high->index_1h` score `0.2146` n `117` status `ready` deltaP `10.0172` edge `-0.0029` maxDD `-0.5764`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
