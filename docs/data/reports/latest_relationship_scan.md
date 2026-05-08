# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-08T06:52:20.083710+00:00`
- Price records: `623`
- Market context records: `729`
- Flow alert records: `2059`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `1009`

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

- `market_context_high->crypto_major_24h` score `12.0019` n `146` status `ready` deltaP `28.9725` edge `0.8404` maxDD `-1.3382`
- `market_context_high->crypto_alt_24h` score `6.3895` n `146` status `ready` deltaP `7.854` edge `0.4849` maxDD `-0.0508`
- `market_context_high->index_24h` score `-0.2561` n `146` status `ready` deltaP `0.0249` edge `0.178` maxDD `-5.9609`
- `market_context_high->fx_4h` score `-0.341` n `149` status `ready` deltaP `5.3135` edge `0.008` maxDD `-1.6381`
- `market_context_high->fx_1h` score `-0.434` n `156` status `ready` deltaP `2.8861` edge `0.0024` maxDD `-0.291`
- `market_context_high->commodity_1h` score `-0.5185` n `156` status `ready` deltaP `2.0606` edge `0.0405` maxDD `-3.7959`
- `market_context_high->index_1h` score `-0.9124` n `156` status `ready` deltaP `0.8881` edge `0.0034` maxDD `-2.8282`
- `market_context_high->crypto_major_4h` score `-0.977` n `149` status `ready` deltaP `17.7515` edge `0.127` maxDD `-22.648`
- `market_context_high->equity_1h` score `-1.0328` n `156` status `ready` deltaP `-0.5753` edge `-0.0012` maxDD `-4.4826`
- `market_context_high->equity_24h` score `-1.0535` n `146` status `ready` deltaP `-1.7129` edge `0.1841` maxDD `-10.5047`
- `market_context_high->crypto_major_1h` score `-1.0944` n `156` status `ready` deltaP `5.355` edge `-0.0037` maxDD `-11.4508`
- `market_context_high->crypto_alt_1h` score `-1.4909` n `156` status `ready` deltaP `3.8596` edge `-0.0185` maxDD `-8.1842`
- `market_context_high->unknown_1h` score `-1.5836` n `156` status `ready` deltaP `-4.7398` edge `-0.0232` maxDD `-3.5069`
- `market_context_high->index_4h` score `-1.87` n `149` status `ready` deltaP `0.906` edge `-0.0096` maxDD `-6.5149`
- `market_context_high->crypto_alt_4h` score `-2.0172` n `149` status `ready` deltaP `3.1014` edge `0.0682` maxDD `-15.2248`
- `market_context_high->equity_4h` score `-2.8412` n `149` status `ready` deltaP `-2.0791` edge `-0.0077` maxDD `-10.5498`
- `market_context_high->metal_1h` score `-3.2458` n `156` status `ready` deltaP `-4.4634` edge `-0.0448` maxDD `-9.0076`
- `market_context_high->commodity_4h` score `-3.5643` n `149` status `ready` deltaP `-5.0597` edge `0.0868` maxDD `-13.0076`
- `market_context_high->unknown_4h` score `-3.9494` n `149` status `ready` deltaP `4.5907` edge `-0.1719` maxDD `-8.3588`
- `market_context_high->fx_24h` score `-5.2503` n `146` status `ready` deltaP `-14.2539` edge `-0.0609` maxDD `-21.0414`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
