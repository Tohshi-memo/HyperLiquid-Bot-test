# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-18T08:22:32.598385+00:00`
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
- `risk_on_high->commodity_24h` score `8.8828` n `52` status `ready` deltaP `50.0` edge `0.4069` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `8.8828` n `52` status `ready` deltaP `50.0` edge `0.4069` maxDD `0.0`
- `market_context_high->commodity_24h` score `7.5837` n `149` status `ready` deltaP `43.2886` edge `0.3959` maxDD `-0.8682`
- `risk_on_high->commodity_4h` score `2.8643` n `52` status `ready` deltaP `32.8447` edge `0.0547` maxDD `-0.1313`
- `risk_on_and_context->commodity_4h` score `2.8643` n `52` status `ready` deltaP `32.8447` edge `0.0547` maxDD `-0.1313`
- `market_context_high->commodity_4h` score `2.764` n `149` status `ready` deltaP `29.347` edge `0.0765` maxDD `-0.345`
- `news_risk_high->crypto_alt_4h` score `2.6814` n `77` status `ready` deltaP `18.0809` edge `0.4383` maxDD `-12.8718`
- `market_context_high->commodity_1h` score `1.2092` n `149` status `ready` deltaP `16.9594` edge `0.0254` maxDD `-0.3491`
- `risk_on_high->fx_24h` score `1.1121` n `52` status `ready` deltaP `19.9519` edge `-0.0361` maxDD `-0.0054`
- `risk_on_and_context->fx_24h` score `1.1121` n `52` status `ready` deltaP `19.9519` edge `-0.0361` maxDD `-0.0054`
- `news_risk_high->equity_4h` score `1.0669` n `77` status `ready` deltaP `13.7215` edge `0.129` maxDD `-3.3619`
- `market_context_high->fx_24h` score `0.9773` n `149` status `ready` deltaP `17.177` edge `-0.0115` maxDD `-0.0593`
- `risk_on_high->commodity_1h` score `0.5859` n `52` status `ready` deltaP `10.0415` edge `0.0171` maxDD `-0.1507`
- `risk_on_and_context->commodity_1h` score `0.5859` n `52` status `ready` deltaP `10.0415` edge `0.0171` maxDD `-0.1507`
- `news_risk_high->equity_1h` score `0.4413` n `89` status `ready` deltaP `12.1712` edge `0.0276` maxDD `-1.8403`
- `news_risk_high->fx_4h` score `0.1985` n `77` status `ready` deltaP `7.0815` edge `0.0229` maxDD `-0.2398`
- `news_risk_high->index_1h` score `0.1217` n `89` status `ready` deltaP `6.0301` edge `0.0015` maxDD `-0.5244`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
