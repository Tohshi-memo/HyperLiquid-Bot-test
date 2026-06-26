# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-26T14:22:26.888855+00:00`
- Price records: `672`
- Market context records: `4835`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `7610`

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

- `market_context_high->unknown_1h` score `13.8015` n `109` status `ready` deltaP `11.038` edge `1.1183` maxDD `-1.674`
- `market_context_high->unknown_4h` score `9.5101` n `102` status `ready` deltaP `21.9392` edge `0.7591` maxDD `-4.0284`
- `market_context_high->unknown_24h` score `3.8807` n `96` status `ready` deltaP `20.1389` edge `0.2498` maxDD `-2.1866`
- `market_context_high->index_4h` score `0.5789` n `102` status `ready` deltaP `8.6263` edge `0.0374` maxDD `-0.7334`
- `market_context_high->equity_1h` score `0.2822` n `109` status `ready` deltaP `4.5775` edge `0.0546` maxDD `-2.928`
- `market_context_high->equity_4h` score `0.2531` n `102` status `ready` deltaP `10.5003` edge `0.1006` maxDD `-6.3852`
- `market_context_high->commodity_4h` score `0.1018` n `102` status `ready` deltaP `13.1337` edge `0.0427` maxDD `-4.377`
- `market_context_high->commodity_1h` score `0.0759` n `109` status `ready` deltaP `4.5006` edge `0.0279` maxDD `-1.1869`
- `market_context_high->fx_4h` score `-0.2102` n `102` status `ready` deltaP `5.3593` edge `0.0055` maxDD `-0.788`
- `market_context_high->crypto_alt_4h` score `-0.2508` n `102` status `ready` deltaP `12.6793` edge `0.159` maxDD `-19.0551`
- `market_context_high->fx_1h` score `-0.8096` n `109` status `ready` deltaP `-5.1228` edge `-0.0047` maxDD `-0.8626`
- `market_context_high->index_1h` score `-0.8113` n `109` status `ready` deltaP `-0.5892` edge `0.0118` maxDD `-0.7054`
- `market_context_high->crypto_alt_1h` score `-1.2909` n `109` status `ready` deltaP `4.09` edge `-0.0004` maxDD `-12.7225`
- `market_context_high->crypto_major_4h` score `-1.7014` n `102` status `ready` deltaP `9.1493` edge `0.102` maxDD `-27.8228`
- `market_context_high->crypto_major_1h` score `-1.9645` n `109` status `ready` deltaP `2.8155` edge `-0.0131` maxDD `-17.9354`
- `market_context_high->fx_24h` score `-2.0904` n `96` status `ready` deltaP `-8.6806` edge `-0.0153` maxDD `-2.749`
- `market_context_high->metal_1h` score `-2.0995` n `109` status `ready` deltaP `0.8309` edge `-0.0644` maxDD `-13.4916`
- `market_context_high->commodity_24h` score `-2.9262` n `96` status `ready` deltaP `14.5833` edge `0.0385` maxDD `-27.5371`
- `market_context_high->metal_4h` score `-3.2923` n `102` status `ready` deltaP `8.3632` edge `-0.108` maxDD `-26.2547`
- `market_context_high->index_24h` score `-4.3064` n `96` status `ready` deltaP `-5.5556` edge `-0.1218` maxDD `-23.4611`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
