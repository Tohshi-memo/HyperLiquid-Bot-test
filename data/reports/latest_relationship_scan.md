# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-26T10:37:28.081669+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `3455`

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

- `news_risk_high->unknown_4h` score `3243.2431` n `31` status `ready` deltaP `3.4815` edge `270.2527` maxDD `-0.1191`
- `news_risk_high->unknown_1h` score `3233.1661` n `31` status `ready` deltaP `1.4825` edge `269.4382` maxDD `-0.7395`
- `market_context_high->unknown_1h` score `102.8743` n `31` status `ready` deltaP `1.4825` edge `8.5724` maxDD `-0.4209`
- `news_risk_high->equity_24h` score `37.2912` n `31` status `ready` deltaP `44.4444` edge `2.8113` maxDD `0.0`
- `news_risk_high->crypto_major_24h` score `36.7942` n `31` status `ready` deltaP `45.3125` edge `2.7641` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `31.1106` n `31` status `ready` deltaP `44.6181` edge `2.2951` maxDD `0.0`
- `news_risk_high->crypto_alt_4h` score `11.046` n `31` status `ready` deltaP `27.9799` edge `0.821` maxDD `-5.2957`
- `news_risk_high->equity_4h` score `10.8246` n `31` status `ready` deltaP `39.5112` edge `0.6867` maxDD `-2.178`
- `news_risk_high->metal_24h` score `8.9608` n `31` status `ready` deltaP `30.9924` edge `0.5676` maxDD `-0.1986`
- `news_risk_high->crypto_major_4h` score `7.039` n `31` status `ready` deltaP `19.6744` edge `0.913` maxDD `-7.6714`
- `news_risk_high->index_24h` score `6.1903` n `31` status `ready` deltaP `45.8333` edge `0.2103` maxDD `0.0`
- `news_risk_high->fx_24h` score `5.1243` n `31` status `ready` deltaP `43.4476` edge `0.1502` maxDD `-0.0262`
- `news_risk_high->equity_1h` score `3.8561` n `31` status `ready` deltaP `21.185` edge `0.1988` maxDD `-0.1621`
- `news_risk_high->index_4h` score `3.5829` n `31` status `ready` deltaP `38.4442` edge `0.0683` maxDD `-0.4146`
- `news_risk_high->index_1h` score `2.7884` n `31` status `ready` deltaP `32.8907` edge `0.0216` maxDD `-0.0136`
- `news_risk_high->crypto_major_1h` score `2.4821` n `31` status `ready` deltaP `9.8609` edge `0.2986` maxDD `-1.6897`
- `news_risk_high->crypto_alt_1h` score `2.2744` n `31` status `ready` deltaP `13.0046` edge `0.2406` maxDD `-1.5232`
- `market_context_high->fx_4h` score `2.041` n `31` status `ready` deltaP `26.0474` edge `0.0249` maxDD `-0.2774`
- `news_risk_high->metal_1h` score `1.5126` n `31` status `ready` deltaP `29.5827` edge `0.0246` maxDD `-0.2315`
- `news_risk_high->metal_4h` score `1.0762` n `31` status `ready` deltaP `16.3208` edge `0.0849` maxDD `-0.7918`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
