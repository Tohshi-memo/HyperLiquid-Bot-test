# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-19T19:37:28.982250+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8502`

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

- `news_risk_high->crypto_major_24h` score `51.2255` n `72` status `ready` deltaP `27.7777` edge `4.1728` maxDD `-5.8019`
- `market_context_high->unknown_4h` score `45.0151` n `120` status `ready` deltaP `-3.5874` edge `3.7985` maxDD `-0.5326`
- `news_risk_high->crypto_alt_24h` score `44.7579` n `72` status `ready` deltaP `33.6806` edge `3.6432` maxDD `-9.3661`
- `risk_on_high->unknown_4h` score `30.4686` n `30` status `ready` deltaP `-18.5874` edge `2.6855` maxDD `-0.4694`
- `risk_on_and_context->unknown_4h` score `30.4686` n `30` status `ready` deltaP `-18.5874` edge `2.6855` maxDD `-0.4694`
- `risk_on_high->commodity_24h` score `10.1152` n `30` status `ready` deltaP `48.7847` edge `0.5177` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `10.1152` n `30` status `ready` deltaP `48.7847` edge `0.5177` maxDD `0.0`
- `news_risk_high->equity_24h` score `8.9557` n `72` status `ready` deltaP `37.3264` edge `0.5017` maxDD `-0.0053`
- `market_context_high->commodity_24h` score `7.7875` n `120` status `ready` deltaP `40.4514` edge `0.4318` maxDD `-0.8682`
- `news_risk_high->crypto_alt_4h` score `5.5788` n `98` status `ready` deltaP `20.8561` edge `0.4468` maxDD `-7.675`
- `news_risk_high->crypto_major_4h` score `4.2445` n `98` status `ready` deltaP `21.3134` edge `0.3374` maxDD `-8.0625`
- `news_risk_high->crypto_alt_1h` score `3.2568` n `98` status `ready` deltaP `18.7737` edge `0.1928` maxDD `-2.058`
- `market_context_high->commodity_4h` score `2.6299` n `120` status `ready` deltaP `27.2053` edge `0.0796` maxDD `-0.345`
- `news_risk_high->crypto_major_1h` score `2.3635` n `98` status `ready` deltaP `19.6719` edge `0.1181` maxDD `-2.8494`
- `risk_on_high->commodity_4h` score `2.2527` n `30` status `ready` deltaP `24.7053` edge `0.058` maxDD `-0.1313`
- `risk_on_and_context->commodity_4h` score `2.2527` n `30` status `ready` deltaP `24.7053` edge `0.058` maxDD `-0.1313`
- `news_risk_high->metal_24h` score `1.7273` n `72` status `ready` deltaP `22.5694` edge `0.0779` maxDD `-2.4203`
- `market_context_high->commodity_1h` score `1.442` n `120` status `ready` deltaP `17.9042` edge `0.026` maxDD `-0.3491`
- `news_risk_high->metal_4h` score `0.849` n `98` status `ready` deltaP `19.4344` edge `0.0466` maxDD `-2.0994`
- `risk_on_high->commodity_1h` score `0.7635` n `30` status `ready` deltaP `14.5709` edge `0.0193` maxDD `-0.1507`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
