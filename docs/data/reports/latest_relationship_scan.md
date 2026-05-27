# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-27T06:22:17.357140+00:00`
- Price records: `672`
- Market context records: `2016`
- Flow alert records: `7694`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9085`

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

- `market_context_high->crypto_major_4h` score `8.9277` n `207` status `ready` deltaP `30.9105` edge `0.5909` maxDD `-1.9063`
- `market_context_high->crypto_alt_4h` score `8.4236` n `207` status `ready` deltaP `24.7548` edge `0.6514` maxDD `-5.1574`
- `market_context_high->unknown_4h` score `5.8885` n `207` status `ready` deltaP `18.9341` edge `0.4394` maxDD `-2.6599`
- `market_context_high->equity_4h` score `2.8766` n `207` status `ready` deltaP `16.5253` edge `0.239` maxDD `-5.0894`
- `market_context_high->crypto_major_1h` score `1.5176` n `207` status `ready` deltaP `12.3868` edge `0.1425` maxDD `-3.2225`
- `market_context_high->index_4h` score `1.2846` n `207` status `ready` deltaP `12.0766` edge `0.0949` maxDD `-1.8022`
- `market_context_high->crypto_alt_1h` score `1.2245` n `207` status `ready` deltaP `9.9916` edge `0.1468` maxDD `-4.9097`
- `market_context_high->unknown_24h` score `0.5235` n `188` status `ready` deltaP `15.9101` edge `0.4696` maxDD `-35.8966`
- `market_context_high->metal_24h` score `0.3075` n `188` status `ready` deltaP `12.8133` edge `0.1828` maxDD `-12.7414`
- `market_context_high->equity_24h` score `0.2333` n `188` status `ready` deltaP `14.7734` edge `0.4108` maxDD `-33.1875`
- `market_context_high->equity_1h` score `0.1555` n `207` status `ready` deltaP `6.4191` edge `0.049` maxDD `-2.6402`
- `market_context_high->unknown_1h` score `0.0451` n `207` status `ready` deltaP `3.8134` edge `0.0503` maxDD `-3.0902`
- `market_context_high->index_24h` score `-0.1109` n `188` status `ready` deltaP `3.0749` edge `0.0931` maxDD `-4.1604`
- `market_context_high->fx_24h` score `-0.1534` n `188` status `ready` deltaP `13.2942` edge `0.0257` maxDD `-2.1686`
- `market_context_high->index_1h` score `-0.3718` n `207` status `ready` deltaP `1.8536` edge `0.0157` maxDD `-1.3898`
- `market_context_high->fx_1h` score `-0.8252` n `207` status `ready` deltaP `-0.99` edge `0.0006` maxDD `-0.3548`
- `market_context_high->fx_4h` score `-0.9942` n `207` status `ready` deltaP `-5.7036` edge `-0.0013` maxDD `-1.0513`
- `market_context_high->metal_1h` score `-1.0038` n `207` status `ready` deltaP `3.0584` edge `0.0147` maxDD `-5.166`
- `market_context_high->metal_4h` score `-1.5738` n `207` status `ready` deltaP `7.1572` edge `0.0834` maxDD `-11.9812`
- `market_context_high->commodity_1h` score `-1.8144` n `207` status `ready` deltaP `3.2218` edge `0.0017` maxDD `-15.7972`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
