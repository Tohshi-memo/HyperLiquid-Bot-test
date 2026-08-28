# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-28T04:52:28.961258+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11831`

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

- `news_risk_high->unknown_24h` score `52.7478` n `50` status `ready` deltaP `11.6319` edge `4.3181` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `27.465` n `50` status `ready` deltaP `37.8403` edge `2.0806` maxDD `-2.8629`
- `news_risk_high->unknown_4h` score `12.6616` n `50` status `ready` deltaP `24.6402` edge `0.9008` maxDD `-0.1279`
- `news_risk_high->metal_24h` score `5.3629` n `50` status `ready` deltaP `49.0417` edge `0.1242` maxDD `-0.0053`
- `news_risk_high->equity_24h` score `5.2447` n `50` status `ready` deltaP `29.4861` edge `0.3333` maxDD `-4.7584`
- `news_risk_high->fx_4h` score `3.8689` n `50` status `ready` deltaP `45.2012` edge `0.0301` maxDD `-0.0559`
- `market_context_high->unknown_24h` score `3.3234` n `128` status `ready` deltaP `5.3819` edge `0.3143` maxDD `-3.1917`
- `news_risk_high->unknown_1h` score `2.99` n `50` status `ready` deltaP `16.2275` edge `0.1766` maxDD `-0.8495`
- `news_risk_high->index_24h` score `2.7449` n `50` status `ready` deltaP `30.7083` edge `0.0391` maxDD `-0.2064`
- `market_context_high->unknown_4h` score `2.2186` n `148` status `ready` deltaP `17.8024` edge `0.1069` maxDD `-0.5894`
- `news_risk_high->fx_1h` score `1.5635` n `50` status `ready` deltaP `20.9521` edge `0.0076` maxDD `-0.0257`
- `news_risk_high->equity_1h` score `1.3752` n `50` status `ready` deltaP `18.4611` edge `0.0194` maxDD `-0.2301`
- `news_risk_high->equity_4h` score `1.3118` n `50` status `ready` deltaP `21.2744` edge `0.0438` maxDD `-2.105`
- `market_context_high->unknown_1h` score `0.8666` n `148` status `ready` deltaP `8.5248` edge `0.0604` maxDD `-1.6015`
- `news_risk_high->commodity_1h` score `0.516` n `50` status `ready` deltaP `14.2994` edge `0.0021` maxDD `-0.5024`
- `news_risk_high->metal_4h` score `0.2906` n `50` status `ready` deltaP `10.9695` edge `0.0042` maxDD `-0.249`
- `news_risk_high->index_1h` score `0.1795` n `50` status `ready` deltaP `8.4072` edge `0.0009` maxDD `-0.0486`
- `news_risk_high->metal_1h` score `0.1669` n `50` status `ready` deltaP `6.4491` edge `0.001` maxDD `-0.1413`
- `news_risk_high->crypto_major_24h` score `-0.0125` n `50` status `ready` deltaP `18.0278` edge `-0.0719` maxDD `-2.6128`
- `market_context_high->metal_24h` score `-0.0254` n `128` status `ready` deltaP `13.5417` edge `0.0719` maxDD `-3.8102`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
