# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-25T11:22:30.553264+00:00`
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

- `news_risk_high->unknown_24h` score `43.6103` n `51` status `ready` deltaP `2.0833` edge `3.6203` maxDD `0.0`
- `news_risk_high->unknown_4h` score `13.0114` n `51` status `ready` deltaP `25.7831` edge `0.917` maxDD `-0.0348`
- `news_risk_high->equity_24h` score `9.6867` n `51` status `ready` deltaP `35.8967` edge `0.661` maxDD `-4.7801`
- `news_risk_high->index_24h` score `4.583` n `51` status `ready` deltaP `44.9551` edge `0.0974` maxDD `-0.2147`
- `news_risk_high->unknown_1h` score `3.1343` n `52` status `ready` deltaP `15.7991` edge `0.1914` maxDD `-0.8426`
- `news_risk_high->fx_4h` score `3.1289` n `51` status `ready` deltaP `37.0158` edge `0.0274` maxDD `-0.0746`
- `news_risk_high->equity_4h` score `2.3376` n `51` status `ready` deltaP `22.5072` edge `0.1218` maxDD `-2.164`
- `market_context_high->unknown_4h` score `2.0173` n `133` status `ready` deltaP `20.2251` edge `0.0741` maxDD `-0.5994`
- `news_risk_high->fx_1h` score `1.2132` n `52` status `ready` deltaP `16.6628` edge `0.007` maxDD `-0.0257`
- `news_risk_high->equity_1h` score `0.7603` n `52` status `ready` deltaP `16.8125` edge `0.0218` maxDD `-0.9128`
- `news_risk_high->index_4h` score `0.3868` n `51` status `ready` deltaP `9.2808` edge `0.0101` maxDD `-0.1788`
- `news_risk_high->commodity_1h` score `0.2512` n `52` status `ready` deltaP `9.0166` edge `-0.0079` maxDD `-0.5024`
- `news_risk_high->index_1h` score `0.0603` n `52` status `ready` deltaP `6.1723` edge `0.0019` maxDD `-0.1583`
- `market_context_high->unknown_1h` score `0.0594` n `133` status `ready` deltaP `11.7216` edge `-0.0283` maxDD `-1.5916`
- `news_risk_high->metal_4h` score `-0.2883` n `51` status `ready` deltaP `6.1484` edge `-0.0119` maxDD `-0.249`
- `news_risk_high->metal_1h` score `-0.3906` n `52` status `ready` deltaP `-0.1727` edge `-0.0088` maxDD `-0.1413`
- `market_context_high->fx_1h` score `-0.474` n `133` status `ready` deltaP `1.9` edge `-0.0002` maxDD `-0.8587`
- `market_context_high->metal_4h` score `-0.6761` n `133` status `ready` deltaP `6.399` edge `-0.0353` maxDD `-2.4293`
- `news_risk_high->metal_24h` score `-0.69` n `51` status `ready` deltaP `21.6503` edge `-0.1976` maxDD `-0.0053`
- `market_context_high->index_1h` score `-1.1436` n `133` status `ready` deltaP `-5.3228` edge `-0.006` maxDD `-1.3054`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
