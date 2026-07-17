# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-17T21:28:12.656310+00:00`
- Price records: `672`
- Market context records: `7070`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11502`

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

- `market_context_high->fx_4h` score `0.7051` n `181` status `ready` deltaP `17.4993` edge `0.0121` maxDD `-0.9333`
- `market_context_high->fx_1h` score `-0.1548` n `181` status `ready` deltaP `4.443` edge `0.0026` maxDD `-0.276`
- `market_context_high->unknown_1h` score `-0.2099` n `181` status `ready` deltaP `0.4152` edge `0.0356` maxDD `-1.4688`
- `market_context_high->crypto_alt_1h` score `-0.3102` n `181` status `ready` deltaP `1.7948` edge `0.0347` maxDD `-4.5815`
- `market_context_high->crypto_major_1h` score `-0.5751` n `181` status `ready` deltaP `4.051` edge `0.0345` maxDD `-7.1523`
- `market_context_high->unknown_4h` score `-0.7423` n `181` status `ready` deltaP `-4.8469` edge `0.1339` maxDD `-4.742`
- `market_context_high->index_1h` score `-0.7625` n `181` status `ready` deltaP `-1.0215` edge `-0.004` maxDD `-2.2895`
- `market_context_high->commodity_1h` score `-0.8727` n `181` status `ready` deltaP `-4.6283` edge `-0.0194` maxDD `-1.9306`
- `market_context_high->metal_1h` score `-1.3484` n `181` status `ready` deltaP `-4.8426` edge `-0.0033` maxDD `-2.1427`
- `market_context_high->commodity_4h` score `-1.6415` n `181` status `ready` deltaP `-7.3078` edge `-0.0457` maxDD `-2.9494`
- `market_context_high->equity_1h` score `-1.8633` n `181` status `ready` deltaP `4.6639` edge `-0.0277` maxDD `-14.716`
- `market_context_high->index_4h` score `-2.2783` n `181` status `ready` deltaP `1.8015` edge `-0.0342` maxDD `-12.2591`
- `market_context_high->commodity_24h` score `-2.4399` n `181` status `ready` deltaP `-2.4517` edge `-0.0561` maxDD `-4.4704`
- `market_context_high->crypto_alt_4h` score `-2.9579` n `181` status `ready` deltaP `0.2577` edge `-0.0024` maxDD `-22.2831`
- `market_context_high->crypto_major_4h` score `-3.1007` n `181` status `ready` deltaP `2.2386` edge `0.016` maxDD `-24.6094`
- `market_context_high->fx_24h` score `-3.5999` n `181` status `ready` deltaP `-0.7021` edge `-0.0126` maxDD `-3.9503`
- `market_context_high->metal_4h` score `-3.6853` n `181` status `ready` deltaP `-0.6729` edge `-0.0043` maxDD `-5.5324`
- `market_context_high->unknown_24h` score `-4.2672` n `181` status `ready` deltaP `-16.3789` edge `0.0768` maxDD `-23.5076`
- `market_context_high->equity_4h` score `-7.9189` n `181` status `ready` deltaP `4.259` edge `-0.1566` maxDD `-63.963`
- `market_context_high->metal_24h` score `-15.674` n `181` status `ready` deltaP `-21.8108` edge `-0.1014` maxDD `-44.4154`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
