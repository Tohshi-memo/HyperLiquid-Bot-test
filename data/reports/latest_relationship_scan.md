# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-11T16:07:28.293192+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `11708`

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

- `market_context_high->unknown_4h` score `72.518` n `88` status `ready` deltaP `8.2871` edge `6.0327` maxDD `-0.9161`
- `market_context_high->equity_24h` score `29.0432` n `88` status `ready` deltaP `25.142` edge `2.4918` maxDD `-16.7984`
- `news_risk_high->equity_4h` score `11.4928` n `53` status `ready` deltaP `34.7158` edge `0.8385` maxDD `-6.9762`
- `market_context_high->crypto_alt_24h` score `9.0977` n `88` status `ready` deltaP `39.0151` edge `1.4157` maxDD `-33.4213`
- `market_context_high->index_24h` score `5.2403` n `88` status `ready` deltaP `25.2525` edge `0.3146` maxDD `-2.3671`
- `market_context_high->metal_24h` score `4.3777` n `88` status `ready` deltaP `31.2026` edge `0.2121` maxDD `-1.4245`
- `news_risk_high->crypto_major_4h` score `3.7783` n `53` status `ready` deltaP `19.9811` edge `0.3304` maxDD `-9.2335`
- `news_risk_high->metal_4h` score `3.7226` n `53` status `ready` deltaP `37.4023` edge `0.0985` maxDD `-1.0104`
- `news_risk_high->equity_1h` score `3.459` n `53` status `ready` deltaP `18.0149` edge `0.2394` maxDD `-3.6997`
- `news_risk_high->commodity_4h` score `2.7106` n `53` status `ready` deltaP `24.4248` edge `0.0884` maxDD `-0.3611`
- `news_risk_high->index_4h` score `2.3217` n `53` status `ready` deltaP `21.6607` edge `0.0927` maxDD `-0.8235`
- `news_risk_high->crypto_alt_4h` score `1.8488` n `53` status `ready` deltaP `22.9924` edge `0.2476` maxDD `-10.1088`
- `news_risk_high->metal_1h` score `1.8024` n `53` status `ready` deltaP `22.1472` edge `0.028` maxDD `-0.3692`
- `news_risk_high->index_1h` score `1.3257` n `53` status `ready` deltaP `17.3257` edge `0.0251` maxDD `-0.4103`
- `news_risk_high->crypto_major_1h` score `0.7324` n `53` status `ready` deltaP `18.7916` edge `0.0738` maxDD `-7.0808`
- `news_risk_high->crypto_alt_1h` score `0.7195` n `53` status `ready` deltaP `17.7437` edge `0.0719` maxDD `-6.1688`
- `market_context_high->metal_1h` score `-0.1999` n `88` status `ready` deltaP `4.9946` edge `0.0177` maxDD `-1.4122`
- `news_risk_high->commodity_1h` score `-0.3373` n `53` status `ready` deltaP `-3.847` edge `0.031` maxDD `-0.3438`
- `market_context_high->commodity_1h` score `-0.557` n `88` status `ready` deltaP `0.8914` edge `-0.0091` maxDD `-1.7935`
- `market_context_high->crypto_major_24h` score `-0.6315` n `88` status `ready` deltaP `17.2191` edge `0.9951` maxDD `-80.6681`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
