# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-13T01:52:27.482655+00:00`
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

- `risk_on_high->crypto_alt_4h` score `5.2989` n `48` status `ready` deltaP `20.7826` edge `0.3478` maxDD `-1.9151`
- `risk_on_and_context->crypto_alt_4h` score `5.2989` n `48` status `ready` deltaP `20.7826` edge `0.3478` maxDD `-1.9151`
- `risk_on_high->commodity_24h` score `4.8994` n `37` status `ready` deltaP `30.087` edge `0.2077` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `4.8994` n `37` status `ready` deltaP `30.087` edge `0.2077` maxDD `0.0`
- `market_context_high->crypto_alt_4h` score `4.5971` n `100` status `ready` deltaP `15.8659` edge `0.4222` maxDD `-9.2574`
- `risk_on_high->crypto_major_4h` score `4.2482` n `48` status `ready` deltaP `35.4167` edge `0.3938` maxDD `-4.1548`
- `risk_on_and_context->crypto_major_4h` score `4.2482` n `48` status `ready` deltaP `35.4167` edge `0.3938` maxDD `-4.1548`
- `market_context_high->crypto_major_4h` score `4.1452` n `100` status `ready` deltaP `19.25` edge `0.373` maxDD `-7.4722`
- `market_context_high->crypto_alt_1h` score `1.2993` n `107` status `ready` deltaP `11.7186` edge `0.1369` maxDD `-5.8734`
- `market_context_high->crypto_major_1h` score `0.8205` n `107` status `ready` deltaP `5.1807` edge `0.1144` maxDD `-3.7781`
- `market_context_high->index_1h` score `-0.2611` n `107` status `ready` deltaP `2.119` edge `-0.0014` maxDD `-1.0297`
- `market_context_high->fx_1h` score `-0.2802` n `107` status `ready` deltaP `0.268` edge `0.0003` maxDD `-0.3742`
- `market_context_high->unknown_4h` score `-0.3049` n `100` status `ready` deltaP `-4.8415` edge `0.0715` maxDD `-1.8373`
- `market_context_high->metal_4h` score `-0.3384` n `100` status `ready` deltaP `8.6098` edge `0.0097` maxDD `-1.624`
- `risk_on_high->crypto_major_1h` score `-0.3704` n `52` status `ready` deltaP `2.8443` edge `0.0224` maxDD `-3.7781`
- `risk_on_and_context->crypto_major_1h` score `-0.3704` n `52` status `ready` deltaP `2.8443` edge `0.0224` maxDD `-3.7781`
- `market_context_high->metal_1h` score `-0.5283` n `107` status `ready` deltaP `2.8219` edge `0.0004` maxDD `-0.9556`
- `risk_on_high->fx_1h` score `-0.5893` n `52` status `ready` deltaP `-1.0799` edge `-0.0039` maxDD `-0.3742`
- `risk_on_and_context->fx_1h` score `-0.5893` n `52` status `ready` deltaP `-1.0799` edge `-0.0039` maxDD `-0.3742`
- `risk_on_high->metal_1h` score `-0.6157` n `52` status `ready` deltaP `-0.4491` edge `-0.0028` maxDD `-0.8513`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
