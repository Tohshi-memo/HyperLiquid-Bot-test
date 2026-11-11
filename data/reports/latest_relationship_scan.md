# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-11T19:37:29.858628+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `11774`

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

- `market_context_high->unknown_4h` score `76.4639` n `88` status `ready` deltaP `8.592` edge `6.3595` maxDD `-0.9161`
- `market_context_high->equity_24h` score `24.6644` n `88` status `ready` deltaP `22.7114` edge `2.1431` maxDD `-16.7984`
- `news_risk_high->equity_4h` score `10.9753` n `53` status `ready` deltaP `33.4963` edge `0.8035` maxDD `-6.9762`
- `market_context_high->crypto_alt_24h` score `7.6164` n `88` status `ready` deltaP `36.5846` edge `1.242` maxDD `-33.4213`
- `market_context_high->index_24h` score `4.5791` n `88` status `ready` deltaP `22.8219` edge `0.2757` maxDD `-2.3671`
- `market_context_high->metal_24h` score `4.4432` n `88` status `ready` deltaP `31.3762` edge `0.2164` maxDD `-1.4245`
- `news_risk_high->metal_4h` score `3.9418` n `53` status `ready` deltaP `38.9266` edge `0.1066` maxDD `-1.0104`
- `news_risk_high->equity_1h` score `3.3991` n `53` status `ready` deltaP `17.7155` edge `0.2364` maxDD `-3.6997`
- `news_risk_high->crypto_major_4h` score `3.2601` n `53` status `ready` deltaP `18.3042` edge `0.2984` maxDD `-9.2335`
- `news_risk_high->commodity_4h` score `2.6248` n `53` status `ready` deltaP `23.9675` edge `0.0843` maxDD `-0.3611`
- `news_risk_high->index_4h` score `2.1944` n `53` status `ready` deltaP `20.5937` edge `0.0892` maxDD `-0.8235`
- `news_risk_high->metal_1h` score `1.9282` n `53` status `ready` deltaP `23.3448` edge `0.0305` maxDD `-0.3692`
- `news_risk_high->crypto_alt_4h` score `1.6303` n `53` status `ready` deltaP `21.9253` edge `0.2267` maxDD `-10.1088`
- `news_risk_high->index_1h` score `1.2742` n `53` status `ready` deltaP `16.7269` edge `0.0248` maxDD `-0.4103`
- `news_risk_high->crypto_major_1h` score `0.6615` n `53` status `ready` deltaP `18.3425` edge `0.0677` maxDD `-7.0808`
- `news_risk_high->crypto_alt_1h` score `0.6455` n `53` status `ready` deltaP `16.9952` edge `0.0674` maxDD `-6.1688`
- `market_context_high->metal_1h` score `-0.0741` n `88` status `ready` deltaP `6.1922` edge `0.0202` maxDD `-1.4122`
- `news_risk_high->commodity_1h` score `-0.329` n `53` status `ready` deltaP `-3.2482` edge `0.0277` maxDD `-0.3438`
- `market_context_high->fx_24h` score `-0.3703` n `88` status `ready` deltaP `15.4514` edge `0.0261` maxDD `-3.4642`
- `market_context_high->commodity_1h` score `-0.5516` n `88` status `ready` deltaP `1.4902` edge `-0.0124` maxDD `-1.7935`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
