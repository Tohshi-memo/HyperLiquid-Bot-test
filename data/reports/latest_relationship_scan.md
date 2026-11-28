# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-28T00:22:26.853061+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `2814`

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

- `news_risk_high->unknown_1h` score `3309.6097` n `31` status `ready` deltaP `1.6322` edge `275.8075` maxDD `-0.7395`
- `news_risk_high->unknown_4h` score `3168.6041` n `31` status `ready` deltaP `3.3291` edge `264.0338` maxDD `-0.1191`
- `news_risk_high->crypto_major_24h` score `17.4998` n `31` status `ready` deltaP `27.9029` edge `1.2723` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `12.272` n `31` status `ready` deltaP `26.1698` edge `0.8482` maxDD `0.0`
- `news_risk_high->equity_24h` score `11.6921` n `31` status `ready` deltaP `23.9168` edge `0.8149` maxDD `0.0`
- `news_risk_high->crypto_alt_4h` score `7.8173` n `31` status `ready` deltaP `19.9006` edge `0.6058` maxDD `-5.2957`
- `news_risk_high->equity_4h` score `5.3405` n `31` status `ready` deltaP `29.1454` edge `0.2988` maxDD `-2.178`
- `news_risk_high->crypto_major_4h` score `4.9621` n `31` status `ready` deltaP `14.3391` edge `0.6823` maxDD `-7.6714`
- `news_risk_high->fx_24h` score `4.697` n `31` status `ready` deltaP `38.6762` edge `0.1464` maxDD `-0.0262`
- `news_risk_high->metal_24h` score `3.4556` n `31` status `ready` deltaP `12.1877` edge `0.2342` maxDD `-0.1986`
- `news_risk_high->index_4h` score `2.2945` n `31` status `ready` deltaP `28.3832` edge `0.028` maxDD `-0.4146`
- `news_risk_high->index_1h` score `2.2636` n `31` status `ready` deltaP `27.8009` edge `0.0118` maxDD `-0.0136`
- `news_risk_high->equity_1h` score `2.2454` n `31` status `ready` deltaP `15.197` edge `0.1045` maxDD `-0.1621`
- `news_risk_high->index_24h` score `2.1764` n `31` status `ready` deltaP `24.6101` edge `0.0173` maxDD `0.0`
- `news_risk_high->crypto_major_1h` score `1.8858` n `31` status `ready` deltaP `5.6693` edge `0.2501` maxDD `-1.6897`
- `news_risk_high->crypto_alt_1h` score `1.6486` n `31` status `ready` deltaP `8.0645` edge `0.1933` maxDD `-1.5232`
- `news_risk_high->metal_1h` score `1.1247` n `31` status `ready` deltaP `24.4929` edge `0.0088` maxDD `-0.2315`
- `news_risk_high->commodity_4h` score `0.3438` n `31` status `ready` deltaP `8.8267` edge `0.025` maxDD `-0.5151`
- `news_risk_high->metal_4h` score `0.2955` n `31` status `ready` deltaP `10.833` edge `0.0214` maxDD `-0.7918`
- `news_risk_high->commodity_1h` score `-0.3771` n `31` status `ready` deltaP `-2.5111` edge `0.0115` maxDD `-0.0947`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
