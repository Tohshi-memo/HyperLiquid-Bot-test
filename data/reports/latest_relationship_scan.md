# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-29T14:07:27.888494+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11396`

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

- `news_risk_high->unknown_24h` score `50.7546` n `56` status `ready` deltaP `16.1954` edge `4.1761` maxDD `-2.3617`
- `news_risk_high->crypto_alt_24h` score `24.8428` n `56` status `ready` deltaP `37.4504` edge `2.0412` maxDD `-14.9839`
- `market_context_high->unknown_24h` score `8.4117` n `105` status `ready` deltaP `19.2907` edge `0.6456` maxDD `-3.1917`
- `news_risk_high->unknown_4h` score `6.3715` n `80` status `ready` deltaP `11.5854` edge `0.5127` maxDD `-1.7183`
- `market_context_high->metal_24h` score `4.3665` n `105` status `ready` deltaP `31.9941` edge `0.2525` maxDD `-3.1535`
- `news_risk_high->equity_24h` score `2.9643` n `56` status `ready` deltaP `25.1736` edge `0.4014` maxDD `-12.4677`
- `news_risk_high->unknown_1h` score `2.6487` n `80` status `ready` deltaP `5.524` edge `0.2196` maxDD `-0.8558`
- `news_risk_high->crypto_major_24h` score `2.6398` n `56` status `ready` deltaP `21.5278` edge `0.4348` maxDD `-16.524`
- `news_risk_high->fx_4h` score `2.4436` n `80` status `ready` deltaP `35.4268` edge `0.0224` maxDD `-0.3953`
- `market_context_high->unknown_4h` score `2.4428` n `114` status `ready` deltaP `17.2872` edge `0.1315` maxDD `-0.788`
- `news_risk_high->metal_24h` score `1.9049` n `56` status `ready` deltaP `38.5417` edge `0.0587` maxDD `-3.7137`
- `news_risk_high->index_24h` score `1.5688` n `56` status `ready` deltaP `21.4533` edge `0.0297` maxDD `-1.0255`
- `market_context_high->unknown_1h` score `1.121` n `126` status `ready` deltaP `9.4526` edge `0.0785` maxDD `-1.5148`
- `news_risk_high->fx_1h` score `0.7723` n `80` status `ready` deltaP `14.6407` edge `0.0056` maxDD `-0.108`
- `news_risk_high->commodity_1h` score `0.3917` n `80` status `ready` deltaP `11.6018` edge `0.0049` maxDD `-0.5618`
- `market_context_high->crypto_major_4h` score `-0.2206` n `114` status `ready` deltaP `17.7738` edge `0.2082` maxDD `-20.9394`
- `market_context_high->metal_4h` score `-0.3362` n `114` status `ready` deltaP `6.1083` edge `0.0079` maxDD `-3.3377`
- `news_risk_high->index_1h` score `-0.391` n `80` status `ready` deltaP `0.3069` edge `-0.0085` maxDD `-0.8275`
- `market_context_high->commodity_1h` score `-0.4819` n `126` status `ready` deltaP `-0.1045` edge `0.0083` maxDD `-1.5507`
- `news_risk_high->index_4h` score `-0.5364` n `80` status `ready` deltaP `1.7683` edge `-0.0164` maxDD `-1.7996`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
