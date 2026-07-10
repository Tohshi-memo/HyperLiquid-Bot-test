# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-10T20:52:30.034808+00:00`
- Price records: `672`
- Market context records: `6320`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11134`

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

- `news_risk_high->crypto_alt_24h` score `15.429` n `32` status `ready` deltaP `43.2292` edge `1.0123` maxDD `-0.5131`
- `news_risk_high->fx_24h` score `6.0452` n `32` status `ready` deltaP `50.6944` edge `0.1658` maxDD `0.0`
- `news_risk_high->crypto_major_24h` score `4.3637` n `32` status `ready` deltaP `16.6667` edge `0.5263` maxDD `-4.2368`
- `news_risk_high->fx_4h` score `4.2033` n `32` status `ready` deltaP `43.8262` edge `0.0627` maxDD `-0.0345`
- `news_risk_high->commodity_24h` score `3.3551` n `32` status `ready` deltaP `30.0347` edge `0.0999` maxDD `-0.3101`
- `news_risk_high->fx_1h` score `2.4374` n `32` status `ready` deltaP `29.3413` edge `0.0214` maxDD `-0.1113`
- `news_risk_high->crypto_major_1h` score `1.4974` n `32` status `ready` deltaP `14.8765` edge `0.1395` maxDD `-2.0691`
- `news_risk_high->crypto_alt_1h` score `0.9377` n `32` status `ready` deltaP `11.7702` edge `0.0879` maxDD `-1.6923`
- `market_context_high->unknown_1h` score `0.1911` n `208` status `ready` deltaP `-6.2644` edge `0.1585` maxDD `-3.7317`
- `market_context_high->metal_4h` score `0.0108` n `196` status `ready` deltaP `9.0032` edge `0.0372` maxDD `-2.7056`
- `market_context_high->metal_24h` score `-0.2146` n `154` status `ready` deltaP `19.9698` edge `0.0962` maxDD `-11.8809`
- `market_context_high->metal_1h` score `-0.406` n `208` status `ready` deltaP `3.5871` edge `0.0018` maxDD `-1.8877`
- `news_risk_high->index_24h` score `-0.5332` n `32` status `ready` deltaP `3.2986` edge `-0.0032` maxDD `-2.3058`
- `market_context_high->index_4h` score `-0.5739` n `196` status `ready` deltaP `3.9074` edge `0.0192` maxDD `-1.1723`
- `market_context_high->commodity_1h` score `-0.5929` n `208` status `ready` deltaP `-1.0796` edge `-0.0005` maxDD `-2.1314`
- `news_risk_high->metal_1h` score `-0.7465` n `32` status `ready` deltaP `-3.1437` edge `-0.025` maxDD `-1.6464`
- `market_context_high->index_1h` score `-0.7735` n `208` status `ready` deltaP `-3.4517` edge `0.0021` maxDD `-0.9269`
- `market_context_high->fx_1h` score `-0.8124` n `208` status `ready` deltaP `-1.9087` edge `-0.0022` maxDD `-0.889`
- `news_risk_high->unknown_1h` score `-0.8462` n `32` status `ready` deltaP `5.0337` edge `-0.0696` maxDD `-0.7581`
- `market_context_high->crypto_alt_1h` score `-1.0051` n `208` status `ready` deltaP `4.799` edge `0.0144` maxDD `-9.3536`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
