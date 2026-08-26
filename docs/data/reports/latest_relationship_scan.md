# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-26T01:54:48.130997+00:00`
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

- `news_risk_high->unknown_24h` score `45.9633` n `51` status `ready` deltaP `11.1111` edge `3.7562` maxDD `0.0`
- `news_risk_high->unknown_4h` score `12.6668` n `53` status `ready` deltaP `24.675` edge `0.901` maxDD `-0.1281`
- `news_risk_high->equity_24h` score `7.0497` n `51` status `ready` deltaP `29.9939` edge `0.4806` maxDD `-4.7801`
- `news_risk_high->crypto_alt_24h` score `4.5171` n `51` status `ready` deltaP `27.6042` edge `0.1924` maxDD `0.0`
- `news_risk_high->index_24h` score `3.986` n `51` status `ready` deltaP `40.2676` edge `0.0789` maxDD `-0.2147`
- `news_risk_high->unknown_1h` score `3.3649` n `53` status `ready` deltaP `16.3117` edge `0.2072` maxDD `-0.8426`
- `news_risk_high->fx_4h` score `2.8595` n `53` status `ready` deltaP `34.3535` edge `0.0227` maxDD `-0.0746`
- `market_context_high->unknown_4h` score `2.7082` n `133` status `ready` deltaP `22.8166` edge `0.1144` maxDD `-0.5994`
- `news_risk_high->equity_4h` score `1.581` n `53` status `ready` deltaP `18.9744` edge `0.0823` maxDD `-2.164`
- `news_risk_high->metal_24h` score `1.0737` n `51` status `ready` deltaP `29.1156` edge `-0.1004` maxDD `-0.0053`
- `news_risk_high->fx_1h` score `1.0722` n `53` status `ready` deltaP `15.0209` edge `0.0062` maxDD `-0.0257`
- `news_risk_high->commodity_1h` score `0.5182` n `53` status `ready` deltaP `11.7247` edge `-0.0037` maxDD `-0.5024`
- `news_risk_high->equity_1h` score `0.4785` n `53` status `ready` deltaP `13.5239` edge `0.0076` maxDD `-0.9128`
- `market_context_high->unknown_1h` score `0.3474` n `133` status `ready` deltaP `11.8713` edge `-0.0053` maxDD `-1.5916`
- `news_risk_high->index_4h` score `0.0077` n `53` status `ready` deltaP `5.4418` edge `0.0041` maxDD `-0.1788`
- `news_risk_high->index_1h` score `-0.0573` n `53` status `ready` deltaP `4.1493` edge `0.0003` maxDD `-0.1583`
- `market_context_high->fx_1h` score `-0.4942` n `133` status `ready` deltaP `1.6006` edge `-0.0008` maxDD `-0.8587`
- `news_risk_high->metal_1h` score `-0.5385` n `53` status `ready` deltaP `-1.5111` edge `-0.0122` maxDD `-0.1413`
- `news_risk_high->metal_4h` score `-0.7041` n `53` status `ready` deltaP `3.2904` edge `-0.0275` maxDD `-0.249`
- `news_risk_high->commodity_4h` score `-1.0734` n `53` status `ready` deltaP `-2.4304` edge `0.0019` maxDD `-1.1986`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
