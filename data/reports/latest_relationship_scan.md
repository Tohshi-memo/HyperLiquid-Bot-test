# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-13T03:37:26.565902+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9686`

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

- `risk_on_high->crypto_alt_4h` score `5.338` n `50` status `ready` deltaP `19.561` edge `0.3592` maxDD `-1.9151`
- `risk_on_and_context->crypto_alt_4h` score `5.338` n `50` status `ready` deltaP `19.561` edge `0.3592` maxDD `-1.9151`
- `risk_on_high->commodity_24h` score `5.2882` n `44` status `ready` deltaP `30.087` edge `0.2401` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `5.2882` n `44` status `ready` deltaP `30.087` edge `0.2401` maxDD `0.0`
- `market_context_high->crypto_alt_4h` score `4.6032` n `102` status `ready` deltaP `15.2081` edge `0.4271` maxDD `-9.2574`
- `risk_on_high->crypto_major_4h` score `4.5111` n `50` status `ready` deltaP `35.7927` edge `0.425` maxDD `-4.1548`
- `risk_on_and_context->crypto_major_4h` score `4.5111` n `50` status `ready` deltaP `35.7927` edge `0.425` maxDD `-4.1548`
- `market_context_high->crypto_major_4h` score `4.3106` n `102` status `ready` deltaP `19.5182` edge `0.385` maxDD `-7.4722`
- `market_context_high->crypto_alt_1h` score `1.6607` n `114` status `ready` deltaP `12.9662` edge `0.1587` maxDD `-5.8734`
- `market_context_high->crypto_major_1h` score `1.3573` n `114` status `ready` deltaP `7.0596` edge `0.1466` maxDD `-3.7781`
- `market_context_high->unknown_4h` score `0.065` n `102` status `ready` deltaP `-4.5821` edge `0.1006` maxDD `-1.8373`
- `market_context_high->fx_1h` score `-0.285` n `114` status `ready` deltaP `1.8097` edge `0.0022` maxDD `-0.3742`
- `market_context_high->metal_4h` score `-0.5582` n `102` status `ready` deltaP `7.4725` edge `0.0082` maxDD `-1.6961`
- `risk_on_high->crypto_major_1h` score `-0.585` n `52` status `ready` deltaP `1.7964` edge `0.0115` maxDD `-3.7781`
- `risk_on_and_context->crypto_major_1h` score `-0.585` n `52` status `ready` deltaP `1.7964` edge `0.0115` maxDD `-3.7781`
- `market_context_high->metal_1h` score `-0.5892` n `114` status `ready` deltaP `5.2422` edge `0.0029` maxDD `-0.9556`
- `market_context_high->index_1h` score `-0.612` n `114` status `ready` deltaP `-0.1027` edge `-0.003` maxDD `-1.3154`
- `risk_on_high->fx_1h` score `-0.6314` n `52` status `ready` deltaP `-1.5304` edge `-0.0044` maxDD `-0.3742`
- `risk_on_and_context->fx_1h` score `-0.6314` n `52` status `ready` deltaP `-1.5304` edge `-0.0044` maxDD `-0.3742`
- `risk_on_high->metal_1h` score `-0.6468` n `52` status `ready` deltaP `-0.8982` edge `-0.0038` maxDD `-0.8513`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
