# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-11T07:07:26.128869+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `11726`

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

- `market_context_high->unknown_4h` score `79.3536` n `88` status `ready` deltaP `7.6774` edge `6.6064` maxDD `-0.9161`
- `market_context_high->equity_24h` score `34.0732` n `88` status `ready` deltaP `31.392` edge `2.8693` maxDD `-16.7984`
- `news_risk_high->equity_4h` score `13.0057` n `47` status `ready` deltaP `37.0816` edge `0.9488` maxDD `-6.9762`
- `market_context_high->crypto_alt_24h` score `8.5076` n `88` status `ready` deltaP `34.3276` edge `1.3713` maxDD `-33.4213`
- `market_context_high->index_24h` score `6.1387` n `88` status `ready` deltaP `31.5025` edge `0.3478` maxDD `-2.3671`
- `market_context_high->metal_24h` score `3.9461` n `88` status `ready` deltaP `30.6818` edge `0.1796` maxDD `-1.4245`
- `news_risk_high->equity_1h` score `3.7851` n `51` status `ready` deltaP `19.0912` edge `0.2594` maxDD `-3.6997`
- `news_risk_high->crypto_major_4h` score `3.7055` n `47` status `ready` deltaP `22.6713` edge `0.3064` maxDD `-9.2335`
- `news_risk_high->metal_4h` score `3.492` n `47` status `ready` deltaP `34.954` edge `0.0956` maxDD `-1.0104`
- `news_risk_high->commodity_4h` score `3.3162` n `47` status `ready` deltaP `26.8941` edge `0.1224` maxDD `-0.3611`
- `news_risk_high->index_4h` score `3.0703` n `47` status `ready` deltaP `29.4726` edge `0.103` maxDD `-0.8235`
- `news_risk_high->crypto_alt_4h` score `2.1807` n `47` status `ready` deltaP `27.2314` edge `0.2619` maxDD `-10.1088`
- `news_risk_high->metal_1h` score `1.5339` n `51` status `ready` deltaP `19.3906` edge `0.024` maxDD `-0.3692`
- `news_risk_high->index_1h` score `1.4861` n `51` status `ready` deltaP `19.2409` edge `0.0257` maxDD `-0.4103`
- `news_risk_high->crypto_alt_1h` score `0.642` n `51` status `ready` deltaP `18.7478` edge `0.0511` maxDD `-6.1688`
- `news_risk_high->crypto_major_1h` score `0.5242` n `51` status `ready` deltaP `18.5981` edge `0.0484` maxDD `-7.0808`
- `news_risk_high->commodity_1h` score `-0.0755` n `51` status `ready` deltaP `-1.7142` edge `0.0386` maxDD `-0.3438`
- `market_context_high->metal_1h` score `-0.3724` n `88` status `ready` deltaP `3.3479` edge `0.0143` maxDD `-1.4122`
- `market_context_high->commodity_1h` score `-0.3802` n `88` status `ready` deltaP `2.9872` edge `-0.0004` maxDD `-1.7935`
- `market_context_high->commodity_4h` score `-0.655` n `88` status `ready` deltaP `1.5798` edge `0.0161` maxDD `-4.182`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
