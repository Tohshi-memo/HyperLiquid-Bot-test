# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-13T10:22:34.025006+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9798`

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

- `market_context_high->crypto_alt_4h` score `7.8426` n `117` status `ready` deltaP `20.2705` edge `0.6633` maxDD `-9.2574`
- `market_context_high->crypto_major_4h` score `6.9553` n `117` status `ready` deltaP `24.0163` edge `0.5754` maxDD `-7.4722`
- `risk_on_high->crypto_alt_4h` score `6.4315` n `54` status `ready` deltaP `22.5497` edge `0.4304` maxDD `-1.9151`
- `risk_on_and_context->crypto_alt_4h` score `6.4315` n `54` status `ready` deltaP `22.5497` edge `0.4304` maxDD `-1.9151`
- `risk_on_high->commodity_24h` score `5.5886` n `48` status `ready` deltaP `30.7826` edge `0.2605` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `5.5886` n `48` status `ready` deltaP `30.7826` edge `0.2605` maxDD `0.0`
- `risk_on_high->crypto_major_4h` score `5.0607` n `54` status `ready` deltaP `37.1217` edge `0.4866` maxDD `-4.1548`
- `risk_on_and_context->crypto_major_4h` score `5.0607` n `54` status `ready` deltaP `37.1217` edge `0.4866` maxDD `-4.1548`
- `market_context_high->unknown_4h` score `2.6934` n `117` status `ready` deltaP `-3.467` edge `0.3122` maxDD `-1.8373`
- `market_context_high->crypto_alt_1h` score `2.0541` n `117` status `ready` deltaP `14.6144` edge `0.1805` maxDD `-5.8734`
- `market_context_high->crypto_major_1h` score `1.5415` n `117` status `ready` deltaP `7.7576` edge `0.1573` maxDD `-3.7781`
- `market_context_high->metal_4h` score `0.068` n `117` status `ready` deltaP `12.2408` edge `0.0286` maxDD `-1.6961`
- `risk_on_high->crypto_major_1h` score `-0.1544` n `54` status `ready` deltaP `3.1992` edge `0.0311` maxDD `-3.7781`
- `risk_on_and_context->crypto_major_1h` score `-0.1544` n `54` status `ready` deltaP `3.1992` edge `0.0311` maxDD `-3.7781`
- `market_context_high->fx_1h` score `-0.2663` n `117` status `ready` deltaP `1.9982` edge `0.0025` maxDD `-0.3742`
- `risk_on_high->crypto_alt_1h` score `-0.398` n `54` status `ready` deltaP `4.358` edge `0.0225` maxDD `-5.8734`
- `risk_on_and_context->crypto_alt_1h` score `-0.398` n `54` status `ready` deltaP `4.358` edge `0.0225` maxDD `-5.8734`
- `market_context_high->metal_1h` score `-0.4991` n `117` status `ready` deltaP `6.0674` edge `0.0049` maxDD `-0.9556`
- `risk_on_high->metal_1h` score `-0.5388` n `54` status `ready` deltaP `0.6543` edge `-0.0003` maxDD `-0.8513`
- `risk_on_and_context->metal_1h` score `-0.5388` n `54` status `ready` deltaP `0.6543` edge `-0.0003` maxDD `-0.8513`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
