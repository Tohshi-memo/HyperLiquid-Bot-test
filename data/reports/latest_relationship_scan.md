# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-30T10:07:36.318394+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `7492`

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

- `news_risk_high->unknown_24h` score `526.3144` n `135` status `ready` deltaP `1.9097` edge `43.8468` maxDD `0.0`
- `market_context_high->unknown_1h` score `461.4283` n `46` status `ready` deltaP `7.7063` edge `38.4059` maxDD `-0.0597`
- `market_context_high->unknown_4h` score `386.9097` n `34` status `ready` deltaP `8.2317` edge `32.1876` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `17.1055` n `135` status `ready` deltaP `27.5116` edge `1.263` maxDD `-1.0093`
- `news_risk_high->equity_24h` score `7.3651` n `135` status `ready` deltaP `26.1227` edge `0.6745` maxDD `-9.4579`
- `news_risk_high->crypto_major_24h` score `7.0665` n `135` status `ready` deltaP `23.9931` edge `0.7443` maxDD `-15.8971`
- `news_risk_high->index_24h` score `3.5378` n `135` status `ready` deltaP `32.3148` edge `0.1272` maxDD `-0.4916`
- `news_risk_high->metal_24h` score `3.1377` n `135` status `ready` deltaP `24.4907` edge `0.2256` maxDD `-2.192`
- `market_context_high->fx_4h` score `2.783` n `34` status `ready` deltaP `32.0211` edge `0.0315` maxDD `-0.0449`
- `news_risk_high->equity_4h` score `2.7175` n `135` status `ready` deltaP `28.2565` edge `0.1982` maxDD `-9.143`
- `market_context_high->crypto_alt_1h` score `2.4318` n `46` status `ready` deltaP `13.8701` edge `0.1765` maxDD `-3.6387`
- `market_context_high->crypto_major_4h` score `2.1567` n `34` status `ready` deltaP `5.3802` edge `0.2142` maxDD `-3.294`
- `market_context_high->crypto_major_1h` score `2.0344` n `46` status `ready` deltaP `11.9891` edge `0.1506` maxDD `-3.546`
- `news_risk_high->crypto_alt_4h` score `1.5021` n `135` status `ready` deltaP `9.7403` edge `0.3262` maxDD `-15.9436`
- `market_context_high->fx_1h` score `1.1783` n `46` status `ready` deltaP `17.2351` edge `0.0097` maxDD `-0.113`
- `news_risk_high->crypto_alt_1h` score `0.9675` n `135` status `ready` deltaP `8.6527` edge `0.114` maxDD `-4.2849`
- `news_risk_high->equity_1h` score `0.9056` n `135` status `ready` deltaP `9.4012` edge `0.0751` maxDD `-1.6514`
- `news_risk_high->index_1h` score `0.4826` n `135` status `ready` deltaP `8.6682` edge `0.0112` maxDD `-0.302`
- `market_context_high->equity_1h` score `0.4102` n `46` status `ready` deltaP `5.9229` edge `0.0539` maxDD `-2.4027`
- `market_context_high->metal_4h` score `-0.1583` n `34` status `ready` deltaP `11.8275` edge `-0.0248` maxDD `-2.614`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
