# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-07T02:22:32.415501+00:00`
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

- `market_context_high->unknown_24h` score `9.6906` n `109` status `ready` deltaP `3.7571` edge `0.7868` maxDD `-0.0104`
- `market_context_high->commodity_4h` score `1.2423` n `120` status `ready` deltaP `13.9431` edge `0.0952` maxDD `-2.7703`
- `market_context_high->metal_24h` score `0.892` n `109` status `ready` deltaP `3.7004` edge `0.1665` maxDD `-2.6802`
- `market_context_high->fx_24h` score `0.5699` n `109` status `ready` deltaP `21.4854` edge `0.0504` maxDD `-4.3126`
- `market_context_high->commodity_1h` score `0.5075` n `120` status `ready` deltaP `8.0988` edge `0.0299` maxDD `-1.3282`
- `market_context_high->fx_1h` score `0.0398` n `120` status `ready` deltaP `6.6018` edge `-0.0039` maxDD `-0.8012`
- `market_context_high->fx_4h` score `-0.3458` n `120` status `ready` deltaP `6.2195` edge `0.0002` maxDD `-1.8797`
- `market_context_high->metal_1h` score `-0.5552` n `120` status `ready` deltaP `-2.2255` edge `-0.0069` maxDD `-1.6224`
- `market_context_high->crypto_alt_1h` score `-0.8043` n `120` status `ready` deltaP `-3.2934` edge `-0.0101` maxDD `-3.0178`
- `market_context_high->index_1h` score `-0.982` n `120` status `ready` deltaP `-2.2255` edge `-0.0136` maxDD `-1.6054`
- `market_context_high->index_24h` score `-1.171` n `109` status `ready` deltaP `-1.8808` edge `0.0819` maxDD `-7.8922`
- `market_context_high->equity_1h` score `-1.289` n `120` status `ready` deltaP `4.0968` edge `-0.0361` maxDD `-10.5179`
- `market_context_high->metal_4h` score `-1.329` n `120` status `ready` deltaP `1.0976` edge `0.0054` maxDD `-3.211`
- `market_context_high->index_4h` score `-1.6194` n `120` status `ready` deltaP `-6.9106` edge `-0.0361` maxDD `-4.7021`
- `market_context_high->crypto_alt_4h` score `-1.8756` n `120` status `ready` deltaP `2.1138` edge `-0.0314` maxDD `-5.7857`
- `market_context_high->crypto_major_1h` score `-2.6513` n `120` status `ready` deltaP `-6.9012` edge `-0.0376` maxDD `-7.6533`
- `market_context_high->crypto_alt_24h` score `-3.3157` n `109` status `ready` deltaP `-7.8157` edge `-0.0799` maxDD `-4.5445`
- `market_context_high->equity_4h` score `-5.9227` n `120` status `ready` deltaP `0.8028` edge `-0.2358` maxDD `-34.9766`
- `market_context_high->commodity_24h` score `-6.3376` n `109` status `ready` deltaP `9.8099` edge `-0.0014` maxDD `-52.7876`
- `market_context_high->crypto_major_4h` score `-7.2281` n `120` status `ready` deltaP `-6.0366` edge `-0.1409` maxDD `-27.3622`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
