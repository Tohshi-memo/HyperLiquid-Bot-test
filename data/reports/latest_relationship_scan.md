# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-27T06:07:17.595539+00:00`
- Price records: `672`
- Market context records: `2015`
- Flow alert records: `7691`
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

- `market_context_high->crypto_major_4h` score `8.9335` n `208` status `ready` deltaP `30.9686` edge `0.591` maxDD `-1.9063`
- `market_context_high->crypto_alt_4h` score `8.4379` n `208` status `ready` deltaP `24.8593` edge `0.6519` maxDD `-5.1574`
- `market_context_high->unknown_4h` score `5.8682` n `208` status `ready` deltaP `19.0549` edge `0.4369` maxDD `-2.6599`
- `market_context_high->equity_4h` score `2.8681` n `208` status `ready` deltaP `16.4634` edge `0.2387` maxDD `-5.0894`
- `market_context_high->crypto_major_1h` score `1.5317` n `208` status `ready` deltaP `12.5633` edge `0.1425` maxDD `-3.2225`
- `market_context_high->index_4h` score `1.2785` n `208` status `ready` deltaP `12.0309` edge `0.0947` maxDD `-1.8022`
- `market_context_high->crypto_alt_1h` score `1.241` n `208` status `ready` deltaP `10.1681` edge `0.147` maxDD `-4.9097`
- `market_context_high->unknown_24h` score `0.6687` n `188` status `ready` deltaP `15.9101` edge `0.4817` maxDD `-35.8966`
- `market_context_high->metal_24h` score `0.4347` n `188` status `ready` deltaP `13.1741` edge `0.191` maxDD `-12.7414`
- `market_context_high->equity_24h` score `0.3329` n `188` status `ready` deltaP `14.7734` edge `0.4191` maxDD `-33.1875`
- `market_context_high->equity_1h` score `0.1531` n `208` status `ready` deltaP `6.4343` edge `0.0487` maxDD `-2.6402`
- `market_context_high->unknown_1h` score `0.0118` n `208` status `ready` deltaP `3.6821` edge `0.0484` maxDD `-3.0902`
- `market_context_high->index_24h` score `-0.0617` n `188` status `ready` deltaP `3.0749` edge `0.0972` maxDD `-4.1604`
- `market_context_high->fx_24h` score `-0.0714` n `188` status `ready` deltaP `13.6549` edge `0.0258` maxDD `-2.1561`
- `market_context_high->index_1h` score `-0.3697` n `208` status `ready` deltaP `1.8943` edge `0.0156` maxDD `-1.3898`
- `market_context_high->fx_1h` score `-0.8047` n `208` status `ready` deltaP `-0.7485` edge `0.0007` maxDD `-0.3548`
- `market_context_high->fx_4h` score `-1.0076` n `208` status `ready` deltaP `-5.9451` edge `-0.0014` maxDD `-1.0513`
- `market_context_high->metal_1h` score `-1.0138` n `208` status `ready` deltaP `3.1293` edge `0.0134` maxDD `-5.166`
- `market_context_high->metal_4h` score `-1.5599` n `208` status `ready` deltaP `7.2115` edge `0.0842` maxDD `-11.9812`
- `market_context_high->commodity_1h` score `-1.8087` n `208` status `ready` deltaP `3.302` edge `0.0019` maxDD `-15.7972`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
