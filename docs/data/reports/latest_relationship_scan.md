# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-08T17:52:36.872652+00:00`
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

- `risk_on_high->crypto_alt_24h` score `6.9007` n `117` status `ready` deltaP `16.3862` edge `0.4888` maxDD `-0.8386`
- `risk_on_and_context->crypto_alt_24h` score `6.9007` n `117` status `ready` deltaP `16.3862` edge `0.4888` maxDD `-0.8386`
- `risk_on_high->crypto_alt_4h` score `5.3434` n `117` status `ready` deltaP `29.8728` edge `0.2833` maxDD `-1.9733`
- `risk_on_and_context->crypto_alt_4h` score `5.3434` n `117` status `ready` deltaP `29.8728` edge `0.2833` maxDD `-1.9733`
- `risk_on_high->crypto_major_24h` score `4.2916` n `117` status `ready` deltaP `19.3643` edge `0.8279` maxDD `-24.5429`
- `risk_on_and_context->crypto_major_24h` score `4.2916` n `117` status `ready` deltaP `19.3643` edge `0.8279` maxDD `-24.5429`
- `risk_on_high->crypto_major_4h` score `4.099` n `117` status `ready` deltaP `23.5421` edge `0.2705` maxDD `-3.8693`
- `risk_on_and_context->crypto_major_4h` score `4.099` n `117` status `ready` deltaP `23.5421` edge `0.2705` maxDD `-3.8693`
- `market_context_high->crypto_alt_24h` score `1.8533` n `241` status `ready` deltaP `9.0414` edge `0.1769` maxDD `-3.9523`
- `risk_on_high->crypto_alt_1h` score `0.8122` n `117` status `ready` deltaP `3.6479` edge `0.0786` maxDD `-1.1521`
- `risk_on_and_context->crypto_alt_1h` score `0.8122` n `117` status `ready` deltaP `3.6479` edge `0.0786` maxDD `-1.1521`
- `risk_on_high->index_24h` score `0.7273` n `117` status `ready` deltaP `9.9359` edge `-0.0014` maxDD `-0.0051`
- `risk_on_and_context->index_24h` score `0.7273` n `117` status `ready` deltaP `9.9359` edge `-0.0014` maxDD `-0.0051`
- `risk_on_high->metal_1h` score `0.1827` n `117` status `ready` deltaP `8.4818` edge `-0.0001` maxDD `-0.3081`
- `risk_on_and_context->metal_1h` score `0.1827` n `117` status `ready` deltaP `8.4818` edge `-0.0001` maxDD `-0.3081`
- `risk_on_high->equity_1h` score `0.1188` n `117` status `ready` deltaP `12.1271` edge `-0.0178` maxDD `-2.2516`
- `risk_on_and_context->equity_1h` score `0.1188` n `117` status `ready` deltaP `12.1271` edge `-0.0178` maxDD `-2.2516`
- `risk_on_high->index_1h` score `0.1126` n `117` status `ready` deltaP `8.3705` edge `-0.005` maxDD `-0.5764`
- `risk_on_and_context->index_1h` score `0.1126` n `117` status `ready` deltaP `8.3705` edge `-0.005` maxDD `-0.5764`
- `risk_on_high->crypto_major_1h` score `0.0358` n `117` status `ready` deltaP `3.2858` edge `0.0538` maxDD `-3.1509`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
