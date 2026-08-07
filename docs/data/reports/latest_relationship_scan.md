# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-07T02:37:25.264408+00:00`
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

- `market_context_high->unknown_24h` score `7.4286` n `109` status `ready` deltaP `3.7571` edge `0.5983` maxDD `-0.0104`
- `market_context_high->commodity_4h` score `1.2557` n `120` status `ready` deltaP `14.0955` edge `0.0953` maxDD `-2.7703`
- `market_context_high->metal_24h` score `0.8884` n `109` status `ready` deltaP `3.7004` edge `0.1662` maxDD `-2.6802`
- `market_context_high->fx_24h` score `0.5714` n `109` status `ready` deltaP `21.4854` edge `0.0506` maxDD `-4.3126`
- `market_context_high->commodity_1h` score `0.4943` n `120` status `ready` deltaP `7.9491` edge `0.0298` maxDD `-1.3282`
- `market_context_high->fx_1h` score `0.032` n `120` status `ready` deltaP `6.4521` edge `-0.0039` maxDD `-0.8012`
- `market_context_high->fx_4h` score `-0.3355` n `120` status `ready` deltaP `6.372` edge `0.0005` maxDD `-1.8797`
- `market_context_high->metal_1h` score `-0.556` n `120` status `ready` deltaP `-2.2255` edge `-0.007` maxDD `-1.6224`
- `market_context_high->crypto_alt_1h` score `-0.8121` n `120` status `ready` deltaP `-3.4431` edge `-0.0101` maxDD `-3.0178`
- `market_context_high->index_1h` score `-0.982` n `120` status `ready` deltaP `-2.2255` edge `-0.0136` maxDD `-1.6054`
- `market_context_high->index_24h` score `-1.1576` n `109` status `ready` deltaP `-1.7139` edge `0.0825` maxDD `-7.8922`
- `market_context_high->equity_1h` score `-1.2898` n `120` status `ready` deltaP `4.0968` edge `-0.0362` maxDD `-10.5179`
- `market_context_high->metal_4h` score `-1.3436` n `120` status `ready` deltaP `0.9451` edge `0.0052` maxDD `-3.211`
- `market_context_high->index_4h` score `-1.6052` n `120` status `ready` deltaP `-6.7582` edge `-0.0353` maxDD `-4.7021`
- `market_context_high->crypto_alt_4h` score `-1.8804` n `120` status `ready` deltaP `2.1138` edge `-0.0318` maxDD `-5.7857`
- `market_context_high->crypto_major_1h` score `-2.6333` n `120` status `ready` deltaP `-6.7515` edge `-0.0371` maxDD `-7.6533`
- `market_context_high->crypto_alt_24h` score `-3.3567` n `109` status `ready` deltaP `-7.9827` edge `-0.0822` maxDD `-4.5445`
- `market_context_high->equity_4h` score `-5.9056` n `120` status `ready` deltaP `0.8028` edge `-0.2336` maxDD `-34.9766`
- `market_context_high->commodity_24h` score `-6.3415` n `109` status `ready` deltaP `9.8099` edge `-0.0019` maxDD `-52.7876`
- `market_context_high->crypto_major_4h` score `-7.2099` n `120` status `ready` deltaP `-5.8841` edge `-0.1404` maxDD `-27.3622`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
