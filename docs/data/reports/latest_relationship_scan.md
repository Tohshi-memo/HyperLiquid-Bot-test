# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-28T10:52:18.069836+00:00`
- Price records: `672`
- Market context records: `2134`
- Flow alert records: `8040`
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

- `market_context_high->crypto_alt_4h` score `13.1807` n `158` status `ready` deltaP `36.7687` edge `0.9469` maxDD `-5.1574`
- `market_context_high->crypto_major_4h` score `11.826` n `158` status `ready` deltaP `41.0698` edge `0.7647` maxDD `-1.9063`
- `market_context_high->unknown_4h` score `6.2899` n `158` status `ready` deltaP `24.3555` edge `0.4367` maxDD `-2.6599`
- `news_risk_high->commodity_4h` score `6.0841` n `31` status `ready` deltaP `26.4801` edge `0.3976` maxDD `-3.0367`
- `market_context_high->equity_4h` score `5.0178` n `158` status `ready` deltaP `26.6247` edge `0.3501` maxDD `-5.0894`
- `market_context_high->index_24h` score `3.4615` n `157` status `ready` deltaP `14.2045` edge `0.3166` maxDD `-4.1604`
- `market_context_high->crypto_major_1h` score `3.2038` n `158` status `ready` deltaP `17.5851` edge `0.2019` maxDD `-2.1721`
- `market_context_high->metal_4h` score `3.0893` n `158` status `ready` deltaP `21.4032` edge `0.2535` maxDD `-4.7664`
- `market_context_high->index_4h` score `3.0449` n `158` status `ready` deltaP `22.0651` edge `0.175` maxDD `-1.8022`
- `news_risk_high->fx_4h` score `3.0318` n `31` status `ready` deltaP `36.9689` edge `0.015` maxDD `-0.0381`
- `market_context_high->crypto_alt_1h` score `2.9927` n `158` status `ready` deltaP `15.4893` edge `0.2325` maxDD `-4.9097`
- `news_risk_high->unknown_1h` score `2.8173` n `33` status `ready` deltaP `30.1715` edge `0.0639` maxDD `-1.7548`
- `market_context_high->equity_24h` score `2.7471` n `157` status `ready` deltaP `25.6309` edge `0.5479` maxDD `-33.1875`
- `market_context_high->unknown_24h` score `2.3783` n `157` status `ready` deltaP `26.1654` edge `0.5558` maxDD `-35.8966`
- `market_context_high->crypto_major_24h` score `1.7688` n `157` status `ready` deltaP `21.6373` edge `0.9411` maxDD `-62.3533`
- `news_risk_high->unknown_4h` score `1.3985` n `31` status `ready` deltaP `18.0468` edge `0.1313` maxDD `-2.7857`
- `news_risk_high->commodity_1h` score `0.8198` n `33` status `ready` deltaP `8.0249` edge `0.0828` maxDD `-2.1052`
- `market_context_high->equity_1h` score `0.7855` n `158` status `ready` deltaP `9.8689` edge `0.0785` maxDD `-2.6402`
- `market_context_high->metal_1h` score `0.5343` n `158` status `ready` deltaP `8.4931` edge `0.0549` maxDD `-2.3594`
- `market_context_high->metal_24h` score `0.3903` n `157` status `ready` deltaP `12.0986` edge `0.3595` maxDD `-23.2095`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
