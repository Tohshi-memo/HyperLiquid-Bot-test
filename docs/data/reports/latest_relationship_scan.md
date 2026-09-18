# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-18T07:52:28.767754+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8284`

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

- `market_context_high->unknown_4h` score `39.8332` n `149` status `ready` deltaP `-0.0061` edge `3.3428` maxDD `-0.5326`
- `risk_on_high->unknown_4h` score `13.7119` n `52` status `ready` deltaP `-7.2467` edge `1.2135` maxDD `-0.4694`
- `risk_on_and_context->unknown_4h` score `13.7119` n `52` status `ready` deltaP `-7.2467` edge `1.2135` maxDD `-0.4694`
- `risk_on_high->commodity_24h` score `8.8852` n `52` status `ready` deltaP `50.0` edge `0.4071` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `8.8852` n `52` status `ready` deltaP `50.0` edge `0.4071` maxDD `0.0`
- `market_context_high->commodity_24h` score `7.5861` n `149` status `ready` deltaP `43.2886` edge `0.3961` maxDD `-0.8682`
- `risk_on_high->commodity_4h` score `2.8703` n `52` status `ready` deltaP `32.8447` edge `0.0552` maxDD `-0.1313`
- `risk_on_and_context->commodity_4h` score `2.8703` n `52` status `ready` deltaP `32.8447` edge `0.0552` maxDD `-0.1313`
- `market_context_high->commodity_4h` score `2.77` n `149` status `ready` deltaP `29.347` edge `0.077` maxDD `-0.345`
- `news_risk_high->crypto_alt_4h` score `2.7206` n `75` status `ready` deltaP `17.6931` edge `0.4459` maxDD `-12.8718`
- `market_context_high->commodity_1h` score `1.2104` n `149` status `ready` deltaP `16.9594` edge `0.0255` maxDD `-0.3491`
- `risk_on_high->fx_24h` score `1.1519` n `52` status `ready` deltaP `20.2991` edge `-0.0351` maxDD `-0.0054`
- `risk_on_and_context->fx_24h` score `1.1519` n `52` status `ready` deltaP `20.2991` edge `-0.0351` maxDD `-0.0054`
- `market_context_high->fx_24h` score `1.017` n `149` status `ready` deltaP `17.5242` edge `-0.0105` maxDD `-0.0593`
- `news_risk_high->equity_4h` score `0.9699` n `75` status `ready` deltaP `13.1606` edge `0.1203` maxDD `-3.3619`
- `risk_on_high->commodity_1h` score `0.5871` n `52` status `ready` deltaP `10.0415` edge `0.0172` maxDD `-0.1507`
- `risk_on_and_context->commodity_1h` score `0.5871` n `52` status `ready` deltaP `10.0415` edge `0.0172` maxDD `-0.1507`
- `news_risk_high->equity_1h` score `0.468` n `87` status `ready` deltaP `12.5662` edge `0.0284` maxDD `-1.8403`
- `news_risk_high->fx_4h` score `0.1647` n `75` status `ready` deltaP `6.4167` edge `0.023` maxDD `-0.2398`
- `news_risk_high->index_1h` score `0.0627` n `87` status `ready` deltaP `5.3221` edge `0.0013` maxDD `-0.5244`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
