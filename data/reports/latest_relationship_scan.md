# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-24T20:52:33.729493+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `7840`

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

- `market_context_high->unknown_4h` score `17.5102` n `102` status `ready` deltaP `-2.1431` edge `1.507` maxDD `-1.016`
- `market_context_high->commodity_24h` score `1.5039` n `71` status `ready` deltaP `21.3493` edge `0.0739` maxDD `-3.6055`
- `market_context_high->commodity_4h` score `0.9489` n `102` status `ready` deltaP `12.9453` edge `0.049` maxDD `-1.165`
- `market_context_high->commodity_1h` score `-0.1537` n `109` status `ready` deltaP `4.524` edge `0.0071` maxDD `-1.0053`
- `market_context_high->fx_1h` score `-0.1966` n `109` status `ready` deltaP `1.1495` edge `0.0026` maxDD `-0.1712`
- `market_context_high->fx_4h` score `-0.3987` n `102` status `ready` deltaP `0.5858` edge `0.0056` maxDD `-0.5168`
- `market_context_high->index_1h` score `-1.1533` n `109` status `ready` deltaP `-3.5873` edge `-0.007` maxDD `-1.2155`
- `market_context_high->metal_1h` score `-1.2409` n `109` status `ready` deltaP `-2.7276` edge `-0.0058` maxDD `-1.6873`
- `market_context_high->crypto_major_1h` score `-3.0274` n `109` status `ready` deltaP `-2.5737` edge `-0.0552` maxDD `-11.0607`
- `market_context_high->fx_24h` score `-3.0431` n `71` status `ready` deltaP `-10.49` edge `-0.0055` maxDD `-2.2528`
- `market_context_high->metal_4h` score `-3.6041` n `102` status `ready` deltaP `-12.4253` edge `-0.0301` maxDD `-5.9927`
- `market_context_high->equity_1h` score `-4.1754` n `109` status `ready` deltaP `-2.7084` edge `-0.097` maxDD `-12.6316`
- `market_context_high->metal_24h` score `-4.3919` n `71` status `ready` deltaP `-14.2532` edge `0.022` maxDD `-8.1046`
- `market_context_high->crypto_alt_1h` score `-4.8494` n `109` status `ready` deltaP `-8.044` edge `-0.089` maxDD `-16.2522`
- `market_context_high->index_4h` score `-4.9282` n `102` status `ready` deltaP `-23.924` edge `-0.0509` maxDD `-5.3565`
- `market_context_high->crypto_major_24h` score `-6.1806` n `71` status `ready` deltaP `-11.9327` edge `-0.2556` maxDD `-28.2456`
- `market_context_high->index_24h` score `-8.704` n `71` status `ready` deltaP `-38.9255` edge `-0.1681` maxDD `-8.1518`
- `market_context_high->crypto_major_4h` score `-16.269` n `102` status `ready` deltaP `-30.7` edge `-0.4012` maxDD `-47.9909`
- `market_context_high->crypto_alt_24h` score `-16.5293` n `71` status `ready` deltaP `-8.8273` edge `-0.7526` maxDD `-91.9485`
- `market_context_high->equity_4h` score `-17.1612` n `102` status `ready` deltaP `-23.9898` edge `-0.4748` maxDD `-51.2958`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
