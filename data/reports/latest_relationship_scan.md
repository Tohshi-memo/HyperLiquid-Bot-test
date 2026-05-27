# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-27T15:22:23.017173+00:00`
- Price records: `672`
- Market context records: `2051`
- Flow alert records: `7799`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9125`

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

- `market_context_high->crypto_major_4h` score `9.3492` n `205` status `ready` deltaP `32.7897` edge `0.6135` maxDD `-1.9063`
- `market_context_high->crypto_alt_4h` score `8.6493` n `205` status `ready` deltaP `25.1613` edge `0.6675` maxDD `-5.1574`
- `market_context_high->unknown_4h` score `6.2796` n `205` status `ready` deltaP `19.9229` edge `0.4654` maxDD `-2.6599`
- `market_context_high->unknown_24h` score `3.3381` n `205` status `ready` deltaP `17.6876` edge `0.6923` maxDD `-35.8966`
- `market_context_high->equity_4h` score `3.2334` n `205` status `ready` deltaP `18.2096` edge `0.2575` maxDD `-5.0894`
- `market_context_high->index_4h` score `1.786` n `205` status `ready` deltaP `14.3391` edge `0.1216` maxDD `-1.8022`
- `market_context_high->crypto_major_1h` score `1.7047` n `206` status `ready` deltaP `13.4062` edge `0.1513` maxDD `-3.2225`
- `market_context_high->crypto_alt_1h` score `1.3253` n `206` status `ready` deltaP `10.4122` edge `0.1524` maxDD `-4.9097`
- `market_context_high->equity_24h` score `1.0239` n `205` status `ready` deltaP `17.8749` edge `0.456` maxDD `-33.1875`
- `market_context_high->index_24h` score `0.9033` n `205` status `ready` deltaP `6.3769` edge `0.1556` maxDD `-4.1604`
- `market_context_high->equity_1h` score `0.4105` n `206` status `ready` deltaP `8.2714` edge `0.0579` maxDD `-2.6402`
- `market_context_high->unknown_1h` score `0.2652` n `206` status `ready` deltaP `4.6596` edge `0.063` maxDD `-3.0902`
- `market_context_high->index_1h` score `-0.1343` n `206` status `ready` deltaP `3.7571` edge `0.0228` maxDD `-1.3898`
- `market_context_high->fx_24h` score `-0.4433` n `205` status `ready` deltaP `11.8145` edge `0.0236` maxDD `-2.811`
- `market_context_high->metal_4h` score `-0.7693` n `205` status `ready` deltaP `10.6887` edge `0.1269` maxDD `-11.9812`
- `market_context_high->crypto_major_24h` score `-0.7799` n `205` status `ready` deltaP `18.0885` edge `0.673` maxDD `-62.3533`
- `market_context_high->fx_1h` score `-0.7915` n `206` status `ready` deltaP `-0.5988` edge `0.0008` maxDD `-0.3548`
- `market_context_high->metal_1h` score `-0.7932` n `206` status `ready` deltaP `4.1466` edge `0.025` maxDD `-5.166`
- `market_context_high->fx_4h` score `-1.4428` n `205` status `ready` deltaP `-4.7394` edge `-0.0005` maxDD `-1.0513`
- `market_context_high->commodity_1h` score `-1.9504` n `206` status `ready` deltaP `1.6423` edge `-0.0052` maxDD `-15.7972`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
