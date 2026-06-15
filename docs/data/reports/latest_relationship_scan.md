# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-15T02:22:32.169948+00:00`
- Price records: `672`
- Market context records: `3950`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11267`

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

- `risk_on_high->unknown_4h` score `144.0392` n `41` status `ready` deltaP `2.5915` edge `12.1672` maxDD `-10.8303`
- `risk_on_and_context->unknown_4h` score `144.0392` n `41` status `ready` deltaP `2.5915` edge `12.1672` maxDD `-10.8303`
- `market_context_high->unknown_4h` score `18.5441` n `168` status `ready` deltaP `-1.7784` edge `2.0981` maxDD `-35.6052`
- `market_context_high->unknown_24h` score `18.5133` n `157` status `ready` deltaP `-9.3463` edge `2.7277` maxDD `-78.4762`
- `risk_on_high->equity_24h` score `9.2555` n `41` status `ready` deltaP `42.0139` edge `0.4912` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `9.2555` n `41` status `ready` deltaP `42.0139` edge `0.4912` maxDD `0.0`
- `risk_on_high->equity_4h` score `3.4314` n `41` status `ready` deltaP `36.433` edge `0.0478` maxDD `-0.0458`
- `risk_on_and_context->equity_4h` score `3.4314` n `41` status `ready` deltaP `36.433` edge `0.0478` maxDD `-0.0458`
- `market_context_high->metal_24h` score `3.3857` n `157` status `ready` deltaP `17.8112` edge `0.3149` maxDD `-9.1203`
- `market_context_high->index_24h` score `3.363` n `157` status `ready` deltaP `26.0394` edge `0.2206` maxDD `-7.1159`
- `market_context_high->equity_24h` score `3.1631` n `157` status `ready` deltaP `19.7209` edge `0.4351` maxDD `-14.5715`
- `risk_on_high->index_24h` score `2.8725` n `41` status `ready` deltaP `29.8611` edge `0.0403` maxDD `0.0`
- `risk_on_and_context->index_24h` score `2.8725` n `41` status `ready` deltaP `29.8611` edge `0.0403` maxDD `0.0`
- `market_context_high->crypto_major_4h` score `2.0236` n `168` status `ready` deltaP `19.0186` edge `0.1985` maxDD `-7.8662`
- `risk_on_high->crypto_major_4h` score `1.9427` n `41` status `ready` deltaP `21.9512` edge `0.0821` maxDD `-2.6576`
- `risk_on_and_context->crypto_major_4h` score `1.9427` n `41` status `ready` deltaP `21.9512` edge `0.0821` maxDD `-2.6576`
- `market_context_high->equity_4h` score `1.7489` n `168` status `ready` deltaP `16.9062` edge `0.1633` maxDD `-7.0879`
- `market_context_high->metal_1h` score `0.7436` n `169` status `ready` deltaP `11.1177` edge `0.0514` maxDD `-2.751`
- `market_context_high->crypto_major_1h` score `0.7078` n `169` status `ready` deltaP `11.0823` edge `0.0839` maxDD `-4.904`
- `risk_on_high->commodity_24h` score `0.6155` n `41` status `ready` deltaP `3.5569` edge `0.2685` maxDD `-13.9406`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
