# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-16T09:52:28.712013+00:00`
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

- `news_risk_high->unknown_4h` score `366.0686` n `83` status `ready` deltaP `-21.6629` edge `30.7396` maxDD `-4.1571`
- `news_risk_high->crypto_alt_24h` score `24.1383` n `78` status `ready` deltaP `47.7698` edge `1.7321` maxDD `-1.4564`
- `news_risk_high->crypto_major_24h` score `21.0637` n `78` status `ready` deltaP `39.7303` edge `1.6375` maxDD `-9.098`
- `news_risk_high->equity_24h` score `15.2418` n `78` status `ready` deltaP `47.7697` edge `1.1291` maxDD `-6.5262`
- `news_risk_high->index_24h` score `7.9111` n `78` status `ready` deltaP `55.6891` edge `0.3056` maxDD `-0.075`
- `news_risk_high->metal_24h` score `6.746` n `78` status `ready` deltaP `38.4882` edge `0.351` maxDD `-0.6334`
- `risk_on_high->commodity_24h` score `5.4648` n `52` status `ready` deltaP `35.0694` edge `0.2216` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `5.4648` n `52` status `ready` deltaP `35.0694` edge `0.2216` maxDD `0.0`
- `market_context_high->commodity_24h` score `4.1656` n `149` status `ready` deltaP `28.358` edge `0.2106` maxDD `-0.8682`
- `risk_on_high->fx_24h` score `2.3657` n `52` status `ready` deltaP `31.9311` edge `-0.0115` maxDD `-0.0054`
- `risk_on_and_context->fx_24h` score `2.3657` n `52` status `ready` deltaP `31.9311` edge `-0.0115` maxDD `-0.0054`
- `market_context_high->fx_24h` score `2.2308` n `149` status `ready` deltaP `29.1562` edge `0.0131` maxDD `-0.0593`
- `risk_on_high->commodity_4h` score `2.0759` n `52` status `ready` deltaP `27.2045` edge `0.0266` maxDD `-0.1313`
- `risk_on_and_context->commodity_4h` score `2.0759` n `52` status `ready` deltaP `27.2045` edge `0.0266` maxDD `-0.1313`
- `market_context_high->commodity_4h` score `1.9756` n `149` status `ready` deltaP `23.7068` edge `0.0484` maxDD `-0.345`
- `market_context_high->commodity_1h` score `0.8257` n `149` status `ready` deltaP `13.5163` edge `0.0164` maxDD `-0.3491`
- `risk_on_high->crypto_alt_4h` score `0.5692` n `52` status `ready` deltaP `10.7646` edge `0.1627` maxDD `-6.2526`
- `risk_on_and_context->crypto_alt_4h` score `0.5692` n `52` status `ready` deltaP `10.7646` edge `0.1627` maxDD `-6.2526`
- `news_risk_high->index_4h` score `0.5662` n `83` status `ready` deltaP `15.3945` edge `0.0328` maxDD `-0.6935`
- `risk_on_high->commodity_1h` score `0.2025` n `52` status `ready` deltaP `6.5984` edge `0.0081` maxDD `-0.1507`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
