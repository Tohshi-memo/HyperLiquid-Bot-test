# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-11T05:22:24.681326+00:00`
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

- `market_context_high->unknown_4h` score `78.8002` n `88` status `ready` deltaP `7.525` edge `6.5613` maxDD `-0.9161`
- `market_context_high->equity_24h` score `34.4726` n `88` status `ready` deltaP `32.2601` edge `2.8968` maxDD `-16.7984`
- `news_risk_high->equity_4h` score `12.297` n `41` status `ready` deltaP `35.2135` edge `0.9022` maxDD `-6.9762`
- `market_context_high->crypto_alt_24h` score `8.1012` n `88` status `ready` deltaP `33.1124` edge `1.3273` maxDD `-33.4213`
- `market_context_high->index_24h` score `6.1773` n `88` status `ready` deltaP `31.8497` edge `0.3487` maxDD `-2.3671`
- `news_risk_high->equity_1h` score `3.8966` n `47` status `ready` deltaP `20.544` edge `0.259` maxDD `-3.6997`
- `market_context_high->metal_24h` score `3.6076` n `88` status `ready` deltaP `29.4665` edge `0.1595` maxDD `-1.4245`
- `news_risk_high->crypto_major_4h` score `3.3945` n `41` status `ready` deltaP `21.7987` edge `0.2863` maxDD `-9.2335`
- `news_risk_high->commodity_4h` score `3.1537` n `41` status `ready` deltaP `23.933` edge `0.1286` maxDD `-0.3611`
- `news_risk_high->metal_4h` score `3.056` n `41` status `ready` deltaP `32.7744` edge `0.0738` maxDD `-1.0104`
- `news_risk_high->index_4h` score `2.7606` n `41` status `ready` deltaP `26.9817` edge `0.0938` maxDD `-0.8235`
- `news_risk_high->crypto_alt_4h` score `2.6544` n `41` status `ready` deltaP `31.5548` edge `0.2938` maxDD `-10.1088`
- `news_risk_high->metal_1h` score `1.6105` n `47` status `ready` deltaP `20.8434` edge `0.0207` maxDD `-0.3692`
- `news_risk_high->index_1h` score `1.4417` n `47` status `ready` deltaP `18.7158` edge `0.0255` maxDD `-0.4103`
- `news_risk_high->crypto_alt_1h` score `1.1679` n `47` status `ready` deltaP `23.2068` edge `0.0888` maxDD `-6.1688`
- `news_risk_high->crypto_major_1h` score `0.8256` n `47` status `ready` deltaP `21.5282` edge `0.0675` maxDD `-7.0808`
- `news_risk_high->commodity_1h` score `-0.1975` n `47` status `ready` deltaP `-4.0578` edge `0.0352` maxDD `-0.3438`
- `market_context_high->commodity_1h` score `-0.4051` n `88` status `ready` deltaP `2.6878` edge `-0.0016` maxDD `-1.7935`
- `market_context_high->metal_1h` score `-0.4468` n `88` status `ready` deltaP `3.0485` edge `0.0101` maxDD `-1.4122`
- `market_context_high->commodity_4h` score `-0.6549` n `88` status `ready` deltaP `1.7323` edge `0.0151` maxDD `-4.182`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
