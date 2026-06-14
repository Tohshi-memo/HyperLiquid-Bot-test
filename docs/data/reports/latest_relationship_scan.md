# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-14T21:37:28.246649+00:00`
- Price records: `672`
- Market context records: `3930`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11443`

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

- `risk_on_high->unknown_4h` score `72.0778` n `51` status `ready` deltaP `-0.7173` edge `9.4597` maxDD `-13.467`
- `risk_on_and_context->unknown_4h` score `72.0778` n `51` status `ready` deltaP `-0.7173` edge `9.4597` maxDD `-13.467`
- `market_context_high->unknown_4h` score `14.1983` n `187` status `ready` deltaP `-3.3911` edge `1.7467` maxDD `-35.6052`
- `risk_on_high->equity_24h` score `11.2271` n `40` status `ready` deltaP `42.0139` edge `0.6555` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `11.2271` n `40` status `ready` deltaP `42.0139` edge `0.6555` maxDD `0.0`
- `risk_on_high->equity_4h` score `5.5242` n `51` status `ready` deltaP `38.6089` edge `0.2077` maxDD `-0.0458`
- `risk_on_and_context->equity_4h` score `5.5242` n `51` status `ready` deltaP `38.6089` edge `0.2077` maxDD `-0.0458`
- `risk_on_high->crypto_major_4h` score `4.9074` n `51` status `ready` deltaP `26.7755` edge `0.297` maxDD `-2.6576`
- `risk_on_and_context->crypto_major_4h` score `4.9074` n `51` status `ready` deltaP `26.7755` edge `0.297` maxDD `-2.6576`
- `risk_on_high->index_24h` score `4.4656` n `40` status `ready` deltaP `30.0347` edge `0.1719` maxDD `0.0`
- `risk_on_and_context->index_24h` score `4.4656` n `40` status `ready` deltaP `30.0347` edge `0.1719` maxDD `0.0`
- `market_context_high->equity_24h` score `3.9744` n `165` status `ready` deltaP `20.8018` edge `0.4955` maxDD `-14.5715`
- `market_context_high->index_24h` score `3.7248` n `165` status `ready` deltaP `25.7923` edge `0.2524` maxDD `-7.1159`
- `risk_on_high->crypto_major_1h` score `2.4868` n `51` status `ready` deltaP `13.9574` edge `0.1684` maxDD `-2.3372`
- `risk_on_and_context->crypto_major_1h` score `2.4868` n `51` status `ready` deltaP `13.9574` edge `0.1684` maxDD `-2.3372`
- `market_context_high->metal_24h` score `2.3623` n `165` status `ready` deltaP `15.8649` edge `0.2426` maxDD `-9.1203`
- `market_context_high->crypto_major_4h` score `2.2982` n `187` status `ready` deltaP `18.2193` edge `0.2465` maxDD `-9.4488`
- `risk_on_high->commodity_24h` score `1.9978` n `40` status `ready` deltaP `4.1667` edge `0.3239` maxDD `-11.1486`
- `risk_on_and_context->commodity_24h` score `1.9978` n `40` status `ready` deltaP `4.1667` edge `0.3239` maxDD `-11.1486`
- `market_context_high->equity_4h` score `1.5391` n `187` status `ready` deltaP `16.3273` edge `0.1898` maxDD `-8.2982`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
