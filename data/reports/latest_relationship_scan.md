# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-15T05:07:31.423784+00:00`
- Price records: `672`
- Market context records: `3961`
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

- `risk_on_high->unknown_4h` score `148.2068` n `40` status `ready` deltaP `1.7073` edge `12.5204` maxDD `-10.8303`
- `risk_on_and_context->unknown_4h` score `148.2068` n `40` status `ready` deltaP `1.7073` edge `12.5204` maxDD `-10.8303`
- `market_context_high->unknown_24h` score `33.9568` n `146` status `ready` deltaP `-7.5128` edge `3.532` maxDD `-44.1745`
- `market_context_high->unknown_4h` score `22.3022` n `157` status `ready` deltaP `1.5321` edge `2.3892` maxDD `-35.6052`
- `risk_on_high->equity_24h` score `8.8739` n `40` status `ready` deltaP `42.0139` edge `0.4594` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `8.8739` n `40` status `ready` deltaP `42.0139` edge `0.4594` maxDD `0.0`
- `risk_on_high->equity_4h` score `3.387` n `40` status `ready` deltaP `37.439` edge `0.0374` maxDD `-0.0458`
- `risk_on_and_context->equity_4h` score `3.387` n `40` status `ready` deltaP `37.439` edge `0.0374` maxDD `-0.0458`
- `market_context_high->metal_24h` score `3.0869` n `146` status `ready` deltaP `16.1316` edge `0.3012` maxDD `-9.1203`
- `market_context_high->index_24h` score `3.0555` n `146` status `ready` deltaP `25.7515` edge `0.1969` maxDD `-7.1159`
- `risk_on_high->index_24h` score `2.6745` n `40` status `ready` deltaP `29.8611` edge `0.0238` maxDD `0.0`
- `risk_on_and_context->index_24h` score `2.6745` n `40` status `ready` deltaP `29.8611` edge `0.0238` maxDD `0.0`
- `market_context_high->equity_4h` score `2.3402` n `157` status `ready` deltaP `19.5568` edge `0.1949` maxDD `-7.0879`
- `market_context_high->crypto_major_4h` score `2.3161` n `157` status `ready` deltaP `19.8404` edge `0.2174` maxDD `-7.8662`
- `market_context_high->equity_24h` score `2.142` n `146` status `ready` deltaP `18.0413` edge `0.3612` maxDD `-14.5715`
- `risk_on_high->crypto_major_4h` score `1.6682` n `40` status `ready` deltaP `20.3659` edge `0.0698` maxDD `-2.6576`
- `risk_on_and_context->crypto_major_4h` score `1.6682` n `40` status `ready` deltaP `20.3659` edge `0.0698` maxDD `-2.6576`
- `market_context_high->crypto_major_1h` score `1.6469` n `168` status `ready` deltaP `12.639` edge `0.1072` maxDD `-2.3372`
- `risk_on_high->commodity_24h` score `1.0239` n `40` status `ready` deltaP `4.1667` edge `0.2857` maxDD `-12.9187`
- `risk_on_and_context->commodity_24h` score `1.0239` n `40` status `ready` deltaP `4.1667` edge `0.2857` maxDD `-12.9187`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
