# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-29T07:07:24.520238+00:00`
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

- `news_risk_high->unknown_24h` score `58.4478` n `50` status `ready` deltaP `22.2222` edge `4.7225` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `33.1574` n `50` status `ready` deltaP `46.5208` edge `2.4971` maxDD `-2.8629`
- `news_risk_high->crypto_major_24h` score `9.8903` n `50` status `ready` deltaP `28.0972` edge `0.6862` maxDD `-2.6128`
- `market_context_high->unknown_24h` score `7.7565` n `120` status `ready` deltaP `15.5555` edge `0.6159` maxDD `-3.1917`
- `news_risk_high->equity_24h` score `7.6237` n `50` status `ready` deltaP `30.5278` edge `0.5246` maxDD `-4.7584`
- `news_risk_high->unknown_4h` score `6.5483` n `79` status `ready` deltaP `11.3153` edge `0.5247` maxDD `-1.6886`
- `news_risk_high->metal_24h` score `4.6669` n `50` status `ready` deltaP `44.1806` edge `0.0986` maxDD `-0.0053`
- `market_context_high->metal_24h` score `3.4841` n `120` status `ready` deltaP `29.5139` edge `0.1955` maxDD `-3.1535`
- `news_risk_high->unknown_1h` score `2.7052` n `80` status `ready` deltaP `5.524` edge `0.2243` maxDD `-0.8558`
- `market_context_high->unknown_4h` score `2.5598` n `120` status `ready` deltaP `19.5326` edge `0.1238` maxDD `-0.5894`
- `news_risk_high->index_24h` score `2.5355` n `50` status `ready` deltaP `27.2361` edge `0.0448` maxDD `-0.2064`
- `news_risk_high->fx_4h` score `2.2685` n `79` status `ready` deltaP `33.3128` edge `0.0219` maxDD `-0.3953`
- `market_context_high->unknown_1h` score `1.279` n `120` status `ready` deltaP `9.6907` edge `0.087` maxDD `-1.6015`
- `news_risk_high->fx_1h` score `0.6633` n `80` status `ready` deltaP `13.2934` edge `0.0055` maxDD `-0.108`
- `news_risk_high->commodity_1h` score `0.4992` n `80` status `ready` deltaP `13.5479` edge `0.0057` maxDD `-0.5618`
- `market_context_high->metal_4h` score `-0.1518` n `120` status `ready` deltaP `9.3394` edge `0.01` maxDD `-3.3377`
- `market_context_high->fx_1h` score `-0.3164` n `120` status `ready` deltaP `4.9601` edge `-0.0004` maxDD `-0.8587`
- `news_risk_high->index_1h` score `-0.3902` n `80` status `ready` deltaP `0.3069` edge `-0.0084` maxDD `-0.8275`
- `news_risk_high->index_4h` score `-0.5597` n `79` status `ready` deltaP `1.3353` edge `-0.0165` maxDD `-1.7996`
- `news_risk_high->commodity_4h` score `-0.5764` n `79` status `ready` deltaP `7.3402` edge `0.0113` maxDD `-2.0635`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
