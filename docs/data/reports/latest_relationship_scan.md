# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-24T20:37:28.908743+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `7836`

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

- `market_context_high->unknown_4h` score `17.4382` n `102` status `ready` deltaP `-2.1431` edge `1.501` maxDD `-1.016`
- `market_context_high->commodity_24h` score `1.4073` n `72` status `ready` deltaP `20.4861` edge `0.0716` maxDD `-3.6055`
- `market_context_high->commodity_4h` score `0.9321` n `102` status `ready` deltaP `12.9453` edge `0.0476` maxDD `-1.165`
- `market_context_high->fx_1h` score `-0.1719` n `110` status `ready` deltaP `1.6249` edge `0.0026` maxDD `-0.1712`
- `market_context_high->commodity_1h` score `-0.1916` n `110` status `ready` deltaP `4.1399` edge `0.0065` maxDD `-1.0053`
- `market_context_high->fx_4h` score `-0.3987` n `102` status `ready` deltaP `0.5858` edge `0.0056` maxDD `-0.5168`
- `market_context_high->index_1h` score `-1.1107` n `110` status `ready` deltaP `-3.0702` edge `-0.0069` maxDD `-1.2155`
- `market_context_high->metal_1h` score `-1.1946` n `110` status `ready` deltaP `-2.1938` edge `-0.0055` maxDD `-1.6873`
- `market_context_high->crypto_major_1h` score `-2.9732` n `110` status `ready` deltaP `-2.1067` edge `-0.0538` maxDD `-11.0607`
- `market_context_high->fx_24h` score `-3.1198` n `72` status `ready` deltaP `-10.7639` edge `-0.0055` maxDD `-2.2847`
- `market_context_high->metal_4h` score `-3.6065` n `102` status `ready` deltaP `-12.4253` edge `-0.0303` maxDD `-5.9927`
- `market_context_high->equity_1h` score `-4.1202` n `110` status `ready` deltaP `-2.1829` edge `-0.0959` maxDD `-12.6316`
- `market_context_high->metal_24h` score `-4.4554` n `72` status `ready` deltaP `-14.4097` edge `0.0226` maxDD `-8.1589`
- `market_context_high->crypto_alt_1h` score `-4.8431` n `110` status `ready` deltaP `-8.2363` edge `-0.0872` maxDD `-16.2522`
- `market_context_high->index_4h` score `-4.9306` n `102` status `ready` deltaP `-23.924` edge `-0.0511` maxDD `-5.3565`
- `market_context_high->crypto_major_24h` score `-6.427` n `72` status `ready` deltaP `-12.5` edge `-0.2678` maxDD `-29.161`
- `market_context_high->index_24h` score `-8.7848` n `72` status `ready` deltaP `-39.0625` edge `-0.1682` maxDD `-8.2762`
- `market_context_high->crypto_major_4h` score `-16.3578` n `102` status `ready` deltaP `-30.7` edge `-0.4086` maxDD `-47.9909`
- `market_context_high->crypto_alt_24h` score `-17.132` n `72` status `ready` deltaP `-9.375` edge `-0.7829` maxDD `-95.0805`
- `market_context_high->equity_4h` score `-17.1936` n `102` status `ready` deltaP `-23.9898` edge `-0.4775` maxDD `-51.2958`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
