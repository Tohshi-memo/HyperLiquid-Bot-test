# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-07T02:52:34.023350+00:00`
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

- `market_context_high->unknown_24h` score `5.1654` n `109` status `ready` deltaP `3.7571` edge `0.4097` maxDD `-0.0104`
- `market_context_high->commodity_4h` score `1.2533` n `120` status `ready` deltaP `14.0955` edge `0.0951` maxDD `-2.7703`
- `market_context_high->metal_24h` score `0.8848` n `109` status `ready` deltaP `3.7004` edge `0.1659` maxDD `-2.6802`
- `market_context_high->fx_24h` score `0.5722` n `109` status `ready` deltaP `21.4854` edge `0.0507` maxDD `-4.3126`
- `market_context_high->commodity_1h` score `0.4931` n `120` status `ready` deltaP `7.9491` edge `0.0297` maxDD `-1.3282`
- `market_context_high->fx_1h` score `0.0234` n `120` status `ready` deltaP `6.3024` edge `-0.004` maxDD `-0.8012`
- `market_context_high->fx_4h` score `-0.3253` n `120` status `ready` deltaP `6.5244` edge `0.0008` maxDD `-1.8797`
- `market_context_high->metal_1h` score `-0.5552` n `120` status `ready` deltaP `-2.2255` edge `-0.0069` maxDD `-1.6224`
- `market_context_high->crypto_alt_1h` score `-0.8214` n `120` status `ready` deltaP `-3.5928` edge `-0.0103` maxDD `-3.0178`
- `market_context_high->index_1h` score `-0.982` n `120` status `ready` deltaP `-2.2255` edge `-0.0136` maxDD `-1.6054`
- `market_context_high->index_24h` score `-1.1458` n `109` status `ready` deltaP `-1.5469` edge `0.0829` maxDD `-7.8922`
- `market_context_high->equity_1h` score `-1.2922` n `120` status `ready` deltaP `4.0968` edge `-0.0365` maxDD `-10.5179`
- `market_context_high->metal_4h` score `-1.3594` n `120` status `ready` deltaP `0.7927` edge `0.0049` maxDD `-3.211`
- `market_context_high->index_4h` score `-1.5911` n `120` status `ready` deltaP `-6.6057` edge `-0.0345` maxDD `-4.7021`
- `market_context_high->crypto_alt_4h` score `-1.884` n `120` status `ready` deltaP `2.1138` edge `-0.0321` maxDD `-5.7857`
- `market_context_high->crypto_major_1h` score `-2.6333` n `120` status `ready` deltaP `-6.7515` edge `-0.0371` maxDD `-7.6533`
- `market_context_high->crypto_alt_24h` score `-3.3976` n `109` status `ready` deltaP `-8.1496` edge `-0.0845` maxDD `-4.5445`
- `market_context_high->equity_4h` score `-5.8876` n `120` status `ready` deltaP `0.8028` edge `-0.2313` maxDD `-34.9766`
- `market_context_high->commodity_24h` score `-6.3454` n `109` status `ready` deltaP `9.8099` edge `-0.0024` maxDD `-52.7876`
- `market_context_high->crypto_major_4h` score `-7.2111` n `120` status `ready` deltaP `-5.8841` edge `-0.1405` maxDD `-27.3622`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
