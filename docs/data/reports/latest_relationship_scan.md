# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-18T15:07:30.862223+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8438`

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

- `market_context_high->unknown_4h` score `39.937` n `149` status `ready` deltaP `-0.4634` edge `3.3545` maxDD `-0.5326`
- `risk_on_high->unknown_4h` score `13.8157` n `52` status `ready` deltaP `-7.704` edge `1.2252` maxDD `-0.4694`
- `risk_on_and_context->unknown_4h` score `13.8157` n `52` status `ready` deltaP `-7.704` edge `1.2252` maxDD `-0.4694`
- `news_risk_high->crypto_alt_24h` score `12.7908` n `35` status `ready` deltaP `24.886` edge `1.0379` maxDD `-9.3661`
- `risk_on_high->commodity_24h` score `8.704` n `52` status `ready` deltaP `48.7847` edge `0.4001` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `8.704` n `52` status `ready` deltaP `48.7847` edge `0.4001` maxDD `0.0`
- `market_context_high->commodity_24h` score `7.4048` n `149` status `ready` deltaP `42.0733` edge `0.3891` maxDD `-0.8682`
- `news_risk_high->crypto_alt_4h` score `3.237` n `95` status `ready` deltaP `21.3398` edge `0.4878` maxDD `-12.8718`
- `news_risk_high->crypto_major_24h` score `3.1945` n `35` status `ready` deltaP `-10.2679` edge `0.6775` maxDD `-13.2931`
- `risk_on_high->commodity_4h` score `2.7763` n `52` status `ready` deltaP `32.5399` edge `0.0494` maxDD `-0.1313`
- `risk_on_and_context->commodity_4h` score `2.7763` n `52` status `ready` deltaP `32.5399` edge `0.0494` maxDD `-0.1313`
- `market_context_high->commodity_4h` score `2.676` n `149` status `ready` deltaP `29.0422` edge `0.0712` maxDD `-0.345`
- `market_context_high->commodity_1h` score `1.0941` n `149` status `ready` deltaP `16.0612` edge `0.0218` maxDD `-0.3491`
- `news_risk_high->equity_4h` score `0.7115` n `95` status `ready` deltaP `12.6861` edge `0.1008` maxDD `-4.1995`
- `risk_on_high->fx_24h` score `0.6729` n `52` status `ready` deltaP `16.3061` edge `-0.0484` maxDD `-0.0054`
- `risk_on_and_context->fx_24h` score `0.6729` n `52` status `ready` deltaP `16.3061` edge `-0.0484` maxDD `-0.0054`
- `market_context_high->fx_24h` score `0.538` n `149` status `ready` deltaP `13.5312` edge `-0.0238` maxDD `-0.0593`
- `risk_on_high->commodity_1h` score `0.4709` n `52` status `ready` deltaP `9.1433` edge `0.0135` maxDD `-0.1507`
- `risk_on_and_context->commodity_1h` score `0.4709` n `52` status `ready` deltaP `9.1433` edge `0.0135` maxDD `-0.1507`
- `news_risk_high->crypto_major_4h` score `0.3925` n `95` status `ready` deltaP `13.405` edge `0.2856` maxDD `-19.972`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
