# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-22T00:52:27.802259+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9964`

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

- `market_context_high->unknown_4h` score `39.4294` n `52` status `ready` deltaP `7.3171` edge `3.237` maxDD `0.0`
- `market_context_high->crypto_major_24h` score `21.1087` n `51` status `ready` deltaP `13.8276` edge `2.0129` maxDD `-25.0154`
- `news_risk_high->crypto_major_24h` score `10.6885` n `101` status `ready` deltaP `-0.1891` edge `1.5778` maxDD `-46.1999`
- `market_context_high->equity_24h` score `10.4786` n `51` status `ready` deltaP `7.0568` edge `0.9792` maxDD `-9.5753`
- `news_risk_high->crypto_alt_24h` score `6.1849` n `101` status `ready` deltaP `0.1959` edge `1.0022` maxDD `-32.7147`
- `market_context_high->crypto_alt_24h` score `6.15` n `51` status `ready` deltaP `12.1936` edge `0.7712` maxDD `-25.1993`
- `market_context_high->index_24h` score `3.7328` n `51` status `ready` deltaP `11.0498` edge `0.2835` maxDD `-1.0213`
- `news_risk_high->crypto_alt_4h` score `3.0342` n `101` status `ready` deltaP `14.8032` edge `0.2751` maxDD `-7.675`
- `news_risk_high->commodity_24h` score `2.5464` n `101` status `ready` deltaP `31.3565` edge `0.248` maxDD `-3.4467`
- `news_risk_high->crypto_alt_1h` score `2.3265` n `101` status `ready` deltaP `14.2853` edge `0.1452` maxDD `-2.058`
- `news_risk_high->crypto_major_4h` score `2.1344` n `101` status `ready` deltaP `16.3276` edge `0.1948` maxDD `-8.0625`
- `news_risk_high->crypto_major_1h` score `1.624` n `101` status `ready` deltaP `15.932` edge `0.0814` maxDD `-2.8494`
- `news_risk_high->fx_4h` score `0.5446` n `101` status `ready` deltaP `12.1468` edge `0.028` maxDD `-0.421`
- `market_context_high->equity_1h` score `0.498` n `52` status `ready` deltaP `3.5813` edge `0.0424` maxDD `-0.3155`
- `news_risk_high->metal_1h` score `0.4543` n `101` status `ready` deltaP `12.9513` edge `0.0117` maxDD `-0.8144`
- `market_context_high->index_1h` score `0.4317` n `52` status `ready` deltaP `7.7499` edge `0.0097` maxDD `-0.031`
- `market_context_high->index_4h` score `0.399` n `52` status `ready` deltaP `14.0009` edge `0.0054` maxDD `-0.8066`
- `news_risk_high->metal_4h` score `0.1991` n `101` status `ready` deltaP `13.4403` edge `0.0324` maxDD `-2.0994`
- `market_context_high->fx_1h` score `0.1889` n `52` status `ready` deltaP `6.7941` edge `0.0061` maxDD `-0.1854`
- `market_context_high->metal_24h` score `0.1477` n `51` status `ready` deltaP `17.0241` edge `-0.0778` maxDD `-0.2042`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
