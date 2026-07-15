# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-15T01:37:25.450962+00:00`
- Price records: `672`
- Market context records: `6769`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11700`

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

- `market_context_high->unknown_24h` score `1.0472` n `176` status `ready` deltaP `0.5366` edge `0.5059` maxDD `-12.3511`
- `market_context_high->commodity_24h` score `-0.0015` n `176` status `ready` deltaP `8.144` edge `0.1324` maxDD `-5.2791`
- `market_context_high->crypto_major_1h` score `-0.0365` n `176` status `ready` deltaP `7.6518` edge `0.0303` maxDD `-4.2122`
- `market_context_high->crypto_alt_1h` score `-0.2563` n `176` status `ready` deltaP `4.5999` edge `0.0244` maxDD `-3.7803`
- `market_context_high->fx_1h` score `-0.3976` n `176` status `ready` deltaP `-0.4151` edge `0.0003` maxDD `-0.5468`
- `market_context_high->commodity_1h` score `-0.5876` n `176` status `ready` deltaP `0.1463` edge `-0.008` maxDD `-2.1314`
- `market_context_high->index_1h` score `-0.6325` n `176` status `ready` deltaP `-1.4664` edge `0.0001` maxDD `-0.7136`
- `market_context_high->metal_1h` score `-0.7534` n `176` status `ready` deltaP `-5.8894` edge `-0.0048` maxDD `-1.2017`
- `market_context_high->equity_1h` score `-1.1879` n `176` status `ready` deltaP `3.1063` edge `-0.017` maxDD `-3.8827`
- `market_context_high->fx_4h` score `-1.2066` n `176` status `ready` deltaP `7.6913` edge `0.0004` maxDD `-2.1765`
- `market_context_high->index_4h` score `-1.2381` n `176` status `ready` deltaP `6.2916` edge `-0.0127` maxDD `-5.7046`
- `market_context_high->commodity_4h` score `-1.4559` n `176` status `ready` deltaP `-2.2311` edge `-0.0228` maxDD `-5.5853`
- `market_context_high->unknown_1h` score `-1.7633` n `176` status `ready` deltaP `-7.0257` edge `-0.01` maxDD `-3.2083`
- `market_context_high->crypto_major_4h` score `-2.6335` n `176` status `ready` deltaP `3.0488` edge `-0.0265` maxDD `-16.8495`
- `market_context_high->metal_4h` score `-2.7315` n `176` status `ready` deltaP `-7.3864` edge `-0.0149` maxDD `-5.2172`
- `market_context_high->crypto_alt_4h` score `-2.7867` n `176` status `ready` deltaP `1.6075` edge `-0.0278` maxDD `-19.2145`
- `market_context_high->unknown_4h` score `-3.5833` n `176` status `ready` deltaP `-15.5627` edge `0.0417` maxDD `-10.2579`
- `market_context_high->equity_4h` score `-4.2151` n `176` status `ready` deltaP `2.7023` edge `-0.1315` maxDD `-27.1529`
- `market_context_high->fx_24h` score `-4.2813` n `176` status `ready` deltaP `-7.702` edge `-0.0018` maxDD `-5.6237`
- `market_context_high->metal_24h` score `-8.6902` n `176` status `ready` deltaP `-14.8517` edge `-0.1666` maxDD `-28.2147`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
