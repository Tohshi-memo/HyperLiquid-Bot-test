# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-03T21:07:31.727462+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5931`

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

- `market_context_high->unknown_24h` score `44.35` n `40` status `ready` deltaP `28.8194` edge `3.5037` maxDD `0.0`
- `market_context_high->unknown_4h` score `14.9059` n `57` status `ready` deltaP `10.8793` edge `1.2141` maxDD `-1.2244`
- `market_context_high->crypto_alt_24h` score `10.8929` n `40` status `ready` deltaP `48.75` edge `0.6001` maxDD `-0.3889`
- `market_context_high->commodity_24h` score `10.5432` n `40` status `ready` deltaP `50.9722` edge `0.5448` maxDD `-0.1479`
- `news_risk_high->fx_24h` score `0.9977` n `31` status `ready` deltaP `12.192` edge `0.0671` maxDD `-1.5526`
- `news_risk_high->commodity_1h` score `0.8968` n `31` status `ready` deltaP `19.2389` edge `0.0079` maxDD `-0.6947`
- `market_context_high->commodity_4h` score `0.8794` n `57` status `ready` deltaP `10.4862` edge `0.088` maxDD `-2.7703`
- `news_risk_high->equity_4h` score `0.4181` n `31` status `ready` deltaP `-8.4972` edge `0.1599` maxDD `-2.8064`
- `market_context_high->commodity_1h` score `0.3203` n `69` status `ready` deltaP `6.5695` edge `0.0245` maxDD `-1.3282`
- `market_context_high->fx_1h` score `0.2635` n `69` status `ready` deltaP `8.9712` edge `-0.003` maxDD `-0.7878`
- `news_risk_high->fx_4h` score `0.1066` n `31` status `ready` deltaP `4.2831` edge `0.0354` maxDD `-0.356`
- `market_context_high->fx_4h` score `0.0128` n `57` status `ready` deltaP `13.2248` edge `-0.0011` maxDD `-1.8797`
- `news_risk_high->index_4h` score `-0.0186` n `31` status `ready` deltaP `-1.5883` edge `0.0471` maxDD `-0.3783`
- `news_risk_high->commodity_4h` score `-0.0328` n `31` status `ready` deltaP `10.656` edge `-0.0237` maxDD `-1.6728`
- `news_risk_high->index_1h` score `-0.0898` n `31` status `ready` deltaP `2.1441` edge `-0.006` maxDD `-0.5845`
- `news_risk_high->crypto_alt_1h` score `-0.1159` n `31` status `ready` deltaP `10.0927` edge `-0.0181` maxDD `-3.1233`
- `market_context_high->crypto_alt_4h` score `-0.1518` n `57` status `ready` deltaP `6.7502` edge `0.0261` maxDD `-4.9116`
- `market_context_high->crypto_alt_1h` score `-0.2817` n `69` status `ready` deltaP `2.4256` edge `0.0146` maxDD `-3.0178`
- `market_context_high->index_1h` score `-0.3197` n `69` status `ready` deltaP `3.8271` edge `-0.0131` maxDD `-1.6054`
- `news_risk_high->fx_1h` score `-0.3338` n `31` status `ready` deltaP `-2.062` edge `0.0021` maxDD `-0.1588`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
