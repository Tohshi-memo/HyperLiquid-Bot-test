# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-25T08:37:14.022690+00:00`
- Price records: `672`
- Market context records: `1826`
- Flow alert records: `7154`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4474`

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

- `market_context_high->crypto_alt_4h` score `6.8932` n `189` status `ready` deltaP `22.3795` edge `0.5397` maxDD `-5.1574`
- `market_context_high->metal_24h` score `6.8043` n `178` status `ready` deltaP `27.2433` edge `0.628` maxDD `-12.7414`
- `news_risk_high->commodity_4h` score `6.476` n `30` status `ready` deltaP `29.1057` edge `0.4111` maxDD `-3.5713`
- `market_context_high->crypto_major_4h` score `6.4654` n `189` status `ready` deltaP `26.1284` edge `0.4892` maxDD `-4.9684`
- `market_context_high->unknown_4h` score `4.4887` n `189` status `ready` deltaP `16.9272` edge `0.4636` maxDD `-9.8581`
- `market_context_high->index_24h` score `3.6166` n `178` status `ready` deltaP `17.8683` edge `0.3051` maxDD `-4.1604`
- `news_risk_high->commodity_1h` score `3.2147` n `30` status `ready` deltaP `24.4212` edge `0.1368` maxDD `-1.2043`
- `market_context_high->equity_4h` score `3.0025` n `189` status `ready` deltaP `16.4344` edge `0.2501` maxDD `-5.0894`
- `market_context_high->unknown_24h` score `2.6305` n `178` status `ready` deltaP `14.2127` edge `0.6565` maxDD `-35.8966`
- `market_context_high->equity_24h` score `2.3682` n `178` status `ready` deltaP `16.4091` edge `0.5778` maxDD `-33.1875`
- `news_risk_high->fx_4h` score `0.9026` n `30` status `ready` deltaP `21.6362` edge `-0.0013` maxDD `-0.1774`
- `market_context_high->index_4h` score `0.8027` n `189` status `ready` deltaP `11.6991` edge `0.0978` maxDD `-3.7119`
- `market_context_high->crypto_major_1h` score `0.4626` n `196` status `ready` deltaP `6.4891` edge `0.0939` maxDD `-3.2225`
- `market_context_high->crypto_alt_1h` score `0.3266` n `196` status `ready` deltaP `6.5227` edge `0.0951` maxDD `-4.9097`
- `news_risk_high->unknown_4h` score `0.203` n `30` status `ready` deltaP `8.3028` edge `0.043` maxDD `-2.7857`
- `market_context_high->equity_1h` score `0.0032` n `196` status `ready` deltaP `5.1815` edge `0.0451` maxDD `-2.6836`
- `market_context_high->crypto_major_24h` score `-0.067` n `178` status `ready` deltaP `18.1648` edge `0.7319` maxDD `-62.3533`
- `market_context_high->fx_24h` score `-0.155` n `178` status `ready` deltaP `11.6086` edge `0.0146` maxDD `-1.3925`
- `news_risk_high->unknown_1h` score `-0.4317` n `30` status `ready` deltaP `16.5569` edge `-0.1185` maxDD `-2.1115`
- `market_context_high->unknown_1h` score `-0.4887` n `196` status `ready` deltaP `3.1896` edge `0.0332` maxDD `-3.6151`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
