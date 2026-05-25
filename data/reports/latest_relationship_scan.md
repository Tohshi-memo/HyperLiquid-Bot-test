# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-25T09:07:22.906581+00:00`
- Price records: `672`
- Market context records: `1828`
- Flow alert records: `7160`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4488`

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

- `market_context_high->crypto_alt_4h` score `6.9083` n `191` status `ready` deltaP `22.6288` edge `0.5393` maxDD `-5.1574`
- `market_context_high->metal_24h` score `6.7513` n `178` status `ready` deltaP `26.8961` edge `0.6259` maxDD `-12.7414`
- `market_context_high->crypto_major_4h` score `6.4587` n `191` status `ready` deltaP `26.3001` edge `0.4875` maxDD `-4.9684`
- `news_risk_high->commodity_4h` score `6.4288` n `30` status `ready` deltaP `28.8008` edge `0.4092` maxDD `-3.5713`
- `market_context_high->unknown_4h` score `4.4724` n `191` status `ready` deltaP `17.0684` edge `0.4613` maxDD `-9.8581`
- `market_context_high->index_24h` score `3.595` n `178` status `ready` deltaP `17.8683` edge `0.3033` maxDD `-4.1604`
- `news_risk_high->commodity_1h` score `3.2147` n `30` status `ready` deltaP `24.4212` edge `0.1368` maxDD `-1.2043`
- `market_context_high->equity_4h` score `2.9877` n `191` status `ready` deltaP `16.6837` edge `0.2472` maxDD `-5.0894`
- `market_context_high->unknown_24h` score `2.7051` n `178` status `ready` deltaP `14.56` edge `0.6604` maxDD `-35.8966`
- `market_context_high->equity_24h` score `2.2648` n `178` status `ready` deltaP `16.0619` edge `0.5715` maxDD `-33.1875`
- `news_risk_high->fx_4h` score `0.9019` n `30` status `ready` deltaP `21.6362` edge `-0.0014` maxDD `-0.1774`
- `market_context_high->index_4h` score `0.8051` n `191` status `ready` deltaP `11.8791` edge `0.0968` maxDD `-3.7119`
- `market_context_high->crypto_major_1h` score `0.4458` n `196` status `ready` deltaP `6.3394` edge `0.0935` maxDD `-3.2225`
- `market_context_high->crypto_alt_1h` score `0.3194` n `196` status `ready` deltaP `6.5227` edge `0.0945` maxDD `-4.9097`
- `news_risk_high->unknown_4h` score `0.1803` n `30` status `ready` deltaP `8.1504` edge `0.0411` maxDD `-2.7857`
- `market_context_high->equity_1h` score `-0.0064` n `196` status `ready` deltaP `5.0318` edge `0.0453` maxDD `-2.6836`
- `market_context_high->crypto_major_24h` score `-0.0334` n `178` status `ready` deltaP `18.1648` edge `0.7347` maxDD `-62.3533`
- `market_context_high->fx_24h` score `-0.1279` n `178` status `ready` deltaP `11.7822` edge `0.0157` maxDD `-1.3925`
- `news_risk_high->unknown_1h` score `-0.452` n `30` status `ready` deltaP `16.4072` edge `-0.1201` maxDD `-2.1115`
- `market_context_high->unknown_1h` score `-0.5199` n `196` status `ready` deltaP `3.0399` edge `0.0316` maxDD `-3.6151`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
