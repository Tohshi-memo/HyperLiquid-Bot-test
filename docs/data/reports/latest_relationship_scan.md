# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-13T03:22:28.628042+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9902`

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

- `risk_on_high->commodity_24h` score `5.2462` n `43` status `ready` deltaP `30.087` edge `0.2366` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `5.2462` n `43` status `ready` deltaP `30.087` edge `0.2366` maxDD `0.0`
- `risk_on_high->crypto_alt_4h` score `5.1185` n `49` status `ready` deltaP `19.142` edge `0.3437` maxDD `-1.9151`
- `risk_on_and_context->crypto_alt_4h` score `5.1185` n `49` status `ready` deltaP `19.142` edge `0.3437` maxDD `-1.9151`
- `market_context_high->crypto_alt_4h` score `4.5178` n `101` status `ready` deltaP `15.0401` edge `0.4211` maxDD `-9.2574`
- `risk_on_high->crypto_major_4h` score `4.2896` n `49` status `ready` deltaP `35.5369` edge `0.3983` maxDD `-4.1548`
- `risk_on_and_context->crypto_major_4h` score `4.2896` n `49` status `ready` deltaP `35.5369` edge `0.3983` maxDD `-4.1548`
- `market_context_high->crypto_major_4h` score `4.1525` n `101` status `ready` deltaP `19.3114` edge `0.3732` maxDD `-7.4722`
- `market_context_high->crypto_alt_1h` score `1.589` n `113` status `ready` deltaP `12.8054` edge `0.1538` maxDD `-5.8734`
- `market_context_high->crypto_major_1h` score `1.3004` n `113` status `ready` deltaP `6.8134` edge `0.1435` maxDD `-3.7781`
- `market_context_high->fx_1h` score `-0.3238` n `113` status `ready` deltaP `1.4138` edge `0.0016` maxDD `-0.3742`
- `market_context_high->unknown_4h` score `-0.3737` n `101` status `ready` deltaP `-4.786` edge `0.0654` maxDD `-1.8373`
- `market_context_high->metal_1h` score `-0.4047` n `113` status `ready` deltaP `4.854` edge `0.0027` maxDD `-0.9556`
- `market_context_high->metal_4h` score `-0.4532` n `101` status `ready` deltaP `8.0355` edge `0.0086` maxDD `-1.6615`
- `risk_on_high->crypto_major_1h` score `-0.5574` n `52` status `ready` deltaP `1.9461` edge `0.0128` maxDD `-3.7781`
- `risk_on_and_context->crypto_major_1h` score `-0.5574` n `52` status `ready` deltaP `1.9461` edge `0.0128` maxDD `-3.7781`
- `risk_on_high->fx_1h` score `-0.6302` n `52` status `ready` deltaP `-1.5304` edge `-0.0043` maxDD `-0.3742`
- `risk_on_and_context->fx_1h` score `-0.6302` n `52` status `ready` deltaP `-1.5304` edge `-0.0043` maxDD `-0.3742`
- `market_context_high->index_1h` score `-0.6381` n `113` status `ready` deltaP `-0.5607` edge `-0.0033` maxDD `-1.3154`
- `risk_on_high->metal_1h` score `-0.6468` n `52` status `ready` deltaP `-0.8982` edge `-0.0038` maxDD `-0.8513`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
