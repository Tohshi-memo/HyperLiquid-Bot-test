# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-13T01:07:41.091629+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9338`

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

- `risk_on_high->crypto_alt_4h` score `5.2293` n `48` status `ready` deltaP `20.7826` edge `0.342` maxDD `-1.9151`
- `risk_on_and_context->crypto_alt_4h` score `5.2293` n `48` status `ready` deltaP `20.7826` edge `0.342` maxDD `-1.9151`
- `risk_on_high->commodity_24h` score `4.627` n `34` status `ready` deltaP `30.087` edge `0.185` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `4.627` n `34` status `ready` deltaP `30.087` edge `0.185` maxDD `0.0`
- `market_context_high->crypto_alt_4h` score `4.5275` n `100` status `ready` deltaP `15.8659` edge `0.4164` maxDD `-9.2574`
- `risk_on_high->crypto_major_4h` score `4.2116` n `48` status `ready` deltaP `35.4167` edge `0.3891` maxDD `-4.1548`
- `risk_on_and_context->crypto_major_4h` score `4.2116` n `48` status `ready` deltaP `35.4167` edge `0.3891` maxDD `-4.1548`
- `market_context_high->crypto_major_4h` score `4.0888` n `100` status `ready` deltaP `19.25` edge `0.3683` maxDD `-7.4722`
- `market_context_high->crypto_alt_1h` score `0.6316` n `104` status `ready` deltaP `11.0894` edge `0.1138` maxDD `-5.8734`
- `market_context_high->crypto_major_1h` score `0.2629` n `104` status `ready` deltaP `4.2549` edge `0.0859` maxDD `-3.7781`
- `market_context_high->unknown_4h` score `-0.0875` n `100` status `ready` deltaP `-4.689` edge `0.0886` maxDD `-1.8373`
- `market_context_high->index_1h` score `-0.1067` n `104` status `ready` deltaP `3.5748` edge `0.0009` maxDD `-0.7394`
- `risk_on_high->crypto_major_1h` score `-0.2552` n `52` status `ready` deltaP `3.2934` edge `0.029` maxDD `-3.7781`
- `risk_on_and_context->crypto_major_1h` score `-0.2552` n `52` status `ready` deltaP `3.2934` edge `0.029` maxDD `-3.7781`
- `market_context_high->metal_1h` score `-0.3322` n `104` status `ready` deltaP `4.3586` edge `0.0015` maxDD `-0.8513`
- `market_context_high->metal_4h` score `-0.3396` n `100` status `ready` deltaP `8.6098` edge `0.0096` maxDD `-1.624`
- `market_context_high->fx_1h` score `-0.3628` n `104` status `ready` deltaP `-1.0799` edge `-0.0013` maxDD `-0.3742`
- `risk_on_high->crypto_alt_1h` score `-0.558` n `52` status `ready` deltaP `3.3971` edge `0.0084` maxDD `-5.8734`
- `risk_on_and_context->crypto_alt_1h` score `-0.558` n `52` status `ready` deltaP `3.3971` edge `0.0084` maxDD `-5.8734`
- `risk_on_high->fx_1h` score `-0.5893` n `52` status `ready` deltaP `-1.0799` edge `-0.0039` maxDD `-0.3742`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
