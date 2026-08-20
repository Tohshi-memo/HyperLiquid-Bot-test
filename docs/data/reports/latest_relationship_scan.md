# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-20T07:37:24.612774+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `88`

- Symbol pattern count: `10800`

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

- `market_context_high->equity_4h` score `1.7524` n `96` status `ready` deltaP `9.4766` edge `0.1717` maxDD `-2.4411`
- `market_context_high->equity_1h` score `1.639` n `97` status `ready` deltaP `13.683` edge `0.0755` maxDD `-0.4112`
- `market_context_high->index_1h` score `0.7933` n `97` status `ready` deltaP `14.3157` edge `0.0094` maxDD `-0.0982`
- `market_context_high->metal_4h` score `0.3164` n `96` status `ready` deltaP `11.9918` edge `0.004` maxDD `-1.273`
- `market_context_high->commodity_24h` score `0.0545` n `96` status `ready` deltaP `6.0764` edge `0.1498` maxDD `-4.666`
- `market_context_high->index_4h` score `0.0135` n `96` status `ready` deltaP `7.0376` edge `0.0197` maxDD `-0.5728`
- `market_context_high->fx_4h` score `0.0107` n `96` status `ready` deltaP `7.19` edge `0.0037` maxDD `-0.3539`
- `market_context_high->unknown_1h` score `-0.161` n `97` status `ready` deltaP `5.701` edge `-0.0287` maxDD `-0.4843`
- `market_context_high->metal_1h` score `-0.245` n `97` status `ready` deltaP `2.4276` edge `0.0021` maxDD `-0.4291`
- `market_context_high->fx_1h` score `-0.3149` n `97` status `ready` deltaP `-1.0633` edge `0.0026` maxDD `-0.2043`
- `market_context_high->unknown_24h` score `-0.5565` n `96` status `ready` deltaP `17.7083` edge `-0.1138` maxDD `-1.0505`
- `market_context_high->commodity_4h` score `-0.8319` n `96` status `ready` deltaP `-3.379` edge `0.0009` maxDD `-2.4692`
- `market_context_high->crypto_alt_1h` score `-0.8591` n `97` status `ready` deltaP `-0.7161` edge `-0.0252` maxDD `-2.413`
- `market_context_high->crypto_major_1h` score `-0.8758` n `97` status `ready` deltaP `2.1282` edge `-0.042` maxDD `-2.7581`
- `market_context_high->commodity_1h` score `-0.9285` n `97` status `ready` deltaP `-8.4974` edge `-0.0058` maxDD `-1.1941`
- `market_context_high->crypto_alt_4h` score `-1.9886` n `96` status `ready` deltaP `4.4207` edge `-0.0682` maxDD `-5.4926`
- `market_context_high->crypto_major_4h` score `-2.1601` n `96` status `ready` deltaP `6.7327` edge `-0.1228` maxDD `-3.1677`
- `market_context_high->fx_24h` score `-3.2714` n `96` status `ready` deltaP `-16.6666` edge `-0.0032` maxDD `-1.9981`
- `market_context_high->index_24h` score `-3.813` n `96` status `ready` deltaP `-0.8681` edge `-0.0663` maxDD `-18.3411`
- `market_context_high->metal_24h` score `-4.4008` n `96` status `ready` deltaP `-16.6667` edge `-0.1223` maxDD `-11.4635`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
