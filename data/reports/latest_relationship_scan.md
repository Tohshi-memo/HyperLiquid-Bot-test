# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-23T22:22:16.537723+00:00`
- Price records: `672`
- Market context records: `1673`
- Flow alert records: `6725`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8854`

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

- `market_context_high->metal_24h` score `9.2505` n `160` status `ready` deltaP `28.0017` edge `0.8268` maxDD `-12.7414`
- `market_context_high->crypto_alt_4h` score `5.1358` n `195` status `ready` deltaP `22.8901` edge `0.5418` maxDD `-16.3135`
- `market_context_high->index_24h` score `3.849` n `160` status `ready` deltaP `19.5523` edge `0.3282` maxDD `-5.3574`
- `market_context_high->crypto_major_4h` score `3.2118` n `195` status `ready` deltaP `18.9955` edge `0.4119` maxDD `-13.3376`
- `market_context_high->equity_4h` score `2.4308` n `195` status `ready` deltaP `13.5632` edge `0.2216` maxDD `-5.0894`
- `market_context_high->equity_24h` score `1.8561` n `160` status `ready` deltaP `18.7824` edge `0.5193` maxDD `-33.1875`
- `market_context_high->crypto_alt_1h` score `0.8014` n `204` status `ready` deltaP `7.0418` edge `0.1222` maxDD `-4.1892`
- `market_context_high->crypto_alt_24h` score `0.5575` n `160` status `ready` deltaP `25.7353` edge `1.0558` maxDD `-88.8062`
- `market_context_high->crypto_major_24h` score `0.2865` n `160` status `ready` deltaP `24.7816` edge `0.7301` maxDD `-62.3533`
- `market_context_high->index_4h` score `-0.0199` n `195` status `ready` deltaP `4.9563` edge `0.0742` maxDD `-3.7119`
- `market_context_high->equity_1h` score `-0.1378` n `204` status `ready` deltaP `3.3404` edge `0.0471` maxDD `-2.8014`
- `market_context_high->crypto_major_1h` score `-0.2685` n `204` status `ready` deltaP `4.2767` edge `0.0765` maxDD `-5.5244`
- `market_context_high->fx_24h` score `-0.4744` n `160` status `ready` deltaP `6.6263` edge `0.0212` maxDD `-1.3925`
- `market_context_high->index_1h` score `-0.6264` n `204` status `ready` deltaP `-0.3493` edge `0.0133` maxDD `-1.7205`
- `market_context_high->metal_4h` score `-0.8566` n `195` status `ready` deltaP `11.5659` edge `0.1207` maxDD `-12.5349`
- `market_context_high->fx_1h` score `-0.8618` n `204` status `ready` deltaP `-0.8835` edge `-0.0027` maxDD `-0.3914`
- `market_context_high->metal_1h` score `-1.0333` n `204` status `ready` deltaP `5.3657` edge `0.0117` maxDD `-6.3532`
- `market_context_high->unknown_24h` score `-1.1312` n `160` status `ready` deltaP `11.7063` edge `0.3639` maxDD `-35.8966`
- `market_context_high->fx_4h` score `-1.2564` n `195` status `ready` deltaP `-8.3224` edge `-0.0127` maxDD `-1.4313`
- `market_context_high->commodity_1h` score `-2.1887` n `204` status `ready` deltaP `-0.5577` edge `-0.0322` maxDD `-14.9083`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
