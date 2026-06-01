# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-01T23:22:21.569576+00:00`
- Price records: `672`
- Market context records: `2607`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9216`

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

- `market_context_high->unknown_24h` score `8.0637` n `143` status `ready` deltaP `18.1952` edge `0.5835` maxDD `-1.626`
- `market_context_high->crypto_alt_4h` score `5.3167` n `146` status `ready` deltaP `25.0439` edge `0.544` maxDD `-15.4319`
- `market_context_high->crypto_major_4h` score `3.5659` n `146` status `ready` deltaP `15.0685` edge `0.3777` maxDD `-10.1468`
- `market_context_high->crypto_alt_1h` score `1.3988` n `146` status `ready` deltaP `11.5803` edge `0.1581` maxDD `-6.1656`
- `market_context_high->unknown_4h` score `0.8079` n `146` status `ready` deltaP `7.3797` edge `0.1231` maxDD `-3.7312`
- `market_context_high->crypto_alt_24h` score `0.7741` n `143` status `ready` deltaP `2.0907` edge `0.6884` maxDD `-39.0265`
- `market_context_high->crypto_major_1h` score `0.7437` n `146` status `ready` deltaP `8.8631` edge `0.1223` maxDD `-4.2199`
- `market_context_high->index_24h` score `0.6992` n `143` status `ready` deltaP `8.3613` edge `0.1006` maxDD `-2.5127`
- `market_context_high->index_4h` score `0.2108` n `146` status `ready` deltaP `8.8227` edge `0.0429` maxDD `-2.3986`
- `market_context_high->index_1h` score `-0.0784` n `146` status `ready` deltaP `4.5402` edge `0.0126` maxDD `-1.2855`
- `market_context_high->commodity_1h` score `-0.4182` n `146` status `ready` deltaP `5.3523` edge `0.0173` maxDD `-4.3601`
- `market_context_high->unknown_1h` score `-0.4668` n `146` status `ready` deltaP `1.8005` edge `0.0154` maxDD `-2.6375`
- `market_context_high->metal_1h` score `-0.5757` n `146` status `ready` deltaP `1.7103` edge `0.0154` maxDD `-2.9823`
- `market_context_high->fx_1h` score `-0.6126` n `146` status `ready` deltaP `-0.2358` edge `0.004` maxDD `-0.278`
- `market_context_high->metal_4h` score `-0.641` n `146` status `ready` deltaP `4.6546` edge `0.0543` maxDD `-4.7664`
- `market_context_high->equity_1h` score `-0.7665` n `146` status `ready` deltaP `0.0718` edge `0.0195` maxDD `-2.7085`
- `market_context_high->fx_4h` score `-0.8754` n `146` status `ready` deltaP `0.0793` edge `0.0123` maxDD `-0.8621`
- `market_context_high->fx_24h` score `-0.88` n `143` status `ready` deltaP `4.0392` edge `-0.0009` maxDD `-1.6157`
- `market_context_high->commodity_4h` score `-1.1126` n `146` status `ready` deltaP `3.0341` edge `0.0314` maxDD `-10.2078`
- `market_context_high->equity_4h` score `-1.329` n `146` status `ready` deltaP `1.6497` edge `0.0187` maxDD `-5.9024`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
