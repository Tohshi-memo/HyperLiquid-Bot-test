# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-29T14:37:32.105685+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `6784`

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

- `market_context_high->unknown_24h` score `1460.1909` n `140` status `ready` deltaP `-2.0189` edge `121.7713` maxDD `-3.6878`
- `market_context_high->unknown_4h` score `51.9868` n `140` status `ready` deltaP `6.6333` edge `4.3013` maxDD `-0.3966`
- `market_context_high->index_24h` score `1.7642` n `140` status `ready` deltaP `23.3135` edge `0.0099` maxDD `-0.1315`
- `market_context_high->commodity_4h` score `0.2722` n `140` status `ready` deltaP `13.3144` edge `0.0558` maxDD `-1.0837`
- `market_context_high->fx_1h` score `0.0306` n `140` status `ready` deltaP `5.6801` edge `0.0005` maxDD `-0.1986`
- `market_context_high->metal_1h` score `-0.0374` n `140` status `ready` deltaP `8.5586` edge `0.0075` maxDD `-0.881`
- `market_context_high->metal_4h` score `-0.1884` n `140` status `ready` deltaP `11.2021` edge `0.0066` maxDD `-3.1019`
- `market_context_high->fx_4h` score `-0.2414` n `140` status `ready` deltaP `4.2291` edge `0.0007` maxDD `-0.4545`
- `market_context_high->commodity_1h` score `-0.3465` n `140` status `ready` deltaP `1.3131` edge `0.0138` maxDD `-0.4475`
- `market_context_high->crypto_major_1h` score `-0.7839` n `140` status `ready` deltaP `4.5167` edge `0.0248` maxDD `-6.2854`
- `market_context_high->equity_1h` score `-0.8259` n `140` status `ready` deltaP `0.1155` edge `0.0158` maxDD `-5.1294`
- `market_context_high->fx_24h` score `-0.9516` n `140` status `ready` deltaP `6.1012` edge `0.0131` maxDD `-0.9792`
- `market_context_high->index_1h` score `-1.0612` n `140` status `ready` deltaP `-3.2934` edge `-0.0023` maxDD `-1.1344`
- `market_context_high->crypto_alt_1h` score `-1.4397` n `140` status `ready` deltaP `1.5996` edge `0.0133` maxDD `-10.0166`
- `market_context_high->metal_24h` score `-1.9747` n `140` status `ready` deltaP `2.0387` edge `0.0021` maxDD `-10.5088`
- `market_context_high->index_4h` score `-2.6792` n `140` status `ready` deltaP `-8.4887` edge `-0.0269` maxDD `-4.1819`
- `market_context_high->equity_4h` score `-2.7579` n `140` status `ready` deltaP `-3.5061` edge `-0.0654` maxDD `-14.5174`
- `market_context_high->crypto_major_4h` score `-3.0482` n `140` status `ready` deltaP `3.1315` edge `-0.0401` maxDD `-22.3929`
- `market_context_high->crypto_major_24h` score `-3.9729` n `140` status `ready` deltaP `-4.3998` edge `0.0057` maxDD `-29.1905`
- `market_context_high->equity_24h` score `-3.9969` n `140` status `ready` deltaP `6.1707` edge `-0.0985` maxDD `-14.0571`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
