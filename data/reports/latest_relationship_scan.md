# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-25T15:37:26.972018+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `14776`

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

- `news_risk_high->unknown_24h` score `44.0354` n `51` status `ready` deltaP `3.9931` edge `3.643` maxDD `0.0`
- `news_risk_high->unknown_4h` score `12.523` n `53` status `ready` deltaP `23.9128` edge `0.8941` maxDD `-0.1281`
- `news_risk_high->equity_24h` score `8.523` n `51` status `ready` deltaP `32.9453` edge `0.5837` maxDD `-4.7801`
- `news_risk_high->index_24h` score `4.2818` n `51` status `ready` deltaP `42.5245` edge `0.0885` maxDD `-0.2147`
- `news_risk_high->unknown_1h` score `3.1502` n `53` status `ready` deltaP `16.162` edge `0.1903` maxDD `-0.8426`
- `news_risk_high->fx_4h` score `3.0258` n `53` status `ready` deltaP `35.8779` edge `0.0264` maxDD `-0.0746`
- `market_context_high->unknown_4h` score `2.5644` n `133` status `ready` deltaP `22.0544` edge `0.1075` maxDD `-0.5994`
- `news_risk_high->equity_4h` score `1.9707` n `53` status `ready` deltaP `21.5658` edge `0.0975` maxDD `-2.164`
- `news_risk_high->fx_1h` score `1.1992` n `53` status `ready` deltaP `16.5179` edge `0.0068` maxDD `-0.0257`
- `news_risk_high->equity_1h` score `0.5354` n `53` status `ready` deltaP `14.5718` edge `0.0079` maxDD `-0.9128`
- `news_risk_high->commodity_1h` score `0.3852` n `53` status `ready` deltaP `10.3774` edge `-0.0058` maxDD `-0.5024`
- `news_risk_high->index_4h` score `0.256` n `53` status `ready` deltaP `8.1857` edge `0.0065` maxDD `-0.1788`
- `market_context_high->unknown_1h` score `0.1326` n `133` status `ready` deltaP `11.7216` edge `-0.0222` maxDD `-1.5916`
- `news_risk_high->index_1h` score `-0.0386` n `53` status `ready` deltaP `4.4487` edge `0.0007` maxDD `-0.1583`
- `news_risk_high->metal_24h` score `-0.3476` n `51` status `ready` deltaP `23.56` edge `-0.1818` maxDD `-0.0053`
- `news_risk_high->metal_4h` score `-0.3548` n `53` status `ready` deltaP `6.1867` edge `-0.0177` maxDD `-0.249`
- `news_risk_high->metal_1h` score `-0.4091` n `53` status `ready` deltaP `-0.1638` edge `-0.0104` maxDD `-0.1413`
- `market_context_high->fx_1h` score `-0.4117` n `133` status `ready` deltaP `3.0976` edge `-0.0002` maxDD `-0.8587`
- `market_context_high->metal_4h` score `-0.8552` n `133` status `ready` deltaP `5.1795` edge `-0.0421` maxDD `-2.4293`
- `news_risk_high->crypto_alt_24h` score `-1.0131` n `51` status `ready` deltaP `20.4861` edge `-0.221` maxDD `0.0`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
