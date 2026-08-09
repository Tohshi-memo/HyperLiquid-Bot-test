# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-09T08:37:25.477454+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `8841`

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

- `market_context_high->equity_24h` score `3.738` n `103` status `ready` deltaP `4.5729` edge `0.587` maxDD `-21.1456`
- `market_context_high->metal_24h` score `2.7024` n `103` status `ready` deltaP `13.0799` edge `0.1956` maxDD `-2.2743`
- `market_context_high->commodity_4h` score `1.1462` n `143` status `ready` deltaP `14.7472` edge `0.0645` maxDD `-2.7169`
- `market_context_high->fx_24h` score `0.7837` n `103` status `ready` deltaP `21.575` edge `0.0433` maxDD `-1.9329`
- `market_context_high->commodity_1h` score `0.7737` n `143` status `ready` deltaP `10.6916` edge `0.0275` maxDD `-0.7439`
- `market_context_high->index_24h` score `0.5618` n `103` status `ready` deltaP `9.1002` edge `0.1645` maxDD `-5.9181`
- `market_context_high->fx_1h` score `-0.2942` n `143` status `ready` deltaP `4.2953` edge `-0.0036` maxDD `-0.9639`
- `market_context_high->index_1h` score `-0.4314` n `143` status `ready` deltaP `-1.6927` edge `-0.0051` maxDD `-0.7809`
- `market_context_high->fx_4h` score `-0.4579` n `143` status `ready` deltaP `5.9803` edge `-0.0027` maxDD `-1.6928`
- `market_context_high->metal_1h` score `-0.69` n `143` status `ready` deltaP `-4.8877` edge `-0.0063` maxDD `-0.9664`
- `market_context_high->equity_1h` score `-0.9157` n `143` status `ready` deltaP `-0.1873` edge `0.0078` maxDD `-4.6286`
- `market_context_high->index_4h` score `-0.9172` n `143` status `ready` deltaP `-1.0681` edge `-0.0088` maxDD `-1.1743`
- `market_context_high->metal_4h` score `-0.9583` n `143` status `ready` deltaP `-0.7462` edge `-0.017` maxDD `-2.7373`
- `market_context_high->crypto_alt_1h` score `-1.8964` n `143` status `ready` deltaP `-10.1336` edge `-0.0263` maxDD `-2.4677`
- `market_context_high->equity_4h` score `-2.527` n `143` status `ready` deltaP `-1.4188` edge `-0.0674` maxDD `-7.6983`
- `market_context_high->crypto_major_1h` score `-3.1208` n `143` status `ready` deltaP `-10.5377` edge `-0.0576` maxDD `-7.2436`
- `market_context_high->crypto_major_24h` score `-3.2733` n `103` status `ready` deltaP `5.8725` edge `-0.0625` maxDD `-14.2873`
- `market_context_high->crypto_alt_4h` score `-3.5947` n `143` status `ready` deltaP `-6.7521` edge `-0.0889` maxDD `-6.585`
- `market_context_high->crypto_alt_24h` score `-4.9803` n `103` status `ready` deltaP `-13.4878` edge `-0.1808` maxDD `-4.5445`
- `market_context_high->unknown_1h` score `-7.8053` n `143` status `ready` deltaP `-5.7944` edge `-0.5671` maxDD `-1.2437`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
