# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-16T16:52:35.118288+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `11441`

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

- `news_risk_high->unknown_4h` score `367.4374` n `83` status `ready` deltaP `-21.0531` edge `30.8496` maxDD `-4.1571`
- `news_risk_high->crypto_alt_24h` score `23.1207` n `78` status `ready` deltaP `47.7698` edge `1.6473` maxDD `-1.4564`
- `news_risk_high->crypto_major_24h` score `20.4793` n `78` status `ready` deltaP `39.7303` edge `1.5888` maxDD `-9.098`
- `news_risk_high->equity_24h` score `13.9125` n `78` status `ready` deltaP `44.8184` edge `1.038` maxDD `-6.5262`
- `news_risk_high->index_24h` score `7.3218` n `78` status `ready` deltaP `50.828` edge `0.2889` maxDD `-0.075`
- `news_risk_high->metal_24h` score `5.841` n `78` status `ready` deltaP `34.4952` edge `0.3022` maxDD `-0.6334`
- `risk_on_high->commodity_24h` score `5.7317` n `52` status `ready` deltaP `36.1111` edge `0.2369` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `5.7317` n `52` status `ready` deltaP `36.1111` edge `0.2369` maxDD `0.0`
- `market_context_high->commodity_24h` score `4.4325` n `149` status `ready` deltaP `29.3997` edge `0.2259` maxDD `-0.8682`
- `risk_on_high->fx_24h` score `2.3801` n `52` status `ready` deltaP `31.9311` edge `-0.0103` maxDD `-0.0054`
- `risk_on_and_context->fx_24h` score `2.3801` n `52` status `ready` deltaP `31.9311` edge `-0.0103` maxDD `-0.0054`
- `market_context_high->fx_24h` score `2.2452` n `149` status `ready` deltaP `29.1562` edge `0.0143` maxDD `-0.0593`
- `risk_on_high->commodity_4h` score `2.2372` n `52` status `ready` deltaP `28.5764` edge `0.0309` maxDD `-0.1313`
- `risk_on_and_context->commodity_4h` score `2.2372` n `52` status `ready` deltaP `28.5764` edge `0.0309` maxDD `-0.1313`
- `market_context_high->commodity_4h` score `2.1369` n `149` status `ready` deltaP `25.0787` edge `0.0527` maxDD `-0.345`
- `market_context_high->commodity_1h` score `0.906` n `149` status `ready` deltaP `14.1151` edge `0.0191` maxDD `-0.3491`
- `risk_on_high->crypto_alt_4h` score `0.4374` n `52` status `ready` deltaP `9.8499` edge `0.1519` maxDD `-6.2526`
- `risk_on_and_context->crypto_alt_4h` score `0.4374` n `52` status `ready` deltaP `9.8499` edge `0.1519` maxDD `-6.2526`
- `news_risk_high->index_4h` score `0.382` n `83` status `ready` deltaP `12.3457` edge `0.0295` maxDD `-0.6935`
- `risk_on_high->commodity_1h` score `0.2828` n `52` status `ready` deltaP `7.1972` edge `0.0108` maxDD `-0.1507`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
