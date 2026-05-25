# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-25T01:22:18.128960+00:00`
- Price records: `672`
- Market context records: `1796`
- Flow alert records: `7065`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8872`

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

- `market_context_high->metal_24h` score `7.1769` n `189` status `ready` deltaP `28.5714` edge `0.6502` maxDD `-12.7414`
- `news_risk_high->commodity_4h` score `6.451` n `30` status `ready` deltaP `29.2582` edge `0.408` maxDD `-3.5713`
- `market_context_high->crypto_alt_4h` score `5.7754` n `194` status `ready` deltaP `21.5551` edge `0.5142` maxDD `-9.1295`
- `market_context_high->crypto_major_4h` score `4.569` n `194` status `ready` deltaP `23.2619` edge `0.4534` maxDD `-9.8853`
- `market_context_high->unknown_4h` score `3.9407` n `194` status `ready` deltaP `16.0234` edge `0.4372` maxDD `-10.2508`
- `news_risk_high->commodity_1h` score `3.2686` n `30` status `ready` deltaP `24.8703` edge `0.1383` maxDD `-1.2043`
- `market_context_high->equity_4h` score `2.9311` n `194` status `ready` deltaP `16.322` edge `0.2449` maxDD `-5.0894`
- `market_context_high->index_24h` score `2.7187` n `189` status `ready` deltaP `13.7401` edge `0.2578` maxDD `-4.1604`
- `market_context_high->equity_24h` score `1.4976` n `189` status `ready` deltaP `15.1869` edge `0.5134` maxDD `-33.1875`
- `market_context_high->unknown_24h` score `0.9488` n `189` status `ready` deltaP `12.3016` edge `0.5291` maxDD `-35.8966`
- `market_context_high->index_4h` score `0.8827` n `194` status `ready` deltaP `12.4591` edge `0.0994` maxDD `-3.7119`
- `news_risk_high->fx_4h` score `0.8672` n `30` status `ready` deltaP `21.1789` edge `-0.0028` maxDD `-0.1774`
- `news_risk_high->unknown_4h` score `0.4356` n `30` status `ready` deltaP `10.2845` edge `0.0596` maxDD `-2.7857`
- `market_context_high->crypto_alt_1h` score `0.3746` n `196` status `ready` deltaP `7.2712` edge `0.0939` maxDD `-4.8924`
- `market_context_high->crypto_major_1h` score `0.2465` n `196` status `ready` deltaP `5.1082` edge `0.0851` maxDD `-3.2225`
- `market_context_high->equity_1h` score `-0.0973` n `196` status `ready` deltaP `4.3108` edge `0.044` maxDD `-2.8014`
- `market_context_high->index_1h` score `-0.3633` n `196` status `ready` deltaP `2.4747` edge `0.0164` maxDD `-1.7205`
- `market_context_high->fx_24h` score `-0.3898` n `189` status `ready` deltaP `9.003` edge `0.0124` maxDD `-1.3925`
- `market_context_high->metal_4h` score `-0.3948` n `194` status `ready` deltaP `12.1606` edge `0.1375` maxDD `-12.5349`
- `news_risk_high->unknown_1h` score `-0.3967` n `30` status `ready` deltaP `17.1557` edge `-0.118` maxDD `-2.1115`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
