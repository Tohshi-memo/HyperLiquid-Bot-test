# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-11T17:37:30.223961+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `11762`

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

- `market_context_high->unknown_4h` score `72.8941` n `88` status `ready` deltaP `8.7445` edge `6.061` maxDD `-0.9161`
- `market_context_high->equity_24h` score `27.2199` n `88` status `ready` deltaP `24.1003` edge `2.3468` maxDD `-16.7984`
- `news_risk_high->equity_4h` score `11.2643` n `53` status `ready` deltaP `34.2585` edge `0.8225` maxDD `-6.9762`
- `market_context_high->crypto_alt_24h` score `8.3914` n `88` status `ready` deltaP `37.9735` edge `1.3321` maxDD `-33.4213`
- `market_context_high->index_24h` score `4.971` n `88` status `ready` deltaP `24.2108` edge `0.2991` maxDD `-2.3671`
- `market_context_high->metal_24h` score `4.3993` n `88` status `ready` deltaP `31.2026` edge `0.2139` maxDD `-1.4245`
- `news_risk_high->metal_4h` score `3.8498` n `53` status `ready` deltaP `38.3169` edge `0.103` maxDD `-1.0104`
- `news_risk_high->crypto_major_4h` score `3.4663` n `53` status `ready` deltaP `19.0664` edge `0.3105` maxDD `-9.2335`
- `news_risk_high->equity_1h` score `3.4135` n `53` status `ready` deltaP `17.8652` edge `0.2366` maxDD `-3.6997`
- `news_risk_high->commodity_4h` score `2.5692` n `53` status `ready` deltaP `23.6626` edge `0.0817` maxDD `-0.3611`
- `news_risk_high->index_4h` score `2.2817` n `53` status `ready` deltaP `21.3558` edge `0.0914` maxDD `-0.8235`
- `news_risk_high->metal_1h` score `1.8959` n `53` status `ready` deltaP `23.0454` edge `0.0298` maxDD `-0.3692`
- `news_risk_high->crypto_alt_4h` score `1.6382` n `53` status `ready` deltaP `22.0777` edge `0.2267` maxDD `-10.1088`
- `news_risk_high->index_1h` score `1.3125` n `53` status `ready` deltaP `17.176` edge `0.025` maxDD `-0.4103`
- `news_risk_high->crypto_major_1h` score `0.6482` n `53` status `ready` deltaP `18.1928` edge `0.067` maxDD `-7.0808`
- `news_risk_high->crypto_alt_1h` score `0.6361` n `53` status `ready` deltaP `17.1449` edge `0.0652` maxDD `-6.1688`
- `market_context_high->metal_1h` score `-0.1064` n `88` status `ready` deltaP `5.8928` edge `0.0195` maxDD `-1.4122`
- `news_risk_high->commodity_1h` score `-0.3818` n `53` status `ready` deltaP `-3.6973` edge `0.0263` maxDD `-0.3438`
- `market_context_high->fx_24h` score `-0.5246` n `88` status `ready` deltaP `14.0625` edge `0.0225` maxDD `-3.4642`
- `market_context_high->commodity_1h` score `-0.5859` n `88` status `ready` deltaP `1.0411` edge `-0.0138` maxDD `-1.7935`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
