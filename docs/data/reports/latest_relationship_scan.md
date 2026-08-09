# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-09T07:22:30.423182+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `8827`

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

- `market_context_high->equity_24h` score `3.6876` n `103` status `ready` deltaP `4.5729` edge `0.5828` maxDD `-21.1456`
- `market_context_high->metal_24h` score `2.7151` n `103` status `ready` deltaP `13.2535` edge `0.1955` maxDD `-2.2743`
- `market_context_high->commodity_4h` score `1.2462` n `140` status `ready` deltaP `15.4268` edge `0.0683` maxDD `-2.7169`
- `market_context_high->commodity_1h` score `0.86` n `143` status `ready` deltaP `11.2904` edge `0.0307` maxDD `-0.7439`
- `market_context_high->fx_24h` score `0.8024` n `103` status `ready` deltaP `21.575` edge `0.0457` maxDD `-1.9329`
- `market_context_high->index_24h` score `0.5571` n `103` status `ready` deltaP `9.1002` edge `0.1639` maxDD `-5.9181`
- `market_context_high->fx_1h` score `-0.2918` n `143` status `ready` deltaP `4.2953` edge `-0.0034` maxDD `-0.9639`
- `market_context_high->fx_4h` score `-0.3608` n `140` status `ready` deltaP `7.1341` edge `-0.0023` maxDD `-1.6928`
- `market_context_high->index_1h` score `-0.4439` n `143` status `ready` deltaP `-1.8424` edge `-0.0057` maxDD `-0.7809`
- `market_context_high->metal_1h` score `-0.6931` n `143` status `ready` deltaP `-4.8877` edge `-0.0067` maxDD `-0.9664`
- `market_context_high->equity_1h` score `-0.9612` n `143` status `ready` deltaP `-0.4868` edge `0.006` maxDD `-4.6286`
- `market_context_high->index_4h` score `-0.9696` n `140` status `ready` deltaP `-1.6028` edge `-0.0096` maxDD `-1.1743`
- `market_context_high->metal_4h` score `-1.005` n `140` status `ready` deltaP `-1.5854` edge `-0.0174` maxDD `-2.7373`
- `market_context_high->crypto_alt_1h` score `-1.9204` n `143` status `ready` deltaP `-10.2833` edge `-0.0273` maxDD `-2.4677`
- `market_context_high->equity_4h` score `-2.5698` n `140` status `ready` deltaP `-1.9381` edge `-0.0675` maxDD `-7.6983`
- `market_context_high->crypto_major_1h` score `-3.1555` n `143` status `ready` deltaP `-10.6874` edge `-0.0595` maxDD `-7.2436`
- `market_context_high->crypto_major_24h` score `-3.1915` n `103` status `ready` deltaP `6.2197` edge `-0.058` maxDD `-14.2873`
- `market_context_high->crypto_alt_4h` score `-3.6357` n `140` status `ready` deltaP `-6.8598` edge `-0.0916` maxDD `-6.585`
- `market_context_high->crypto_alt_24h` score `-4.7249` n `103` status `ready` deltaP `-12.6197` edge `-0.1653` maxDD `-4.5445`
- `market_context_high->unknown_1h` score `-7.8209` n `143` status `ready` deltaP `-5.9441` edge `-0.5674` maxDD `-1.2437`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
