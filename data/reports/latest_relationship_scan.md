# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-13T13:22:25.885868+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `13342`

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

- `market_context_high->unknown_24h` score `18098.0381` n `56` status `ready` deltaP `10.2093` edge `1508.1213` maxDD `-0.5614`
- `news_risk_high->unknown_1h` score `414.0086` n `82` status `ready` deltaP `-4.6517` edge `34.5739` maxDD `-1.7068`
- `news_risk_high->crypto_major_24h` score `18.1246` n `82` status `ready` deltaP `37.8512` edge `1.4051` maxDD `-9.098`
- `news_risk_high->crypto_alt_24h` score `18.1238` n `82` status `ready` deltaP `34.3061` edge `1.3304` maxDD `-2.2369`
- `news_risk_high->equity_24h` score `8.1751` n `82` status `ready` deltaP `23.6501` edge `0.7016` maxDD `-6.5742`
- `news_risk_high->index_24h` score `6.727` n `82` status `ready` deltaP `47.767` edge `0.2598` maxDD `-0.0797`
- `market_context_high->crypto_alt_24h` score `6.5174` n `56` status `ready` deltaP `22.8079` edge `0.7675` maxDD `-4.0528`
- `news_risk_high->metal_24h` score `4.5636` n `82` status `ready` deltaP `24.2431` edge `0.2641` maxDD `-0.6334`
- `market_context_high->equity_24h` score `4.3886` n `56` status `ready` deltaP `39.8522` edge `0.4563` maxDD `-10.0809`
- `market_context_high->commodity_24h` score `4.0598` n `56` status `ready` deltaP `39.8276` edge `0.0728` maxDD `0.0`
- `market_context_high->index_24h` score `2.5515` n `56` status `ready` deltaP `45.7636` edge `0.0756` maxDD `-1.6193`
- `market_context_high->metal_24h` score `1.5023` n `56` status `ready` deltaP `17.0567` edge `0.1278` maxDD `-0.9124`
- `risk_on_high->crypto_alt_4h` score `0.4901` n `65` status `ready` deltaP `11.2195` edge `0.1555` maxDD `-6.7304`
- `risk_on_and_context->crypto_alt_4h` score `0.4901` n `65` status `ready` deltaP `11.2195` edge `0.1555` maxDD `-6.7304`
- `news_risk_high->index_4h` score `0.4164` n `82` status `ready` deltaP `12.3475` edge `0.0339` maxDD `-0.6935`
- `risk_on_high->fx_1h` score `0.1101` n `65` status `ready` deltaP `4.7029` edge `0.0034` maxDD `-0.0464`
- `risk_on_and_context->fx_1h` score `0.1101` n `65` status `ready` deltaP `4.7029` edge `0.0034` maxDD `-0.0464`
- `risk_on_high->metal_1h` score `-0.0233` n `65` status `ready` deltaP `4.362` edge `0.002` maxDD `-0.3081`
- `risk_on_and_context->metal_1h` score `-0.0233` n `65` status `ready` deltaP `4.362` edge `0.002` maxDD `-0.3081`
- `market_context_high->fx_1h` score `-0.0556` n `144` status `ready` deltaP `3.7841` edge `-0.0007` maxDD `-0.5323`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
