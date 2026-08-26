# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-26T18:37:36.671635+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `14792`

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

- `news_risk_high->unknown_24h` score `47.8361` n `50` status `ready` deltaP `11.5717` edge `3.9092` maxDD `0.0`
- `news_risk_high->unknown_4h` score `12.3981` n `50` status `ready` deltaP `26.7769` edge `0.8646` maxDD `-0.1281`
- `news_risk_high->crypto_alt_24h` score `11.3656` n `50` status `ready` deltaP `35.0328` edge `0.7577` maxDD `-2.8629`
- `news_risk_high->equity_24h` score `7.8877` n `50` status `ready` deltaP `34.2591` edge `0.522` maxDD `-4.7801`
- `news_risk_high->index_24h` score `4.1568` n `50` status `ready` deltaP `41.3679` edge `0.0858` maxDD `-0.2147`
- `news_risk_high->fx_4h` score `3.5018` n `50` status `ready` deltaP `41.3171` edge `0.0254` maxDD `-0.0559`
- `market_context_high->unknown_4h` score `3.2583` n `137` status `ready` deltaP `25.4776` edge `0.1425` maxDD `-0.5994`
- `news_risk_high->unknown_1h` score `2.5976` n `50` status `ready` deltaP `15.0299` edge `0.1518` maxDD `-0.8426`
- `news_risk_high->metal_24h` score `2.0953` n `50` status `ready` deltaP `31.8515` edge `-0.0335` maxDD `-0.0053`
- `news_risk_high->equity_4h` score `1.448` n `50` status `ready` deltaP `19.2473` edge `0.0694` maxDD `-2.164`
- `news_risk_high->fx_1h` score `1.3228` n `50` status `ready` deltaP `18.1078` edge `0.0065` maxDD `-0.0257`
- `news_risk_high->equity_1h` score `1.2783` n `50` status `ready` deltaP `16.8144` edge `0.0225` maxDD `-0.2455`
- `market_context_high->unknown_1h` score `1.2286` n `137` status `ready` deltaP `12.4022` edge `0.0646` maxDD `-1.5916`
- `news_risk_high->commodity_1h` score `0.5121` n `50` status `ready` deltaP `14.1497` edge `0.0026` maxDD `-0.5024`
- `news_risk_high->index_1h` score `0.1201` n `50` status `ready` deltaP `7.0599` edge `0.0023` maxDD `-0.0505`
- `news_risk_high->index_4h` score `0.086` n `50` status `ready` deltaP `6.2549` edge `0.0052` maxDD `-0.1788`
- `news_risk_high->metal_1h` score `0.0555` n `50` status `ready` deltaP `4.8024` edge `-0.0023` maxDD `-0.1413`
- `news_risk_high->metal_4h` score `-0.0812` n `50` status `ready` deltaP `7.8816` edge `-0.0062` maxDD `-0.249`
- `market_context_high->fx_1h` score `-0.4193` n `137` status `ready` deltaP `3.0421` edge `-0.0008` maxDD `-0.8587`
- `market_context_high->unknown_24h` score `-0.5794` n `133` status `ready` deltaP `5.5567` edge `-0.0126` maxDD `-3.1513`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
