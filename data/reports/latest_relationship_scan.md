# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-15T02:52:32.943998+00:00`
- Price records: `672`
- Market context records: `3952`
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

- `risk_on_high->unknown_4h` score `144.0428` n `41` status `ready` deltaP `2.5915` edge `12.1675` maxDD `-10.8303`
- `risk_on_and_context->unknown_4h` score `144.0428` n `41` status `ready` deltaP `2.5915` edge `12.1675` maxDD `-10.8303`
- `market_context_high->unknown_24h` score `21.1854` n `155` status `ready` deltaP `-9.0524` edge `2.8679` maxDD `-72.7017`
- `market_context_high->unknown_4h` score `19.1832` n `166` status `ready` deltaP `-1.1258` edge `2.147` maxDD `-35.6052`
- `risk_on_high->equity_24h` score `9.2351` n `41` status `ready` deltaP `42.0139` edge `0.4895` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `9.2351` n `41` status `ready` deltaP `42.0139` edge `0.4895` maxDD `0.0`
- `risk_on_high->equity_4h` score `3.3638` n `41` status `ready` deltaP `36.1281` edge `0.0442` maxDD `-0.0458`
- `risk_on_and_context->equity_4h` score `3.3638` n `41` status `ready` deltaP `36.1281` edge `0.0442` maxDD `-0.0458`
- `market_context_high->index_24h` score `3.329` n `155` status `ready` deltaP `25.9901` edge `0.2181` maxDD `-7.1159`
- `market_context_high->metal_24h` score `3.3194` n `155` status `ready` deltaP `17.5236` edge `0.3113` maxDD `-9.1203`
- `market_context_high->equity_24h` score `3.0309` n `155` status `ready` deltaP `19.4333` edge `0.426` maxDD `-14.5715`
- `risk_on_high->index_24h` score `2.8605` n `41` status `ready` deltaP `29.8611` edge `0.0393` maxDD `0.0`
- `risk_on_and_context->index_24h` score `2.8605` n `41` status `ready` deltaP `29.8611` edge `0.0393` maxDD `0.0`
- `market_context_high->crypto_major_4h` score `2.1161` n `166` status `ready` deltaP `19.5599` edge `0.2026` maxDD `-7.8662`
- `market_context_high->equity_4h` score `1.9042` n `166` status `ready` deltaP `17.5121` edge `0.1722` maxDD `-7.0879`
- `risk_on_high->crypto_major_4h` score `1.8859` n `41` status `ready` deltaP `21.6463` edge `0.0794` maxDD `-2.6576`
- `risk_on_and_context->crypto_major_4h` score `1.8859` n `41` status `ready` deltaP `21.6463` edge `0.0794` maxDD `-2.6576`
- `market_context_high->metal_1h` score `0.8161` n `169` status `ready` deltaP `11.5597` edge `0.0545` maxDD `-2.751`
- `market_context_high->crypto_major_1h` score `0.7174` n `169` status `ready` deltaP `11.0823` edge `0.0847` maxDD `-4.904`
- `risk_on_high->commodity_24h` score `0.6239` n `41` status `ready` deltaP `3.5569` edge `0.2692` maxDD `-13.9406`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
