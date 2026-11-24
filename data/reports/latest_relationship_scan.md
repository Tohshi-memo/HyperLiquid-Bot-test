# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-24T07:52:29.014585+00:00`
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

- `market_context_high->unknown_1h` score `32334.7395` n `45` status `ready` deltaP `1.5668` edge `2694.5606` maxDD `-0.4206`
- `market_context_high->unknown_4h` score `22200.0518` n `45` status `ready` deltaP `2.2629` edge `1850.0031` maxDD `-0.7759`
- `news_risk_high->unknown_1h` score `1125.2101` n `31` status `ready` deltaP `1.7819` edge `93.7732` maxDD `-0.7389`
- `news_risk_high->unknown_4h` score `964.6987` n `31` status `ready` deltaP `3.4815` edge `80.374` maxDD `-0.119`
- `news_risk_high->crypto_major_24h` score `35.1058` n `31` status `ready` deltaP `46.5278` edge `2.6153` maxDD `0.0`
- `news_risk_high->equity_24h` score `34.901` n `31` status `ready` deltaP `41.4931` edge `2.6318` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `30.4433` n `31` status `ready` deltaP `44.2708` edge `2.2418` maxDD `0.0`
- `news_risk_high->metal_24h` score `11.4993` n `31` status `ready` deltaP `41.4091` edge `0.7097` maxDD `-0.1986`
- `news_risk_high->crypto_alt_4h` score `10.2888` n `31` status `ready` deltaP `22.3397` edge `0.7955` maxDD `-5.2957`
- `news_risk_high->equity_4h` score `8.5589` n `31` status `ready` deltaP `30.6698` edge `0.557` maxDD `-2.1911`
- `news_risk_high->fx_24h` score `6.6927` n `31` status `ready` deltaP `56.4684` edge `0.1941` maxDD `-0.0262`
- `news_risk_high->crypto_major_4h` score `6.4627` n `31` status `ready` deltaP `13.272` edge `0.8818` maxDD `-7.6714`
- `news_risk_high->index_24h` score `5.2838` n `31` status `ready` deltaP `39.0625` edge `0.1799` maxDD `0.0`
- `news_risk_high->equity_1h` score `3.2193` n `31` status `ready` deltaP `17.7419` edge `0.1687` maxDD `-0.163`
- `market_context_high->fx_4h` score `3.0322` n `45` status `ready` deltaP `36.3381` edge `0.0389` maxDD `-0.2774`
- `news_risk_high->index_4h` score `2.6804` n `31` status `ready` deltaP `29.9076` edge `0.05` maxDD `-0.4146`
- `news_risk_high->crypto_major_1h` score `2.4945` n `31` status `ready` deltaP `10.7591` edge `0.2942` maxDD `-1.6897`
- `news_risk_high->index_1h` score `2.4614` n `31` status `ready` deltaP `29.4476` edge `0.0173` maxDD `-0.0136`
- `news_risk_high->crypto_alt_1h` score `2.1031` n `31` status `ready` deltaP `10.31` edge `0.2366` maxDD `-1.5232`
- `news_risk_high->metal_1h` score `1.6248` n `31` status `ready` deltaP `30.93` edge `0.03` maxDD `-0.2315`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
