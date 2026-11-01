# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-01T02:37:30.641059+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `6255`

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

- `market_context_high->unknown_24h` score `4857.6752` n `72` status `ready` deltaP `-4.8611` edge `404.8636` maxDD `-0.9938`
- `market_context_high->unknown_4h` score `209.6681` n `72` status `ready` deltaP `0.83` edge `17.4801` maxDD `-0.3966`
- `news_risk_high->unknown_1h` score `81.4684` n `108` status `ready` deltaP `-5.0454` edge `6.8513` maxDD `-0.9571`
- `news_risk_high->crypto_alt_24h` score `14.7001` n `92` status `ready` deltaP `35.0921` edge `1.1084` maxDD `-6.3871`
- `market_context_high->equity_24h` score `13.5364` n `72` status `ready` deltaP `26.3889` edge `1.1504` maxDD `-10.1969`
- `market_context_high->index_24h` score `5.4999` n `72` status `ready` deltaP `47.3958` edge `0.1605` maxDD `-0.1187`
- `news_risk_high->crypto_alt_4h` score `5.48` n `108` status `ready` deltaP `20.7317` edge `0.4571` maxDD `-7.4246`
- `market_context_high->commodity_4h` score `2.8688` n `72` status `ready` deltaP `28.6755` edge `0.0813` maxDD `-0.3387`
- `market_context_high->metal_4h` score `1.2157` n `72` status `ready` deltaP `15.0745` edge `0.0433` maxDD `-0.7323`
- `market_context_high->fx_1h` score `1.0593` n `72` status `ready` deltaP `15.9598` edge `0.0003` maxDD `-0.1407`
- `news_risk_high->crypto_alt_1h` score `0.8553` n `108` status `ready` deltaP `8.8767` edge `0.1075` maxDD `-3.9659`
- `market_context_high->metal_1h` score `0.7394` n `72` status `ready` deltaP `10.4291` edge `0.0211` maxDD `-0.3209`
- `market_context_high->commodity_24h` score `0.7121` n `72` status `ready` deltaP `27.0833` edge `0.1111` maxDD `-10.3625`
- `market_context_high->fx_4h` score `0.4377` n `72` status `ready` deltaP `10.9926` edge `0.0023` maxDD `-0.1285`
- `market_context_high->equity_4h` score `0.3755` n `72` status `ready` deltaP `-4.9458` edge `0.2043` maxDD `-4.1883`
- `market_context_high->equity_1h` score `0.3268` n `72` status `ready` deltaP `1.6883` edge `0.1182` maxDD `-2.3383`
- `market_context_high->crypto_major_1h` score `-0.2518` n `72` status `ready` deltaP `1.0479` edge `0.0635` maxDD `-5.2213`
- `market_context_high->commodity_1h` score `-0.3742` n `72` status `ready` deltaP `0.2162` edge `0.0188` maxDD `-0.4475`
- `market_context_high->index_1h` score `-0.4876` n `72` status `ready` deltaP `-1.2392` edge `0.0016` maxDD `-1.1344`
- `market_context_high->crypto_alt_1h` score `-0.5946` n `72` status `ready` deltaP `-0.3826` edge `0.0846` maxDD `-5.9953`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
