# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-21T19:07:17.197862+00:00`
- Price records: `672`
- Market context records: `1451`
- Flow alert records: `6091`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8809`

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

- `market_context_high->crypto_alt_24h` score `13.2073` n `161` status `ready` deltaP `28.8658` edge `1.1098` maxDD `-15.1306`
- `market_context_high->crypto_major_24h` score `12.0456` n `161` status `ready` deltaP `27.5233` edge `0.9335` maxDD `-8.0553`
- `market_context_high->metal_24h` score `11.6445` n `161` status `ready` deltaP `14.7731` edge `1.0386` maxDD `-6.3373`
- `market_context_high->index_24h` score `4.3897` n `161` status `ready` deltaP `19.7765` edge `0.3426` maxDD `-5.3574`
- `market_context_high->equity_24h` score `4.3265` n `161` status `ready` deltaP `12.9788` edge `0.5067` maxDD `-14.2815`
- `market_context_high->equity_4h` score `1.6305` n `223` status `ready` deltaP `7.5557` edge `0.1685` maxDD `-3.6396`
- `market_context_high->fx_24h` score `0.2341` n `161` status `ready` deltaP `11.3127` edge `0.049` maxDD `-1.3925`
- `market_context_high->index_1h` score `-0.0794` n `228` status `ready` deltaP `3.824` edge `0.0144` maxDD `-1.7205`
- `market_context_high->equity_1h` score `-0.089` n `228` status `ready` deltaP `2.2954` edge `0.0373` maxDD `-2.8014`
- `market_context_high->crypto_alt_4h` score `-0.3754` n `223` status `ready` deltaP `10.871` edge `0.2282` maxDD `-19.5565`
- `market_context_high->index_4h` score `-0.4489` n `223` status `ready` deltaP `1.214` edge `0.0634` maxDD `-3.7119`
- `market_context_high->fx_1h` score `-0.4685` n `228` status `ready` deltaP `0.8352` edge `-0.0024` maxDD `-0.3914`
- `market_context_high->crypto_alt_1h` score `-0.5541` n `228` status `ready` deltaP `1.9488` edge `0.0432` maxDD `-4.1892`
- `market_context_high->fx_4h` score `-1.0166` n `223` status `ready` deltaP `-3.6859` edge `-0.0087` maxDD `-1.4313`
- `market_context_high->crypto_major_4h` score `-1.0931` n `223` status `ready` deltaP `5.6245` edge `0.1423` maxDD `-13.3376`
- `market_context_high->metal_1h` score `-1.1339` n `228` status `ready` deltaP `5.0084` edge `0.0057` maxDD `-6.3532`
- `market_context_high->commodity_1h` score `-1.2213` n `228` status `ready` deltaP `-1.3263` edge `-0.0008` maxDD `-4.7041`
- `market_context_high->crypto_major_1h` score `-1.6451` n `228` status `ready` deltaP `-1.1109` edge `0.006` maxDD `-6.1883`
- `market_context_high->metal_4h` score `-1.8136` n `223` status `ready` deltaP `7.9733` edge `0.0649` maxDD `-12.5349`
- `market_context_high->commodity_4h` score `-3.549` n `223` status `ready` deltaP `-11.8745` edge `-0.0639` maxDD `-12.6214`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
