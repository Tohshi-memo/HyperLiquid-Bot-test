# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-19T10:22:20.426340+00:00`
- Price records: `672`
- Market context records: `1210`
- Flow alert records: `5390`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8776`

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

- `market_context_high->crypto_major_24h` score `18.6885` n `130` status `ready` deltaP `44.0946` edge `1.3766` maxDD `-8.0553`
- `market_context_high->crypto_alt_24h` score `7.1642` n `130` status `ready` deltaP `21.9979` edge `0.652` maxDD `-15.1306`
- `market_context_high->unknown_4h` score `6.9566` n `130` status `ready` deltaP `3.0699` edge `0.6809` maxDD `-6.7322`
- `market_context_high->commodity_24h` score `5.3115` n `130` status `ready` deltaP `-3.117` edge `0.6337` maxDD `-8.6239`
- `market_context_high->metal_24h` score `4.4621` n `130` status `ready` deltaP `-3.2612` edge `0.5603` maxDD `-6.3373`
- `market_context_high->equity_4h` score `2.8723` n `130` status `ready` deltaP `14.8335` edge `0.2068` maxDD `-3.6396`
- `market_context_high->index_24h` score `2.2171` n `130` status `ready` deltaP `18.2239` edge `0.1719` maxDD `-5.3574`
- `market_context_high->equity_24h` score `1.8839` n `130` status `ready` deltaP `18.4215` edge `0.3514` maxDD `-14.2815`
- `market_context_high->index_4h` score `0.9813` n `130` status `ready` deltaP `10.6614` edge `0.079` maxDD `-2.1308`
- `market_context_high->fx_24h` score `0.8354` n `130` status `ready` deltaP `9.5646` edge `0.0597` maxDD `-0.9743`
- `market_context_high->index_1h` score `0.5936` n `130` status `ready` deltaP `9.2631` edge `0.0194` maxDD `-0.5353`
- `market_context_high->equity_1h` score `0.4796` n `130` status `ready` deltaP `4.5601` edge `0.047` maxDD `-1.3281`
- `market_context_high->metal_1h` score `-0.1247` n `130` status `ready` deltaP `9.0972` edge `-0.01` maxDD `-2.2164`
- `market_context_high->fx_1h` score `-0.1526` n `130` status `ready` deltaP `4.8687` edge `0.0004` maxDD `-0.3124`
- `market_context_high->crypto_major_4h` score `-0.1796` n `130` status `ready` deltaP `5.6684` edge `0.1313` maxDD `-8.3693`
- `market_context_high->crypto_alt_1h` score `-0.3644` n `130` status `ready` deltaP `0.5942` edge `0.0336` maxDD `-3.4088`
- `market_context_high->crypto_major_1h` score `-0.38` n `130` status `ready` deltaP `3.0977` edge `0.0072` maxDD `-4.1256`
- `market_context_high->unknown_24h` score `-0.5046` n `130` status `ready` deltaP `0.1523` edge `0.2299` maxDD `-10.1706`
- `market_context_high->commodity_1h` score `-0.7648` n `130` status `ready` deltaP `-2.287` edge `0.013` maxDD `-2.252`
- `market_context_high->metal_4h` score `-0.7947` n `130` status `ready` deltaP `10.3963` edge `-0.0281` maxDD `-6.4478`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
