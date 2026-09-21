# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-21T14:07:39.184256+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `8866`

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

- `market_context_high->unknown_4h` score `31.3813` n `58` status `ready` deltaP `1.23` edge `2.6219` maxDD `-0.5326`
- `news_risk_high->crypto_major_24h` score `19.7121` n `101` status `ready` deltaP `7.2762` edge `2.28` maxDD `-46.1999`
- `news_risk_high->crypto_alt_24h` score `13.7661` n `101` status `ready` deltaP `7.6612` edge `1.5842` maxDD `-32.7147`
- `news_risk_high->crypto_alt_4h` score `3.4025` n `101` status `ready` deltaP `16.6324` edge `0.2936` maxDD `-7.675`
- `news_risk_high->crypto_major_4h` score `3.1231` n `101` status `ready` deltaP `19.9861` edge `0.2528` maxDD `-8.0625`
- `news_risk_high->crypto_alt_1h` score `2.4164` n `101` status `ready` deltaP `14.8841` edge `0.1487` maxDD `-2.058`
- `news_risk_high->crypto_major_1h` score `1.7811` n `101` status `ready` deltaP `16.5308` edge `0.0905` maxDD `-2.8494`
- `news_risk_high->commodity_24h` score `1.3786` n `101` status `ready` deltaP `24.0649` edge `0.1469` maxDD `-3.4467`
- `market_context_high->equity_1h` score `0.7468` n `58` status `ready` deltaP `5.4099` edge `0.0515` maxDD `-0.36`
- `market_context_high->index_1h` score `0.5903` n `58` status `ready` deltaP `9.2298` edge `0.0132` maxDD `-0.0435`
- `news_risk_high->metal_1h` score `0.4603` n `101` status `ready` deltaP `13.101` edge `0.0112` maxDD `-0.8144`
- `market_context_high->fx_1h` score `0.4085` n `58` status `ready` deltaP `9.5241` edge `0.0062` maxDD `-0.1854`
- `news_risk_high->fx_4h` score `0.2891` n `101` status `ready` deltaP `9.4029` edge `0.025` maxDD `-0.421`
- `news_risk_high->metal_4h` score `0.2847` n `101` status `ready` deltaP `14.6598` edge `0.0314` maxDD `-2.0994`
- `market_context_high->index_4h` score `0.2568` n `58` status `ready` deltaP `13.5618` edge `0.0062` maxDD `-1.0949`
- `market_context_high->metal_1h` score `0.1824` n `58` status `ready` deltaP `4.6511` edge `0.015` maxDD `-0.1314`
- `news_risk_high->fx_1h` score `-0.1405` n `101` status `ready` deltaP `3.8907` edge `0.0067` maxDD `-0.2147`
- `news_risk_high->equity_1h` score `-0.3281` n `101` status `ready` deltaP `1.0227` edge `0.0064` maxDD `-0.9112`
- `market_context_high->fx_4h` score `-0.448` n `58` status `ready` deltaP `1.209` edge `-0.0031` maxDD `-0.6588`
- `news_risk_high->metal_24h` score `-0.4772` n `101` status `ready` deltaP `8.7355` edge `-0.035` maxDD `-2.4203`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
