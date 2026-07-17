# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-17T07:52:28.793233+00:00`
- Price records: `672`
- Market context records: `7007`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11539`

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

- `market_context_high->unknown_24h` score `-0.1462` n `222` status `ready` deltaP `-5.1943` edge `0.4709` maxDD `-18.7342`
- `market_context_high->fx_1h` score `-0.262` n `235` status `ready` deltaP `2.0563` edge `0.0012` maxDD `-0.5468`
- `market_context_high->crypto_alt_1h` score `-0.4533` n `235` status `ready` deltaP `2.199` edge `0.034` maxDD `-4.5815`
- `market_context_high->index_1h` score `-0.6454` n `235` status `ready` deltaP `1.0472` edge `0.0014` maxDD `-2.2895`
- `market_context_high->metal_1h` score `-0.6821` n `235` status `ready` deltaP `-1.5849` edge `-0.0001` maxDD `-2.1427`
- `market_context_high->crypto_major_1h` score `-0.893` n `235` status `ready` deltaP `4.2477` edge `0.0325` maxDD `-7.1523`
- `market_context_high->fx_4h` score `-0.95` n `235` status `ready` deltaP `11.6963` edge `0.0066` maxDD `-2.1765`
- `market_context_high->commodity_1h` score `-1.2076` n `235` status `ready` deltaP `-2.1117` edge `-0.0144` maxDD `-2.4388`
- `market_context_high->unknown_1h` score `-1.3003` n `235` status `ready` deltaP `-1.5531` edge `-0.0079` maxDD `-3.2083`
- `market_context_high->commodity_4h` score `-1.6397` n `235` status `ready` deltaP `-3.846` edge `-0.0356` maxDD `-5.5853`
- `market_context_high->index_4h` score `-1.7385` n `235` status `ready` deltaP `8.3426` edge `-0.0086` maxDD `-12.2591`
- `market_context_high->equity_1h` score `-1.8192` n `235` status `ready` deltaP `3.8527` edge `-0.0035` maxDD `-15.7664`
- `market_context_high->metal_4h` score `-1.8986` n `235` status `ready` deltaP `6.7365` edge `0.01` maxDD `-5.5324`
- `market_context_high->unknown_4h` score `-2.4979` n `235` status `ready` deltaP `-5.4897` edge `0.065` maxDD `-10.2579`
- `market_context_high->crypto_alt_4h` score `-2.6512` n `235` status `ready` deltaP `2.2262` edge `0.0238` maxDD `-22.2831`
- `market_context_high->crypto_major_4h` score `-3.0975` n `235` status `ready` deltaP `2.1945` edge `0.0167` maxDD `-24.6094`
- `market_context_high->commodity_24h` score `-3.6395` n `222` status `ready` deltaP `-5.9216` edge `-0.0927` maxDD `-4.6891`
- `market_context_high->fx_24h` score `-4.3975` n `222` status `ready` deltaP `-6.9961` edge `-0.0167` maxDD `-5.583`
- `market_context_high->equity_4h` score `-7.2631` n `235` status `ready` deltaP `5.7071` edge `-0.0475` maxDD `-66.7371`
- `market_context_high->index_24h` score `-11.6664` n `222` status `ready` deltaP `-0.6147` edge `-0.0846` maxDD `-59.5597`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
