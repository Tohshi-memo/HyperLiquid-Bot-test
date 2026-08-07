# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-07T04:07:27.515370+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11765`

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

- `market_context_high->commodity_4h` score `1.1805` n `120` status `ready` deltaP `13.4857` edge `0.0931` maxDD `-2.7703`
- `market_context_high->metal_24h` score `0.8476` n `109` status `ready` deltaP `3.7004` edge `0.1628` maxDD `-2.6802`
- `market_context_high->fx_24h` score `0.5769` n `109` status `ready` deltaP `21.4854` edge `0.0513` maxDD `-4.3126`
- `market_context_high->commodity_1h` score `0.4799` n `120` status `ready` deltaP `7.7994` edge `0.0296` maxDD `-1.3282`
- `market_context_high->fx_1h` score `0.0242` n `120` status `ready` deltaP `6.3024` edge `-0.0039` maxDD `-0.8012`
- `market_context_high->fx_4h` score `-0.27` n `120` status `ready` deltaP `7.2866` edge `0.0028` maxDD `-1.8797`
- `market_context_high->metal_1h` score `-0.5389` n `120` status `ready` deltaP `-1.9261` edge `-0.0068` maxDD `-1.6224`
- `market_context_high->crypto_alt_1h` score `-0.7708` n `120` status `ready` deltaP `-2.994` edge `-0.0078` maxDD `-3.0178`
- `market_context_high->index_1h` score `-0.9413` n `120` status `ready` deltaP `-1.7764` edge `-0.0132` maxDD `-1.6054`
- `market_context_high->index_24h` score `-1.0899` n `109` status `ready` deltaP `-0.7122` edge `0.0845` maxDD `-7.8922`
- `market_context_high->equity_1h` score `-1.2649` n `120` status `ready` deltaP `4.3962` edge `-0.035` maxDD `-10.5179`
- `market_context_high->metal_4h` score `-1.448` n `120` status `ready` deltaP `0.0305` edge `0.0026` maxDD `-3.211`
- `market_context_high->index_4h` score `-1.5202` n `120` status `ready` deltaP `-5.8435` edge `-0.0305` maxDD `-4.7021`
- `market_context_high->crypto_alt_4h` score `-1.8672` n `120` status `ready` deltaP `2.1138` edge `-0.0307` maxDD `-5.7857`
- `market_context_high->crypto_major_1h` score `-2.553` n `120` status `ready` deltaP `-6.1527` edge `-0.0344` maxDD `-7.6533`
- `market_context_high->crypto_alt_24h` score `-3.576` n `109` status `ready` deltaP `-8.9843` edge `-0.0938` maxDD `-4.5445`
- `market_context_high->equity_4h` score `-5.8` n `120` status `ready` deltaP `1.1077` edge `-0.2221` maxDD `-34.9766`
- `market_context_high->unknown_24h` score `-6.1098` n `109` status `ready` deltaP `3.7571` edge `-0.5299` maxDD `-0.0104`
- `market_context_high->commodity_24h` score `-6.3345` n `109` status `ready` deltaP `9.8099` edge `-0.001` maxDD `-52.7876`
- `market_context_high->crypto_major_4h` score `-7.1833` n `120` status `ready` deltaP `-5.7317` edge `-0.1392` maxDD `-27.3622`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
