# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-27T07:22:28.819538+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9638`

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

- `market_context_high->unknown_4h` score `79.8797` n `138` status `ready` deltaP `3.3448` edge `6.6679` maxDD `-1.0178`
- `market_context_high->unknown_1h` score `25.0163` n `138` status `ready` deltaP `0.8722` edge `2.1278` maxDD `-1.5807`
- `market_context_high->index_24h` score `1.2712` n `120` status `ready` deltaP `23.7738` edge `0.0305` maxDD `-2.3114`
- `market_context_high->fx_1h` score `0.5316` n `138` status `ready` deltaP `11.4922` edge `0.0035` maxDD `-0.1986`
- `market_context_high->fx_4h` score `0.4811` n `138` status `ready` deltaP `13.4611` edge `0.0102` maxDD `-0.4545`
- `market_context_high->metal_1h` score `0.1131` n `138` status `ready` deltaP `11.6354` edge `0.0116` maxDD `-1.3073`
- `market_context_high->metal_24h` score `-0.1531` n `120` status `ready` deltaP `18.004` edge `0.1129` maxDD `-6.204`
- `market_context_high->commodity_1h` score `-0.2163` n `138` status `ready` deltaP `2.9767` edge `0.0122` maxDD `-1.0053`
- `market_context_high->fx_24h` score `-0.4538` n `120` status `ready` deltaP `11.5728` edge `0.0219` maxDD `-1.2451`
- `market_context_high->crypto_major_1h` score `-0.4611` n `138` status `ready` deltaP `5.8926` edge `0.0299` maxDD `-6.9306`
- `market_context_high->index_1h` score `-0.574` n `138` status `ready` deltaP `-0.2278` edge `-0.0021` maxDD `-1.5978`
- `market_context_high->commodity_4h` score `-0.6647` n `138` status `ready` deltaP `4.3501` edge `0.0385` maxDD `-1.165`
- `market_context_high->metal_4h` score `-0.7625` n `138` status `ready` deltaP `9.6413` edge `0.0014` maxDD `-4.7416`
- `market_context_high->equity_1h` score `-1.4933` n `138` status `ready` deltaP `2.1912` edge `0.0001` maxDD `-10.4923`
- `market_context_high->crypto_alt_1h` score `-2.0269` n `138` status `ready` deltaP `-1.2345` edge `-0.0072` maxDD `-12.8878`
- `market_context_high->equity_24h` score `-2.3969` n `120` status `ready` deltaP `2.3541` edge `-0.0161` maxDD `-16.5513`
- `market_context_high->index_4h` score `-2.745` n `138` status `ready` deltaP `-4.0827` edge `-0.0239` maxDD `-5.8774`
- `market_context_high->crypto_major_4h` score `-3.6576` n `138` status `ready` deltaP `3.3934` edge `-0.0596` maxDD `-27.2224`
- `market_context_high->crypto_major_24h` score `-4.5899` n `120` status `ready` deltaP `-0.4997` edge `-0.0994` maxDD `-29.1905`
- `market_context_high->equity_4h` score `-5.1521` n `138` status `ready` deltaP `2.8566` edge `-0.1199` maxDD `-37.1067`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
