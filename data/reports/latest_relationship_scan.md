# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-16T08:52:32.910879+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `11471`

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

- `news_risk_high->unknown_4h` score `365.4866` n `83` status `ready` deltaP `-21.6629` edge `30.6911` maxDD `-4.1571`
- `news_risk_high->crypto_alt_24h` score `24.2823` n `78` status `ready` deltaP `47.7698` edge `1.7441` maxDD `-1.4564`
- `news_risk_high->crypto_major_24h` score `21.1069` n `78` status `ready` deltaP `39.7303` edge `1.6411` maxDD `-9.098`
- `news_risk_high->equity_24h` score `15.4366` n `78` status `ready` deltaP `48.4642` edge `1.1407` maxDD `-6.5262`
- `news_risk_high->index_24h` score `7.993` n `78` status `ready` deltaP `56.3835` edge `0.3078` maxDD `-0.075`
- `news_risk_high->metal_24h` score `6.7844` n `78` status `ready` deltaP `38.4882` edge `0.3542` maxDD `-0.6334`
- `risk_on_high->commodity_24h` score `5.4997` n `52` status `ready` deltaP `35.4167` edge `0.2222` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `5.4997` n `52` status `ready` deltaP `35.4167` edge `0.2222` maxDD `0.0`
- `market_context_high->commodity_24h` score `4.2006` n `149` status `ready` deltaP `28.7053` edge `0.2112` maxDD `-0.8682`
- `risk_on_high->fx_24h` score `2.3657` n `52` status `ready` deltaP `31.9311` edge `-0.0115` maxDD `-0.0054`
- `risk_on_and_context->fx_24h` score `2.3657` n `52` status `ready` deltaP `31.9311` edge `-0.0115` maxDD `-0.0054`
- `market_context_high->fx_24h` score `2.2308` n `149` status `ready` deltaP `29.1562` edge `0.0131` maxDD `-0.0593`
- `risk_on_high->commodity_4h` score `2.0443` n `52` status `ready` deltaP `26.8996` edge `0.026` maxDD `-0.1313`
- `risk_on_and_context->commodity_4h` score `2.0443` n `52` status `ready` deltaP `26.8996` edge `0.026` maxDD `-0.1313`
- `market_context_high->commodity_4h` score `1.944` n `149` status `ready` deltaP `23.4019` edge `0.0478` maxDD `-0.345`
- `market_context_high->commodity_1h` score `0.7994` n `149` status `ready` deltaP `13.2169` edge `0.0162` maxDD `-0.3491`
- `news_risk_high->index_4h` score `0.6096` n `83` status `ready` deltaP `16.0043` edge `0.0343` maxDD `-0.6935`
- `risk_on_high->crypto_alt_4h` score `0.5739` n `52` status `ready` deltaP `10.7646` edge `0.1633` maxDD `-6.2526`
- `risk_on_and_context->crypto_alt_4h` score `0.5739` n `52` status `ready` deltaP `10.7646` edge `0.1633` maxDD `-6.2526`
- `risk_on_high->commodity_1h` score `0.1761` n `52` status `ready` deltaP `6.299` edge `0.0079` maxDD `-0.1507`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
