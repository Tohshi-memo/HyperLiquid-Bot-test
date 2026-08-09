# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-09T05:07:32.630781+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `8811`

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

- `market_context_high->equity_24h` score `3.5472` n `103` status `ready` deltaP `4.5729` edge `0.5711` maxDD `-21.1456`
- `market_context_high->metal_24h` score `2.6959` n `103` status `ready` deltaP `13.2535` edge `0.1939` maxDD `-2.2743`
- `market_context_high->commodity_4h` score `1.4045` n `134` status `ready` deltaP `15.4555` edge `0.0813` maxDD `-2.7169`
- `market_context_high->commodity_1h` score `0.9387` n `142` status `ready` deltaP `11.7336` edge `0.0343` maxDD `-0.7439`
- `market_context_high->fx_24h` score `0.8007` n `103` status `ready` deltaP `21.2277` edge `0.0478` maxDD `-1.9329`
- `market_context_high->index_24h` score `0.5407` n `103` status `ready` deltaP `9.1002` edge `0.1618` maxDD `-5.9181`
- `market_context_high->fx_4h` score `-0.2808` n `134` status `ready` deltaP `8.1042` edge `-0.0021` maxDD `-1.6928`
- `market_context_high->fx_1h` score `-0.3129` n `142` status `ready` deltaP `4.0757` edge `-0.0037` maxDD `-0.9639`
- `market_context_high->index_1h` score `-0.5138` n `142` status `ready` deltaP `-3.0657` edge `-0.0065` maxDD `-0.7809`
- `market_context_high->index_4h` score `-0.6832` n `134` status `ready` deltaP `-2.2616` edge `-0.012` maxDD `-1.1743`
- `market_context_high->metal_1h` score `-0.6841` n `142` status `ready` deltaP `-4.6681` edge `-0.007` maxDD `-0.9664`
- `market_context_high->equity_1h` score `-1.0017` n `142` status `ready` deltaP `-0.6031` edge `0.0034` maxDD `-4.6286`
- `market_context_high->metal_4h` score `-1.0941` n `134` status `ready` deltaP `-3.0875` edge `-0.0188` maxDD `-2.7373`
- `market_context_high->crypto_alt_1h` score `-1.9975` n `142` status `ready` deltaP `-10.7067` edge `-0.0309` maxDD `-2.4677`
- `market_context_high->equity_4h` score `-2.6803` n `134` status `ready` deltaP `-2.5095` edge `-0.0729` maxDD `-7.6983`
- `market_context_high->crypto_major_1h` score `-3.2159` n `142` status `ready` deltaP `-10.8459` edge `-0.0636` maxDD `-7.2335`
- `market_context_high->crypto_major_24h` score `-3.3175` n `103` status `ready` deltaP `6.2197` edge `-0.0685` maxDD `-14.2873`
- `market_context_high->crypto_alt_4h` score `-3.9761` n `134` status `ready` deltaP `-8.5047` edge `-0.109` maxDD `-6.585`
- `market_context_high->crypto_alt_24h` score `-4.555` n `103` status `ready` deltaP `-12.4461` edge `-0.1523` maxDD `-4.5445`
- `market_context_high->unknown_1h` score `-8.3372` n `142` status `ready` deltaP `-6.4877` edge `-0.6068` maxDD `-1.2437`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
