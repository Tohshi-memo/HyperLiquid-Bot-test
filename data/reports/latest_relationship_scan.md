# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-25T16:37:29.041711+00:00`
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

- `news_risk_high->unknown_24h` score `44.2014` n `51` status `ready` deltaP `4.6875` edge `3.6522` maxDD `0.0`
- `news_risk_high->unknown_4h` score `12.557` n `53` status `ready` deltaP `24.2176` edge `0.8949` maxDD `-0.1281`
- `news_risk_high->equity_24h` score `8.3258` n `51` status `ready` deltaP `32.2508` edge `0.5719` maxDD `-4.7801`
- `news_risk_high->index_24h` score `4.2698` n `51` status `ready` deltaP `42.5245` edge `0.0875` maxDD `-0.2147`
- `news_risk_high->unknown_1h` score `3.1634` n `53` status `ready` deltaP `16.162` edge `0.1914` maxDD `-0.8426`
- `news_risk_high->fx_4h` score `3.0002` n `53` status `ready` deltaP `35.573` edge `0.0263` maxDD `-0.0746`
- `market_context_high->unknown_4h` score `2.5984` n `133` status `ready` deltaP `22.3592` edge `0.1083` maxDD `-0.5994`
- `news_risk_high->equity_4h` score `1.8535` n `53` status `ready` deltaP `20.9561` edge `0.0918` maxDD `-2.164`
- `news_risk_high->fx_1h` score `1.1872` n `53` status `ready` deltaP `16.3682` edge `0.0068` maxDD `-0.0257`
- `news_risk_high->equity_1h` score `0.5019` n `53` status `ready` deltaP `14.1227` edge `0.0066` maxDD `-0.9128`
- `news_risk_high->commodity_1h` score `0.3709` n `53` status `ready` deltaP `10.2277` edge `-0.006` maxDD `-0.5024`
- `news_risk_high->index_4h` score `0.2572` n `53` status `ready` deltaP `8.1857` edge `0.0066` maxDD `-0.1788`
- `market_context_high->unknown_1h` score `0.1458` n `133` status `ready` deltaP `11.7216` edge `-0.0211` maxDD `-1.5916`
- `news_risk_high->index_1h` score `-0.0394` n `53` status `ready` deltaP `4.4487` edge `0.0006` maxDD `-0.1583`
- `news_risk_high->metal_24h` score `-0.2128` n `51` status `ready` deltaP `24.2545` edge `-0.1752` maxDD `-0.0053`
- `market_context_high->fx_1h` score `-0.4195` n `133` status `ready` deltaP `2.9479` edge `-0.0002` maxDD `-0.8587`
- `news_risk_high->metal_1h` score `-0.4271` n `53` status `ready` deltaP `-0.3135` edge `-0.0109` maxDD `-0.1413`
- `news_risk_high->metal_4h` score `-0.4288` n `53` status `ready` deltaP `5.5769` edge `-0.0198` maxDD `-0.249`
- `news_risk_high->crypto_alt_24h` score `-0.6204` n `51` status `ready` deltaP `21.1806` edge `-0.1929` maxDD `0.0`
- `market_context_high->metal_4h` score `-0.9292` n `133` status `ready` deltaP `4.5697` edge `-0.0442` maxDD `-2.4293`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
