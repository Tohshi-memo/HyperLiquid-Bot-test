# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-21T08:22:28.658902+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `9154`

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

- `market_context_high->unknown_4h` score `33.2677` n `58` status `ready` deltaP `1.23` edge `2.7791` maxDD `-0.5326`
- `news_risk_high->crypto_major_24h` score `23.1209` n `101` status `ready` deltaP `11.0956` edge `2.5386` maxDD `-46.1999`
- `news_risk_high->crypto_alt_24h` score `17.8649` n `101` status `ready` deltaP `11.4807` edge `1.9003` maxDD `-32.7147`
- `news_risk_high->crypto_alt_4h` score `4.2307` n `101` status `ready` deltaP `18.6141` edge `0.3494` maxDD `-7.675`
- `news_risk_high->crypto_major_4h` score `3.9141` n `101` status `ready` deltaP `21.0532` edge `0.3116` maxDD `-8.0625`
- `news_risk_high->crypto_alt_1h` score `2.6767` n `101` status `ready` deltaP `15.932` edge `0.1634` maxDD `-2.058`
- `news_risk_high->crypto_major_1h` score `2.07` n `101` status `ready` deltaP `17.8781` edge `0.1056` maxDD `-2.8494`
- `news_risk_high->commodity_24h` score `1.1072` n `101` status `ready` deltaP `22.8496` edge `0.1202` maxDD `-3.4467`
- `market_context_high->equity_1h` score `0.8798` n `58` status `ready` deltaP `6.6075` edge `0.0546` maxDD `-0.36`
- `market_context_high->index_1h` score `0.7208` n `58` status `ready` deltaP `10.7268` edge `0.0141` maxDD `-0.0435`
- `news_risk_high->metal_1h` score `0.5538` n `101` status `ready` deltaP `13.9992` edge `0.013` maxDD `-0.8144`
- `news_risk_high->metal_4h` score `0.3478` n `101` status `ready` deltaP `15.2695` edge `0.0326` maxDD `-2.0994`
- `market_context_high->fx_1h` score `0.3331` n `58` status `ready` deltaP `8.6259` edge `0.0059` maxDD `-0.1854`
- `market_context_high->index_4h` score `0.324` n `58` status `ready` deltaP `14.6289` edge `0.0077` maxDD `-1.0949`
- `market_context_high->metal_1h` score `0.2758` n `58` status `ready` deltaP `5.5493` edge `0.0168` maxDD `-0.1314`
- `news_risk_high->fx_4h` score `0.2345` n `101` status `ready` deltaP `8.9456` edge `0.0235` maxDD `-0.421`
- `news_risk_high->equity_1h` score `-0.1951` n `101` status `ready` deltaP `2.2203` edge `0.0095` maxDD `-0.9112`
- `market_context_high->crypto_major_1h` score `-0.2149` n `58` status `ready` deltaP `-1.9409` edge `0.0669` maxDD `-2.7494`
- `news_risk_high->fx_1h` score `-0.216` n `101` status `ready` deltaP `2.9925` edge `0.0064` maxDD `-0.2147`
- `news_risk_high->metal_24h` score `-0.4224` n `101` status `ready` deltaP `9.43` edge `-0.0326` maxDD `-2.4203`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
