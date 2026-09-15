# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-15T16:22:33.357771+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `10887`

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

- `news_risk_high->unknown_4h` score `396.2385` n `78` status `ready` deltaP `-23.6749` edge `33.2671` maxDD `-4.1517`
- `news_risk_high->unknown_24h` score `23.6016` n `78` status `ready` deltaP `21.1806` edge `1.8256` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `22.893` n `78` status `ready` deltaP `47.7698` edge `1.6284` maxDD `-1.4626`
- `news_risk_high->crypto_major_24h` score `18.1794` n `78` status `ready` deltaP `39.5566` edge `1.3983` maxDD `-9.098`
- `news_risk_high->equity_24h` score `15.3437` n `78` status `ready` deltaP `49.8531` edge `1.1237` maxDD `-6.5262`
- `news_risk_high->index_24h` score `8.4213` n `78` status `ready` deltaP `59.6821` edge `0.3215` maxDD `-0.075`
- `news_risk_high->metal_24h` score `6.4985` n `78` status `ready` deltaP `37.7938` edge `0.335` maxDD `-0.6334`
- `risk_on_high->commodity_24h` score `6.0388` n `52` status `ready` deltaP `38.1944` edge `0.2486` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `6.0388` n `52` status `ready` deltaP `38.1944` edge `0.2486` maxDD `0.0`
- `market_context_high->commodity_24h` score `4.7418` n `137` status `ready` deltaP `30.8951` edge `0.2417` maxDD `-0.8682`
- `risk_on_high->fx_24h` score `3.2236` n `52` status `ready` deltaP `38.8755` edge `0.0137` maxDD `-0.0054`
- `risk_on_and_context->fx_24h` score `3.2236` n `52` status `ready` deltaP `38.8755` edge `0.0137` maxDD `-0.0054`
- `market_context_high->fx_24h` score `2.8266` n `137` status `ready` deltaP `35.6891` edge `0.0192` maxDD `-0.0593`
- `risk_on_high->commodity_4h` score `1.6436` n `52` status `ready` deltaP `23.2411` edge `0.017` maxDD `-0.1313`
- `risk_on_and_context->commodity_4h` score `1.6436` n `52` status `ready` deltaP `23.2411` edge `0.017` maxDD `-0.1313`
- `market_context_high->commodity_4h` score `1.5433` n `149` status `ready` deltaP `19.7434` edge `0.0388` maxDD `-0.345`
- `news_risk_high->index_4h` score `0.7422` n `78` status `ready` deltaP `17.8784` edge `0.0388` maxDD `-0.6935`
- `market_context_high->commodity_1h` score `0.6568` n `149` status `ready` deltaP `11.8696` edge `0.0133` maxDD `-0.3491`
- `risk_on_high->metal_1h` score `0.184` n `52` status `ready` deltaP `7.1626` edge `0.0064` maxDD `-0.1115`
- `risk_on_and_context->metal_1h` score `0.184` n `52` status `ready` deltaP `7.1626` edge `0.0064` maxDD `-0.1115`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
