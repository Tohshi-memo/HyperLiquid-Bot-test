# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-18T05:37:12.811872+00:00`
- Price records: `672`
- Market context records: `1088`
- Flow alert records: `5036`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8786`

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

- `market_context_high->crypto_major_24h` score `16.5939` n `155` status `ready` deltaP `35.6513` edge `1.1915` maxDD `-3.3749`
- `market_context_high->crypto_alt_24h` score `5.8057` n `155` status `ready` deltaP `12.2414` edge `0.5256` maxDD `-9.5387`
- `market_context_high->equity_24h` score `5.6389` n `155` status `ready` deltaP `14.8609` edge `0.4205` maxDD `-3.6396`
- `market_context_high->metal_24h` score `4.7445` n `155` status `ready` deltaP `-2.7758` edge `0.5806` maxDD `-6.3373`
- `market_context_high->index_24h` score `4.6252` n `155` status `ready` deltaP `14.9905` edge `0.3163` maxDD `-2.1308`
- `market_context_high->equity_4h` score `1.9819` n `163` status `ready` deltaP `10.5885` edge `0.1609` maxDD `-3.6396`
- `market_context_high->crypto_major_4h` score `1.1536` n `163` status `ready` deltaP `11.8257` edge `0.1859` maxDD `-6.4882`
- `market_context_high->index_4h` score `0.9719` n `163` status `ready` deltaP `8.2794` edge `0.0941` maxDD `-2.1308`
- `market_context_high->index_1h` score `0.6592` n `173` status `ready` deltaP `8.7189` edge `0.0285` maxDD `-0.5353`
- `market_context_high->equity_1h` score `0.5484` n `173` status `ready` deltaP `3.6248` edge `0.0593` maxDD `-1.3546`
- `market_context_high->crypto_major_1h` score `0.1992` n `173` status `ready` deltaP `7.5707` edge `0.0427` maxDD `-4.1256`
- `market_context_high->fx_1h` score `0.0488` n `173` status `ready` deltaP `7.2505` edge `0.0013` maxDD `-0.3124`
- `market_context_high->metal_1h` score `-0.1024` n `173` status `ready` deltaP `7.2756` edge `0.004` maxDD `-2.2164`
- `market_context_high->crypto_alt_1h` score `-0.2413` n `173` status `ready` deltaP `2.9508` edge `0.0445` maxDD `-3.4088`
- `market_context_high->crypto_alt_4h` score `-0.3547` n `163` status `ready` deltaP `7.751` edge `0.1692` maxDD `-13.0347`
- `market_context_high->fx_4h` score `-0.5977` n `163` status `ready` deltaP `3.0918` edge `0.0024` maxDD `-1.6381`
- `market_context_high->commodity_1h` score `-0.6821` n `173` status `ready` deltaP `-0.9545` edge `-0.0003` maxDD `-3.7959`
- `market_context_high->metal_4h` score `-1.7352` n `163` status `ready` deltaP `5.7357` edge `-0.0653` maxDD `-9.2991`
- `market_context_high->unknown_4h` score `-2.2907` n `163` status `ready` deltaP `8.7545` edge `-0.1276` maxDD `-6.7322`
- `market_context_high->fx_24h` score `-3.1278` n `155` status `ready` deltaP `4.4596` edge `-0.0231` maxDD `-19.2774`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
