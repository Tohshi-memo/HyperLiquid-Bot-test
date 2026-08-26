# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-26T12:37:30.790218+00:00`
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

- `news_risk_high->unknown_24h` score `44.8722` n `53` status `ready` deltaP `11.6319` edge `3.6618` maxDD `0.0`
- `news_risk_high->unknown_4h` score `12.088` n `53` status `ready` deltaP `24.3701` edge `0.8548` maxDD `-0.1281`
- `news_risk_high->crypto_alt_24h` score `9.9254` n `53` status `ready` deltaP `31.2958` edge `0.6626` maxDD `-2.8629`
- `news_risk_high->equity_24h` score `6.9365` n `53` status `ready` deltaP `29.4189` edge `0.475` maxDD `-4.7801`
- `news_risk_high->index_24h` score `4.0361` n `53` status `ready` deltaP `40.114` edge `0.0841` maxDD `-0.2147`
- `news_risk_high->fx_4h` score `2.9169` n `53` status `ready` deltaP `35.1157` edge `0.0224` maxDD `-0.0746`
- `news_risk_high->unknown_1h` score `2.7531` n `53` status `ready` deltaP `15.4135` edge `0.1622` maxDD `-0.8426`
- `market_context_high->unknown_4h` score `2.7211` n `136` status `ready` deltaP `22.6776` edge `0.1164` maxDD `-0.5994`
- `news_risk_high->metal_24h` score `1.7972` n `53` status `ready` deltaP `29.1896` edge `-0.0406` maxDD `-0.0053`
- `news_risk_high->equity_4h` score `1.7561` n `53` status `ready` deltaP `19.889` edge `0.0908` maxDD `-2.164`
- `news_risk_high->fx_1h` score `1.0902` n `53` status `ready` deltaP `15.3203` edge `0.0057` maxDD `-0.0257`
- `market_context_high->unknown_1h` score `1.0656` n `137` status `ready` deltaP `11.6537` edge `0.056` maxDD `-1.5916`
- `news_risk_high->equity_1h` score `0.484` n `53` status `ready` deltaP `12.9251` edge `0.0123` maxDD `-0.9128`
- `news_risk_high->commodity_1h` score `0.4464` n `53` status `ready` deltaP `10.8265` edge `-0.0037` maxDD `-0.5024`
- `news_risk_high->index_4h` score `0.1985` n `53` status `ready` deltaP `7.2711` edge `0.0078` maxDD `-0.1788`
- `news_risk_high->index_1h` score `-0.0573` n `53` status `ready` deltaP `3.9996` edge `0.0013` maxDD `-0.1583`
- `news_risk_high->metal_4h` score `-0.2022` n `53` status `ready` deltaP `6.3391` edge `-0.006` maxDD `-0.249`
- `news_risk_high->metal_1h` score `-0.324` n `53` status `ready` deltaP `0.5847` edge `-0.0083` maxDD `-0.1413`
- `market_context_high->fx_1h` score `-0.452` n `137` status `ready` deltaP `2.4433` edge `-0.001` maxDD `-0.8587`
- `news_risk_high->commodity_4h` score `-0.9496` n `53` status `ready` deltaP `-0.7536` edge `0.0066` maxDD `-1.1986`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
