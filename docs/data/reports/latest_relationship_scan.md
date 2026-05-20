# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-20T22:42:09.107756+00:00`
- Price records: `672`
- Market context records: `1364`
- Flow alert records: `5840`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8804`

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

- `market_context_high->crypto_major_24h` score `13.2419` n `137` status `ready` deltaP `32.2169` edge `1.0019` maxDD `-8.0553`
- `market_context_high->metal_24h` score `12.6304` n `137` status `ready` deltaP `13.4479` edge `1.1296` maxDD `-6.3373`
- `market_context_high->crypto_alt_24h` score `10.1044` n `137` status `ready` deltaP `28.5394` edge `0.8534` maxDD `-15.1306`
- `market_context_high->index_24h` score `4.1388` n `137` status `ready` deltaP `22.9407` edge `0.3006` maxDD `-5.3574`
- `market_context_high->equity_24h` score `2.7466` n `137` status `ready` deltaP `15.9254` edge `0.3554` maxDD `-14.2815`
- `market_context_high->equity_4h` score `2.097` n `162` status `ready` deltaP `11.0471` edge `0.1716` maxDD `-3.6396`
- `market_context_high->fx_24h` score `1.0301` n `137` status `ready` deltaP `12.6508` edge `0.0527` maxDD `-0.7623`
- `market_context_high->metal_4h` score `0.0979` n `162` status `ready` deltaP `12.3833` edge `0.0687` maxDD `-6.4478`
- `market_context_high->index_1h` score `-0.0241` n `174` status `ready` deltaP `4.3379` edge `0.0134` maxDD `-1.6329`
- `market_context_high->index_4h` score `-0.0871` n `162` status `ready` deltaP `3.7545` edge `0.0727` maxDD `-3.7119`
- `market_context_high->equity_1h` score `-0.1188` n `174` status `ready` deltaP `1.9668` edge `0.0241` maxDD `-2.5289`
- `market_context_high->fx_1h` score `-0.3469` n `174` status `ready` deltaP `0.9275` edge `-0.0041` maxDD `-0.3914`
- `market_context_high->metal_1h` score `-0.362` n `174` status `ready` deltaP `6.1532` edge `0.0008` maxDD `-3.3919`
- `market_context_high->crypto_alt_1h` score `-0.5877` n `174` status `ready` deltaP `-0.8689` edge `0.0175` maxDD `-3.6309`
- `market_context_high->commodity_1h` score `-0.6081` n `174` status `ready` deltaP `0.3768` edge `0.0083` maxDD `-2.252`
- `market_context_high->commodity_24h` score `-1.0224` n `137` status `ready` deltaP `-10.4902` edge `0.3033` maxDD `-20.4854`
- `market_context_high->crypto_major_1h` score `-1.1119` n `174` status `ready` deltaP `-3.0955` edge `-0.0154` maxDD `-6.1883`
- `market_context_high->crypto_alt_4h` score `-1.4729` n `162` status `ready` deltaP `7.3377` edge `0.1603` maxDD `-19.5565`
- `market_context_high->fx_4h` score `-2.0285` n `162` status `ready` deltaP `-9.0691` edge `-0.015` maxDD `-1.1531`
- `market_context_high->crypto_major_4h` score `-2.0299` n `162` status `ready` deltaP `2.1492` edge `0.0874` maxDD `-13.3376`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
