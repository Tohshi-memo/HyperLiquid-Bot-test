# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-19T04:07:14.529838+00:00`
- Price records: `672`
- Market context records: `1184`
- Flow alert records: `5313`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8768`

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

- `market_context_high->crypto_major_24h` score `18.7105` n `144` status `ready` deltaP `44.4445` edge `1.3761` maxDD `-8.0553`
- `market_context_high->crypto_alt_24h` score `8.2778` n `144` status `ready` deltaP `22.2223` edge `0.7433` maxDD `-15.1306`
- `market_context_high->metal_24h` score `4.3676` n `144` status `ready` deltaP `-2.7778` edge `0.5492` maxDD `-6.3373`
- `market_context_high->equity_4h` score `2.7311` n `144` status `ready` deltaP `14.5833` edge `0.1967` maxDD `-3.6396`
- `market_context_high->index_24h` score `2.6112` n `144` status `ready` deltaP `14.9306` edge `0.2267` maxDD `-5.3574`
- `market_context_high->equity_24h` score `2.4908` n `144` status `ready` deltaP `15.2778` edge `0.3384` maxDD `-14.2815`
- `market_context_high->unknown_4h` score `2.4402` n `144` status `ready` deltaP `5.2507` edge `0.29` maxDD `-6.7322`
- `market_context_high->index_4h` score `1.1164` n `144` status `ready` deltaP `10.3998` edge `0.092` maxDD `-2.1308`
- `market_context_high->index_1h` score `0.6996` n `144` status `ready` deltaP `9.6889` edge `0.0254` maxDD `-0.5353`
- `market_context_high->equity_1h` score `0.2965` n `144` status `ready` deltaP `2.7861` edge `0.0439` maxDD `-1.3546`
- `market_context_high->fx_1h` score `-0.0321` n `144` status `ready` deltaP `6.2791` edge `-0.0004` maxDD `-0.3124`
- `market_context_high->crypto_major_4h` score `-0.1444` n `144` status `ready` deltaP `7.08` edge `0.1264` maxDD `-8.3693`
- `market_context_high->crypto_major_1h` score `-0.2653` n `144` status `ready` deltaP `4.2083` edge `0.0145` maxDD `-4.1256`
- `market_context_high->metal_1h` score `-0.2851` n `144` status `ready` deltaP `7.4518` edge `-0.0124` maxDD `-2.2164`
- `market_context_high->crypto_alt_1h` score `-0.4438` n `144` status `ready` deltaP `-0.079` edge `0.0279` maxDD `-3.4088`
- `market_context_high->fx_24h` score `-0.8379` n `144` status `ready` deltaP `5.9028` edge `0.0263` maxDD `-8.513`
- `market_context_high->fx_4h` score `-1.0305` n `144` status `ready` deltaP `-4.7934` edge `-0.0059` maxDD `-1.2071`
- `market_context_high->commodity_1h` score `-1.055` n `144` status `ready` deltaP `-3.8673` edge `-0.0003` maxDD `-2.2799`
- `market_context_high->crypto_alt_4h` score `-1.4066` n `144` status `ready` deltaP `2.5745` edge `0.099` maxDD `-16.7194`
- `market_context_high->metal_4h` score `-1.8784` n `144` status `ready` deltaP `4.4377` edge `-0.075` maxDD `-9.2991`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
