# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-25T11:37:23.967117+00:00`
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

- `news_risk_high->unknown_24h` score `43.6091` n `51` status `ready` deltaP `2.0833` edge `3.6202` maxDD `0.0`
- `news_risk_high->unknown_4h` score `13.0102` n `51` status `ready` deltaP `25.7831` edge `0.9169` maxDD `-0.0348`
- `news_risk_high->equity_24h` score `9.6224` n `51` status `ready` deltaP `35.7231` edge `0.6568` maxDD `-4.7801`
- `news_risk_high->index_24h` score `4.5619` n `51` status `ready` deltaP `44.7814` edge `0.0968` maxDD `-0.2147`
- `news_risk_high->fx_4h` score `3.1423` n `51` status `ready` deltaP `37.1682` edge `0.0275` maxDD `-0.0746`
- `news_risk_high->unknown_1h` score `3.0638` n `53` status `ready` deltaP `16.0123` edge `0.1841` maxDD `-0.8426`
- `news_risk_high->equity_4h` score `2.2858` n `51` status `ready` deltaP `22.3547` edge `0.1185` maxDD `-2.164`
- `market_context_high->unknown_4h` score `2.0161` n `133` status `ready` deltaP `20.2251` edge `0.074` maxDD `-0.5994`
- `news_risk_high->fx_1h` score `1.1153` n `53` status `ready` deltaP `15.47` edge `0.0068` maxDD `-0.0257`
- `news_risk_high->equity_1h` score `0.6671` n `53` status `ready` deltaP `15.47` edge `0.0188` maxDD `-0.9128`
- `news_risk_high->index_4h` score `0.3687` n `51` status `ready` deltaP `9.1284` edge `0.0096` maxDD `-0.1788`
- `news_risk_high->commodity_1h` score `0.3205` n `53` status `ready` deltaP `9.7786` edge `-0.0072` maxDD `-0.5024`
- `market_context_high->unknown_1h` score `0.0462` n `133` status `ready` deltaP `11.5719` edge `-0.0284` maxDD `-1.5916`
- `news_risk_high->index_1h` score `-0.0005` n `53` status `ready` deltaP `5.0475` edge `0.0016` maxDD `-0.1583`
- `news_risk_high->metal_4h` score `-0.2955` n `51` status `ready` deltaP `6.1484` edge `-0.0125` maxDD `-0.249`
- `news_risk_high->metal_1h` score `-0.306` n `53` status `ready` deltaP `0.7344` edge `-0.0078` maxDD `-0.1413`
- `market_context_high->fx_1h` score `-0.4662` n `133` status `ready` deltaP `2.0497` edge `-0.0002` maxDD `-0.8587`
- `market_context_high->metal_4h` score `-0.6833` n `133` status `ready` deltaP `6.399` edge `-0.0359` maxDD `-2.4293`
- `news_risk_high->metal_24h` score `-0.6912` n `51` status `ready` deltaP `21.6503` edge `-0.1977` maxDD `-0.0053`
- `market_context_high->index_1h` score `-1.1436` n `133` status `ready` deltaP `-5.3228` edge `-0.006` maxDD `-1.3054`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
