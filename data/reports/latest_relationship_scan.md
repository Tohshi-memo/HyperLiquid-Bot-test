# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-29T06:07:26.513878+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11794`

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

- `news_risk_high->unknown_24h` score `58.1438` n `50` status `ready` deltaP `21.5278` edge `4.7018` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `33.2918` n `50` status `ready` deltaP `46.5208` edge `2.5083` maxDD `-2.8629`
- `news_risk_high->crypto_major_24h` score `9.766` n `50` status `ready` deltaP `27.9236` edge `0.677` maxDD `-2.6128`
- `news_risk_high->equity_24h` score `7.4663` n `50` status `ready` deltaP `30.1806` edge `0.5138` maxDD `-4.7584`
- `market_context_high->unknown_24h` score `7.4525` n `120` status `ready` deltaP `14.8611` edge `0.5952` maxDD `-3.1917`
- `news_risk_high->unknown_4h` score `6.4975` n `79` status `ready` deltaP `11.0104` edge `0.5225` maxDD `-1.6886`
- `news_risk_high->metal_24h` score `4.5657` n `50` status `ready` deltaP `43.4861` edge `0.0948` maxDD `-0.0053`
- `market_context_high->metal_24h` score `3.3829` n `120` status `ready` deltaP `28.8194` edge `0.1917` maxDD `-3.1535`
- `news_risk_high->unknown_1h` score `2.692` n `80` status `ready` deltaP `5.524` edge `0.2232` maxDD `-0.8558`
- `news_risk_high->index_24h` score `2.5108` n `50` status `ready` deltaP `27.0625` edge `0.0439` maxDD `-0.2064`
- `market_context_high->unknown_4h` score `2.509` n `120` status `ready` deltaP `19.2277` edge `0.1216` maxDD `-0.5894`
- `news_risk_high->fx_4h` score `2.2941` n `79` status `ready` deltaP `33.6176` edge `0.022` maxDD `-0.3953`
- `market_context_high->unknown_1h` score `1.2658` n `120` status `ready` deltaP `9.6907` edge `0.0859` maxDD `-1.6015`
- `news_risk_high->fx_1h` score `0.6513` n `80` status `ready` deltaP `13.1437` edge `0.0055` maxDD `-0.108`
- `news_risk_high->commodity_1h` score `0.4992` n `80` status `ready` deltaP `13.5479` edge `0.0057` maxDD `-0.5618`
- `market_context_high->metal_4h` score `-0.1446` n `120` status `ready` deltaP `9.4918` edge `0.0099` maxDD `-3.3377`
- `market_context_high->fx_1h` score `-0.3242` n `120` status `ready` deltaP `4.8104` edge `-0.0004` maxDD `-0.8587`
- `news_risk_high->index_1h` score `-0.4058` n `80` status `ready` deltaP `0.0075` edge `-0.0084` maxDD `-0.8275`
- `news_risk_high->index_4h` score `-0.5265` n `79` status `ready` deltaP `1.9451` edge `-0.0163` maxDD `-1.7996`
- `news_risk_high->commodity_4h` score `-0.5851` n `79` status `ready` deltaP `7.1878` edge `0.0112` maxDD `-2.0635`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
