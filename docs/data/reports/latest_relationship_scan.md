# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-18T18:22:35.205565+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8296`

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

- `market_context_high->unknown_4h` score `39.5802` n `149` status `ready` deltaP `-0.7683` edge `3.3268` maxDD `-0.5326`
- `news_risk_high->crypto_alt_24h` score `25.4746` n `36` status `ready` deltaP `32.6389` edge `2.0432` maxDD `-9.3661`
- `news_risk_high->crypto_major_24h` score `14.0809` n `36` status `ready` deltaP `5.7292` edge `1.8919` maxDD `-7.3212`
- `risk_on_high->unknown_4h` score `13.4589` n `52` status `ready` deltaP `-8.0089` edge `1.1975` maxDD `-0.4694`
- `risk_on_and_context->unknown_4h` score `13.4589` n `52` status `ready` deltaP `-8.0089` edge `1.1975` maxDD `-0.4694`
- `risk_on_high->commodity_24h` score `8.5985` n `52` status `ready` deltaP `47.9167` edge `0.3971` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `8.5985` n `52` status `ready` deltaP `47.9167` edge `0.3971` maxDD `0.0`
- `market_context_high->commodity_24h` score `7.2994` n `149` status `ready` deltaP `41.2053` edge `0.3861` maxDD `-0.8682`
- `news_risk_high->crypto_alt_4h` score `7.2715` n `89` status `ready` deltaP `24.6095` edge `0.567` maxDD `-7.675`
- `risk_on_high->commodity_4h` score `2.8067` n `52` status `ready` deltaP `32.8447` edge `0.0499` maxDD `-0.1313`
- `risk_on_and_context->commodity_4h` score `2.8067` n `52` status `ready` deltaP `32.8447` edge `0.0499` maxDD `-0.1313`
- `market_context_high->commodity_4h` score `2.7064` n `149` status `ready` deltaP `29.347` edge `0.0717` maxDD `-0.345`
- `news_risk_high->crypto_major_4h` score `1.7` n `89` status `ready` deltaP `15.965` edge `0.32` maxDD `-12.6788`
- `news_risk_high->equity_4h` score `1.6317` n `89` status `ready` deltaP `15.4905` edge `0.1227` maxDD `-4.1995`
- `news_risk_high->equity_24h` score `1.2752` n `36` status `ready` deltaP `8.8542` edge `0.2339` maxDD `-4.6884`
- `market_context_high->commodity_1h` score `1.1289` n `149` status `ready` deltaP `16.3606` edge `0.0227` maxDD `-0.3491`
- `news_risk_high->equity_1h` score `0.7518` n `89` status `ready` deltaP `11.6464` edge `0.0321` maxDD `-1.4342`
- `risk_on_high->commodity_1h` score `0.5056` n `52` status `ready` deltaP `9.4427` edge `0.0144` maxDD `-0.1507`
- `risk_on_and_context->commodity_1h` score `0.5056` n `52` status `ready` deltaP `9.4427` edge `0.0144` maxDD `-0.1507`
- `risk_on_high->fx_24h` score `0.4335` n `52` status `ready` deltaP `14.0491` edge `-0.0533` maxDD `-0.0054`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
