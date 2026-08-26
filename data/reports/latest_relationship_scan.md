# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-26T13:07:27.741451+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `14760`

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

- `news_risk_high->unknown_24h` score `44.9598` n `53` status `ready` deltaP `11.6319` edge `3.6691` maxDD `0.0`
- `news_risk_high->unknown_4h` score `12.158` n `53` status `ready` deltaP `24.675` edge `0.8586` maxDD `-0.1281`
- `news_risk_high->crypto_alt_24h` score `10.318` n `53` status `ready` deltaP `31.6431` edge `0.693` maxDD `-2.8629`
- `news_risk_high->equity_24h` score `6.8789` n `53` status `ready` deltaP `29.4189` edge `0.4702` maxDD `-4.7801`
- `news_risk_high->index_24h` score `4.0289` n `53` status `ready` deltaP `40.114` edge `0.0835` maxDD `-0.2147`
- `news_risk_high->fx_4h` score `2.9436` n `53` status `ready` deltaP `35.4205` edge `0.0226` maxDD `-0.0746`
- `market_context_high->unknown_4h` score `2.7911` n `136` status `ready` deltaP `22.9825` edge `0.1202` maxDD `-0.5994`
- `news_risk_high->unknown_1h` score `2.7651` n `53` status `ready` deltaP `15.4135` edge `0.1632` maxDD `-0.8426`
- `news_risk_high->metal_24h` score `1.8116` n `53` status `ready` deltaP `29.1896` edge `-0.0394` maxDD `-0.0053`
- `news_risk_high->equity_4h` score `1.7321` n `53` status `ready` deltaP `19.889` edge `0.0888` maxDD `-2.164`
- `news_risk_high->fx_1h` score `1.1153` n `53` status `ready` deltaP `15.6197` edge `0.0058` maxDD `-0.0257`
- `market_context_high->unknown_1h` score `1.0776` n `137` status `ready` deltaP `11.6537` edge `0.057` maxDD `-1.5916`
- `news_risk_high->commodity_1h` score `0.4607` n `53` status `ready` deltaP `10.9762` edge `-0.0035` maxDD `-0.5024`
- `news_risk_high->equity_1h` score `0.4458` n `53` status `ready` deltaP `12.9251` edge `0.0074` maxDD `-0.9128`
- `news_risk_high->index_4h` score `0.1949` n `53` status `ready` deltaP `7.2711` edge `0.0075` maxDD `-0.1788`
- `news_risk_high->index_1h` score `-0.0604` n `53` status `ready` deltaP `3.9996` edge `0.0009` maxDD `-0.1583`
- `news_risk_high->metal_4h` score `-0.1574` n `53` status `ready` deltaP `6.644` edge `-0.0043` maxDD `-0.249`
- `news_risk_high->metal_1h` score `-0.2905` n `53` status `ready` deltaP `0.8841` edge `-0.0075` maxDD `-0.1413`
- `market_context_high->fx_1h` score `-0.4356` n `137` status `ready` deltaP `2.7427` edge `-0.0009` maxDD `-0.8587`
- `news_risk_high->commodity_4h` score `-0.9496` n `53` status `ready` deltaP `-0.7536` edge `0.0066` maxDD `-1.1986`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
