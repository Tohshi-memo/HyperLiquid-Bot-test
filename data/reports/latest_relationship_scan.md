# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-11T16:22:29.781405+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `11730`

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

- `market_context_high->unknown_4h` score `72.5386` n `88` status `ready` deltaP `8.4396` edge `6.0334` maxDD `-0.9161`
- `market_context_high->equity_24h` score `28.7581` n `88` status `ready` deltaP `24.9684` edge `2.4692` maxDD `-16.7984`
- `news_risk_high->equity_4h` score `11.4362` n `53` status `ready` deltaP `34.5633` edge `0.8348` maxDD `-6.9762`
- `market_context_high->crypto_alt_24h` score `8.9958` n `88` status `ready` deltaP `38.8415` edge `1.4038` maxDD `-33.4213`
- `market_context_high->index_24h` score `5.1976` n `88` status `ready` deltaP `25.0789` edge `0.3122` maxDD `-2.3671`
- `market_context_high->metal_24h` score `4.3825` n `88` status `ready` deltaP `31.2026` edge `0.2125` maxDD `-1.4245`
- `news_risk_high->metal_4h` score `3.742` n `53` status `ready` deltaP `37.5547` edge `0.0991` maxDD `-1.0104`
- `news_risk_high->crypto_major_4h` score `3.7265` n `53` status `ready` deltaP `19.8286` edge `0.3271` maxDD `-9.2335`
- `news_risk_high->equity_1h` score `3.3991` n `53` status `ready` deltaP `17.8652` edge `0.2354` maxDD `-3.6997`
- `news_risk_high->commodity_4h` score `2.6708` n `53` status `ready` deltaP `24.2723` edge `0.0861` maxDD `-0.3611`
- `news_risk_high->index_4h` score `2.3059` n `53` status `ready` deltaP `21.5083` edge `0.0924` maxDD `-0.8235`
- `news_risk_high->metal_1h` score `1.8168` n `53` status `ready` deltaP `22.2969` edge `0.0282` maxDD `-0.3692`
- `news_risk_high->crypto_alt_4h` score `1.8112` n `53` status `ready` deltaP `22.8399` edge `0.2438` maxDD `-10.1088`
- `news_risk_high->index_1h` score `1.3101` n `53` status `ready` deltaP `17.176` edge `0.0248` maxDD `-0.4103`
- `news_risk_high->crypto_major_1h` score `0.7083` n `53` status `ready` deltaP `18.6419` edge `0.0717` maxDD `-7.0808`
- `news_risk_high->crypto_alt_1h` score `0.6962` n `53` status `ready` deltaP `17.594` edge `0.0699` maxDD `-6.1688`
- `market_context_high->metal_1h` score `-0.1855` n `88` status `ready` deltaP `5.1443` edge `0.0179` maxDD `-1.4122`
- `news_risk_high->commodity_1h` score `-0.3529` n `53` status `ready` deltaP `-3.847` edge `0.0297` maxDD `-0.3438`
- `market_context_high->commodity_1h` score `-0.5671` n `88` status `ready` deltaP `0.8914` edge `-0.0104` maxDD `-1.7935`
- `market_context_high->fx_24h` score `-0.6169` n `88` status `ready` deltaP `13.1944` edge `0.0206` maxDD `-3.4642`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
