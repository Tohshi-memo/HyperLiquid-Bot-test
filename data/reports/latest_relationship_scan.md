# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-28T16:37:27.667557+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `7506`

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

- `news_risk_high->unknown_1h` score `3435.6023` n `31` status `ready` deltaP `2.3807` edge `286.3019` maxDD `-0.7395`
- `news_risk_high->unknown_4h` score `3268.8513` n `31` status `ready` deltaP `3.634` edge `272.3857` maxDD `-0.1191`
- `news_risk_high->crypto_major_24h` score `24.9076` n `31` status `ready` deltaP `37.9549` edge `1.8226` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `18.9003` n `31` status `ready` deltaP `36.0485` edge `1.3347` maxDD `0.0`
- `news_risk_high->equity_24h` score `13.0772` n `31` status `ready` deltaP `29.2894` edge `0.8945` maxDD `0.0`
- `news_risk_high->crypto_alt_4h` score `9.3962` n `31` status `ready` deltaP `24.3214` edge `0.7079` maxDD `-5.2957`
- `news_risk_high->crypto_major_4h` score `5.9681` n `31` status `ready` deltaP `18.7598` edge `0.7818` maxDD `-7.6714`
- `news_risk_high->equity_4h` score `5.9592` n `31` status `ready` deltaP `33.4137` edge `0.3219` maxDD `-2.178`
- `news_risk_high->fx_24h` score `5.1213` n `31` status `ready` deltaP `42.3157` edge `0.1575` maxDD `-0.0262`
- `news_risk_high->metal_24h` score `3.9278` n `31` status `ready` deltaP `17.0403` edge `0.2412` maxDD `-0.1986`
- `news_risk_high->index_4h` score `2.6803` n `31` status `ready` deltaP `32.6515` edge `0.0317` maxDD `-0.4146`
- `news_risk_high->index_24h` score `2.4669` n `31` status `ready` deltaP `26.5165` edge `0.0288` maxDD `0.0`
- `news_risk_high->index_1h` score `2.3678` n `31` status `ready` deltaP `28.9985` edge `0.0125` maxDD `-0.0136`
- `news_risk_high->equity_1h` score `2.3054` n `31` status `ready` deltaP `15.3467` edge `0.1085` maxDD `-0.1621`
- `news_risk_high->crypto_major_1h` score `2.0869` n `31` status `ready` deltaP `7.0166` edge `0.2669` maxDD `-1.6897`
- `news_risk_high->crypto_alt_1h` score `1.9798` n `31` status `ready` deltaP `10.9088` edge `0.2168` maxDD `-1.5232`
- `news_risk_high->metal_1h` score `1.1613` n `31` status `ready` deltaP `25.0917` edge `0.0095` maxDD `-0.2315`
- `news_risk_high->commodity_4h` score `0.5114` n `31` status `ready` deltaP `11.5706` edge `0.0282` maxDD `-0.5151`
- `news_risk_high->metal_4h` score `0.4495` n `31` status `ready` deltaP `13.1196` edge `0.0259` maxDD `-0.7918`
- `market_context_high->fx_1h` score `0.425` n `65` status `ready` deltaP `11.2391` edge `0.0017` maxDD `-0.1042`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
