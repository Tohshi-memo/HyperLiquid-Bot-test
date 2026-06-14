# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-14T19:22:41.211687+00:00`
- Price records: `672`
- Market context records: `3921`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11427`

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

- `risk_on_high->unknown_4h` score `61.2516` n `59` status `ready` deltaP `5.511` edge `8.0302` maxDD `-13.467`
- `risk_on_and_context->unknown_4h` score `61.2516` n `59` status `ready` deltaP `5.511` edge `8.0302` maxDD `-13.467`
- `risk_on_high->equity_24h` score `16.2575` n `39` status `ready` deltaP `42.0139` edge `1.0747` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `16.2575` n `39` status `ready` deltaP `42.0139` edge `1.0747` maxDD `0.0`
- `market_context_high->unknown_4h` score `12.9574` n `195` status `ready` deltaP `-1.5033` edge `1.6307` maxDD `-35.6052`
- `risk_on_high->crypto_major_4h` score `8.4596` n `59` status `ready` deltaP `29.5086` edge `0.5748` maxDD `-2.6576`
- `risk_on_and_context->crypto_major_4h` score `8.4596` n `59` status `ready` deltaP `29.5086` edge `0.5748` maxDD `-2.6576`
- `risk_on_high->equity_4h` score `6.5486` n `59` status `ready` deltaP `38.3785` edge `0.2946` maxDD `-0.0458`
- `risk_on_and_context->equity_4h` score `6.5486` n `59` status `ready` deltaP `38.3785` edge `0.2946` maxDD `-0.0458`
- `risk_on_high->index_24h` score `6.4372` n `39` status `ready` deltaP `30.0347` edge `0.3362` maxDD `0.0`
- `risk_on_and_context->index_24h` score `6.4372` n `39` status `ready` deltaP `30.0347` edge `0.3362` maxDD `0.0`
- `market_context_high->equity_24h` score `4.986` n `165` status `ready` deltaP `20.8018` edge `0.5798` maxDD `-14.5715`
- `risk_on_high->crypto_major_24h` score `4.8181` n `39` status `ready` deltaP `-12.0059` edge `0.9448` maxDD `-12.7642`
- `risk_on_and_context->crypto_major_24h` score `4.8181` n `39` status `ready` deltaP `-12.0059` edge `0.9448` maxDD `-12.7642`
- `market_context_high->index_24h` score `4.116` n `165` status `ready` deltaP `25.7923` edge `0.285` maxDD `-7.1159`
- `market_context_high->crypto_major_4h` score `3.3572` n `195` status `ready` deltaP `19.5912` edge `0.3256` maxDD `-9.4488`
- `risk_on_high->crypto_major_1h` score `3.0016` n `59` status `ready` deltaP `14.1074` edge `0.2103` maxDD `-2.3372`
- `risk_on_and_context->crypto_major_1h` score `3.0016` n `59` status `ready` deltaP `14.1074` edge `0.2103` maxDD `-2.3372`
- `market_context_high->metal_24h` score `2.5501` n `165` status `ready` deltaP `17.1622` edge `0.2496` maxDD `-9.1203`
- `market_context_high->equity_4h` score `1.8895` n `195` status `ready` deltaP `17.1529` edge `0.2135` maxDD `-8.2982`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
