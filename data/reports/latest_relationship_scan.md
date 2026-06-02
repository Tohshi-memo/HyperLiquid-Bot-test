# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-02T00:52:19.212660+00:00`
- Price records: `672`
- Market context records: `2614`
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

- `market_context_high->unknown_24h` score `7.9698` n `146` status `ready` deltaP `18.2958` edge `0.575` maxDD `-1.626`
- `market_context_high->crypto_alt_4h` score `5.1655` n `146` status `ready` deltaP `25.0439` edge `0.5314` maxDD `-15.4319`
- `market_context_high->crypto_major_4h` score `3.3875` n `146` status `ready` deltaP `14.4587` edge `0.3669` maxDD `-10.1468`
- `market_context_high->crypto_alt_1h` score `1.3472` n `146` status `ready` deltaP `11.4306` edge `0.1548` maxDD `-6.1656`
- `market_context_high->unknown_4h` score `1.1061` n `146` status `ready` deltaP `7.837` edge `0.1449` maxDD `-3.7312`
- `market_context_high->index_24h` score `0.7416` n `146` status `ready` deltaP `8.8018` edge `0.1012` maxDD `-2.5127`
- `market_context_high->crypto_major_1h` score `0.7305` n `146` status `ready` deltaP `8.8631` edge `0.1212` maxDD `-4.2199`
- `market_context_high->crypto_alt_24h` score `0.5584` n `146` status `ready` deltaP `2.0643` edge `0.6706` maxDD `-39.0265`
- `market_context_high->index_4h` score `0.2024` n `146` status `ready` deltaP `8.8227` edge `0.0422` maxDD `-2.3986`
- `market_context_high->index_1h` score `-0.088` n `146` status `ready` deltaP `4.3905` edge `0.0128` maxDD `-1.2855`
- `market_context_high->commodity_1h` score `-0.4015` n `146` status `ready` deltaP `5.502` edge `0.0177` maxDD `-4.3601`
- `market_context_high->unknown_1h` score `-0.4512` n `146` status `ready` deltaP `1.9502` edge `0.0157` maxDD `-2.6375`
- `market_context_high->metal_1h` score `-0.5757` n `146` status `ready` deltaP `1.7103` edge `0.0154` maxDD `-2.9823`
- `market_context_high->fx_1h` score `-0.6389` n `146` status `ready` deltaP `-0.5352` edge `0.0038` maxDD `-0.278`
- `market_context_high->equity_1h` score `-0.7533` n `146` status `ready` deltaP `-0.0779` edge `0.0216` maxDD `-2.7085`
- `market_context_high->metal_4h` score `-0.7918` n `146` status `ready` deltaP `4.0448` edge `0.0458` maxDD `-4.7664`
- `market_context_high->fx_24h` score `-0.9053` n `146` status `ready` deltaP `3.8884` edge `-0.002` maxDD `-1.6157`
- `market_context_high->fx_4h` score `-0.9228` n `146` status `ready` deltaP `-0.378` edge `0.0114` maxDD `-0.8621`
- `market_context_high->commodity_4h` score `-1.03` n `146` status `ready` deltaP `3.7963` edge `0.0369` maxDD `-10.2078`
- `market_context_high->equity_4h` score `-1.383` n `146` status `ready` deltaP `1.6497` edge `0.0142` maxDD `-5.9024`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
