# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-18T21:07:44.099914+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11621`

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

- `market_context_high->crypto_major_24h` score `2.6899` n `91` status `ready` deltaP `9.6822` edge `0.2804` maxDD `-4.9964`
- `market_context_high->commodity_24h` score `1.6177` n `91` status `ready` deltaP `18.7691` edge `0.2656` maxDD `-4.666`
- `market_context_high->equity_1h` score `1.367` n `96` status `ready` deltaP `11.2588` edge `0.069` maxDD `-0.4112`
- `market_context_high->equity_4h` score `1.0489` n `96` status `ready` deltaP `6.4278` edge `0.1334` maxDD `-2.4411`
- `market_context_high->metal_4h` score `0.9367` n `96` status `ready` deltaP `15.6504` edge `0.0313` maxDD `-1.273`
- `market_context_high->index_1h` score `0.7234` n `96` status `ready` deltaP `13.5167` edge `0.0089` maxDD `-0.0982`
- `market_context_high->crypto_major_4h` score `0.7012` n `96` status `ready` deltaP `9.0193` edge `0.1004` maxDD `-3.1677`
- `market_context_high->unknown_1h` score `0.5082` n `96` status `ready` deltaP `9.6557` edge `0.0007` maxDD `-0.4843`
- `market_context_high->crypto_alt_4h` score `0.2104` n `96` status `ready` deltaP `9.6037` edge `0.0805` maxDD `-5.4926`
- `market_context_high->unknown_24h` score `0.1044` n `91` status `ready` deltaP `14.9973` edge `-0.0699` maxDD `-0.3771`
- `market_context_high->metal_1h` score `0.0529` n `96` status `ready` deltaP `4.9214` edge `0.0103` maxDD `-0.4291`
- `market_context_high->fx_4h` score `-0.1861` n `96` status `ready` deltaP `3.9888` edge `-0.0002` maxDD `-0.3539`
- `market_context_high->index_4h` score `-0.382` n `96` status `ready` deltaP `2.7693` edge `0.0152` maxDD `-0.5728`
- `market_context_high->crypto_alt_1h` score `-0.394` n `96` status `ready` deltaP `2.3765` edge `0.0138` maxDD `-2.413`
- `market_context_high->fx_1h` score `-0.4475` n `96` status `ready` deltaP `-3.4182` edge `0.0013` maxDD `-0.2043`
- `market_context_high->commodity_4h` score `-0.4643` n `96` status `ready` deltaP `2.5661` edge `0.0084` maxDD `-2.4692`
- `market_context_high->crypto_major_1h` score `-0.499` n `96` status `ready` deltaP `1.0354` edge `0.0136` maxDD `-2.7581`
- `market_context_high->commodity_1h` score `-0.9087` n `96` status `ready` deltaP `-8.0402` edge `-0.0063` maxDD `-1.1941`
- `market_context_high->metal_24h` score `-2.0097` n `91` status `ready` deltaP `-4.5444` edge `0.0497` maxDD `-8.831`
- `market_context_high->fx_24h` score `-4.2425` n `91` status `ready` deltaP `-26.5186` edge `-0.0268` maxDD `-1.3293`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
