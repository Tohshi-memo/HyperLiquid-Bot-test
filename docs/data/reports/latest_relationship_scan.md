# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-11T02:37:31.739632+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `11740`

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

- `market_context_high->unknown_4h` score `80.7862` n `88` status `ready` deltaP `7.525` edge `6.7268` maxDD `-0.9161`
- `market_context_high->equity_24h` score `34.666` n `88` status `ready` deltaP `32.6073` edge `2.9106` maxDD `-16.7984`
- `news_risk_high->equity_4h` score `9.408` n `33` status `ready` deltaP `31.6658` edge `0.6851` maxDD `-6.9762`
- `market_context_high->crypto_alt_24h` score `7.4511` n `88` status `ready` deltaP `32.0707` edge `1.2509` maxDD `-33.4213`
- `market_context_high->index_24h` score `6.1305` n `88` status `ready` deltaP `31.8497` edge `0.3448` maxDD `-2.3671`
- `news_risk_high->equity_1h` score `3.5574` n `42` status `ready` deltaP `18.2991` edge `0.2457` maxDD `-3.6997`
- `news_risk_high->commodity_4h` score `3.0875` n `33` status `ready` deltaP `21.0505` edge `0.1423` maxDD `-0.3611`
- `market_context_high->metal_24h` score `2.9785` n `88` status `ready` deltaP `27.5568` edge `0.1198` maxDD `-1.4245`
- `news_risk_high->crypto_alt_4h` score `1.4036` n `33` status `ready` deltaP `25.0508` edge `0.1768` maxDD `-10.1088`
- `news_risk_high->index_1h` score `1.382` n `42` status `ready` deltaP `18.2991` edge `0.0233` maxDD `-0.4103`
- `news_risk_high->metal_1h` score `1.3806` n `42` status `ready` deltaP `18.1494` edge `0.0195` maxDD `-0.3692`
- `news_risk_high->metal_4h` score `1.3375` n `33` status `ready` deltaP `28.6355` edge `0.0182` maxDD `-1.0104`
- `news_risk_high->index_4h` score `1.3051` n `33` status `ready` deltaP `22.2515` edge `0.0626` maxDD `-0.8235`
- `news_risk_high->crypto_major_4h` score `1.2076` n `33` status `ready` deltaP `15.6551` edge `0.1992` maxDD `-9.2335`
- `news_risk_high->crypto_alt_1h` score `0.7479` n `42` status `ready` deltaP `20.1098` edge `0.0556` maxDD `-6.1688`
- `news_risk_high->crypto_major_1h` score `0.464` n `42` status `ready` deltaP `20.1098` edge `0.0306` maxDD `-7.0808`
- `news_risk_high->commodity_1h` score `-0.2527` n `42` status `ready` deltaP `-5.375` edge `0.0369` maxDD `-0.3438`
- `market_context_high->metal_1h` score `-0.3808` n `88` status `ready` deltaP `3.6473` edge `0.0116` maxDD `-1.4122`
- `market_context_high->commodity_1h` score `-0.4027` n `88` status `ready` deltaP `2.6878` edge `-0.0013` maxDD `-1.7935`
- `market_context_high->commodity_4h` score `-0.6806` n `88` status `ready` deltaP `1.7323` edge `0.0118` maxDD `-4.182`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
