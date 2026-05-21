# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-21T00:22:13.322962+00:00`
- Price records: `672`
- Market context records: `1372`
- Flow alert records: `5861`
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

- `market_context_high->crypto_major_24h` score `13.0973` n `144` status `ready` deltaP `31.25` edge `0.9963` maxDD `-8.0553`
- `market_context_high->metal_24h` score `12.2623` n `144` status `ready` deltaP `13.5417` edge `1.0983` maxDD `-6.3373`
- `market_context_high->crypto_alt_24h` score `10.5593` n `144` status `ready` deltaP `28.6459` edge `0.8906` maxDD `-15.1306`
- `market_context_high->index_24h` score `4.1138` n `144` status `ready` deltaP `22.2222` edge `0.3033` maxDD `-5.3574`
- `market_context_high->equity_24h` score `2.6036` n `144` status `ready` deltaP `15.2778` edge `0.3478` maxDD `-14.2815`
- `market_context_high->equity_4h` score `1.5612` n `169` status `ready` deltaP `8.5943` edge `0.1558` maxDD `-3.6396`
- `market_context_high->fx_24h` score `0.3816` n `144` status `ready` deltaP `10.0695` edge `0.0465` maxDD `-1.2129`
- `market_context_high->index_1h` score `-0.0853` n `181` status `ready` deltaP `3.506` edge `0.0122` maxDD `-1.7205`
- `market_context_high->metal_4h` score `-0.1344` n `169` status `ready` deltaP `10.7402` edge `0.0603` maxDD `-6.4478`
- `market_context_high->equity_1h` score `-0.1589` n `181` status `ready` deltaP `1.9627` edge `0.0224` maxDD `-2.8014`
- `market_context_high->index_4h` score `-0.3292` n `169` status `ready` deltaP `0.8397` edge `0.0611` maxDD `-3.7119`
- `market_context_high->fx_1h` score `-0.4415` n `181` status `ready` deltaP `1.9445` edge `-0.0032` maxDD `-0.3914`
- `market_context_high->metal_1h` score `-0.4599` n `181` status `ready` deltaP `5.6266` edge `0.0024` maxDD `-3.5762`
- `market_context_high->commodity_1h` score `-0.6941` n `181` status `ready` deltaP `-0.3689` edge `0.0061` maxDD `-2.252`
- `market_context_high->crypto_alt_1h` score `-0.8061` n `181` status `ready` deltaP `0.1017` edge `0.0192` maxDD `-3.6309`
- `market_context_high->crypto_major_1h` score `-1.0019` n `181` status `ready` deltaP `-2.119` edge `-0.0078` maxDD `-6.1883`
- `market_context_high->fx_4h` score `-1.3396` n `169` status `ready` deltaP `-8.9388` edge `-0.0151` maxDD `-1.4313`
- `market_context_high->crypto_alt_4h` score `-1.6646` n `169` status `ready` deltaP `6.6063` edge `0.1492` maxDD `-19.5565`
- `market_context_high->crypto_major_4h` score `-1.9021` n `169` status `ready` deltaP `3.102` edge `0.0917` maxDD `-13.3376`
- `market_context_high->unknown_4h` score `-3.0686` n `169` status `ready` deltaP `1.3367` edge `-0.1752` maxDD `-11.1695`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
