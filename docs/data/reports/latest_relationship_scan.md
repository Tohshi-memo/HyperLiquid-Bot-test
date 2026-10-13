# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-13T00:52:23.512022+00:00`
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

- `risk_on_high->crypto_alt_4h` score `5.1885` n `48` status `ready` deltaP `20.7826` edge `0.3386` maxDD `-1.9151`
- `risk_on_and_context->crypto_alt_4h` score `5.1885` n `48` status `ready` deltaP `20.7826` edge `0.3386` maxDD `-1.9151`
- `risk_on_high->commodity_24h` score `4.5154` n `33` status `ready` deltaP `30.087` edge `0.1757` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `4.5154` n `33` status `ready` deltaP `30.087` edge `0.1757` maxDD `0.0`
- `market_context_high->crypto_alt_4h` score `4.4867` n `100` status `ready` deltaP `15.8659` edge `0.413` maxDD `-9.2574`
- `risk_on_high->crypto_major_4h` score `4.1866` n `48` status `ready` deltaP `35.4167` edge `0.3859` maxDD `-4.1548`
- `risk_on_and_context->crypto_major_4h` score `4.1866` n `48` status `ready` deltaP `35.4167` edge `0.3859` maxDD `-4.1548`
- `market_context_high->crypto_major_4h` score `4.0504` n `100` status `ready` deltaP `19.25` edge `0.3651` maxDD `-7.4722`
- `market_context_high->crypto_alt_1h` score `0.7827` n `103` status `ready` deltaP `11.6868` edge `0.1206` maxDD `-5.1861`
- `market_context_high->crypto_major_1h` score `0.2803` n `103` status `ready` deltaP `4.6` edge `0.0858` maxDD `-3.7757`
- `market_context_high->unknown_4h` score `-0.0035` n `100` status `ready` deltaP `-4.689` edge `0.0956` maxDD `-1.8373`
- `market_context_high->index_1h` score `-0.079` n `103` status `ready` deltaP `3.9287` edge `0.0013` maxDD `-0.6765`
- `risk_on_high->crypto_major_1h` score `-0.1992` n `51` status `ready` deltaP `4.1241` edge `0.0281` maxDD `-3.7757`
- `risk_on_and_context->crypto_major_1h` score `-0.1992` n `51` status `ready` deltaP `4.1241` edge `0.0281` maxDD `-3.7757`
- `market_context_high->metal_1h` score `-0.2805` n `103` status `ready` deltaP `4.741` edge `0.0013` maxDD `-0.8426`
- `market_context_high->metal_4h` score `-0.3408` n `100` status `ready` deltaP `8.6098` edge `0.0095` maxDD `-1.624`
- `risk_on_high->crypto_alt_1h` score `-0.3409` n `51` status `ready` deltaP `4.4529` edge `0.0206` maxDD `-5.1861`
- `risk_on_and_context->crypto_alt_1h` score `-0.3409` n `51` status `ready` deltaP `4.4529` edge `0.0206` maxDD `-5.1861`
- `market_context_high->fx_1h` score `-0.38` n `103` status `ready` deltaP `-1.3966` edge `-0.0014` maxDD `-0.3742`
- `risk_on_high->metal_1h` score `-0.5392` n `51` status `ready` deltaP `0.3816` edge `-0.0028` maxDD `-0.8426`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
