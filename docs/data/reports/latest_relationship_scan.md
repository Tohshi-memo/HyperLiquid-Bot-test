# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-24T07:37:25.400752+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4584`

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

- `market_context_high->unknown_1h` score `32334.9638` n `45` status `ready` deltaP `1.7165` edge `2694.5783` maxDD `-0.4206`
- `market_context_high->unknown_4h` score `22201.4114` n `45` status `ready` deltaP `2.2629` edge `1850.1164` maxDD `-0.7759`
- `news_risk_high->unknown_1h` score `1125.4345` n `31` status `ready` deltaP `1.9316` edge `93.7909` maxDD `-0.7389`
- `news_risk_high->unknown_4h` score `966.0583` n `31` status `ready` deltaP `3.4815` edge `80.4873` maxDD `-0.119`
- `news_risk_high->crypto_major_24h` score `35.0679` n `31` status `ready` deltaP `46.3542` edge `2.6133` maxDD `0.0`
- `news_risk_high->equity_24h` score `34.9646` n `31` status `ready` deltaP `41.4931` edge `2.6371` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `30.4409` n `31` status `ready` deltaP `44.2708` edge `2.2416` maxDD `0.0`
- `news_risk_high->metal_24h` score `11.5149` n `31` status `ready` deltaP `41.4091` edge `0.711` maxDD `-0.1986`
- `news_risk_high->crypto_alt_4h` score `10.2996` n `31` status `ready` deltaP `22.3397` edge `0.7964` maxDD `-5.2957`
- `news_risk_high->equity_4h` score `8.5347` n `31` status `ready` deltaP `30.5173` edge `0.556` maxDD `-2.1911`
- `news_risk_high->fx_24h` score `6.6903` n `31` status `ready` deltaP `56.4684` edge `0.1939` maxDD `-0.0262`
- `news_risk_high->crypto_major_4h` score `6.4643` n `31` status `ready` deltaP `13.272` edge `0.882` maxDD `-7.6714`
- `news_risk_high->index_24h` score `5.2958` n `31` status `ready` deltaP `39.0625` edge `0.1809` maxDD `0.0`
- `news_risk_high->equity_1h` score `3.2169` n `31` status `ready` deltaP `17.7419` edge `0.1685` maxDD `-0.163`
- `market_context_high->fx_4h` score `3.0456` n `45` status `ready` deltaP `36.4905` edge `0.039` maxDD `-0.2774`
- `news_risk_high->index_4h` score `2.667` n `31` status `ready` deltaP `29.7551` edge `0.0499` maxDD `-0.4146`
- `news_risk_high->crypto_major_1h` score `2.4937` n `31` status `ready` deltaP `10.7591` edge `0.2941` maxDD `-1.6897`
- `news_risk_high->index_1h` score `2.4602` n `31` status `ready` deltaP `29.4476` edge `0.0172` maxDD `-0.0136`
- `news_risk_high->crypto_alt_1h` score `2.1007` n `31` status `ready` deltaP `10.31` edge `0.2363` maxDD `-1.5232`
- `news_risk_high->metal_1h` score `1.6248` n `31` status `ready` deltaP `30.93` edge `0.03` maxDD `-0.2315`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
