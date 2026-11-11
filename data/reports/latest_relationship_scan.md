# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-11T17:22:39.539482+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `11746`

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

- `market_context_high->unknown_4h` score `72.7427` n `88` status `ready` deltaP `8.592` edge `6.0494` maxDD `-0.9161`
- `market_context_high->equity_24h` score `27.5554` n `88` status `ready` deltaP `24.2739` edge `2.3736` maxDD `-16.7984`
- `news_risk_high->equity_4h` score `11.322` n `53` status `ready` deltaP `34.4109` edge `0.8263` maxDD `-6.9762`
- `market_context_high->crypto_alt_24h` score `8.5182` n `88` status `ready` deltaP `38.1471` edge `1.3472` maxDD `-33.4213`
- `market_context_high->index_24h` score `5.0209` n `88` status `ready` deltaP `24.3844` edge `0.3021` maxDD `-2.3671`
- `market_context_high->metal_24h` score `4.3957` n `88` status `ready` deltaP `31.2026` edge `0.2136` maxDD `-1.4245`
- `news_risk_high->metal_4h` score `3.8304` n `53` status `ready` deltaP `38.1645` edge `0.1024` maxDD `-1.0104`
- `news_risk_high->crypto_major_4h` score `3.5241` n `53` status `ready` deltaP `19.2189` edge `0.3143` maxDD `-9.2335`
- `news_risk_high->equity_1h` score `3.4171` n `53` status `ready` deltaP `17.8652` edge `0.2369` maxDD `-3.6997`
- `news_risk_high->commodity_4h` score `2.5656` n `53` status `ready` deltaP `23.6626` edge `0.0814` maxDD `-0.3611`
- `news_risk_high->index_4h` score `2.2987` n `53` status `ready` deltaP `21.5083` edge `0.0918` maxDD `-0.8235`
- `news_risk_high->metal_1h` score `1.8815` n `53` status `ready` deltaP `22.8957` edge `0.0296` maxDD `-0.3692`
- `news_risk_high->crypto_alt_4h` score `1.6719` n `53` status `ready` deltaP `22.2302` edge `0.23` maxDD `-10.1088`
- `news_risk_high->index_1h` score `1.3137` n `53` status `ready` deltaP `17.176` edge `0.0251` maxDD `-0.4103`
- `news_risk_high->crypto_major_1h` score `0.6654` n `53` status `ready` deltaP `18.3425` edge `0.0682` maxDD `-7.0808`
- `news_risk_high->crypto_alt_1h` score `0.6548` n `53` status `ready` deltaP `17.2946` edge `0.0666` maxDD `-6.1688`
- `market_context_high->metal_1h` score `-0.1208` n `88` status `ready` deltaP `5.7431` edge `0.0193` maxDD `-1.4122`
- `news_risk_high->commodity_1h` score `-0.4009` n `53` status `ready` deltaP `-3.847` edge `0.0257` maxDD `-0.3438`
- `market_context_high->fx_24h` score `-0.5445` n `88` status `ready` deltaP `13.8889` edge `0.022` maxDD `-3.4642`
- `market_context_high->commodity_1h` score `-0.5983` n `88` status `ready` deltaP `0.8914` edge `-0.0144` maxDD `-1.7935`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
