# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-03T07:23:31.213752+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5903`

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

- `market_context_high->crypto_alt_24h` score `12.9867` n `40` status `ready` deltaP `51.4583` edge `0.7789` maxDD `-2.1786`
- `market_context_high->commodity_24h` score `11.0034` n `40` status `ready` deltaP `51.3194` edge `0.5876` maxDD `-0.6889`
- `news_risk_high->equity_4h` score `1.0409` n `33` status `ready` deltaP `-9.4051` edge `0.2253` maxDD `-3.402`
- `news_risk_high->commodity_1h` score `0.9009` n `33` status `ready` deltaP `18.9122` edge `0.0106` maxDD `-0.6947`
- `news_risk_high->fx_24h` score `0.5796` n `33` status `ready` deltaP `10.4324` edge `0.0539` maxDD `-1.6785`
- `news_risk_high->commodity_4h` score `0.439` n `33` status `ready` deltaP `13.6734` edge `-0.0045` maxDD `-1.6728`
- `market_context_high->commodity_1h` score `0.3564` n `47` status `ready` deltaP `7.5646` edge `0.0327` maxDD `-1.3282`
- `market_context_high->commodity_4h` score `0.3005` n `47` status `ready` deltaP `5.0338` edge `0.0896` maxDD `-2.7703`
- `news_risk_high->crypto_alt_1h` score `0.1283` n `33` status `ready` deltaP `11.8037` edge `0.0018` maxDD `-3.1233`
- `news_risk_high->fx_4h` score `0.0183` n `33` status `ready` deltaP `4.028` edge `0.0347` maxDD `-0.4037`
- `market_context_high->fx_4h` score `0.0049` n `47` status `ready` deltaP `13.5703` edge `-0.0044` maxDD `-1.8531`
- `market_context_high->fx_1h` score `-0.0022` n `47` status `ready` deltaP `7.1155` edge `-0.0088` maxDD `-0.7804`
- `news_risk_high->index_4h` score `-0.0111` n `33` status `ready` deltaP `-3.0396` edge `0.0574` maxDD `-0.3783`
- `news_risk_high->index_1h` score `-0.031` n `33` status `ready` deltaP `2.7491` edge `-0.0025` maxDD `-0.5845`
- `market_context_high->crypto_alt_4h` score `-0.2345` n `47` status `ready` deltaP `2.1439` edge `0.0462` maxDD `-4.9116`
- `news_risk_high->fx_1h` score `-0.3153` n `33` status `ready` deltaP `0.2812` edge `0.003` maxDD `-0.1588`
- `news_risk_high->metal_1h` score `-0.4314` n `33` status `ready` deltaP `-2.5631` edge `-0.0063` maxDD `-0.5538`
- `news_risk_high->crypto_major_1h` score `-0.6751` n `33` status `ready` deltaP `3.611` edge `-0.0386` maxDD `-3.762`
- `market_context_high->fx_24h` score `-0.6827` n `40` status `ready` deltaP `0.6597` edge `0.0367` maxDD `-2.506`
- `news_risk_high->equity_1h` score `-1.0323` n `33` status `ready` deltaP `-10.4201` edge `0.0194` maxDD `-2.916`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
