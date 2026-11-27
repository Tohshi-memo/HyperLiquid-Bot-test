# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-27T01:22:25.646165+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `3540`

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

- `news_risk_high->unknown_1h` score `3210.786` n `31` status `ready` deltaP `1.7819` edge `267.5712` maxDD `-0.7395`
- `news_risk_high->unknown_4h` score `3175.173` n `31` status `ready` deltaP `4.3962` edge `264.5741` maxDD `-0.1191`
- `news_risk_high->crypto_major_24h` score `26.3682` n `31` status `ready` deltaP `35.2431` edge `1.9624` maxDD `0.0`
- `news_risk_high->equity_24h` score `23.5162` n `31` status `ready` deltaP `34.7222` edge `1.7282` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `20.2544` n `31` status `ready` deltaP `34.375` edge `1.4587` maxDD `0.0`
- `news_risk_high->crypto_alt_4h` score `9.5094` n `31` status `ready` deltaP `23.7116` edge `0.7214` maxDD `-5.2957`
- `news_risk_high->equity_4h` score `8.2483` n `31` status `ready` deltaP `34.9381` edge `0.5025` maxDD `-2.178`
- `news_risk_high->crypto_major_4h` score `6.2316` n `31` status `ready` deltaP `16.7781` edge `0.8288` maxDD `-7.6714`
- `news_risk_high->metal_24h` score `6.2137` n `31` status `ready` deltaP `22.1383` edge `0.3977` maxDD `-0.1986`
- `news_risk_high->fx_24h` score `4.9592` n `31` status `ready` deltaP `42.0587` edge `0.1457` maxDD `-0.0262`
- `news_risk_high->index_24h` score `4.1724` n `31` status `ready` deltaP `36.2847` edge `0.1058` maxDD `0.0`
- `news_risk_high->equity_1h` score `3.0394` n `31` status `ready` deltaP `17.8916` edge `0.1527` maxDD `-0.1621`
- `news_risk_high->index_4h` score `2.9171` n `31` status `ready` deltaP `32.9564` edge `0.0494` maxDD `-0.4146`
- `news_risk_high->index_1h` score `2.5524` n `31` status `ready` deltaP `30.6452` edge `0.0169` maxDD `-0.0136`
- `news_risk_high->crypto_major_1h` score `2.2148` n `31` status `ready` deltaP `7.6154` edge `0.2793` maxDD `-1.6897`
- `news_risk_high->crypto_alt_1h` score `1.9829` n `31` status `ready` deltaP `10.6094` edge `0.2192` maxDD `-1.5232`
- `news_risk_high->metal_1h` score `1.2922` n `31` status `ready` deltaP `26.7384` edge `0.0153` maxDD `-0.2315`
- `news_risk_high->metal_4h` score `0.5975` n `31` status `ready` deltaP `12.8147` edge `0.0469` maxDD `-0.7918`
- `news_risk_high->commodity_4h` score `0.1934` n `31` status `ready` deltaP `8.9791` edge `0.0047` maxDD `-0.5151`
- `news_risk_high->commodity_1h` score `-0.5257` n `31` status `ready` deltaP `-3.559` edge `0.0061` maxDD `-0.0947`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
