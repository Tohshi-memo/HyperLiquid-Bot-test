# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-21T10:37:27.495767+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `9175`

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

- `market_context_high->unknown_4h` score `32.8069` n `58` status `ready` deltaP `1.23` edge `2.7407` maxDD `-0.5326`
- `news_risk_high->crypto_major_24h` score `21.8307` n `101` status `ready` deltaP `9.5331` edge `2.4415` maxDD `-46.1999`
- `news_risk_high->crypto_alt_24h` score `16.3323` n `101` status `ready` deltaP `9.9182` edge `1.783` maxDD `-32.7147`
- `news_risk_high->crypto_alt_4h` score `3.7561` n `101` status `ready` deltaP `17.2422` edge `0.319` maxDD `-7.675`
- `news_risk_high->crypto_major_4h` score `3.4281` n `101` status `ready` deltaP `20.1385` edge `0.2772` maxDD `-8.0625`
- `news_risk_high->crypto_alt_1h` score `2.5148` n `101` status `ready` deltaP `15.3332` edge `0.1539` maxDD `-2.058`
- `news_risk_high->crypto_major_1h` score `1.8889` n `101` status `ready` deltaP `17.2793` edge `0.0945` maxDD `-2.8494`
- `news_risk_high->commodity_24h` score `1.2417` n `101` status `ready` deltaP `23.8913` edge `0.1305` maxDD `-3.4467`
- `market_context_high->equity_1h` score `0.7875` n `58` status `ready` deltaP `5.859` edge `0.0519` maxDD `-0.36`
- `market_context_high->index_1h` score `0.6825` n `58` status `ready` deltaP `10.2777` edge `0.0139` maxDD `-0.0435`
- `news_risk_high->metal_1h` score `0.5717` n `101` status `ready` deltaP `14.2986` edge `0.0125` maxDD `-0.8144`
- `market_context_high->fx_1h` score `0.3977` n `58` status `ready` deltaP `9.3744` edge `0.0063` maxDD `-0.1854`
- `news_risk_high->fx_4h` score `0.3658` n `101` status `ready` deltaP `10.3175` edge `0.0253` maxDD `-0.421`
- `market_context_high->metal_1h` score `0.2938` n `58` status `ready` deltaP `5.8487` edge `0.0163` maxDD `-0.1314`
- `news_risk_high->metal_4h` score `0.2859` n `101` status `ready` deltaP `14.6598` edge `0.0315` maxDD `-2.0994`
- `market_context_high->index_4h` score `0.2775` n `58` status `ready` deltaP `14.0191` edge `0.0058` maxDD `-1.0949`
- `news_risk_high->fx_1h` score `-0.1513` n `101` status `ready` deltaP `3.741` edge `0.0068` maxDD `-0.2147`
- `news_risk_high->equity_1h` score `-0.2873` n `101` status `ready` deltaP `1.4718` edge `0.0068` maxDD `-0.9112`
- `market_context_high->crypto_major_1h` score `-0.396` n `58` status `ready` deltaP `-2.5397` edge `0.0558` maxDD `-2.7494`
- `market_context_high->fx_4h` score `-0.3981` n `58` status `ready` deltaP `2.1236` edge `-0.0028` maxDD `-0.6588`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
