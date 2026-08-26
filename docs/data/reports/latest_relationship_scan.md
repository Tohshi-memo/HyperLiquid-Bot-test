# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-26T05:22:27.955231+00:00`
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

- `news_risk_high->unknown_24h` score `46.461` n `51` status `ready` deltaP `11.6319` edge `3.7942` maxDD `0.0`
- `news_risk_high->unknown_4h` score `12.1116` n `53` status `ready` deltaP `23.1506` edge `0.8649` maxDD `-0.1281`
- `news_risk_high->crypto_alt_24h` score `7.0372` n `51` status `ready` deltaP `30.0347` edge `0.3862` maxDD `0.0`
- `news_risk_high->equity_24h` score `6.9681` n `51` status `ready` deltaP `29.9939` edge `0.4738` maxDD `-4.7801`
- `news_risk_high->index_24h` score `4.0184` n `51` status `ready` deltaP `40.2676` edge `0.0816` maxDD `-0.2147`
- `news_risk_high->unknown_1h` score `3.0147` n `53` status `ready` deltaP `15.5632` edge `0.183` maxDD `-0.8426`
- `news_risk_high->fx_4h` score `2.8071` n `53` status `ready` deltaP `33.7437` edge `0.0224` maxDD `-0.0746`
- `market_context_high->unknown_4h` score `2.1531` n `133` status `ready` deltaP `21.2922` edge `0.0783` maxDD `-0.5994`
- `news_risk_high->equity_4h` score `1.6761` n `53` status `ready` deltaP `19.2792` edge `0.0882` maxDD `-2.164`
- `market_context_high->unknown_1h` score `1.333` n `136` status `ready` deltaP `11.637` edge `0.0784` maxDD `-1.5916`
- `news_risk_high->metal_24h` score `1.3005` n `51` status `ready` deltaP `29.1156` edge `-0.0815` maxDD `-0.0053`
- `news_risk_high->fx_1h` score `1.0447` n `53` status `ready` deltaP `14.7215` edge `0.0059` maxDD `-0.0257`
- `news_risk_high->commodity_1h` score `0.4811` n `53` status `ready` deltaP `11.2756` edge `-0.0038` maxDD `-0.5024`
- `news_risk_high->equity_1h` score `0.3546` n `53` status `ready` deltaP `12.3263` edge `-0.0003` maxDD `-0.9128`
- `news_risk_high->index_4h` score `0.0209` n `53` status `ready` deltaP `5.4418` edge `0.0052` maxDD `-0.1788`
- `news_risk_high->index_1h` score `-0.1142` n `53` status `ready` deltaP `3.2511` edge `-0.001` maxDD `-0.1583`
- `market_context_high->fx_1h` score `-0.4598` n `136` status `ready` deltaP `2.2631` edge `-0.0008` maxDD `-0.8587`
- `news_risk_high->metal_1h` score `-0.5613` n `53` status `ready` deltaP `-1.6608` edge `-0.0131` maxDD `-0.1413`
- `news_risk_high->metal_4h` score `-0.8245` n `53` status `ready` deltaP `2.0708` edge `-0.0294` maxDD `-0.249`
- `news_risk_high->commodity_4h` score `-1.0451` n `53` status `ready` deltaP `-2.1255` edge `0.0035` maxDD `-1.1986`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
