# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-20T04:07:14.432857+00:00`
- Price records: `672`
- Market context records: `1285`
- Flow alert records: `5610`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8820`

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

- `market_context_high->crypto_major_24h` score `17.6413` n `128` status `ready` deltaP `41.5798` edge `1.3061` maxDD `-8.0553`
- `market_context_high->metal_24h` score `11.5054` n `128` status `ready` deltaP `8.1597` edge `1.0711` maxDD `-6.3373`
- `market_context_high->crypto_alt_24h` score `9.0463` n `128` status `ready` deltaP `26.1284` edge `0.7813` maxDD `-15.1306`
- `market_context_high->index_24h` score `5.5518` n `128` status `ready` deltaP `28.9931` edge `0.378` maxDD `-5.3574`
- `market_context_high->equity_24h` score `3.9078` n `128` status `ready` deltaP `25.3472` edge `0.5647` maxDD `-14.2815`
- `market_context_high->unknown_4h` score `2.5776` n `143` status `ready` deltaP `3.166` edge `0.3817` maxDD `-9.3738`
- `market_context_high->equity_4h` score `2.4138` n `143` status `ready` deltaP `12.2165` edge `0.1902` maxDD `-3.6396`
- `market_context_high->unknown_24h` score `2.3574` n `128` status `ready` deltaP `1.5625` edge `0.459` maxDD `-10.1706`
- `market_context_high->commodity_24h` score `1.4616` n `128` status `ready` deltaP `-13.7153` edge `0.3614` maxDD `-6.8535`
- `market_context_high->fx_24h` score `0.3362` n `128` status `ready` deltaP `5.816` edge `0.0357` maxDD `-0.3831`
- `market_context_high->index_4h` score `0.2947` n `143` status `ready` deltaP `7.2681` edge `0.0918` maxDD `-3.1979`
- `market_context_high->equity_1h` score `0.2796` n `152` status `ready` deltaP `4.172` edge `0.0382` maxDD `-1.7505`
- `market_context_high->metal_4h` score `0.2352` n `143` status `ready` deltaP `14.0841` edge `0.0688` maxDD `-6.4478`
- `market_context_high->index_1h` score `0.1253` n `152` status `ready` deltaP `6.5672` edge `0.0177` maxDD `-1.6329`
- `market_context_high->metal_1h` score `0.0299` n `152` status `ready` deltaP `9.7739` edge `0.0063` maxDD `-2.8509`
- `market_context_high->crypto_alt_1h` score `-0.3533` n `152` status `ready` deltaP `0.7446` edge `0.0368` maxDD `-3.6309`
- `market_context_high->fx_1h` score `-0.5449` n `152` status `ready` deltaP `0.5949` edge `-0.0038` maxDD `-0.3124`
- `market_context_high->crypto_major_1h` score `-0.7742` n `152` status `ready` deltaP `-0.4176` edge `0.0056` maxDD `-5.8323`
- `market_context_high->crypto_alt_4h` score `-0.8974` n `143` status `ready` deltaP `8.8212` edge `0.1581` maxDD `-19.5565`
- `market_context_high->crypto_major_4h` score `-0.9469` n `143` status `ready` deltaP `4.0177` edge `0.1227` maxDD `-13.3376`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
