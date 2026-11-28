# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-28T07:52:28.949044+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `3724`

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

- `news_risk_high->unknown_1h` score `3353.8309` n `31` status `ready` deltaP `1.4825` edge `279.4936` maxDD `-0.7395`
- `news_risk_high->unknown_4h` score `3239.2113` n `31` status `ready` deltaP `3.634` edge `269.9157` maxDD `-0.1191`
- `news_risk_high->crypto_major_24h` score `20.6838` n `31` status `ready` deltaP `32.0624` edge `1.5099` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `14.629` n `31` status `ready` deltaP `29.9827` edge `1.0192` maxDD `0.0`
- `news_risk_high->equity_24h` score `11.8337` n `31` status `ready` deltaP `25.4766` edge `0.8163` maxDD `0.0`
- `news_risk_high->crypto_alt_4h` score `7.9721` n `31` status `ready` deltaP `20.8153` edge `0.6126` maxDD `-5.2957`
- `news_risk_high->equity_4h` score `5.2141` n `31` status `ready` deltaP `28.8405` edge `0.2903` maxDD `-2.178`
- `news_risk_high->crypto_major_4h` score `4.9134` n `31` status `ready` deltaP `14.7964` edge `0.673` maxDD `-7.6714`
- `news_risk_high->fx_24h` score `4.8431` n `31` status `ready` deltaP `39.5427` edge `0.1528` maxDD `-0.0262`
- `news_risk_high->metal_24h` score `3.5643` n `31` status `ready` deltaP `13.9208` edge `0.2317` maxDD `-0.1986`
- `news_risk_high->index_4h` score `2.2847` n `31` status `ready` deltaP `28.2308` edge `0.0282` maxDD `-0.4146`
- `news_risk_high->index_1h` score `2.2744` n `31` status `ready` deltaP `27.9506` edge `0.0117` maxDD `-0.0136`
- `news_risk_high->index_24h` score `2.2679` n `31` status `ready` deltaP `25.3033` edge `0.0203` maxDD `0.0`
- `news_risk_high->equity_1h` score `2.0933` n `31` status `ready` deltaP `13.8497` edge `0.1008` maxDD `-0.1621`
- `news_risk_high->crypto_major_1h` score `1.7985` n `31` status `ready` deltaP `5.5196` edge `0.2399` maxDD `-1.6897`
- `news_risk_high->crypto_alt_1h` score `1.6415` n `31` status `ready` deltaP `8.3639` edge `0.1904` maxDD `-1.5232`
- `news_risk_high->metal_1h` score `1.0889` n `31` status `ready` deltaP `23.8941` edge `0.0082` maxDD `-0.2315`
- `market_context_high->equity_1h` score `0.5476` n `36` status `ready` deltaP `12.7745` edge `0.0259` maxDD `-1.2685`
- `news_risk_high->commodity_4h` score `0.308` n `31` status `ready` deltaP `8.0645` edge `0.0255` maxDD `-0.5151`
- `news_risk_high->metal_4h` score `0.2948` n `31` status `ready` deltaP `10.833` edge `0.0213` maxDD `-0.7918`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
