# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-28T14:22:41.772849+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `7444`

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

- `news_risk_high->unknown_1h` score `3413.6256` n `31` status `ready` deltaP `2.231` edge `284.4715` maxDD `-0.7395`
- `news_risk_high->unknown_4h` score `3235.9521` n `31` status `ready` deltaP `3.634` edge `269.6441` maxDD `-0.1191`
- `news_risk_high->crypto_major_24h` score `24.4091` n `31` status `ready` deltaP `36.5685` edge `1.7903` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `18.2079` n `31` status `ready` deltaP `34.4887` edge `1.2874` maxDD `0.0`
- `news_risk_high->equity_24h` score `13.0808` n `31` status `ready` deltaP `29.2894` edge `0.8948` maxDD `0.0`
- `news_risk_high->crypto_alt_4h` score `9.3048` n `31` status `ready` deltaP `24.1689` edge `0.7013` maxDD `-5.2957`
- `news_risk_high->crypto_major_4h` score `5.9171` n `31` status `ready` deltaP `18.4549` edge `0.7773` maxDD `-7.6714`
- `news_risk_high->equity_4h` score `5.8038` n `31` status `ready` deltaP `32.0417` edge `0.3181` maxDD `-2.178`
- `news_risk_high->fx_24h` score `5.0876` n `31` status `ready` deltaP `41.969` edge `0.157` maxDD `-0.0262`
- `news_risk_high->metal_24h` score `3.965` n `31` status `ready` deltaP `17.0403` edge `0.2443` maxDD `-0.1986`
- `news_risk_high->index_4h` score `2.6036` n `31` status `ready` deltaP `31.7369` edge `0.0314` maxDD `-0.4146`
- `news_risk_high->index_24h` score `2.4561` n `31` status `ready` deltaP `26.5165` edge `0.0279` maxDD `0.0`
- `news_risk_high->index_1h` score `2.381` n `31` status `ready` deltaP `29.1482` edge `0.0126` maxDD `-0.0136`
- `news_risk_high->equity_1h` score `2.2827` n `31` status `ready` deltaP `15.0473` edge `0.1086` maxDD `-0.1621`
- `news_risk_high->crypto_major_1h` score `2.1314` n `31` status `ready` deltaP `7.4657` edge `0.2696` maxDD `-1.6897`
- `news_risk_high->crypto_alt_1h` score `1.9759` n `31` status `ready` deltaP `10.9088` edge `0.2163` maxDD `-1.5232`
- `news_risk_high->metal_1h` score `1.1621` n `31` status `ready` deltaP `25.0917` edge `0.0096` maxDD `-0.2315`
- `market_context_high->metal_4h` score `0.7825` n `50` status `ready` deltaP `12.4573` edge `0.0233` maxDD `-0.2914`
- `news_risk_high->commodity_4h` score `0.4576` n `31` status `ready` deltaP `10.656` edge `0.0274` maxDD `-0.5151`
- `news_risk_high->metal_4h` score `0.3696` n `31` status `ready` deltaP `11.7476` edge `0.0248` maxDD `-0.7918`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
