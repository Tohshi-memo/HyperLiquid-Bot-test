# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-15T15:37:38.902008+00:00`
- Price records: `672`
- Market context records: `4004`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10258`

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

- `risk_on_high->unknown_4h` score `146.782` n `40` status `ready` deltaP `-3.3232` edge `12.4352` maxDD `-10.8303`
- `risk_on_and_context->unknown_4h` score `146.782` n `40` status `ready` deltaP `-3.3232` edge `12.4352` maxDD `-10.8303`
- `market_context_high->unknown_24h` score `48.6942` n `135` status `ready` deltaP `-3.044` edge `4.48` maxDD `-24.1486`
- `market_context_high->unknown_4h` score `26.2862` n `147` status `ready` deltaP `3.1224` edge `2.7106` maxDD `-35.6052`
- `risk_on_high->equity_24h` score `8.75` n `40` status `ready` deltaP `41.3194` edge `0.4537` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `8.75` n `40` status `ready` deltaP `41.3194` edge `0.4537` maxDD `0.0`
- `risk_on_high->equity_4h` score `3.9504` n `40` status `ready` deltaP `37.8963` edge `0.0813` maxDD `-0.0458`
- `risk_on_and_context->equity_4h` score `3.9504` n `40` status `ready` deltaP `37.8963` edge `0.0813` maxDD `-0.0458`
- `market_context_high->index_24h` score `3.5004` n `135` status `ready` deltaP `26.7709` edge `0.1951` maxDD `-5.5496`
- `market_context_high->metal_24h` score `2.8413` n `135` status `ready` deltaP `14.9653` edge `0.2773` maxDD `-8.2238`
- `risk_on_high->index_24h` score `2.4334` n `40` status `ready` deltaP `28.9931` edge `0.0095` maxDD `0.0`
- `risk_on_and_context->index_24h` score `2.4334` n `40` status `ready` deltaP `28.9931` edge `0.0095` maxDD `0.0`
- `market_context_high->equity_4h` score `2.0171` n `147` status `ready` deltaP `19.9881` edge `0.1651` maxDD `-7.0879`
- `market_context_high->equity_24h` score `1.8051` n `135` status `ready` deltaP `16.875` edge `0.3409` maxDD `-14.5715`
- `risk_on_high->crypto_major_4h` score `1.451` n `40` status `ready` deltaP `20.3659` edge `0.0517` maxDD `-2.6576`
- `risk_on_and_context->crypto_major_4h` score `1.451` n `40` status `ready` deltaP `20.3659` edge `0.0517` maxDD `-2.6576`
- `market_context_high->metal_1h` score `1.1572` n `147` status `ready` deltaP `12.4221` edge `0.0611` maxDD `-1.7983`
- `risk_on_high->commodity_24h` score `1.0431` n `40` status `ready` deltaP `4.1667` edge `0.2873` maxDD `-12.9187`
- `risk_on_and_context->commodity_24h` score `1.0431` n `40` status `ready` deltaP `4.1667` edge `0.2873` maxDD `-12.9187`
- `market_context_high->crypto_major_1h` score `0.9777` n `147` status `ready` deltaP `9.9587` edge `0.0693` maxDD `-2.3372`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
