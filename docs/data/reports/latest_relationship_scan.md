# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-09T15:37:39.753290+00:00`
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

- `risk_on_high->crypto_alt_24h` score `9.1198` n `117` status `ready` deltaP `21.5946` edge `0.639` maxDD `-0.8386`
- `risk_on_and_context->crypto_alt_24h` score `9.1198` n `117` status `ready` deltaP `21.5946` edge `0.639` maxDD `-0.8386`
- `risk_on_high->crypto_alt_4h` score `5.5766` n `117` status `ready` deltaP `32.007` edge `0.2885` maxDD `-1.9733`
- `risk_on_and_context->crypto_alt_4h` score `5.5766` n `117` status `ready` deltaP `32.007` edge `0.2885` maxDD `-1.9733`
- `risk_on_high->crypto_major_24h` score `4.4123` n `117` status `ready` deltaP `17.4546` edge `0.8561` maxDD `-24.5429`
- `risk_on_and_context->crypto_major_24h` score `4.4123` n `117` status `ready` deltaP `17.4546` edge `0.8561` maxDD `-24.5429`
- `market_context_high->crypto_alt_24h` score `4.0723` n `241` status `ready` deltaP `14.2498` edge `0.3271` maxDD `-3.9523`
- `risk_on_high->crypto_major_4h` score `3.7762` n `117` status `ready` deltaP `22.6274` edge `0.2497` maxDD `-3.8693`
- `risk_on_and_context->crypto_major_4h` score `3.7762` n `117` status `ready` deltaP `22.6274` edge `0.2497` maxDD `-3.8693`
- `risk_on_high->index_24h` score `2.0744` n `117` status `ready` deltaP `21.9151` edge `0.031` maxDD `-0.0051`
- `risk_on_and_context->index_24h` score `2.0744` n `117` status `ready` deltaP `21.9151` edge `0.031` maxDD `-0.0051`
- `market_context_high->index_24h` score `1.353` n `241` status `ready` deltaP `17.0103` edge `0.0387` maxDD `-0.1483`
- `risk_on_high->crypto_alt_1h` score `0.9262` n `117` status `ready` deltaP `3.6479` edge `0.0881` maxDD `-1.1521`
- `risk_on_and_context->crypto_alt_1h` score `0.9262` n `117` status `ready` deltaP `3.6479` edge `0.0881` maxDD `-1.1521`
- `risk_on_high->metal_24h` score `0.6482` n `117` status `ready` deltaP `19.7383` edge `0.0671` maxDD `-0.9131`
- `risk_on_and_context->metal_24h` score `0.6482` n `117` status `ready` deltaP `19.7383` edge `0.0671` maxDD `-0.9131`
- `risk_on_high->equity_1h` score `0.2387` n `117` status `ready` deltaP `12.8756` edge `-0.0128` maxDD `-2.2516`
- `risk_on_and_context->equity_1h` score `0.2387` n `117` status `ready` deltaP `12.8756` edge `-0.0128` maxDD `-2.2516`
- `risk_on_high->index_1h` score `0.213` n `117` status `ready` deltaP `10.0172` edge `-0.0031` maxDD `-0.5764`
- `risk_on_and_context->index_1h` score `0.213` n `117` status `ready` deltaP `10.0172` edge `-0.0031` maxDD `-0.5764`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
