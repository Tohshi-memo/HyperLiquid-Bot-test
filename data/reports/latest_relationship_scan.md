# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-08T04:07:30.128872+00:00`
- Price records: `672`
- Market context records: `3246`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10598`

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

- `risk_on_high->crypto_major_4h` score `16.701` n `31` status `ready` deltaP `30.8517` edge `1.2983` maxDD `-5.9781`
- `risk_on_and_context->crypto_major_4h` score `16.701` n `31` status `ready` deltaP `30.8517` edge `1.2983` maxDD `-5.9781`
- `market_context_high->crypto_alt_24h` score `14.038` n `103` status `ready` deltaP `17.6088` edge `2.6665` maxDD `-70.3986`
- `market_context_high->commodity_24h` score `13.4867` n `103` status `ready` deltaP `48.1679` edge `0.8456` maxDD `-2.0927`
- `market_context_high->index_24h` score `9.4129` n `103` status `ready` deltaP `30.9685` edge `0.8334` maxDD `-16.1026`
- `market_context_high->equity_24h` score `6.3495` n `103` status `ready` deltaP `18.3539` edge `1.5333` maxDD `-53.663`
- `risk_on_high->crypto_alt_4h` score `5.171` n `31` status `ready` deltaP `12.1312` edge `0.7665` maxDD `-11.7537`
- `risk_on_and_context->crypto_alt_4h` score `5.171` n `31` status `ready` deltaP `12.1312` edge `0.7665` maxDD `-11.7537`
- `risk_on_high->equity_4h` score `4.2131` n `31` status `ready` deltaP `18.809` edge `0.5282` maxDD `-5.7426`
- `risk_on_and_context->equity_4h` score `4.2131` n `31` status `ready` deltaP `18.809` edge `0.5282` maxDD `-5.7426`
- `risk_on_high->crypto_major_1h` score `2.5775` n `31` status `ready` deltaP `10.3776` edge `0.3682` maxDD `-5.8885`
- `risk_on_and_context->crypto_major_1h` score `2.5775` n `31` status `ready` deltaP `10.3776` edge `0.3682` maxDD `-5.8885`
- `market_context_high->crypto_major_24h` score `2.096` n `103` status `ready` deltaP `21.6795` edge `2.1941` maxDD `-152.2601`
- `market_context_high->commodity_4h` score `2.0182` n `144` status `ready` deltaP `18.2249` edge `0.1425` maxDD `-3.9989`
- `risk_on_high->index_4h` score `1.585` n `31` status `ready` deltaP `5.7533` edge `0.2236` maxDD `-1.7001`
- `risk_on_and_context->index_4h` score `1.585` n `31` status `ready` deltaP `5.7533` edge `0.2236` maxDD `-1.7001`
- `risk_on_high->crypto_alt_1h` score `0.6911` n `31` status `ready` deltaP `3.559` edge `0.2086` maxDD `-8.1649`
- `risk_on_and_context->crypto_alt_1h` score `0.6911` n `31` status `ready` deltaP `3.559` edge `0.2086` maxDD `-8.1649`
- `risk_on_high->metal_1h` score `0.4732` n `31` status `ready` deltaP `8.0645` edge `0.0754` maxDD `-1.4793`
- `risk_on_and_context->metal_1h` score `0.4732` n `31` status `ready` deltaP `8.0645` edge `0.0754` maxDD `-1.4793`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
