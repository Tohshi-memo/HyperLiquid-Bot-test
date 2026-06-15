# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-15T04:22:32.865073+00:00`
- Price records: `672`
- Market context records: `3958`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11179`

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

- `risk_on_high->unknown_4h` score `148.1984` n `40` status `ready` deltaP `1.7073` edge `12.5197` maxDD `-10.8303`
- `risk_on_and_context->unknown_4h` score `148.1984` n `40` status `ready` deltaP `1.7073` edge `12.5197` maxDD `-10.8303`
- `market_context_high->unknown_24h` score `29.6785` n `149` status `ready` deltaP `-8.0677` edge `3.3018` maxDD `-53.3182`
- `market_context_high->unknown_4h` score `21.2082` n `160` status `ready` deltaP `0.4573` edge `2.3052` maxDD `-35.6052`
- `risk_on_high->equity_24h` score `8.8499` n `40` status `ready` deltaP `42.0139` edge `0.4574` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `8.8499` n `40` status `ready` deltaP `42.0139` edge `0.4574` maxDD `0.0`
- `risk_on_high->equity_4h` score `3.4101` n `40` status `ready` deltaP `37.5915` edge `0.0383` maxDD `-0.0458`
- `risk_on_and_context->equity_4h` score `3.4101` n `40` status `ready` deltaP `37.5915` edge `0.0383` maxDD `-0.0458`
- `market_context_high->index_24h` score `3.199` n `149` status `ready` deltaP `25.8343` edge `0.2083` maxDD `-7.1159`
- `market_context_high->metal_24h` score `3.1591` n `149` status `ready` deltaP `16.6143` edge `0.304` maxDD `-9.1203`
- `risk_on_high->index_24h` score `2.6601` n `40` status `ready` deltaP `29.8611` edge `0.0226` maxDD `0.0`
- `risk_on_and_context->index_24h` score `2.6601` n `40` status `ready` deltaP `29.8611` edge `0.0226` maxDD `0.0`
- `market_context_high->equity_24h` score `2.5622` n `149` status `ready` deltaP `18.524` edge `0.393` maxDD `-14.5715`
- `market_context_high->equity_4h` score `2.3041` n `160` status `ready` deltaP `19.4665` edge `0.1925` maxDD `-7.0879`
- `market_context_high->crypto_major_4h` score `2.2819` n `160` status `ready` deltaP `19.8933` edge `0.2142` maxDD `-7.8662`
- `risk_on_high->crypto_major_4h` score `1.6888` n `40` status `ready` deltaP `20.5183` edge `0.0705` maxDD `-2.6576`
- `risk_on_and_context->crypto_major_4h` score `1.6888` n `40` status `ready` deltaP `20.5183` edge `0.0705` maxDD `-2.6576`
- `market_context_high->crypto_major_1h` score `1.6289` n `168` status `ready` deltaP `12.639` edge `0.1057` maxDD `-2.3372`
- `risk_on_high->commodity_24h` score `1.0431` n `40` status `ready` deltaP `4.1667` edge `0.2873` maxDD `-12.9187`
- `risk_on_and_context->commodity_24h` score `1.0431` n `40` status `ready` deltaP `4.1667` edge `0.2873` maxDD `-12.9187`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
