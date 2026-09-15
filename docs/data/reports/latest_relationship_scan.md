# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-15T21:08:04.454284+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `11685`

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

- `news_risk_high->unknown_4h` score `389.6568` n `79` status `ready` deltaP `-23.3406` edge `32.7164` maxDD `-4.1517`
- `news_risk_high->unknown_24h` score `25.8204` n `78` status `ready` deltaP `21.1806` edge `2.0105` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `23.8626` n `78` status `ready` deltaP `47.7698` edge `1.7092` maxDD `-1.4626`
- `news_risk_high->crypto_major_24h` score `19.6213` n `78` status `ready` deltaP `39.7303` edge `1.5173` maxDD `-9.098`
- `news_risk_high->equity_24h` score `15.6605` n `78` status `ready` deltaP `49.8531` edge `1.1501` maxDD `-6.5262`
- `news_risk_high->index_24h` score `8.3937` n `78` status `ready` deltaP `59.6821` edge `0.3192` maxDD `-0.075`
- `news_risk_high->metal_24h` score `6.6836` n `78` status `ready` deltaP `38.4882` edge `0.3458` maxDD `-0.6334`
- `risk_on_high->commodity_24h` score `5.9464` n `52` status `ready` deltaP `38.1944` edge `0.2409` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `5.9464` n `52` status `ready` deltaP `38.1944` edge `0.2409` maxDD `0.0`
- `market_context_high->commodity_24h` score `4.6494` n `137` status `ready` deltaP `30.8951` edge `0.234` maxDD `-0.8682`
- `risk_on_high->fx_24h` score `2.8469` n `52` status `ready` deltaP `35.5769` edge `0.0043` maxDD `-0.0054`
- `risk_on_and_context->fx_24h` score `2.8469` n `52` status `ready` deltaP `35.5769` edge `0.0043` maxDD `-0.0054`
- `market_context_high->fx_24h` score `2.4499` n `137` status `ready` deltaP `32.3905` edge `0.0098` maxDD `-0.0593`
- `risk_on_high->commodity_4h` score `1.681` n `52` status `ready` deltaP `23.3935` edge `0.0191` maxDD `-0.1313`
- `risk_on_and_context->commodity_4h` score `1.681` n `52` status `ready` deltaP `23.3935` edge `0.0191` maxDD `-0.1313`
- `market_context_high->commodity_4h` score `1.5807` n `149` status `ready` deltaP `19.8958` edge `0.0409` maxDD `-0.345`
- `market_context_high->commodity_1h` score `0.7359` n `149` status `ready` deltaP `12.6181` edge `0.0149` maxDD `-0.3491`
- `news_risk_high->index_4h` score `0.7059` n `79` status `ready` deltaP `17.3144` edge `0.0379` maxDD `-0.6935`
- `risk_on_high->commodity_1h` score `0.1126` n `52` status `ready` deltaP `5.7002` edge `0.0066` maxDD `-0.1507`
- `risk_on_and_context->commodity_1h` score `0.1126` n `52` status `ready` deltaP `5.7002` edge `0.0066` maxDD `-0.1507`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
