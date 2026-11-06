# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-06T09:07:27.534230+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4042`

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

- `news_risk_high->crypto_alt_4h` score `-0.2694` n `134` status `ready` deltaP `6.1066` edge `0.1884` maxDD `-14.0916`
- `news_risk_high->crypto_alt_1h` score `-0.5304` n `134` status `ready` deltaP `2.2477` edge `0.0398` maxDD `-5.8225`
- `news_risk_high->fx_1h` score `-0.7034` n `134` status `ready` deltaP `-2.6991` edge `-0.0021` maxDD `-0.6065`
- `news_risk_high->index_1h` score `-0.7745` n `134` status `ready` deltaP `2.1003` edge `0.0004` maxDD `-1.3155`
- `news_risk_high->index_4h` score `-1.0241` n `134` status `ready` deltaP `4.2205` edge `0.0106` maxDD `-3.2694`
- `news_risk_high->fx_4h` score `-1.3762` n `134` status `ready` deltaP `-7.8949` edge `-0.0119` maxDD `-1.6185`
- `news_risk_high->metal_1h` score `-1.3787` n `134` status `ready` deltaP `-6.5645` edge `-0.0178` maxDD `-2.5487`
- `news_risk_high->index_24h` score `-1.4963` n `134` status `ready` deltaP `-8.728` edge `0.0915` maxDD `-6.6786`
- `news_risk_high->crypto_major_1h` score `-2.0275` n `134` status `ready` deltaP `-4.6139` edge `-0.0072` maxDD `-6.1465`
- `news_risk_high->fx_24h` score `-2.1598` n `134` status `ready` deltaP `-21.8096` edge `-0.0212` maxDD `-1.4906`
- `news_risk_high->commodity_1h` score `-2.6838` n `134` status `ready` deltaP `-12.5391` edge `-0.0034` maxDD `-3.2657`
- `news_risk_high->crypto_major_4h` score `-3.0222` n `134` status `ready` deltaP `-5.8586` edge `0.0361` maxDD `-14.5781`
- `news_risk_high->equity_1h` score `-3.2308` n `134` status `ready` deltaP `-4.7725` edge `0.0035` maxDD `-14.2732`
- `news_risk_high->equity_24h` score `-3.6096` n `134` status `ready` deltaP `14.9461` edge `0.7957` maxDD `-86.0244`
- `news_risk_high->commodity_4h` score `-4.6055` n `134` status `ready` deltaP `-20.5588` edge `-0.0113` maxDD `-9.5011`
- `news_risk_high->metal_4h` score `-4.6795` n `134` status `ready` deltaP `-10.359` edge `-0.0694` maxDD `-7.7863`
- `news_risk_high->equity_4h` score `-6.793` n `134` status `ready` deltaP `4.6778` edge `0.0506` maxDD `-41.1629`
- `news_risk_high->metal_24h` score `-6.8927` n `134` status `ready` deltaP `-12.3147` edge `-0.2614` maxDD `-10.4717`
- `news_risk_high->commodity_24h` score `-10.7557` n `134` status `ready` deltaP `-21.4197` edge `0.0472` maxDD `-43.0569`
- `news_risk_high->crypto_alt_24h` score `-12.373` n `134` status `ready` deltaP `5.4717` edge `0.0767` maxDD `-118.6236`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
