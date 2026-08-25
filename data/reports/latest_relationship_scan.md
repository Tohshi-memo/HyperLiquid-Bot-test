# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-25T23:22:31.289339+00:00`
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

- `news_risk_high->unknown_24h` score `45.4212` n `51` status `ready` deltaP `9.375` edge `3.7226` maxDD `0.0`
- `news_risk_high->unknown_4h` score `12.6282` n `53` status `ready` deltaP `24.5225` edge `0.8988` maxDD `-0.1281`
- `news_risk_high->equity_24h` score `7.1721` n `51` status `ready` deltaP `29.9939` edge `0.4908` maxDD `-4.7801`
- `news_risk_high->index_24h` score `3.9848` n `51` status `ready` deltaP `40.2676` edge `0.0788` maxDD `-0.2147`
- `news_risk_high->unknown_1h` score `3.209` n `53` status `ready` deltaP `16.0123` edge `0.1962` maxDD `-0.8426`
- `news_risk_high->fx_4h` score `2.9811` n `53` status `ready` deltaP `35.573` edge `0.0247` maxDD `-0.0746`
- `news_risk_high->crypto_alt_24h` score `2.757` n `51` status `ready` deltaP `25.8681` edge `0.0573` maxDD `0.0`
- `market_context_high->unknown_4h` score `2.6696` n `133` status `ready` deltaP `22.6641` edge `0.1122` maxDD `-0.5994`
- `news_risk_high->equity_4h` score `1.4878` n `53` status `ready` deltaP `18.3646` edge `0.0786` maxDD `-2.164`
- `news_risk_high->fx_1h` score `1.1393` n `53` status `ready` deltaP `15.7694` edge `0.0068` maxDD `-0.0257`
- `news_risk_high->metal_24h` score `0.6504` n `51` status `ready` deltaP `27.3795` edge `-0.1241` maxDD `-0.0053`
- `news_risk_high->commodity_1h` score `0.4619` n `53` status `ready` deltaP `11.1259` edge `-0.0044` maxDD `-0.5024`
- `news_risk_high->equity_1h` score `0.3632` n `53` status `ready` deltaP `12.476` edge `-0.0002` maxDD `-0.9128`
- `market_context_high->unknown_1h` score `0.1914` n `133` status `ready` deltaP `11.5719` edge `-0.0163` maxDD `-1.5916`
- `news_risk_high->index_4h` score `0.0029` n `53` status `ready` deltaP `5.4418` edge `0.0037` maxDD `-0.1788`
- `news_risk_high->index_1h` score `-0.0869` n `53` status `ready` deltaP `3.7002` edge `-0.0005` maxDD `-0.1583`
- `market_context_high->unknown_24h` score `-0.186` n `125` status `ready` deltaP `9.375` edge `-0.078` maxDD `0.0`
- `market_context_high->fx_1h` score `-0.4506` n `133` status `ready` deltaP `2.3491` edge `-0.0002` maxDD `-0.8587`
- `news_risk_high->metal_1h` score `-0.6092` n `53` status `ready` deltaP `-2.2596` edge `-0.0131` maxDD `-0.1413`
- `news_risk_high->metal_4h` score `-0.7345` n `53` status `ready` deltaP `2.9855` edge `-0.028` maxDD `-0.249`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
