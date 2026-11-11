# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-11T05:37:25.326695+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `11756`

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

- `market_context_high->unknown_4h` score `78.7054` n `88` status `ready` deltaP `7.525` edge `6.5534` maxDD `-0.9161`
- `market_context_high->equity_24h` score `34.4582` n `88` status `ready` deltaP `32.2601` edge `2.8956` maxDD `-16.7984`
- `news_risk_high->equity_4h` score `12.3369` n `42` status `ready` deltaP `35.5619` edge `0.9032` maxDD `-6.9762`
- `market_context_high->crypto_alt_24h` score `8.1648` n `88` status `ready` deltaP `33.286` edge `1.3343` maxDD `-33.4213`
- `market_context_high->index_24h` score `6.1809` n `88` status `ready` deltaP `31.8497` edge `0.349` maxDD `-2.3671`
- `news_risk_high->equity_1h` score `3.9254` n `47` status `ready` deltaP `20.544` edge `0.2614` maxDD `-3.6997`
- `market_context_high->metal_24h` score `3.6635` n `88` status `ready` deltaP `29.6401` edge `0.163` maxDD `-1.4245`
- `news_risk_high->crypto_major_4h` score `3.2307` n `42` status `ready` deltaP `20.4414` edge `0.2817` maxDD `-9.2335`
- `news_risk_high->commodity_4h` score `3.1845` n `42` status `ready` deltaP `24.5137` edge `0.1273` maxDD `-0.3611`
- `news_risk_high->metal_4h` score `3.1329` n `42` status `ready` deltaP `33.1809` edge `0.0775` maxDD `-1.0104`
- `news_risk_high->index_4h` score `2.8098` n `42` status `ready` deltaP `27.4463` edge `0.0948` maxDD `-0.8235`
- `news_risk_high->crypto_alt_4h` score `2.5093` n `42` status `ready` deltaP `29.9652` edge `0.2858` maxDD `-10.1088`
- `news_risk_high->metal_1h` score `1.6105` n `47` status `ready` deltaP `20.8434` edge `0.0207` maxDD `-0.3692`
- `news_risk_high->index_1h` score `1.4465` n `47` status `ready` deltaP `18.7158` edge `0.0259` maxDD `-0.4103`
- `news_risk_high->crypto_alt_1h` score `1.1905` n `47` status `ready` deltaP `23.3565` edge `0.0907` maxDD `-6.1688`
- `news_risk_high->crypto_major_1h` score `0.8435` n `47` status `ready` deltaP `21.6779` edge `0.0688` maxDD `-7.0808`
- `news_risk_high->commodity_1h` score `-0.185` n `47` status `ready` deltaP `-3.9081` edge `0.0358` maxDD `-0.3438`
- `market_context_high->commodity_1h` score `-0.3926` n `88` status `ready` deltaP `2.8375` edge `-0.001` maxDD `-1.7935`
- `market_context_high->metal_1h` score `-0.4468` n `88` status `ready` deltaP `3.0485` edge `0.0101` maxDD `-1.4122`
- `market_context_high->commodity_4h` score `-0.6525` n `88` status `ready` deltaP `1.7323` edge `0.0154` maxDD `-4.182`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
