# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-18T08:37:26.667155+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8306`

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

- `market_context_high->unknown_4h` score `39.8054` n `149` status `ready` deltaP `-0.1586` edge `3.3415` maxDD `-0.5326`
- `risk_on_high->unknown_4h` score `13.6841` n `52` status `ready` deltaP `-7.3992` edge `1.2122` maxDD `-0.4694`
- `risk_on_and_context->unknown_4h` score `13.6841` n `52` status `ready` deltaP `-7.3992` edge `1.2122` maxDD `-0.4694`
- `risk_on_high->commodity_24h` score `8.8792` n `52` status `ready` deltaP `50.0` edge `0.4066` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `8.8792` n `52` status `ready` deltaP `50.0` edge `0.4066` maxDD `0.0`
- `market_context_high->commodity_24h` score `7.5801` n `149` status `ready` deltaP `43.2886` edge `0.3956` maxDD `-0.8682`
- `risk_on_high->commodity_4h` score `2.8607` n `52` status `ready` deltaP `32.8447` edge `0.0544` maxDD `-0.1313`
- `risk_on_and_context->commodity_4h` score `2.8607` n `52` status `ready` deltaP `32.8447` edge `0.0544` maxDD `-0.1313`
- `market_context_high->commodity_4h` score `2.7604` n `149` status `ready` deltaP `29.347` edge `0.0762` maxDD `-0.345`
- `news_risk_high->crypto_alt_4h` score `2.6979` n `78` status `ready` deltaP `18.2614` edge `0.4392` maxDD `-12.8718`
- `market_context_high->commodity_1h` score `1.19` n `149` status `ready` deltaP `16.8097` edge `0.0248` maxDD `-0.3491`
- `news_risk_high->equity_4h` score `1.1252` n `78` status `ready` deltaP `14.1377` edge `0.1337` maxDD `-3.3619`
- `risk_on_high->fx_24h` score `1.0911` n `52` status `ready` deltaP `19.7783` edge `-0.0367` maxDD `-0.0054`
- `risk_on_and_context->fx_24h` score `1.0911` n `52` status `ready` deltaP `19.7783` edge `-0.0367` maxDD `-0.0054`
- `market_context_high->fx_24h` score `0.9562` n `149` status `ready` deltaP `17.0034` edge `-0.0121` maxDD `-0.0593`
- `risk_on_high->commodity_1h` score `0.5667` n `52` status `ready` deltaP `9.8918` edge `0.0165` maxDD `-0.1507`
- `risk_on_and_context->commodity_1h` score `0.5667` n `52` status `ready` deltaP `9.8918` edge `0.0165` maxDD `-0.1507`
- `news_risk_high->equity_1h` score `0.4116` n `90` status `ready` deltaP `11.6467` edge `0.0273` maxDD `-1.8403`
- `news_risk_high->fx_4h` score `0.214` n `78` status `ready` deltaP `7.3953` edge `0.0228` maxDD `-0.2398`
- `news_risk_high->index_1h` score `0.0814` n `90` status `ready` deltaP `5.5556` edge `0.0013` maxDD `-0.5244`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
