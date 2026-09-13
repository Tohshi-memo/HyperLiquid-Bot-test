# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-13T01:52:26.610259+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `12553`

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

- `market_context_high->unknown_24h` score `16590.1094` n `59` status `ready` deltaP `12.0616` edge `1382.4339` maxDD `-0.082`
- `news_risk_high->unknown_1h` score `379.5436` n `82` status `ready` deltaP `-5.6996` edge `31.7088` maxDD `-1.7068`
- `news_risk_high->crypto_alt_24h` score `18.1411` n `82` status `ready` deltaP `32.7532` edge `1.3422` maxDD `-2.2369`
- `news_risk_high->crypto_major_24h` score `18.0476` n `82` status `ready` deltaP `39.4987` edge `1.3877` maxDD `-9.098`
- `market_context_high->equity_24h` score `10.459` n `59` status `ready` deltaP `46.5278` edge `0.5614` maxDD `0.0`
- `market_context_high->crypto_alt_24h` score `10.2426` n `59` status `ready` deltaP `22.7078` edge `0.7849` maxDD `-3.9523`
- `news_risk_high->equity_24h` score `6.2019` n `82` status `ready` deltaP `16.04` edge `0.5879` maxDD `-6.5742`
- `news_risk_high->index_24h` score `6.1125` n `82` status `ready` deltaP `42.306` edge `0.245` maxDD `-0.0797`
- `news_risk_high->metal_24h` score `4.9926` n `82` status `ready` deltaP `28.0446` edge `0.2745` maxDD `-0.6334`
- `market_context_high->commodity_24h` score `4.2517` n `59` status `ready` deltaP `42.3611` edge `0.0719` maxDD `0.0`
- `market_context_high->index_24h` score `3.9912` n `59` status `ready` deltaP `42.9055` edge `0.0858` maxDD `-0.1391`
- `market_context_high->metal_24h` score `0.3541` n `59` status `ready` deltaP `8.8424` edge `0.1062` maxDD `-2.9132`
- `risk_on_high->crypto_alt_4h` score `0.2114` n `53` status `ready` deltaP `7.9758` edge `0.1414` maxDD `-6.7304`
- `risk_on_and_context->crypto_alt_4h` score `0.2114` n `53` status `ready` deltaP `7.9758` edge `0.1414` maxDD `-6.7304`
- `news_risk_high->index_4h` score `0.1579` n `82` status `ready` deltaP `8.2317` edge `0.0282` maxDD `-0.6935`
- `risk_on_high->metal_1h` score `0.1042` n `55` status `ready` deltaP `6.791` edge `0.0011` maxDD `-0.3081`
- `risk_on_and_context->metal_1h` score `0.1042` n `55` status `ready` deltaP `6.791` edge `0.0011` maxDD `-0.3081`
- `risk_on_high->index_1h` score `-0.1656` n `55` status `ready` deltaP `3.9467` edge `0.0005` maxDD `-0.177`
- `risk_on_and_context->index_1h` score `-0.1656` n `55` status `ready` deltaP `3.9467` edge `0.0005` maxDD `-0.177`
- `risk_on_high->fx_1h` score `-0.1786` n `55` status `ready` deltaP `-0.0327` edge `0.0029` maxDD `-0.0464`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
