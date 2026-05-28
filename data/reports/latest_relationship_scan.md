# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-28T19:07:21.446227+00:00`
- Price records: `672`
- Market context records: `2169`
- Flow alert records: `8140`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9188`

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

- `market_context_high->crypto_alt_4h` score `12.9361` n `135` status `ready` deltaP `36.6215` edge `0.9275` maxDD `-5.1574`
- `market_context_high->crypto_major_4h` score `11.8168` n `135` status `ready` deltaP `42.1997` edge `0.7564` maxDD `-1.9063`
- `market_context_high->unknown_4h` score `5.5149` n `135` status `ready` deltaP `22.6784` edge `0.3833` maxDD `-2.6599`
- `news_risk_high->commodity_4h` score `3.8433` n `43` status `ready` deltaP `31.8526` edge `0.3475` maxDD `-3.0367`
- `market_context_high->equity_4h` score `3.7501` n `135` status `ready` deltaP `24.8193` edge `0.2565` maxDD `-5.0894`
- `market_context_high->crypto_major_1h` score `3.2866` n `135` status `ready` deltaP `17.5649` edge `0.2045` maxDD `-1.817`
- `market_context_high->crypto_alt_1h` score `3.1169` n `135` status `ready` deltaP `16.3673` edge `0.237` maxDD `-4.9097`
- `market_context_high->index_24h` score `2.8073` n `135` status `ready` deltaP `11.5625` edge `0.2797` maxDD `-4.1604`
- `market_context_high->index_4h` score `2.7904` n `135` status `ready` deltaP `22.859` edge `0.1485` maxDD `-1.8022`
- `market_context_high->unknown_24h` score `2.7178` n `135` status `ready` deltaP `27.6042` edge `0.5745` maxDD `-35.8966`
- `market_context_high->crypto_major_24h` score `2.5199` n `135` status `ready` deltaP `20.6134` edge `1.0309` maxDD `-61.2872`
- `news_risk_high->fx_4h` score `2.1026` n `43` status `ready` deltaP `26.8221` edge `0.0148` maxDD `-0.1382`
- `market_context_high->equity_24h` score `1.9859` n `135` status `ready` deltaP `23.9005` edge `0.496` maxDD `-33.1875`
- `market_context_high->metal_4h` score `1.5564` n `135` status `ready` deltaP `18.0815` edge `0.1479` maxDD `-4.7664`
- `news_risk_high->unknown_4h` score `1.5465` n `43` status `ready` deltaP `15.8395` edge `0.0956` maxDD `-2.7857`
- `news_risk_high->equity_4h` score `1.3791` n `43` status `ready` deltaP `-2.2264` edge `0.3124` maxDD `-4.6598`
- `news_risk_high->unknown_1h` score `1.2956` n `43` status `ready` deltaP `21.0451` edge `0.0146` maxDD `-1.7548`
- `news_risk_high->commodity_1h` score `0.7736` n `43` status `ready` deltaP `10.4651` edge `0.0974` maxDD `-2.1052`
- `market_context_high->equity_1h` score `0.5167` n `135` status `ready` deltaP `10.0643` edge `0.0548` maxDD `-2.6402`
- `news_risk_high->fx_1h` score `0.4621` n `43` status `ready` deltaP `8.1395` edge `0.0099` maxDD `-0.0524`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
