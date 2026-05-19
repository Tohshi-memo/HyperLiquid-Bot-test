# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-19T07:07:16.885748+00:00`
- Price records: `672`
- Market context records: `1196`
- Flow alert records: `5350`
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

- `market_context_high->crypto_major_24h` score `18.5472` n `135` status `ready` deltaP `44.294` edge `1.3635` maxDD `-8.0553`
- `market_context_high->crypto_alt_24h` score `7.5371` n `135` status `ready` deltaP `22.0834` edge `0.6825` maxDD `-15.1306`
- `market_context_high->unknown_4h` score `5.3825` n `135` status `ready` deltaP `4.379` edge `0.541` maxDD `-6.7322`
- `market_context_high->metal_24h` score `4.1711` n `135` status `ready` deltaP `-4.2593` edge `0.5427` maxDD `-6.3373`
- `market_context_high->commodity_24h` score `2.8335` n `135` status `ready` deltaP `-3.3102` edge `0.5765` maxDD `-20.4643`
- `market_context_high->equity_4h` score `2.8317` n `135` status `ready` deltaP `14.956` edge `0.2026` maxDD `-3.6396`
- `market_context_high->index_24h` score `2.0108` n `135` status `ready` deltaP `16.3657` edge `0.1671` maxDD `-5.3574`
- `market_context_high->equity_24h` score `1.5367` n `135` status `ready` deltaP `16.6203` edge `0.3189` maxDD `-14.2815`
- `market_context_high->index_4h` score `0.9413` n `135` status `ready` deltaP `10.402` edge `0.0774` maxDD `-2.1308`
- `market_context_high->index_1h` score `0.494` n `135` status `ready` deltaP `8.3788` edge `0.017` maxDD `-0.5353`
- `market_context_high->equity_1h` score `0.3739` n `135` status `ready` deltaP `3.7691` edge `0.0438` maxDD `-1.3546`
- `market_context_high->fx_24h` score `0.3687` n `135` status `ready` deltaP `8.7732` edge `0.0538` maxDD `-3.1917`
- `market_context_high->crypto_major_4h` score `-0.0773` n `135` status `ready` deltaP `6.7965` edge `0.1369` maxDD `-8.3693`
- `market_context_high->fx_1h` score `-0.16` n `135` status `ready` deltaP `4.776` edge `0.0004` maxDD `-0.3124`
- `market_context_high->metal_1h` score `-0.2479` n `135` status `ready` deltaP `8.0073` edge `-0.013` maxDD `-2.2164`
- `market_context_high->crypto_major_1h` score `-0.3241` n `135` status `ready` deltaP `3.6172` edge `0.0109` maxDD `-4.1256`
- `market_context_high->crypto_alt_1h` score `-0.3793` n `135` status `ready` deltaP `0.6077` edge `0.0316` maxDD `-3.4088`
- `market_context_high->commodity_1h` score `-0.833` n `135` status `ready` deltaP `-2.7501` edge `0.0104` maxDD `-2.252`
- `market_context_high->unknown_24h` score `-0.881` n `135` status `ready` deltaP `1.7477` edge `0.1879` maxDD `-10.1706`
- `market_context_high->metal_4h` score `-0.9987` n `135` status `ready` deltaP `8.1086` edge `-0.039` maxDD `-6.4478`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
