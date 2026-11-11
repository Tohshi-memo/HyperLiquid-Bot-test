# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-11T19:23:24.159102+00:00`
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

- `market_context_high->unknown_4h` score `73.5155` n `88` status `ready` deltaP `8.592` edge `6.1138` maxDD `-0.9161`
- `market_context_high->equity_24h` score `24.971` n `88` status `ready` deltaP `22.8851` edge `2.1675` maxDD `-16.7984`
- `news_risk_high->equity_4h` score `10.9741` n `53` status `ready` deltaP `33.4963` edge `0.8034` maxDD `-6.9762`
- `market_context_high->crypto_alt_24h` score `7.7034` n `88` status `ready` deltaP `36.7582` edge `1.252` maxDD `-33.4213`
- `market_context_high->index_24h` score `4.6278` n `88` status `ready` deltaP `22.9955` edge `0.2786` maxDD `-2.3671`
- `market_context_high->metal_24h` score `4.4396` n `88` status `ready` deltaP `31.3762` edge `0.2161` maxDD `-1.4245`
- `news_risk_high->metal_4h` score `3.926` n `53` status `ready` deltaP `38.7742` edge `0.1063` maxDD `-1.0104`
- `news_risk_high->equity_1h` score `3.3919` n `53` status `ready` deltaP `17.7155` edge `0.2358` maxDD `-3.6997`
- `news_risk_high->crypto_major_4h` score `3.2335` n `53` status `ready` deltaP `18.1518` edge `0.2972` maxDD `-9.2335`
- `news_risk_high->commodity_4h` score `2.6116` n `53` status `ready` deltaP `23.9675` edge `0.0832` maxDD `-0.3611`
- `news_risk_high->index_4h` score `2.1956` n `53` status `ready` deltaP `20.5937` edge `0.0893` maxDD `-0.8235`
- `news_risk_high->metal_1h` score `1.9282` n `53` status `ready` deltaP `23.3448` edge `0.0305` maxDD `-0.3692`
- `news_risk_high->crypto_alt_4h` score `1.5997` n `53` status `ready` deltaP `21.7729` edge `0.2238` maxDD `-10.1088`
- `news_risk_high->index_1h` score `1.2742` n `53` status `ready` deltaP `16.7269` edge `0.0248` maxDD `-0.4103`
- `news_risk_high->crypto_major_1h` score `0.6631` n `53` status `ready` deltaP `18.3425` edge `0.0679` maxDD `-7.0808`
- `news_risk_high->crypto_alt_1h` score `0.6479` n `53` status `ready` deltaP `16.9952` edge `0.0677` maxDD `-6.1688`
- `market_context_high->metal_1h` score `-0.0741` n `88` status `ready` deltaP `6.1922` edge `0.0202` maxDD `-1.4122`
- `news_risk_high->commodity_1h` score `-0.3458` n `53` status `ready` deltaP `-3.3979` edge `0.0273` maxDD `-0.3438`
- `market_context_high->fx_24h` score `-0.3902` n `88` status `ready` deltaP `15.2778` edge `0.0256` maxDD `-3.4642`
- `market_context_high->commodity_1h` score `-0.5625` n `88` status `ready` deltaP `1.3405` edge `-0.0128` maxDD `-1.7935`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
