# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-11T16:37:30.895067+00:00`
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

- `market_context_high->unknown_4h` score `72.4832` n `88` status `ready` deltaP `8.2871` edge `6.0298` maxDD `-0.9161`
- `market_context_high->equity_24h` score `28.4358` n `88` status `ready` deltaP `24.7948` edge `2.4435` maxDD `-16.7984`
- `news_risk_high->equity_4h` score `11.3964` n `53` status `ready` deltaP `34.4109` edge `0.8325` maxDD `-6.9762`
- `market_context_high->crypto_alt_24h` score `8.8636` n `88` status `ready` deltaP `38.6679` edge `1.388` maxDD `-33.4213`
- `market_context_high->index_24h` score `5.1526` n `88` status `ready` deltaP `24.9053` edge `0.3096` maxDD `-2.3671`
- `market_context_high->metal_24h` score `4.3825` n `88` status `ready` deltaP `31.2026` edge `0.2125` maxDD `-1.4245`
- `news_risk_high->metal_4h` score `3.7626` n `53` status `ready` deltaP `37.7071` edge `0.0998` maxDD `-1.0104`
- `news_risk_high->crypto_major_4h` score `3.6735` n `53` status `ready` deltaP `19.6762` edge `0.3237` maxDD `-9.2335`
- `news_risk_high->equity_1h` score `3.3931` n `53` status `ready` deltaP `17.8652` edge `0.2349` maxDD `-3.6997`
- `news_risk_high->commodity_4h` score `2.6346` n `53` status `ready` deltaP `24.1199` edge `0.0841` maxDD `-0.3611`
- `news_risk_high->index_4h` score `2.3035` n `53` status `ready` deltaP `21.5083` edge `0.0922` maxDD `-0.8235`
- `news_risk_high->metal_1h` score `1.8323` n `53` status `ready` deltaP `22.4466` edge `0.0285` maxDD `-0.3692`
- `news_risk_high->crypto_alt_4h` score `1.7721` n `53` status `ready` deltaP `22.6875` edge `0.2398` maxDD `-10.1088`
- `news_risk_high->index_1h` score `1.3101` n `53` status `ready` deltaP `17.176` edge `0.0248` maxDD `-0.4103`
- `news_risk_high->crypto_major_1h` score `0.7184` n `53` status `ready` deltaP `18.7916` edge `0.072` maxDD `-7.0808`
- `news_risk_high->crypto_alt_1h` score `0.6977` n `53` status `ready` deltaP `17.594` edge `0.0701` maxDD `-6.1688`
- `market_context_high->metal_1h` score `-0.1699` n `88` status `ready` deltaP `5.294` edge `0.0182` maxDD `-1.4122`
- `news_risk_high->commodity_1h` score `-0.3697` n `53` status `ready` deltaP `-3.847` edge `0.0283` maxDD `-0.3438`
- `market_context_high->commodity_1h` score `-0.5781` n `88` status `ready` deltaP `0.8914` edge `-0.0118` maxDD `-1.7935`
- `market_context_high->fx_24h` score `-0.5994` n `88` status `ready` deltaP `13.3681` edge `0.0209` maxDD `-3.4642`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
