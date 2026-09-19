# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-19T16:47:26.604070+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8654`

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

- `news_risk_high->crypto_major_24h` score `51.8259` n `72` status `ready` deltaP `29.6875` edge `4.2101` maxDD `-5.8019`
- `news_risk_high->crypto_alt_24h` score `45.4528` n `72` status `ready` deltaP `34.8959` edge `3.693` maxDD `-9.3661`
- `market_context_high->unknown_4h` score `44.0258` n `131` status `ready` deltaP `-3.2187` edge `3.7136` maxDD `-0.5326`
- `risk_on_high->unknown_4h` score `19.9752` n `41` status `ready` deltaP `-13.7195` edge `1.7786` maxDD `-0.4694`
- `risk_on_and_context->unknown_4h` score `19.9752` n `41` status `ready` deltaP `-13.7195` edge `1.7786` maxDD `-0.4694`
- `news_risk_high->equity_24h` score `9.5489` n `72` status `ready` deltaP `39.2361` edge `0.5384` maxDD `-0.0053`
- `risk_on_high->commodity_24h` score `9.0994` n `41` status `ready` deltaP `47.7431` edge `0.44` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `9.0994` n `41` status `ready` deltaP `47.7431` edge `0.44` maxDD `0.0`
- `market_context_high->commodity_24h` score `7.5129` n `131` status `ready` deltaP `40.1095` edge `0.4112` maxDD `-0.8682`
- `news_risk_high->crypto_alt_4h` score `5.765` n `98` status `ready` deltaP `21.9232` edge `0.4552` maxDD `-7.675`
- `news_risk_high->crypto_major_4h` score `4.3219` n `98` status `ready` deltaP `21.7707` edge `0.3408` maxDD `-8.0625`
- `news_risk_high->crypto_alt_1h` score `3.3347` n `98` status `ready` deltaP `19.5222` edge `0.1943` maxDD `-2.058`
- `market_context_high->commodity_4h` score `2.5482` n `131` status `ready` deltaP `27.0992` edge `0.0735` maxDD `-0.345`
- `news_risk_high->crypto_major_1h` score `2.4186` n `98` status `ready` deltaP `20.2707` edge `0.1187` maxDD `-2.8494`
- `risk_on_high->commodity_4h` score `2.3954` n `41` status `ready` deltaP `28.0488` edge `0.0476` maxDD `-0.1313`
- `risk_on_and_context->commodity_4h` score `2.3954` n `41` status `ready` deltaP `28.0488` edge `0.0476` maxDD `-0.1313`
- `news_risk_high->metal_24h` score `1.7249` n `72` status `ready` deltaP `22.5694` edge `0.0777` maxDD `-2.4203`
- `market_context_high->commodity_1h` score `1.5166` n `131` status `ready` deltaP `18.8966` edge `0.0256` maxDD `-0.3491`
- `risk_on_high->commodity_1h` score `1.4987` n `41` status `ready` deltaP `18.6359` edge `0.0192` maxDD `-0.1507`
- `risk_on_and_context->commodity_1h` score `1.4987` n `41` status `ready` deltaP `18.6359` edge `0.0192` maxDD `-0.1507`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
