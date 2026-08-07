# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-07T08:09:57.240673+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11739`

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

- `market_context_high->commodity_4h` score `0.9356` n `120` status `ready` deltaP `11.504` edge `0.0859` maxDD `-2.7703`
- `market_context_high->fx_24h` score `0.5706` n `109` status `ready` deltaP `21.3184` edge `0.0516` maxDD `-4.3126`
- `market_context_high->metal_24h` score `0.4976` n `109` status `ready` deltaP `1.5301` edge `0.1481` maxDD `-2.6802`
- `market_context_high->commodity_1h` score `0.4356` n `120` status `ready` deltaP `7.5` edge `0.0279` maxDD `-1.3282`
- `market_context_high->fx_1h` score `0.0888` n `120` status `ready` deltaP `7.3503` edge `-0.0026` maxDD `-0.8012`
- `market_context_high->fx_4h` score `-0.1729` n `120` status `ready` deltaP `8.6585` edge `0.0061` maxDD `-1.8797`
- `market_context_high->metal_1h` score `-0.6518` n `120` status `ready` deltaP `-3.5728` edge `-0.0103` maxDD `-1.6224`
- `market_context_high->crypto_alt_1h` score `-0.8097` n `120` status `ready` deltaP `-3.1437` edge `-0.0118` maxDD `-3.0178`
- `market_context_high->index_1h` score `-1.0192` n `120` status `ready` deltaP `-2.8243` edge `-0.0127` maxDD `-1.6054`
- `market_context_high->index_24h` score `-1.1094` n `109` status `ready` deltaP `-0.7122` edge `0.082` maxDD `-7.8922`
- `market_context_high->equity_1h` score `-1.314` n `120` status `ready` deltaP `3.6477` edge `-0.0363` maxDD `-10.5179`
- `market_context_high->index_4h` score `-1.507` n `120` status `ready` deltaP `-5.8435` edge `-0.0288` maxDD `-4.7021`
- `market_context_high->metal_4h` score `-1.7375` n `120` status `ready` deltaP `-2.1037` edge `-0.0073` maxDD `-3.211`
- `market_context_high->crypto_alt_4h` score `-2.0495` n `120` status `ready` deltaP `1.1992` edge `-0.0398` maxDD `-5.7857`
- `market_context_high->crypto_major_1h` score `-2.6418` n `120` status `ready` deltaP `-6.4521` edge `-0.0398` maxDD `-7.6533`
- `market_context_high->crypto_alt_24h` score `-3.956` n `109` status `ready` deltaP `-11.1546` edge `-0.111` maxDD `-4.5445`
- `market_context_high->equity_4h` score `-5.8628` n `120` status `ready` deltaP `0.6504` edge `-0.2271` maxDD `-34.9766`
- `market_context_high->commodity_24h` score `-6.2963` n `109` status `ready` deltaP `9.8099` edge `0.0039` maxDD `-52.7876`
- `market_context_high->crypto_major_4h` score `-7.3447` n `120` status `ready` deltaP `-6.189` edge `-0.1496` maxDD `-27.3622`
- `market_context_high->unknown_1h` score `-8.3965` n `120` status `ready` deltaP `1.9212` edge `-0.6678` maxDD `-1.2437`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
