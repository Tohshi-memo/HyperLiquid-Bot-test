# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-15T18:52:26.585317+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `11093`

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

- `news_risk_high->unknown_4h` score `396.1749` n `78` status `ready` deltaP `-23.6749` edge `33.2618` maxDD `-4.1517`
- `news_risk_high->unknown_24h` score `24.8796` n `78` status `ready` deltaP `21.1806` edge `1.9321` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `23.2098` n `78` status `ready` deltaP `47.7698` edge `1.6548` maxDD `-1.4626`
- `news_risk_high->crypto_major_24h` score `18.7302` n `78` status `ready` deltaP `39.5566` edge `1.4442` maxDD `-9.098`
- `news_risk_high->equity_24h` score `15.5117` n `78` status `ready` deltaP `49.8531` edge `1.1377` maxDD `-6.5262`
- `news_risk_high->index_24h` score `8.4117` n `78` status `ready` deltaP `59.6821` edge `0.3207` maxDD `-0.075`
- `news_risk_high->metal_24h` score `6.6284` n `78` status `ready` deltaP `38.4882` edge `0.3412` maxDD `-0.6334`
- `risk_on_high->commodity_24h` score `6.016` n `52` status `ready` deltaP `38.1944` edge `0.2467` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `6.016` n `52` status `ready` deltaP `38.1944` edge `0.2467` maxDD `0.0`
- `market_context_high->commodity_24h` score `4.719` n `137` status `ready` deltaP `30.8951` edge `0.2398` maxDD `-0.8682`
- `risk_on_high->fx_24h` score `3.0223` n `52` status `ready` deltaP `37.1394` edge `0.0085` maxDD `-0.0054`
- `risk_on_and_context->fx_24h` score `3.0223` n `52` status `ready` deltaP `37.1394` edge `0.0085` maxDD `-0.0054`
- `market_context_high->fx_24h` score `2.6253` n `137` status `ready` deltaP `33.953` edge `0.014` maxDD `-0.0593`
- `risk_on_high->commodity_4h` score `1.6556` n `52` status `ready` deltaP `23.2411` edge `0.018` maxDD `-0.1313`
- `risk_on_and_context->commodity_4h` score `1.6556` n `52` status `ready` deltaP `23.2411` edge `0.018` maxDD `-0.1313`
- `market_context_high->commodity_4h` score `1.5553` n `149` status `ready` deltaP `19.7434` edge `0.0398` maxDD `-0.345`
- `news_risk_high->index_4h` score `0.7343` n `78` status `ready` deltaP `17.7259` edge `0.0388` maxDD `-0.6935`
- `market_context_high->commodity_1h` score `0.664` n `149` status `ready` deltaP `11.8696` edge `0.0139` maxDD `-0.3491`
- `risk_on_high->metal_1h` score `0.1272` n `52` status `ready` deltaP `6.2644` edge `0.0051` maxDD `-0.1115`
- `risk_on_and_context->metal_1h` score `0.1272` n `52` status `ready` deltaP `6.2644` edge `0.0051` maxDD `-0.1115`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
