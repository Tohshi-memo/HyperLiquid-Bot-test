# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-30T06:07:27.740468+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `7442`

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

- `news_risk_high->unknown_24h` score `1295.0476` n `135` status `ready` deltaP `1.9097` edge `107.9079` maxDD `0.0`
- `market_context_high->unknown_1h` score `838.0964` n `30` status `ready` deltaP `9.8802` edge `69.7755` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `18.6782` n `135` status `ready` deltaP `28.9004` edge `1.3848` maxDD `-1.0093`
- `news_risk_high->equity_24h` score `8.503` n `135` status `ready` deltaP `28.9005` edge `0.7508` maxDD `-9.4579`
- `news_risk_high->crypto_major_24h` score `7.9953` n `135` status `ready` deltaP `23.9931` edge `0.8217` maxDD `-15.8971`
- `news_risk_high->index_24h` score `3.9437` n `135` status `ready` deltaP `35.0926` edge `0.1425` maxDD `-0.4916`
- `news_risk_high->metal_24h` score `3.6131` n `135` status `ready` deltaP `27.2685` edge `0.2467` maxDD `-2.192`
- `news_risk_high->equity_4h` score `3.0126` n `135` status `ready` deltaP `30.0858` edge `0.2106` maxDD `-9.143`
- `news_risk_high->crypto_alt_4h` score `1.9796` n `135` status `ready` deltaP `11.5696` edge `0.3538` maxDD `-15.9436`
- `market_context_high->crypto_alt_1h` score `1.9264` n `30` status `ready` deltaP `16.2176` edge `0.2003` maxDD `-3.5821`
- `market_context_high->crypto_major_1h` score `1.5233` n `30` status `ready` deltaP `11.008` edge `0.1829` maxDD `-3.546`
- `market_context_high->fx_1h` score `1.2454` n `30` status `ready` deltaP `17.8243` edge `0.0072` maxDD `-0.113`
- `news_risk_high->crypto_alt_1h` score `1.1341` n `135` status `ready` deltaP `9.5509` edge `0.1219` maxDD `-4.2849`
- `news_risk_high->equity_1h` score `0.9595` n `135` status `ready` deltaP `9.8503` edge `0.0766` maxDD `-1.6514`
- `market_context_high->equity_1h` score `0.8694` n `30` status `ready` deltaP `13.1836` edge `0.0661` maxDD `-2.4027`
- `news_risk_high->index_1h` score `0.558` n `135` status `ready` deltaP `9.5664` edge `0.0115` maxDD `-0.302`
- `market_context_high->index_1h` score `0.0812` n `30` status `ready` deltaP `4.3812` edge `0.0149` maxDD `-0.3627`
- `market_context_high->metal_1h` score `-0.0583` n `30` status `ready` deltaP `1.008` edge `0.0079` maxDD `-0.4338`
- `news_risk_high->index_4h` score `-0.0591` n `135` status `ready` deltaP `7.7111` edge `0.029` maxDD `-1.493`
- `news_risk_high->metal_1h` score `-0.4994` n `135` status `ready` deltaP `1.008` edge `0.0146` maxDD `-0.7016`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
