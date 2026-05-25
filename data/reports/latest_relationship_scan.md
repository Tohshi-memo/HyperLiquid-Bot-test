# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-25T04:37:14.123120+00:00`
- Price records: `672`
- Market context records: `1809`
- Flow alert records: `7105`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4514`

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

- `market_context_high->crypto_alt_4h` score `7.2714` n `183` status `ready` deltaP `23.733` edge `0.5622` maxDD `-5.1574`
- `market_context_high->metal_24h` score `6.874` n `178` status `ready` deltaP `27.5905` edge `0.6315` maxDD `-12.7414`
- `market_context_high->crypto_major_4h` score `6.7863` n `183` status `ready` deltaP `27.7247` edge `0.5053` maxDD `-4.9684`
- `news_risk_high->commodity_4h` score `6.5245` n `30` status `ready` deltaP `29.563` edge `0.4121` maxDD `-3.5713`
- `market_context_high->unknown_4h` score `4.7003` n `183` status `ready` deltaP `17.5322` edge `0.4772` maxDD `-9.8581`
- `market_context_high->index_24h` score `3.697` n `178` status `ready` deltaP `17.8683` edge `0.3118` maxDD `-4.1604`
- `news_risk_high->commodity_1h` score `3.3189` n `30` status `ready` deltaP `25.1697` edge `0.1405` maxDD `-1.2043`
- `market_context_high->equity_24h` score `3.0224` n `178` status `ready` deltaP `19.1869` edge `0.6138` maxDD `-33.1875`
- `market_context_high->equity_4h` score `2.9389` n `183` status `ready` deltaP `15.6537` edge `0.25` maxDD `-5.0894`
- `market_context_high->unknown_24h` score `2.2348` n `178` status `ready` deltaP `12.4766` edge `0.6351` maxDD `-35.8966`
- `news_risk_high->fx_4h` score `0.9081` n `30` status `ready` deltaP `21.6362` edge `-0.0006` maxDD `-0.1774`
- `market_context_high->index_4h` score `0.7922` n `183` status `ready` deltaP `11.3572` edge `0.0992` maxDD `-3.7119`
- `market_context_high->crypto_major_1h` score `0.374` n `185` status `ready` deltaP `5.742` edge `0.0915` maxDD `-3.2225`
- `news_risk_high->unknown_4h` score `0.3736` n `30` status `ready` deltaP `9.8272` edge `0.0547` maxDD `-2.7857`
- `market_context_high->crypto_alt_1h` score `0.2728` n `185` status `ready` deltaP `6.3158` edge `0.092` maxDD `-4.9097`
- `market_context_high->equity_1h` score `-0.1438` n `185` status `ready` deltaP `3.9287` edge `0.0412` maxDD `-2.6836`
- `market_context_high->crypto_major_24h` score `-0.2009` n `178` status `ready` deltaP `17.9912` edge `0.7219` maxDD `-62.3533`
- `market_context_high->unknown_1h` score `-0.2951` n `185` status `ready` deltaP `3.7045` edge `0.0459` maxDD `-3.6151`
- `market_context_high->fx_24h` score `-0.4423` n `178` status `ready` deltaP `9.3516` edge `0.0057` maxDD `-1.3925`
- `news_risk_high->fx_1h` score `-0.4469` n `30` status `ready` deltaP `-4.6806` edge `0.0001` maxDD `-0.0948`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
