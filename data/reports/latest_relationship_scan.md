# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-28T12:22:21.876508+00:00`
- Price records: `672`
- Market context records: `2141`
- Flow alert records: `8059`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9158`

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

- `market_context_high->crypto_alt_4h` score `13.1675` n `158` status `ready` deltaP `36.7687` edge `0.9458` maxDD `-5.1574`
- `market_context_high->crypto_major_4h` score `11.7636` n `158` status `ready` deltaP `41.0698` edge `0.7595` maxDD `-1.9063`
- `market_context_high->unknown_4h` score `6.5032` n `158` status `ready` deltaP `25.1177` edge `0.4494` maxDD `-2.6599`
- `news_risk_high->commodity_4h` score `6.1492` n `33` status `ready` deltaP `28.0442` edge `0.3926` maxDD `-3.0367`
- `market_context_high->equity_4h` score `4.9938` n `158` status `ready` deltaP `26.6247` edge `0.3481` maxDD `-5.0894`
- `market_context_high->index_24h` score `3.7041` n `157` status `ready` deltaP `15.0323` edge `0.3313` maxDD `-4.1604`
- `market_context_high->crypto_major_1h` score `3.175` n `158` status `ready` deltaP `17.2857` edge `0.2015` maxDD `-2.1721`
- `market_context_high->equity_24h` score `3.1148` n `157` status `ready` deltaP `26.4917` edge `0.5728` maxDD `-33.1875`
- `market_context_high->metal_4h` score `3.0857` n `158` status `ready` deltaP `21.4032` edge `0.2532` maxDD `-4.7664`
- `market_context_high->crypto_alt_1h` score `3.0334` n `158` status `ready` deltaP `15.7887` edge `0.2339` maxDD `-4.9097`
- `market_context_high->index_4h` score `3.0221` n `158` status `ready` deltaP `22.0651` edge `0.1731` maxDD `-1.8022`
- `market_context_high->unknown_24h` score `2.7499` n `157` status `ready` deltaP `27.0148` edge `0.5811` maxDD `-35.8966`
- `news_risk_high->fx_4h` score `2.4455` n `33` status `ready` deltaP `31.6473` edge `0.0112` maxDD `-0.1382`
- `market_context_high->crypto_major_24h` score `2.0014` n `157` status `ready` deltaP `21.8518` edge `0.9695` maxDD `-62.3533`
- `news_risk_high->unknown_4h` score `1.3814` n `33` status `ready` deltaP `17.7338` edge `0.1312` maxDD `-2.7857`
- `news_risk_high->commodity_1h` score `1.3237` n `37` status `ready` deltaP `11.7131` edge `0.1002` maxDD `-2.1052`
- `news_risk_high->unknown_1h` score `1.2912` n `37` status `ready` deltaP `21.9251` edge `0.0042` maxDD `-1.7548`
- `market_context_high->equity_1h` score `0.8059` n `158` status `ready` deltaP `10.0186` edge `0.0792` maxDD `-2.6402`
- `market_context_high->metal_1h` score `0.6206` n `158` status `ready` deltaP `9.0919` edge `0.0581` maxDD `-2.3594`
- `market_context_high->metal_24h` score `0.53` n `157` status `ready` deltaP `12.8207` edge `0.3726` maxDD `-23.2095`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
