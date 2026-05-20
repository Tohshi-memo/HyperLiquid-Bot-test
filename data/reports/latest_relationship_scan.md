# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-20T21:22:15.035344+00:00`
- Price records: `672`
- Market context records: `1358`
- Flow alert records: `5823`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8794`

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

- `market_context_high->crypto_major_24h` score `13.4038` n `132` status `ready` deltaP `32.8914` edge `1.0109` maxDD `-8.0553`
- `market_context_high->metal_24h` score `12.6881` n `132` status `ready` deltaP `12.5632` edge `1.1403` maxDD `-6.3373`
- `market_context_high->crypto_alt_24h` score `9.7425` n `132` status `ready` deltaP `28.4565` edge `0.8238` maxDD `-15.1306`
- `market_context_high->index_24h` score `4.1221` n `132` status `ready` deltaP `23.4217` edge `0.296` maxDD `-5.3574`
- `market_context_high->equity_24h` score `2.8791` n `132` status `ready` deltaP `16.351` edge `0.3636` maxDD `-14.2815`
- `market_context_high->equity_4h` score `2.311` n `157` status `ready` deltaP `11.8912` edge `0.1838` maxDD `-3.6396`
- `market_context_high->commodity_24h` score `1.9673` n `132` status `ready` deltaP `-8.9804` edge `0.4002` maxDD `-9.111`
- `market_context_high->fx_24h` score `1.3262` n `132` status `ready` deltaP `14.7412` edge `0.0587` maxDD `-0.3831`
- `market_context_high->metal_4h` score `0.1757` n `157` status `ready` deltaP `13.2205` edge `0.0696` maxDD `-6.4478`
- `market_context_high->index_1h` score `0.0464` n `169` status `ready` deltaP `5.0518` edge `0.0156` maxDD `-1.6329`
- `market_context_high->equity_1h` score `0.0174` n `169` status `ready` deltaP `2.6637` edge `0.0283` maxDD `-1.9017`
- `market_context_high->index_4h` score `-0.0` n `157` status `ready` deltaP `4.8742` edge `0.0764` maxDD `-3.7119`
- `market_context_high->metal_1h` score `-0.175` n `169` status `ready` deltaP `7.1901` edge `-0.001` maxDD `-2.883`
- `market_context_high->fx_1h` score `-0.2937` n `169` status `ready` deltaP `1.9001` edge `-0.0039` maxDD `-0.3808`
- `market_context_high->commodity_1h` score `-0.5353` n `169` status `ready` deltaP `0.5811` edge `0.013` maxDD `-2.252`
- `market_context_high->unknown_24h` score `-0.8007` n `132` status `ready` deltaP `-4.4034` edge `0.2356` maxDD `-10.1706`
- `market_context_high->crypto_alt_1h` score `-0.843` n `169` status `ready` deltaP `-0.4951` edge `0.0201` maxDD `-3.6309`
- `market_context_high->crypto_major_1h` score `-1.1735` n `169` status `ready` deltaP `-3.7248` edge `-0.0191` maxDD `-6.1883`
- `market_context_high->crypto_alt_4h` score `-1.2635` n `157` status `ready` deltaP `8.62` edge `0.1692` maxDD `-19.5565`
- `market_context_high->unknown_4h` score `-1.3679` n `157` status `ready` deltaP `1.5817` edge `0.0412` maxDD `-11.1695`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
