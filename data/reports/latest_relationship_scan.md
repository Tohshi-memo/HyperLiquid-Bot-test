# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-19T22:07:32.505317+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8732`

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

- `news_risk_high->crypto_major_24h` score `51.0968` n `72` status `ready` deltaP `27.0833` edge `4.1667` maxDD `-5.8019`
- `news_risk_high->crypto_alt_24h` score `44.5556` n `72` status `ready` deltaP `33.507` edge `3.6275` maxDD `-9.3661`
- `market_context_high->unknown_4h` score `22.1591` n `110` status `ready` deltaP `-4.648` edge `1.9009` maxDD `-0.5326`
- `news_risk_high->equity_24h` score `8.6723` n `72` status `ready` deltaP `36.9792` edge `0.4804` maxDD `-0.0053`
- `market_context_high->commodity_24h` score `7.9321` n `110` status `ready` deltaP `39.6938` edge `0.4489` maxDD `-0.8682`
- `news_risk_high->crypto_alt_4h` score `5.738` n `98` status `ready` deltaP `21.4659` edge `0.456` maxDD `-7.675`
- `news_risk_high->crypto_major_4h` score `4.4593` n `98` status `ready` deltaP `22.2281` edge `0.3492` maxDD `-8.0625`
- `news_risk_high->crypto_alt_1h` score `3.3108` n `98` status `ready` deltaP `18.7737` edge `0.1973` maxDD `-2.058`
- `market_context_high->commodity_4h` score `2.857` n `110` status `ready` deltaP `28.7916` edge `0.0868` maxDD `-0.2528`
- `news_risk_high->crypto_major_1h` score `2.4607` n `98` status `ready` deltaP `20.121` edge `0.1232` maxDD `-2.8494`
- `news_risk_high->metal_24h` score `1.7002` n `72` status `ready` deltaP `22.3958` edge `0.0768` maxDD `-2.4203`
- `market_context_high->commodity_1h` score `1.5731` n `112` status `ready` deltaP `19.1831` edge `0.0284` maxDD `-0.3491`
- `market_context_high->fx_4h` score `1.0269` n `110` status `ready` deltaP `19.7977` edge `0.0004` maxDD `-0.0779`
- `news_risk_high->metal_4h` score `0.7455` n `98` status `ready` deltaP `18.2149` edge `0.0461` maxDD `-2.0994`
- `news_risk_high->metal_1h` score `0.6824` n `98` status `ready` deltaP `15.1564` edge `0.016` maxDD `-0.8144`
- `news_risk_high->fx_24h` score `0.5194` n `72` status `ready` deltaP `3.2987` edge `0.0395` maxDD `-0.1231`
- `news_risk_high->equity_1h` score `0.4438` n `98` status `ready` deltaP `6.9657` edge `0.0311` maxDD `-0.9112`
- `market_context_high->fx_24h` score `0.3975` n `110` status `ready` deltaP `9.334` edge `-0.0249` maxDD `-0.0027`
- `market_context_high->fx_1h` score `0.2443` n `112` status `ready` deltaP `6.667` edge `0.0017` maxDD `-0.063`
- `news_risk_high->equity_4h` score `-0.1203` n `98` status `ready` deltaP `8.1415` edge `0.0801` maxDD `-5.2186`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
