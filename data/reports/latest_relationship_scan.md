# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-28T04:52:29.876768+00:00`
- Price records: `672`
- Market context records: `8163`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11842`

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

- `news_risk_high->unknown_24h` score `7795.7818` n `32` status `ready` deltaP `37.1528` edge `649.4008` maxDD `0.0`
- `market_context_high->equity_24h` score `19.6407` n `67` status `ready` deltaP `44.4833` edge `1.4312` maxDD `-4.9489`
- `market_context_high->equity_4h` score `9.5309` n `68` status `ready` deltaP `37.9215` edge `0.5649` maxDD `-0.5442`
- `news_risk_high->equity_4h` score `8.9301` n `43` status `ready` deltaP `33.6465` edge `0.5404` maxDD `-0.6428`
- `market_context_high->metal_24h` score `8.3092` n `67` status `ready` deltaP `40.625` edge `0.4216` maxDD `0.0`
- `news_risk_high->crypto_major_4h` score `5.4606` n `43` status `ready` deltaP `20.3382` edge `0.38` maxDD `-2.1767`
- `market_context_high->index_4h` score `3.9915` n `68` status `ready` deltaP `36.4956` edge `0.0936` maxDD `-0.0092`
- `news_risk_high->equity_1h` score `3.5961` n `46` status `ready` deltaP `26.842` edge `0.1516` maxDD `-1.1366`
- `market_context_high->equity_1h` score `3.3875` n `68` status `ready` deltaP `19.9366` edge `0.1697` maxDD `-0.6254`
- `market_context_high->index_24h` score `3.169` n `67` status `ready` deltaP `20.9862` edge `0.1912` maxDD `-1.3621`
- `news_risk_high->index_4h` score `2.8492` n `43` status `ready` deltaP `23.7733` edge `0.098` maxDD `-0.191`
- `market_context_high->metal_4h` score `2.0523` n `68` status `ready` deltaP `22.6596` edge `0.0822` maxDD `-0.979`
- `market_context_high->fx_24h` score `1.8084` n `67` status `ready` deltaP `24.6683` edge `0.0566` maxDD `-0.6283`
- `news_risk_high->metal_4h` score `1.7182` n `43` status `ready` deltaP `15.9564` edge `0.0836` maxDD `-0.7433`
- `market_context_high->index_1h` score `1.6257` n `68` status `ready` deltaP `19.2673` edge `0.0223` maxDD `-0.2217`
- `news_risk_high->crypto_major_1h` score `1.4258` n `46` status `ready` deltaP `7.4915` edge `0.1086` maxDD `-1.1783`
- `market_context_high->commodity_24h` score `1.3692` n `67` status `ready` deltaP `30.0114` edge `0.264` maxDD `-15.7497`
- `market_context_high->crypto_major_4h` score `1.2518` n `68` status `ready` deltaP `8.7787` edge `0.2176` maxDD `-6.7444`
- `news_risk_high->crypto_alt_4h` score `1.1855` n `43` status `ready` deltaP `12.8651` edge `0.2054` maxDD `-5.8012`
- `market_context_high->crypto_major_1h` score `0.9664` n `68` status `ready` deltaP `10.4966` edge `0.0516` maxDD `-1.6171`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
