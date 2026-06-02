# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-02T03:37:21.825717+00:00`
- Price records: `672`
- Market context records: `2625`
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

- `market_context_high->unknown_24h` score `7.6578` n `146` status `ready` deltaP `18.2958` edge `0.549` maxDD `-1.626`
- `market_context_high->crypto_alt_4h` score `5.0817` n `146` status `ready` deltaP `25.1963` edge `0.5234` maxDD `-15.4319`
- `market_context_high->crypto_major_4h` score `3.2479` n `146` status `ready` deltaP `14.1539` edge `0.3573` maxDD `-10.1468`
- `market_context_high->crypto_alt_1h` score `1.2369` n `146` status `ready` deltaP `10.9815` edge `0.1486` maxDD `-6.1656`
- `market_context_high->index_24h` score `1.1853` n `146` status `ready` deltaP `10.5379` edge `0.1266` maxDD `-2.5127`
- `market_context_high->unknown_4h` score `1.0445` n `146` status `ready` deltaP `7.5321` edge `0.1418` maxDD `-3.7312`
- `market_context_high->crypto_major_1h` score `0.6417` n `146` status `ready` deltaP `8.5637` edge `0.1158` maxDD `-4.2199`
- `market_context_high->crypto_alt_24h` score `0.6186` n `146` status `ready` deltaP `2.4116` edge `0.6733` maxDD `-39.0265`
- `market_context_high->index_4h` score `0.317` n `146` status `ready` deltaP `9.28` edge `0.0487` maxDD `-2.3986`
- `market_context_high->index_1h` score `-0.0868` n `146` status `ready` deltaP `4.3905` edge `0.0129` maxDD `-1.2855`
- `market_context_high->unknown_1h` score `-0.222` n `146` status `ready` deltaP `2.0999` edge `0.0338` maxDD `-2.6375`
- `market_context_high->commodity_1h` score `-0.2816` n `146` status `ready` deltaP `6.4002` edge `0.0217` maxDD `-4.3601`
- `market_context_high->metal_1h` score `-0.7268` n `146` status `ready` deltaP `0.8121` edge `0.0088` maxDD `-2.9823`
- `market_context_high->fx_1h` score `-0.7443` n `146` status `ready` deltaP `-1.7328` edge `0.003` maxDD `-0.278`
- `market_context_high->commodity_4h` score `-0.8648` n `146` status `ready` deltaP `5.4731` edge `0.0469` maxDD `-10.2078`
- `market_context_high->equity_1h` score `-0.8912` n `146` status `ready` deltaP `-0.9761` edge `0.0161` maxDD `-2.7085`
- `market_context_high->fx_24h` score `-1.0253` n `146` status `ready` deltaP `2.6731` edge `-0.0039` maxDD `-1.6157`
- `market_context_high->metal_4h` score `-1.0539` n `146` status `ready` deltaP `2.6729` edge `0.0331` maxDD `-4.7664`
- `market_context_high->fx_4h` score `-1.0577` n `146` status `ready` deltaP `-1.7499` edge `0.0093` maxDD `-0.8621`
- `market_context_high->equity_4h` score `-1.3386` n `146` status `ready` deltaP `1.6497` edge `0.0179` maxDD `-5.9024`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
