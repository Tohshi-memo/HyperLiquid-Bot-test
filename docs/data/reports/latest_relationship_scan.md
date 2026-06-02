# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-02T03:52:26.997667+00:00`
- Price records: `672`
- Market context records: `2626`
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

- `market_context_high->unknown_24h` score `7.6446` n `146` status `ready` deltaP `18.2958` edge `0.5479` maxDD `-1.626`
- `market_context_high->crypto_alt_4h` score `5.0865` n `146` status `ready` deltaP `25.1963` edge `0.5238` maxDD `-15.4319`
- `market_context_high->crypto_major_4h` score `3.2649` n `146` status `ready` deltaP `14.3063` edge `0.3577` maxDD `-10.1468`
- `market_context_high->index_24h` score `1.24` n `146` status `ready` deltaP `10.7115` edge `0.13` maxDD `-2.5127`
- `market_context_high->crypto_alt_1h` score `1.2033` n `146` status `ready` deltaP `10.8318` edge `0.1468` maxDD `-6.1656`
- `market_context_high->unknown_4h` score `1.0421` n `146` status `ready` deltaP `7.5321` edge `0.1416` maxDD `-3.7312`
- `market_context_high->crypto_alt_24h` score `0.6306` n `146` status `ready` deltaP `2.4116` edge `0.6743` maxDD `-39.0265`
- `market_context_high->crypto_major_1h` score `0.6177` n `146` status `ready` deltaP `8.414` edge `0.1148` maxDD `-4.2199`
- `market_context_high->index_4h` score `0.34` n `146` status `ready` deltaP `9.4325` edge `0.0496` maxDD `-2.3986`
- `market_context_high->index_1h` score `-0.0856` n `146` status `ready` deltaP `4.3905` edge `0.013` maxDD `-1.2855`
- `market_context_high->unknown_1h` score `-0.228` n `146` status `ready` deltaP `2.0999` edge `0.0333` maxDD `-2.6375`
- `market_context_high->commodity_1h` score `-0.278` n `146` status `ready` deltaP `6.4002` edge `0.022` maxDD `-4.3601`
- `market_context_high->fx_1h` score `-0.7443` n `146` status `ready` deltaP `-1.7328` edge `0.003` maxDD `-0.278`
- `market_context_high->metal_1h` score `-0.7472` n `146` status `ready` deltaP `0.6624` edge `0.0081` maxDD `-2.9823`
- `market_context_high->commodity_4h` score `-0.8514` n `146` status `ready` deltaP `5.6256` edge `0.0476` maxDD `-10.2078`
- `market_context_high->equity_1h` score `-0.9079` n `146` status `ready` deltaP `-1.1258` edge `0.0157` maxDD `-2.7085`
- `market_context_high->fx_24h` score `-1.0404` n `146` status `ready` deltaP `2.4995` edge `-0.004` maxDD `-1.6157`
- `market_context_high->fx_4h` score `-1.0723` n `146` status `ready` deltaP `-1.9024` edge `0.0091` maxDD `-0.8621`
- `market_context_high->metal_4h` score `-1.0769` n `146` status `ready` deltaP `2.5204` edge `0.0322` maxDD `-4.7664`
- `market_context_high->equity_4h` score `-1.335` n `146` status `ready` deltaP `1.6497` edge `0.0182` maxDD `-5.9024`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
