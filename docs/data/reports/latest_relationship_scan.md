# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-15T14:52:30.300418+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `10890`

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

- `news_risk_high->unknown_4h` score `396.437` n `78` status `ready` deltaP `-23.2176` edge `33.2806` maxDD `-4.1517`
- `news_risk_high->crypto_alt_24h` score `22.6672` n `78` status `ready` deltaP `47.4226` edge `1.6119` maxDD `-1.4626`
- `news_risk_high->unknown_24h` score `22.5066` n `78` status `ready` deltaP `21.0069` edge `1.7355` maxDD `0.0`
- `news_risk_high->crypto_major_24h` score `17.7728` n `78` status `ready` deltaP `38.6886` edge `1.3702` maxDD `-9.098`
- `news_risk_high->equity_24h` score `15.1658` n `78` status `ready` deltaP `49.1586` edge `1.1135` maxDD `-6.5262`
- `news_risk_high->index_24h` score `8.411` n `78` status `ready` deltaP `59.5085` edge `0.3218` maxDD `-0.075`
- `news_risk_high->metal_24h` score `6.4438` n `78` status `ready` deltaP `37.6202` edge `0.3316` maxDD `-0.6334`
- `risk_on_high->commodity_24h` score `6.0244` n `52` status `ready` deltaP `38.1944` edge `0.2474` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `6.0244` n `52` status `ready` deltaP `38.1944` edge `0.2474` maxDD `0.0`
- `market_context_high->commodity_24h` score `4.7274` n `137` status `ready` deltaP `30.8951` edge `0.2405` maxDD `-0.8682`
- `risk_on_high->fx_24h` score `3.3502` n `52` status `ready` deltaP `39.9172` edge `0.0173` maxDD `-0.0054`
- `risk_on_and_context->fx_24h` score `3.3502` n `52` status `ready` deltaP `39.9172` edge `0.0173` maxDD `-0.0054`
- `market_context_high->fx_24h` score `2.9532` n `137` status `ready` deltaP `36.7308` edge `0.0228` maxDD `-0.0593`
- `risk_on_high->commodity_4h` score `1.698` n `52` status `ready` deltaP `23.546` edge `0.0195` maxDD `-0.1313`
- `risk_on_and_context->commodity_4h` score `1.698` n `52` status `ready` deltaP `23.546` edge `0.0195` maxDD `-0.1313`
- `market_context_high->commodity_4h` score `1.5977` n `149` status `ready` deltaP `20.0483` edge `0.0413` maxDD `-0.345`
- `market_context_high->commodity_1h` score `0.7227` n `149` status `ready` deltaP `12.4684` edge `0.0148` maxDD `-0.3491`
- `news_risk_high->index_4h` score `0.7059` n `78` status `ready` deltaP `17.421` edge `0.0372` maxDD `-0.6935`
- `market_context_high->fx_4h` score `0.2038` n `149` status `ready` deltaP `10.0384` edge `0.0068` maxDD `-0.1412`
- `risk_on_high->metal_1h` score `0.1856` n `52` status `ready` deltaP `7.1626` edge `0.0066` maxDD `-0.1115`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
