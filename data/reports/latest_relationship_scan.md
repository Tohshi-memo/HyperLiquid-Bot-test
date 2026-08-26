# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-26T05:37:26.021105+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `14808`

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

- `news_risk_high->unknown_24h` score `46.4838` n `51` status `ready` deltaP `11.6319` edge `3.7961` maxDD `0.0`
- `news_risk_high->unknown_4h` score `11.9676` n `53` status `ready` deltaP `23.1506` edge `0.8529` maxDD `-0.1281`
- `news_risk_high->crypto_alt_24h` score `7.2287` n `51` status `ready` deltaP `30.2083` edge `0.401` maxDD `0.0`
- `news_risk_high->equity_24h` score `6.9801` n `51` status `ready` deltaP `29.9939` edge `0.4748` maxDD `-4.7801`
- `news_risk_high->index_24h` score `4.0232` n `51` status `ready` deltaP `40.2676` edge `0.082` maxDD `-0.2147`
- `news_risk_high->unknown_1h` score `2.8755` n `53` status `ready` deltaP `15.4135` edge `0.1724` maxDD `-0.8426`
- `news_risk_high->fx_4h` score `2.8193` n `53` status `ready` deltaP `33.8962` edge `0.0224` maxDD `-0.0746`
- `market_context_high->unknown_4h` score `2.0091` n `133` status `ready` deltaP `21.2922` edge `0.0663` maxDD `-0.5994`
- `news_risk_high->equity_4h` score `1.6845` n `53` status `ready` deltaP `19.2792` edge `0.0889` maxDD `-2.164`
- `news_risk_high->metal_24h` score `1.3185` n `51` status `ready` deltaP `29.1156` edge `-0.08` maxDD `-0.0053`
- `market_context_high->unknown_1h` score `1.1938` n `136` status `ready` deltaP `11.4873` edge `0.0678` maxDD `-1.5916`
- `news_risk_high->fx_1h` score `1.0447` n `53` status `ready` deltaP `14.7215` edge `0.0059` maxDD `-0.0257`
- `news_risk_high->commodity_1h` score `0.4799` n `53` status `ready` deltaP `11.2756` edge `-0.0039` maxDD `-0.5024`
- `news_risk_high->equity_1h` score `0.3538` n `53` status `ready` deltaP `12.3263` edge `-0.0004` maxDD `-0.9128`
- `news_risk_high->index_4h` score `0.0221` n `53` status `ready` deltaP `5.4418` edge `0.0053` maxDD `-0.1788`
- `news_risk_high->index_1h` score `-0.1142` n `53` status `ready` deltaP `3.2511` edge `-0.001` maxDD `-0.1583`
- `market_context_high->fx_1h` score `-0.4598` n `136` status `ready` deltaP `2.2631` edge `-0.0008` maxDD `-0.8587`
- `news_risk_high->metal_1h` score `-0.5469` n `53` status `ready` deltaP `-1.5111` edge `-0.0129` maxDD `-0.1413`
- `news_risk_high->metal_4h` score `-0.8233` n `53` status `ready` deltaP `2.0708` edge `-0.0293` maxDD `-0.249`
- `news_risk_high->commodity_4h` score `-1.0451` n `53` status `ready` deltaP `-2.1255` edge `0.0035` maxDD `-1.1986`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
