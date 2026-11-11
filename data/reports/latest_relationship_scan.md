# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-11T16:52:30.183537+00:00`
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

- `market_context_high->unknown_4h` score `72.5302` n `88` status `ready` deltaP `8.4396` edge `6.0327` maxDD `-0.9161`
- `market_context_high->equity_24h` score `28.1159` n `88` status `ready` deltaP `24.6212` edge `2.418` maxDD `-16.7984`
- `news_risk_high->equity_4h` score `11.3736` n `53` status `ready` deltaP `34.4109` edge `0.8306` maxDD `-6.9762`
- `market_context_high->crypto_alt_24h` score `8.7461` n `88` status `ready` deltaP `38.4943` edge `1.3741` maxDD `-33.4213`
- `market_context_high->index_24h` score `5.1075` n `88` status `ready` deltaP `24.7317` edge `0.307` maxDD `-2.3671`
- `market_context_high->metal_24h` score `4.3825` n `88` status `ready` deltaP `31.2026` edge `0.2125` maxDD `-1.4245`
- `news_risk_high->metal_4h` score `3.7856` n `53` status `ready` deltaP `37.8596` edge `0.1007` maxDD `-1.0104`
- `news_risk_high->crypto_major_4h` score `3.6265` n `53` status `ready` deltaP `19.5237` edge `0.3208` maxDD `-9.2335`
- `news_risk_high->equity_1h` score `3.3991` n `53` status `ready` deltaP `17.8652` edge `0.2354` maxDD `-3.6997`
- `news_risk_high->commodity_4h` score `2.6068` n `53` status `ready` deltaP `23.9675` edge `0.0828` maxDD `-0.3611`
- `news_risk_high->index_4h` score `2.3023` n `53` status `ready` deltaP `21.5083` edge `0.0921` maxDD `-0.8235`
- `news_risk_high->metal_1h` score `1.8479` n `53` status `ready` deltaP `22.5963` edge `0.0288` maxDD `-0.3692`
- `news_risk_high->crypto_alt_4h` score `1.74` n `53` status `ready` deltaP `22.535` edge `0.2367` maxDD `-10.1088`
- `news_risk_high->index_1h` score `1.3113` n `53` status `ready` deltaP `17.176` edge `0.0249` maxDD `-0.4103`
- `news_risk_high->crypto_major_1h` score `0.7059` n `53` status `ready` deltaP `18.6419` edge `0.0714` maxDD `-7.0808`
- `news_risk_high->crypto_alt_1h` score `0.6969` n `53` status `ready` deltaP `17.594` edge `0.07` maxDD `-6.1688`
- `market_context_high->metal_1h` score `-0.1543` n `88` status `ready` deltaP `5.4437` edge `0.0185` maxDD `-1.4122`
- `news_risk_high->commodity_1h` score `-0.3805` n `53` status `ready` deltaP `-3.847` edge `0.0274` maxDD `-0.3438`
- `market_context_high->fx_24h` score `-0.5807` n `88` status `ready` deltaP `13.5417` edge `0.0213` maxDD `-3.4642`
- `market_context_high->commodity_1h` score `-0.5851` n `88` status `ready` deltaP `0.8914` edge `-0.0127` maxDD `-1.7935`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
