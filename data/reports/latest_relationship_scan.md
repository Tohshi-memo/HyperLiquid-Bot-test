# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-26T10:52:34.400491+00:00`
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

- `news_risk_high->unknown_24h` score `44.5914` n `53` status `ready` deltaP `11.6319` edge `3.6384` maxDD `0.0`
- `news_risk_high->unknown_4h` score `11.8502` n `53` status `ready` deltaP `23.303` edge `0.8421` maxDD `-0.1281`
- `news_risk_high->crypto_alt_24h` score `8.5622` n `53` status `ready` deltaP `30.0806` edge `0.5571` maxDD `-2.8629`
- `news_risk_high->equity_24h` score `7.0725` n `53` status `ready` deltaP `30.1134` edge `0.4817` maxDD `-4.7801`
- `news_risk_high->index_24h` score `4.0258` n `53` status `ready` deltaP `39.9404` edge `0.0844` maxDD `-0.2147`
- `news_risk_high->fx_4h` score `2.8219` n `53` status `ready` deltaP `34.0486` edge `0.0216` maxDD `-0.0746`
- `news_risk_high->unknown_1h` score `2.7507` n `53` status `ready` deltaP `15.4135` edge `0.162` maxDD `-0.8426`
- `market_context_high->unknown_4h` score `2.4833` n `136` status `ready` deltaP `21.6105` edge `0.1037` maxDD `-0.5994`
- `news_risk_high->equity_4h` score `1.7683` n `53` status `ready` deltaP `20.0414` edge `0.0908` maxDD `-2.164`
- `news_risk_high->metal_24h` score `1.7144` n `53` status `ready` deltaP `29.1896` edge `-0.0475` maxDD `-0.0053`
- `news_risk_high->fx_1h` score `1.1021` n `53` status `ready` deltaP `15.47` edge `0.0057` maxDD `-0.0257`
- `market_context_high->unknown_1h` score `1.069` n `136` status `ready` deltaP `11.4873` edge `0.0574` maxDD `-1.5916`
- `news_risk_high->commodity_1h` score `0.4871` n `53` status `ready` deltaP `11.2756` edge `-0.0033` maxDD `-0.5024`
- `news_risk_high->equity_1h` score `0.4178` n `53` status `ready` deltaP `12.6257` edge `0.0058` maxDD `-0.9128`
- `news_risk_high->index_4h` score `0.1839` n `53` status `ready` deltaP `7.1186` edge `0.0076` maxDD `-0.1788`
- `news_risk_high->index_1h` score `-0.0721` n `53` status `ready` deltaP `3.8499` edge `0.0004` maxDD `-0.1583`
- `news_risk_high->metal_4h` score `-0.3908` n `53` status `ready` deltaP `5.2721` edge `-0.0146` maxDD `-0.249`
- `news_risk_high->metal_1h` score `-0.4055` n `53` status `ready` deltaP `-0.0141` edge `-0.0111` maxDD `-0.1413`
- `market_context_high->fx_1h` score `-0.4224` n `136` status `ready` deltaP `3.0116` edge `-0.001` maxDD `-0.8587`
- `news_risk_high->commodity_4h` score `-0.9519` n `53` status `ready` deltaP `-0.7536` edge `0.0063` maxDD `-1.1986`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
