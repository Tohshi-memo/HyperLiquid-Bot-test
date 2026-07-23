# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-23T06:37:33.673000+00:00`
- Price records: `672`
- Market context records: `7643`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `14697`

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

- `market_context_high->index_1h` score `0.0523` n `146` status `ready` deltaP `6.512` edge `0.0112` maxDD `-0.8324`
- `market_context_high->crypto_major_1h` score `-0.0895` n `146` status `ready` deltaP `8.7544` edge `0.0262` maxDD `-4.0162`
- `market_context_high->crypto_alt_1h` score `-0.1929` n `146` status `ready` deltaP `2.3542` edge `0.0228` maxDD `-2.7243`
- `market_context_high->fx_24h` score `-0.3527` n `145` status `ready` deltaP `9.2803` edge `0.0175` maxDD `-3.0343`
- `market_context_high->commodity_1h` score `-0.3882` n `146` status `ready` deltaP `1.5282` edge `-0.0029` maxDD `-1.5641`
- `market_context_high->equity_1h` score `-0.4729` n `146` status `ready` deltaP `5.677` edge `0.0529` maxDD `-7.7764`
- `market_context_high->commodity_24h` score `-0.5776` n `145` status `ready` deltaP `10.2776` edge `0.0417` maxDD `-7.0012`
- `market_context_high->equity_24h` score `-0.6322` n `145` status `ready` deltaP `15.9318` edge `0.3033` maxDD `-34.5784`
- `market_context_high->metal_1h` score `-0.6769` n `146` status `ready` deltaP `0.6398` edge `0.0135` maxDD `-1.0307`
- `market_context_high->index_4h` score `-0.6802` n `146` status `ready` deltaP `8.2987` edge `0.0276` maxDD `-3.2774`
- `market_context_high->commodity_4h` score `-0.69` n `146` status `ready` deltaP `1.6066` edge `0.0063` maxDD `-2.2943`
- `market_context_high->fx_1h` score `-0.7014` n `146` status `ready` deltaP `-1.0223` edge `-0.0017` maxDD `-0.6615`
- `market_context_high->unknown_24h` score `-0.9237` n `146` status `ready` deltaP `7.1918` edge `-0.0069` maxDD `-4.775`
- `market_context_high->crypto_alt_4h` score `-0.9453` n `146` status `ready` deltaP `3.5019` edge `0.0544` maxDD `-9.5815`
- `market_context_high->crypto_major_4h` score `-1.1017` n `146` status `ready` deltaP `9.4366` edge `0.0636` maxDD `-14.4206`
- `market_context_high->unknown_1h` score `-1.4259` n `146` status `ready` deltaP `-0.2358` edge `-0.0549` maxDD `-1.3217`
- `market_context_high->equity_4h` score `-1.558` n `146` status `ready` deltaP `1.9081` edge `0.2019` maxDD `-20.4824`
- `market_context_high->metal_4h` score `-1.7585` n `146` status `ready` deltaP `-3.0425` edge `0.0405` maxDD `-4.6535`
- `market_context_high->metal_24h` score `-2.1701` n `146` status `ready` deltaP `-3.2772` edge `0.0693` maxDD `-7.3868`
- `market_context_high->fx_4h` score `-2.6289` n `146` status `ready` deltaP `-6.9645` edge `-0.0042` maxDD `-2.1425`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
