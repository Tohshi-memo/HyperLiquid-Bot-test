# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-21T08:52:26.795231+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `9168`

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

- `market_context_high->unknown_4h` score `33.2665` n `58` status `ready` deltaP `1.23` edge `2.779` maxDD `-0.5326`
- `news_risk_high->crypto_major_24h` score `22.8471` n `101` status `ready` deltaP `10.7484` edge `2.5181` maxDD `-46.1999`
- `news_risk_high->crypto_alt_24h` score `17.5419` n `101` status `ready` deltaP `11.1334` edge `1.8757` maxDD `-32.7147`
- `news_risk_high->crypto_alt_4h` score `4.1463` n `101` status `ready` deltaP `18.3093` edge `0.3444` maxDD `-7.675`
- `news_risk_high->crypto_major_4h` score `3.8141` n `101` status `ready` deltaP `20.7483` edge `0.3053` maxDD `-8.0625`
- `news_risk_high->crypto_alt_1h` score `2.6227` n `101` status `ready` deltaP `15.7823` edge `0.1599` maxDD `-2.058`
- `news_risk_high->crypto_major_1h` score `2.0017` n `101` status `ready` deltaP `17.7284` edge `0.1009` maxDD `-2.8494`
- `news_risk_high->commodity_24h` score `1.1342` n `101` status `ready` deltaP `23.0232` edge `0.1225` maxDD `-3.4467`
- `market_context_high->equity_1h` score `0.8318` n `58` status `ready` deltaP `6.3081` edge `0.0526` maxDD `-0.36`
- `market_context_high->index_1h` score `0.6921` n `58` status `ready` deltaP `10.4274` edge `0.0137` maxDD `-0.0435`
- `news_risk_high->metal_1h` score `0.5202` n `101` status `ready` deltaP `13.6998` edge `0.0122` maxDD `-0.8144`
- `market_context_high->fx_1h` score `0.3474` n `58` status `ready` deltaP `8.7756` edge `0.0061` maxDD `-0.1854`
- `news_risk_high->metal_4h` score `0.3418` n `101` status `ready` deltaP `15.2695` edge `0.0321` maxDD `-2.0994`
- `market_context_high->index_4h` score `0.3043` n `58` status `ready` deltaP `14.324` edge `0.0072` maxDD `-1.0949`
- `news_risk_high->fx_4h` score `0.2649` n `101` status `ready` deltaP `9.2504` edge `0.024` maxDD `-0.421`
- `market_context_high->metal_1h` score `0.2423` n `58` status `ready` deltaP `5.2499` edge `0.016` maxDD `-0.1314`
- `news_risk_high->fx_1h` score `-0.2016` n `101` status `ready` deltaP `3.1422` edge `0.0066` maxDD `-0.2147`
- `news_risk_high->equity_1h` score `-0.243` n `101` status `ready` deltaP `1.9209` edge `0.0075` maxDD `-0.9112`
- `market_context_high->crypto_major_1h` score `-0.2833` n `58` status `ready` deltaP `-2.0906` edge `0.0622` maxDD `-2.7494`
- `news_risk_high->metal_24h` score `-0.449` n `101` status `ready` deltaP `9.0828` edge `-0.0337` maxDD `-2.4203`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
