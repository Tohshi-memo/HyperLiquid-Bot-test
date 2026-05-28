# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-28T18:52:22.963579+00:00`
- Price records: `672`
- Market context records: `2168`
- Flow alert records: `8137`
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

- `market_context_high->crypto_alt_4h` score `12.9481` n `135` status `ready` deltaP `36.6215` edge `0.9285` maxDD `-5.1574`
- `market_context_high->crypto_major_4h` score `11.842` n `135` status `ready` deltaP `42.1997` edge `0.7585` maxDD `-1.9063`
- `market_context_high->unknown_4h` score `5.5185` n `135` status `ready` deltaP `22.6784` edge `0.3836` maxDD `-2.6599`
- `news_risk_high->commodity_4h` score `3.8652` n `43` status `ready` deltaP `32.0051` edge `0.3493` maxDD `-3.0367`
- `market_context_high->equity_4h` score `3.7465` n `135` status `ready` deltaP `24.8193` edge `0.2562` maxDD `-5.0894`
- `market_context_high->crypto_major_1h` score `3.3046` n `135` status `ready` deltaP `17.7146` edge `0.205` maxDD `-1.817`
- `market_context_high->crypto_alt_1h` score `3.1169` n `135` status `ready` deltaP `16.3673` edge `0.237` maxDD `-4.9097`
- `market_context_high->index_24h` score `2.8037` n `135` status `ready` deltaP `11.5625` edge `0.2794` maxDD `-4.1604`
- `market_context_high->index_4h` score `2.7904` n `135` status `ready` deltaP `22.859` edge `0.1485` maxDD `-1.8022`
- `market_context_high->unknown_24h` score `2.7226` n `135` status `ready` deltaP `27.6042` edge `0.5749` maxDD `-35.8966`
- `market_context_high->crypto_major_24h` score `2.5145` n `135` status `ready` deltaP `20.6134` edge `1.0302` maxDD `-61.2872`
- `news_risk_high->fx_4h` score `2.1014` n `43` status `ready` deltaP `26.8221` edge `0.0147` maxDD `-0.1382`
- `market_context_high->equity_24h` score `2.0039` n `135` status `ready` deltaP `23.9005` edge `0.4975` maxDD `-33.1875`
- `market_context_high->metal_4h` score `1.56` n `135` status `ready` deltaP `18.0815` edge `0.1482` maxDD `-4.7664`
- `news_risk_high->unknown_4h` score `1.5501` n `43` status `ready` deltaP `15.8395` edge `0.0959` maxDD `-2.7857`
- `news_risk_high->equity_4h` score `1.3768` n `43` status `ready` deltaP `-2.2264` edge `0.3121` maxDD `-4.6598`
- `news_risk_high->unknown_1h` score `1.3172` n `43` status `ready` deltaP `21.1948` edge `0.0154` maxDD `-1.7548`
- `news_risk_high->commodity_1h` score `0.7853` n `43` status `ready` deltaP `10.6148` edge `0.0979` maxDD `-2.1052`
- `market_context_high->equity_1h` score `0.5155` n `135` status `ready` deltaP `10.0643` edge `0.0547` maxDD `-2.6402`
- `news_risk_high->fx_1h` score `0.4621` n `43` status `ready` deltaP `8.1395` edge `0.0099` maxDD `-0.0524`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
