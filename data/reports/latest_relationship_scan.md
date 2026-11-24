# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-24T16:22:31.840497+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4278`

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

- `market_context_high->unknown_1h` score `32299.2158` n `45` status `ready` deltaP `1.7165` edge `2691.5993` maxDD `-0.4209`
- `market_context_high->unknown_4h` score `22116.6859` n `45` status `ready` deltaP `2.7202` edge `1843.0529` maxDD `-0.7765`
- `news_risk_high->unknown_1h` score `1064.2608` n `31` status `ready` deltaP `1.9316` edge `88.6931` maxDD `-0.7395`
- `news_risk_high->unknown_4h` score `863.7384` n `31` status `ready` deltaP `3.9388` edge `71.9576` maxDD `-0.1191`
- `news_risk_high->crypto_major_24h` score `37.3291` n `31` status `ready` deltaP `49.4792` edge `2.7809` maxDD `0.0`
- `news_risk_high->equity_24h` score `35.1522` n `31` status `ready` deltaP `40.9722` edge `2.6562` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `32.4859` n `31` status `ready` deltaP `47.0486` edge `2.3935` maxDD `0.0`
- `news_risk_high->metal_24h` score `11.0942` n `31` status `ready` deltaP `41.2355` edge `0.6771` maxDD `-0.1986`
- `news_risk_high->crypto_alt_4h` score `11.0414` n `31` status `ready` deltaP `24.3214` edge `0.845` maxDD `-5.2957`
- `news_risk_high->equity_4h` score `9.3412` n `31` status `ready` deltaP `32.8039` edge `0.6078` maxDD `-2.178`
- `news_risk_high->crypto_major_4h` score `6.818` n `31` status `ready` deltaP `15.5586` edge `0.9121` maxDD `-7.6714`
- `news_risk_high->fx_24h` score `6.4124` n `31` status `ready` deltaP `53.8643` edge `0.1881` maxDD `-0.0262`
- `news_risk_high->index_24h` score `5.1924` n `31` status `ready` deltaP `38.7153` edge `0.1746` maxDD `0.0`
- `news_risk_high->equity_1h` score `3.5168` n `31` status `ready` deltaP `18.9395` edge `0.1855` maxDD `-0.1621`
- `news_risk_high->index_4h` score `2.917` n `31` status `ready` deltaP `31.8893` edge `0.0565` maxDD `-0.4146`
- `market_context_high->fx_4h` score `2.9133` n `45` status `ready` deltaP `35.271` edge `0.0361` maxDD `-0.2774`
- `news_risk_high->crypto_major_1h` score `2.6036` n `31` status `ready` deltaP `11.6573` edge `0.3022` maxDD `-1.6897`
- `news_risk_high->index_1h` score `2.5668` n `31` status `ready` deltaP `30.4955` edge `0.0191` maxDD `-0.0136`
- `news_risk_high->crypto_alt_1h` score `2.2746` n `31` status `ready` deltaP `11.3579` edge `0.2516` maxDD `-1.5232`
- `news_risk_high->metal_1h` score `1.6497` n `31` status `ready` deltaP `30.93` edge `0.0332` maxDD `-0.2315`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
