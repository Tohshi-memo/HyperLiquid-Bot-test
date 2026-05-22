# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-22T06:37:18.305005+00:00`
- Price records: `672`
- Market context records: `1502`
- Flow alert records: `6233`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8791`

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

- `market_context_high->metal_24h` score `13.2449` n `167` status `ready` deltaP `22.7535` edge `1.0521` maxDD `-6.3373`
- `market_context_high->crypto_alt_24h` score `11.1798` n `167` status `ready` deltaP `28.9328` edge `0.9404` maxDD `-15.1306`
- `market_context_high->crypto_major_24h` score `10.3315` n `167` status `ready` deltaP `27.232` edge `0.7926` maxDD `-8.0553`
- `market_context_high->index_24h` score `3.8015` n `167` status `ready` deltaP `20.089` edge `0.2915` maxDD `-5.3574`
- `market_context_high->equity_24h` score `2.861` n `167` status `ready` deltaP `13.3359` edge `0.3822` maxDD `-14.2815`
- `market_context_high->equity_4h` score `1.0863` n `193` status `ready` deltaP `6.318` edge `0.1314` maxDD `-3.6396`
- `market_context_high->fx_24h` score `0.9955` n `167` status `ready` deltaP `19.4049` edge `0.0585` maxDD `-1.3925`
- `market_context_high->index_1h` score `-0.2436` n `193` status `ready` deltaP `2.7908` edge `0.0076` maxDD `-1.7205`
- `market_context_high->equity_1h` score `-0.2886` n `193` status `ready` deltaP `1.075` edge `0.0288` maxDD `-2.8014`
- `market_context_high->crypto_alt_4h` score `-0.5114` n `193` status `ready` deltaP `9.5839` edge `0.2025` maxDD `-19.5565`
- `market_context_high->fx_1h` score `-0.5241` n `193` status `ready` deltaP `-0.1443` edge `-0.003` maxDD `-0.3914`
- `market_context_high->crypto_alt_1h` score `-0.5633` n `193` status `ready` deltaP `1.6979` edge `0.0441` maxDD `-4.1892`
- `market_context_high->metal_1h` score `-0.6986` n `193` status `ready` deltaP `6.0617` edge `0.0036` maxDD `-6.3532`
- `market_context_high->crypto_major_4h` score `-0.971` n `193` status `ready` deltaP `5.5304` edge `0.1531` maxDD `-13.3376`
- `market_context_high->fx_4h` score `-0.9723` n `193` status `ready` deltaP `-3.3387` edge `-0.0095` maxDD `-1.4313`
- `market_context_high->crypto_major_1h` score `-0.9997` n `193` status `ready` deltaP `-0.8811` edge `0.0134` maxDD `-6.1883`
- `market_context_high->index_4h` score `-1.1177` n `193` status `ready` deltaP `-2.9161` edge `0.0352` maxDD `-3.7119`
- `market_context_high->metal_4h` score `-1.1651` n `193` status `ready` deltaP `11.414` edge `0.096` maxDD `-12.5349`
- `market_context_high->commodity_1h` score `-1.3028` n `193` status `ready` deltaP `-1.5947` edge `-0.0058` maxDD `-4.7041`
- `market_context_high->unknown_24h` score `-4.2164` n `167` status `ready` deltaP `-0.7204` edge `-0.0736` maxDD `-10.1706`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
