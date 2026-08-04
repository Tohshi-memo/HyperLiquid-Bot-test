# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-04T02:07:27.407200+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `64`

- Symbol pattern count: `7932`

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

- `market_context_high->unknown_24h` score `37.3875` n `46` status `ready` deltaP `26.2983` edge `2.9446` maxDD `-0.0103`
- `market_context_high->crypto_alt_24h` score `10.2333` n `46` status `ready` deltaP `47.645` edge `0.5525` maxDD `-0.3889`
- `market_context_high->unknown_4h` score `9.5764` n `77` status `ready` deltaP `8.9286` edge `0.7859` maxDD `-1.4578`
- `market_context_high->commodity_24h` score `8.4503` n `46` status `ready` deltaP `40.1721` edge `0.4543` maxDD `-0.434`
- `news_risk_high->fx_24h` score `1.0325` n `31` status `ready` deltaP `12.192` edge `0.07` maxDD `-1.5526`
- `market_context_high->commodity_4h` score `0.9223` n `77` status `ready` deltaP `12.6426` edge `0.0772` maxDD `-2.7703`
- `news_risk_high->commodity_1h` score `0.8399` n `31` status `ready` deltaP `18.4904` edge `0.0056` maxDD `-0.6947`
- `market_context_high->fx_1h` score `0.3269` n `88` status `ready` deltaP `9.6285` edge `-0.0021` maxDD `-0.7878`
- `market_context_high->commodity_1h` score `0.3104` n `88` status `ready` deltaP `6.4303` edge `0.0246` maxDD `-1.3282`
- `market_context_high->fx_4h` score `0.3065` n `77` status `ready` deltaP `17.4296` edge `0.0091` maxDD `-1.8797`
- `news_risk_high->fx_4h` score `0.0592` n `31` status `ready` deltaP `3.5209` edge `0.0344` maxDD `-0.356`
- `news_risk_high->index_1h` score `-0.1988` n `31` status `ready` deltaP `0.3477` edge `-0.008` maxDD `-0.5845`
- `news_risk_high->crypto_alt_1h` score `-0.2204` n `31` status `ready` deltaP `9.943` edge `-0.0305` maxDD `-3.1233`
- `news_risk_high->commodity_4h` score `-0.2806` n `31` status `ready` deltaP `8.3694` edge `-0.0291` maxDD `-1.6728`
- `news_risk_high->index_4h` score `-0.2913` n `31` status `ready` deltaP `-3.7225` edge `0.0386` maxDD `-0.3783`
- `news_risk_high->fx_1h` score `-0.3393` n `31` status `ready` deltaP `-2.2117` edge `0.0024` maxDD `-0.1588`
- `market_context_high->index_1h` score `-0.418` n `88` status `ready` deltaP `2.3272` edge `-0.0157` maxDD `-1.6054`
- `news_risk_high->unknown_4h` score `-0.4784` n `31` status `ready` deltaP `-1.2097` edge `-0.0044` maxDD `-1.5766`
- `market_context_high->metal_1h` score `-0.4817` n `88` status `ready` deltaP `-0.7213` edge `-0.0075` maxDD `-1.6224`
- `news_risk_high->equity_4h` score `-0.783` n `31` status `ready` deltaP `-16.9305` edge `0.1172` maxDD `-2.8999`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
