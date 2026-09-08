# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-08T17:37:30.593677+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10256`

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

- `risk_on_high->crypto_alt_24h` score `6.9314` n `117` status `ready` deltaP `16.5598` edge `0.4902` maxDD `-0.8386`
- `risk_on_and_context->crypto_alt_24h` score `6.9314` n `117` status `ready` deltaP `16.5598` edge `0.4902` maxDD `-0.8386`
- `risk_on_high->crypto_alt_4h` score `5.3868` n `117` status `ready` deltaP `30.0253` edge `0.2859` maxDD `-1.9733`
- `risk_on_and_context->crypto_alt_4h` score `5.3868` n `117` status `ready` deltaP `30.0253` edge `0.2859` maxDD `-1.9733`
- `risk_on_high->crypto_major_24h` score `4.3116` n `117` status `ready` deltaP `19.538` edge `0.8293` maxDD `-24.5429`
- `risk_on_and_context->crypto_major_24h` score `4.3116` n `117` status `ready` deltaP `19.538` edge `0.8293` maxDD `-24.5429`
- `risk_on_high->crypto_major_4h` score `4.1472` n `117` status `ready` deltaP `23.6945` edge `0.2735` maxDD `-3.8693`
- `risk_on_and_context->crypto_major_4h` score `4.1472` n `117` status `ready` deltaP `23.6945` edge `0.2735` maxDD `-3.8693`
- `market_context_high->crypto_alt_24h` score `1.884` n `241` status `ready` deltaP `9.215` edge `0.1783` maxDD `-3.9523`
- `risk_on_high->crypto_alt_1h` score `0.8134` n `117` status `ready` deltaP `3.6479` edge `0.0787` maxDD `-1.1521`
- `risk_on_and_context->crypto_alt_1h` score `0.8134` n `117` status `ready` deltaP `3.6479` edge `0.0787` maxDD `-1.1521`
- `risk_on_high->index_24h` score `0.7098` n `117` status `ready` deltaP `9.7623` edge `-0.0017` maxDD `-0.0051`
- `risk_on_and_context->index_24h` score `0.7098` n `117` status `ready` deltaP `9.7623` edge `-0.0017` maxDD `-0.0051`
- `risk_on_high->metal_1h` score `0.1921` n `117` status `ready` deltaP `8.6315` edge `0.0001` maxDD `-0.3081`
- `risk_on_and_context->metal_1h` score `0.1921` n `117` status `ready` deltaP `8.6315` edge `0.0001` maxDD `-0.3081`
- `risk_on_high->equity_1h` score `0.138` n `117` status `ready` deltaP `12.2768` edge `-0.0172` maxDD `-2.2516`
- `risk_on_and_context->equity_1h` score `0.138` n `117` status `ready` deltaP `12.2768` edge `-0.0172` maxDD `-2.2516`
- `risk_on_high->index_1h` score `0.1219` n `117` status `ready` deltaP `8.5202` edge `-0.0048` maxDD `-0.5764`
- `risk_on_and_context->index_1h` score `0.1219` n `117` status `ready` deltaP `8.5202` edge `-0.0048` maxDD `-0.5764`
- `risk_on_high->crypto_major_1h` score `0.0418` n `117` status `ready` deltaP `3.2858` edge `0.0543` maxDD `-3.1509`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
