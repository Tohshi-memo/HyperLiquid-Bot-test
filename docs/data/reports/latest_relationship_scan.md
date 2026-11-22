# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-22T14:07:28.511794+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `40`

- Symbol pattern count: `4008`

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

- `market_context_high->unknown_1h` score `12037.3112` n `106` status `ready` deltaP `-0.3927` edge `1003.1317` maxDD `-0.9188`
- `market_context_high->unknown_4h` score `7514.2765` n `106` status `ready` deltaP `-2.5742` edge `626.2374` maxDD `-0.7759`
- `news_risk_high->unknown_1h` score `1416.9489` n `31` status `ready` deltaP `4.4765` edge `118.0668` maxDD `-0.7389`
- `news_risk_high->unknown_4h` score `1264.4181` n `31` status `ready` deltaP `3.634` edge `105.3496` maxDD `-0.119`
- `news_risk_high->equity_4h` score `11.9382` n `31` status `ready` deltaP `40.121` edge `0.7756` maxDD `-2.1911`
- `news_risk_high->crypto_alt_4h` score `10.7416` n `31` status `ready` deltaP `23.5592` edge `0.8251` maxDD `-5.2957`
- `news_risk_high->crypto_major_4h` score `6.7042` n `31` status `ready` deltaP `14.7964` edge `0.9026` maxDD `-7.6714`
- `news_risk_high->equity_1h` score `4.0085` n `31` status `ready` deltaP `19.9874` edge `0.2195` maxDD `-0.163`
- `news_risk_high->index_4h` score `3.4804` n `31` status `ready` deltaP `36.1576` edge `0.075` maxDD `-0.4146`
- `news_risk_high->index_1h` score `2.695` n `31` status `ready` deltaP `31.5434` edge `0.0228` maxDD `-0.0136`
- `news_risk_high->crypto_major_1h` score `2.5281` n `31` status `ready` deltaP `9.8609` edge `0.3045` maxDD `-1.6897`
- `news_risk_high->crypto_alt_1h` score `2.1033` n `31` status `ready` deltaP `8.5136` edge `0.2486` maxDD `-1.5232`
- `news_risk_high->metal_4h` score `1.5416` n `31` status `ready` deltaP `20.7415` edge `0.1151` maxDD `-0.7918`
- `news_risk_high->metal_1h` score `1.5151` n `31` status `ready` deltaP `28.5348` edge `0.0319` maxDD `-0.2315`
- `news_risk_high->commodity_4h` score `0.6407` n `31` status `ready` deltaP `15.0767` edge `0.0214` maxDD `-0.5151`
- `news_risk_high->commodity_1h` score `-0.1208` n `31` status `ready` deltaP `0.7823` edge `0.0109` maxDD `-0.0947`
- `market_context_high->metal_1h` score `-0.3285` n `106` status `ready` deltaP `2.4545` edge `0.008` maxDD `-2.6517`
- `market_context_high->index_1h` score `-0.4215` n `106` status `ready` deltaP `1.8416` edge `0.0013` maxDD `-1.2295`
- `market_context_high->fx_1h` score `-1.2239` n `106` status `ready` deltaP `-8.6262` edge `-0.0015` maxDD `-0.4384`
- `market_context_high->fx_4h` score `-1.5346` n `106` status `ready` deltaP `-0.4689` edge `0.0036` maxDD `-1.444`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
