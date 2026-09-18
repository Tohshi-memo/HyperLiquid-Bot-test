# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-18T05:07:29.720984+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8616`

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

- `market_context_high->unknown_4h` score `40.2412` n `149` status `ready` deltaP `-0.0061` edge `3.3768` maxDD `-0.5326`
- `risk_on_high->unknown_4h` score `14.1199` n `52` status `ready` deltaP `-7.2467` edge `1.2475` maxDD `-0.4694`
- `risk_on_and_context->unknown_4h` score `14.1199` n `52` status `ready` deltaP `-7.2467` edge `1.2475` maxDD `-0.4694`
- `risk_on_high->commodity_24h` score `8.9416` n `52` status `ready` deltaP `50.0` edge `0.4118` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `8.9416` n `52` status `ready` deltaP `50.0` edge `0.4118` maxDD `0.0`
- `market_context_high->commodity_24h` score `7.6425` n `149` status `ready` deltaP `43.2886` edge `0.4008` maxDD `-0.8682`
- `risk_on_high->commodity_4h` score `2.9195` n `52` status `ready` deltaP `32.8447` edge `0.0593` maxDD `-0.1313`
- `risk_on_and_context->commodity_4h` score `2.9195` n `52` status `ready` deltaP `32.8447` edge `0.0593` maxDD `-0.1313`
- `market_context_high->commodity_4h` score `2.8192` n `149` status `ready` deltaP `29.347` edge `0.0811` maxDD `-0.345`
- `news_risk_high->crypto_alt_24h` score `2.2658` n `30` status `ready` deltaP `21.4236` edge `0.1839` maxDD `-9.3661`
- `news_risk_high->crypto_alt_4h` score `1.9243` n `68` status `ready` deltaP `13.6837` edge `0.3811` maxDD `-13.05`
- `news_risk_high->index_24h` score `1.812` n `30` status `ready` deltaP `14.8958` edge `0.0693` maxDD `-0.075`
- `risk_on_high->fx_24h` score `1.3659` n `52` status `ready` deltaP `22.2088` edge `-0.03` maxDD `-0.0054`
- `risk_on_and_context->fx_24h` score `1.3659` n `52` status `ready` deltaP `22.2088` edge `-0.03` maxDD `-0.0054`
- `market_context_high->fx_24h` score `1.231` n `149` status `ready` deltaP `19.4339` edge `-0.0054` maxDD `-0.0593`
- `market_context_high->commodity_1h` score `1.226` n `149` status `ready` deltaP `17.1091` edge `0.0258` maxDD `-0.3491`
- `risk_on_high->commodity_1h` score `0.6027` n `52` status `ready` deltaP `10.1912` edge `0.0175` maxDD `-0.1507`
- `risk_on_and_context->commodity_1h` score `0.6027` n `52` status `ready` deltaP `10.1912` edge `0.0175` maxDD `-0.1507`
- `news_risk_high->equity_4h` score `0.2814` n `68` status `ready` deltaP `9.7292` edge `0.0549` maxDD `-3.3619`
- `news_risk_high->equity_1h` score `0.1431` n `78` status `ready` deltaP `8.2067` edge `0.0158` maxDD `-1.8403`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
