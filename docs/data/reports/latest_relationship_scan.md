# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-13T01:22:23.516260+00:00`
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

- `risk_on_high->crypto_alt_4h` score `5.2593` n `48` status `ready` deltaP `20.7826` edge `0.3445` maxDD `-1.9151`
- `risk_on_and_context->crypto_alt_4h` score `5.2593` n `48` status `ready` deltaP `20.7826` edge `0.3445` maxDD `-1.9151`
- `risk_on_high->commodity_24h` score `4.735` n `35` status `ready` deltaP `30.087` edge `0.194` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `4.735` n `35` status `ready` deltaP `30.087` edge `0.194` maxDD `0.0`
- `market_context_high->crypto_alt_4h` score `4.5575` n `100` status `ready` deltaP `15.8659` edge `0.4189` maxDD `-9.2574`
- `risk_on_high->crypto_major_4h` score `4.2287` n `48` status `ready` deltaP `35.4167` edge `0.3913` maxDD `-4.1548`
- `risk_on_and_context->crypto_major_4h` score `4.2287` n `48` status `ready` deltaP `35.4167` edge `0.3913` maxDD `-4.1548`
- `market_context_high->crypto_major_4h` score `4.1152` n `100` status `ready` deltaP `19.25` edge `0.3705` maxDD `-7.4722`
- `market_context_high->crypto_alt_1h` score `0.6569` n `105` status `ready` deltaP `11.306` edge `0.1156` maxDD `-5.8734`
- `market_context_high->crypto_major_1h` score `0.3301` n `105` status `ready` deltaP `4.5723` edge `0.0924` maxDD `-3.7781`
- `market_context_high->index_1h` score `-0.1461` n `105` status `ready` deltaP `3.0803` edge `0.0002` maxDD `-0.8237`
- `market_context_high->unknown_4h` score `-0.1631` n `100` status `ready` deltaP `-4.689` edge `0.0823` maxDD `-1.8373`
- `risk_on_high->crypto_major_1h` score `-0.2852` n `52` status `ready` deltaP `3.1437` edge `0.0275` maxDD `-3.7781`
- `risk_on_and_context->crypto_major_1h` score `-0.2852` n `52` status `ready` deltaP `3.1437` edge `0.0275` maxDD `-3.7781`
- `market_context_high->fx_1h` score `-0.3358` n `105` status `ready` deltaP `-0.622` edge `-0.0009` maxDD `-0.3742`
- `market_context_high->metal_4h` score `-0.3396` n `100` status `ready` deltaP `8.6098` edge `0.0096` maxDD `-1.624`
- `market_context_high->metal_1h` score `-0.3931` n `105` status `ready` deltaP `3.8366` edge `0.0014` maxDD `-0.8563`
- `risk_on_high->crypto_alt_1h` score `-0.5775` n `52` status `ready` deltaP `3.2474` edge `0.0069` maxDD `-5.8734`
- `risk_on_and_context->crypto_alt_1h` score `-0.5775` n `52` status `ready` deltaP `3.2474` edge `0.0069` maxDD `-5.8734`
- `risk_on_high->fx_1h` score `-0.5893` n `52` status `ready` deltaP `-1.0799` edge `-0.0039` maxDD `-0.3742`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
