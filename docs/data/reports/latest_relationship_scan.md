# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-26T02:22:31.883274+00:00`
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

- `news_risk_high->unknown_24h` score `46.0715` n `51` status `ready` deltaP `11.4583` edge `3.7629` maxDD `0.0`
- `news_risk_high->unknown_4h` score `12.6486` n `53` status `ready` deltaP `24.5225` edge `0.9005` maxDD `-0.1281`
- `news_risk_high->equity_24h` score `7.0317` n `51` status `ready` deltaP `29.9939` edge `0.4791` maxDD `-4.7801`
- `news_risk_high->crypto_alt_24h` score `4.8785` n `51` status `ready` deltaP `27.9514` edge `0.2202` maxDD `0.0`
- `news_risk_high->index_24h` score `3.992` n `51` status `ready` deltaP `40.2676` edge `0.0794` maxDD `-0.2147`
- `news_risk_high->unknown_1h` score `3.3458` n `53` status `ready` deltaP `16.162` edge `0.2066` maxDD `-0.8426`
- `news_risk_high->fx_4h` score `2.8583` n `53` status `ready` deltaP `34.3535` edge `0.0226` maxDD `-0.0746`
- `market_context_high->unknown_4h` score `2.69` n `133` status `ready` deltaP `22.6641` edge `0.1139` maxDD `-0.5994`
- `news_risk_high->equity_4h` score `1.5654` n `53` status `ready` deltaP `18.9744` edge `0.081` maxDD `-2.164`
- `news_risk_high->metal_24h` score `1.1061` n `51` status `ready` deltaP `29.1156` edge `-0.0977` maxDD `-0.0053`
- `news_risk_high->fx_1h` score `1.071` n `53` status `ready` deltaP `15.0209` edge `0.0061` maxDD `-0.0257`
- `news_risk_high->commodity_1h` score `0.5062` n `53` status `ready` deltaP `11.575` edge `-0.0037` maxDD `-0.5024`
- `news_risk_high->equity_1h` score `0.4637` n `53` status `ready` deltaP `13.3742` edge `0.0067` maxDD `-0.9128`
- `market_context_high->unknown_1h` score `0.3282` n `133` status `ready` deltaP `11.7216` edge `-0.0059` maxDD `-1.5916`
- `news_risk_high->index_4h` score `0.0077` n `53` status `ready` deltaP `5.4418` edge `0.0041` maxDD `-0.1788`
- `news_risk_high->index_1h` score `-0.0737` n `53` status `ready` deltaP `3.8499` edge `0.0002` maxDD `-0.1583`
- `market_context_high->fx_1h` score `-0.495` n `133` status `ready` deltaP `1.6006` edge `-0.0009` maxDD `-0.8587`
- `news_risk_high->metal_1h` score `-0.5684` n `53` status `ready` deltaP `-1.8105` edge `-0.0127` maxDD `-0.1413`
- `news_risk_high->metal_4h` score `-0.7369` n `53` status `ready` deltaP `2.9855` edge `-0.0282` maxDD `-0.249`
- `news_risk_high->commodity_4h` score `-1.0711` n `53` status `ready` deltaP `-2.4304` edge `0.0022` maxDD `-1.1986`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
