# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-13T02:22:38.575412+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11840`

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

- `news_risk_high->equity_4h` score `7.1354` n `36` status `ready` deltaP `38.5671` edge `0.3375` maxDD `0.0`
- `risk_on_high->commodity_4h` score `2.2853` n `32` status `ready` deltaP `15.7774` edge `0.1035` maxDD `-0.1258`
- `risk_on_and_context->commodity_4h` score `2.2853` n `32` status `ready` deltaP `15.7774` edge `0.1035` maxDD `-0.1258`
- `risk_on_high->commodity_24h` score `2.255` n `32` status `ready` deltaP `19.0972` edge `0.0606` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `2.255` n `32` status `ready` deltaP `19.0972` edge `0.0606` maxDD `0.0`
- `news_risk_high->index_4h` score `2.095` n `36` status `ready` deltaP `23.4248` edge `0.0316` maxDD `-0.0546`
- `risk_on_high->crypto_major_24h` score `2.0458` n `32` status `ready` deltaP `15.9722` edge `0.2714` maxDD `-6.2481`
- `risk_on_and_context->crypto_major_24h` score `2.0458` n `32` status `ready` deltaP `15.9722` edge `0.2714` maxDD `-6.2481`
- `risk_on_high->fx_24h` score `1.7924` n `32` status `ready` deltaP `19.9653` edge `0.0347` maxDD `-0.1418`
- `risk_on_and_context->fx_24h` score `1.7924` n `32` status `ready` deltaP `19.9653` edge `0.0347` maxDD `-0.1418`
- `news_risk_high->equity_1h` score `1.617` n `36` status `ready` deltaP `8.2835` edge `0.1114` maxDD `-0.5496`
- `risk_on_high->commodity_1h` score `1.1628` n `32` status `ready` deltaP `12.762` edge `0.0351` maxDD `-0.1957`
- `risk_on_and_context->commodity_1h` score `1.1628` n `32` status `ready` deltaP `12.762` edge `0.0351` maxDD `-0.1957`
- `market_context_high->commodity_4h` score `1.1037` n `161` status `ready` deltaP `13.4288` edge `0.0663` maxDD `-2.1077`
- `risk_on_high->fx_4h` score `1.068` n `32` status `ready` deltaP `12.2713` edge `0.0213` maxDD `-0.1285`
- `risk_on_and_context->fx_4h` score `1.068` n `32` status `ready` deltaP `12.2713` edge `0.0213` maxDD `-0.1285`
- `market_context_high->commodity_1h` score `0.8889` n `161` status `ready` deltaP `11.0927` edge `0.0298` maxDD `-0.3742`
- `market_context_high->commodity_24h` score `0.286` n `161` status `ready` deltaP `9.1593` edge `0.0431` maxDD `-2.4263`
- `risk_on_high->index_1h` score `0.2509` n `32` status `ready` deltaP `9.2066` edge `0.0083` maxDD `-0.3343`
- `risk_on_and_context->index_1h` score `0.2509` n `32` status `ready` deltaP `9.2066` edge `0.0083` maxDD `-0.3343`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
