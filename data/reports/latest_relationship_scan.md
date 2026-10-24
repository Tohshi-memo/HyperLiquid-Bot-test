# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-24T21:37:26.262201+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `7550`

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

- `market_context_high->unknown_4h` score `17.79` n `102` status `ready` deltaP `-1.3151` edge `1.5248` maxDD `-1.016`
- `market_context_high->commodity_24h` score `1.8001` n `68` status `ready` deltaP `24.1218` edge `0.0801` maxDD `-3.6055`
- `market_context_high->commodity_4h` score `0.9837` n `102` status `ready` deltaP `12.9453` edge `0.0519` maxDD `-1.165`
- `market_context_high->commodity_1h` score `0.0437` n `107` status `ready` deltaP `6.2567` edge `0.012` maxDD `-1.0053`
- `market_context_high->fx_1h` score `-0.1658` n `107` status `ready` deltaP `1.7418` edge `0.0026` maxDD `-0.1712`
- `market_context_high->fx_4h` score `-0.398` n `102` status `ready` deltaP `0.5858` edge `0.0057` maxDD `-0.5168`
- `market_context_high->index_1h` score `-1.0876` n `107` status `ready` deltaP `-2.7814` edge `-0.0069` maxDD `-1.2155`
- `market_context_high->metal_1h` score `-1.312` n `107` status `ready` deltaP `-3.5257` edge `-0.0064` maxDD `-1.6873`
- `market_context_high->fx_24h` score `-2.7987` n `68` status `ready` deltaP `-9.6201` edge `-0.0051` maxDD `-2.1194`
- `market_context_high->crypto_major_1h` score `-3.1827` n `107` status `ready` deltaP `-4.0195` edge `-0.0585` maxDD `-11.0607`
- `market_context_high->metal_4h` score `-3.5295` n `102` status `ready` deltaP `-11.5973` edge `-0.0295` maxDD `-5.985`
- `market_context_high->metal_24h` score `-4.2001` n `68` status `ready` deltaP `-13.7561` edge `0.02` maxDD `-7.931`
- `market_context_high->equity_1h` score `-4.2679` n `107` status `ready` deltaP `-3.4893` edge `-0.0995` maxDD `-12.6316`
- `market_context_high->crypto_alt_1h` score `-4.7003` n `107` status `ready` deltaP `-8.1258` edge `-0.0894` maxDD `-15.8495`
- `market_context_high->index_4h` score `-4.9222` n `102` status `ready` deltaP `-23.924` edge `-0.0504` maxDD `-5.3565`
- `market_context_high->crypto_major_24h` score `-5.4292` n `68` status `ready` deltaP `-10.1307` edge `-0.217` maxDD `-25.5882`
- `market_context_high->index_24h` score `-8.467` n `68` status `ready` deltaP `-38.4906` edge `-0.1682` maxDD `-7.7954`
- `market_context_high->crypto_alt_24h` score `-14.7482` n `68` status `ready` deltaP `-7.0874` edge `-0.6602` maxDD `-83.0005`
- `market_context_high->crypto_major_4h` score `-15.7545` n `102` status `ready` deltaP `-29.0441` edge `-0.3806` maxDD `-47.7583`
- `market_context_high->equity_4h` score `-17.0289` n `102` status `ready` deltaP `-23.1618` edge `-0.4693` maxDD `-51.2958`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
