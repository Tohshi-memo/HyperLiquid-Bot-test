# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-25T05:22:16.377394+00:00`
- Price records: `672`
- Market context records: `1812`
- Flow alert records: `7114`
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

- `market_context_high->crypto_alt_4h` score `7.1508` n `183` status `ready` deltaP `23.2757` edge `0.5552` maxDD `-5.1574`
- `market_context_high->metal_24h` score `6.8596` n `178` status `ready` deltaP `27.5905` edge `0.6303` maxDD `-12.7414`
- `market_context_high->crypto_major_4h` score `6.7053` n `183` status `ready` deltaP `27.2674` edge `0.5016` maxDD `-4.9684`
- `news_risk_high->commodity_4h` score `6.5389` n `30` status `ready` deltaP `29.563` edge `0.4133` maxDD `-3.5713`
- `market_context_high->unknown_4h` score `4.7329` n `183` status `ready` deltaP `17.6846` edge `0.4789` maxDD `-9.8581`
- `market_context_high->index_24h` score `3.6742` n `178` status `ready` deltaP `17.8683` edge `0.3099` maxDD `-4.1604`
- `news_risk_high->commodity_1h` score `3.3189` n `30` status `ready` deltaP `25.1697` edge `0.1405` maxDD `-1.2043`
- `market_context_high->equity_4h` score `2.9581` n `183` status `ready` deltaP `15.6537` edge `0.2516` maxDD `-5.0894`
- `market_context_high->equity_24h` score `2.8944` n `178` status `ready` deltaP `18.6661` edge `0.6066` maxDD `-33.1875`
- `market_context_high->unknown_24h` score `2.3166` n `178` status `ready` deltaP `12.8239` edge `0.6396` maxDD `-35.8966`
- `news_risk_high->fx_4h` score `0.9073` n `30` status `ready` deltaP `21.6362` edge `-0.0007` maxDD `-0.1774`
- `market_context_high->index_4h` score `0.7994` n `183` status `ready` deltaP `11.3572` edge `0.0998` maxDD `-3.7119`
- `market_context_high->crypto_major_1h` score `0.501` n `188` status `ready` deltaP `6.2651` edge `0.0986` maxDD `-3.2225`
- `market_context_high->crypto_alt_1h` score `0.4122` n `188` status `ready` deltaP `6.813` edge `0.1003` maxDD `-4.9097`
- `news_risk_high->unknown_4h` score `0.3948` n `30` status `ready` deltaP `9.9796` edge `0.0564` maxDD `-2.7857`
- `market_context_high->equity_1h` score `-0.0991` n `188` status `ready` deltaP `4.3828` edge `0.0419` maxDD `-2.6836`
- `market_context_high->crypto_major_24h` score `-0.2129` n `178` status `ready` deltaP `17.9912` edge `0.7209` maxDD `-62.3533`
- `market_context_high->index_1h` score `-0.356` n `188` status `ready` deltaP `0.6944` edge `0.0129` maxDD `-1.7205`
- `market_context_high->fx_24h` score `-0.3791` n `178` status `ready` deltaP `9.8725` edge `0.0075` maxDD `-1.3925`
- `market_context_high->unknown_1h` score `-0.3995` n `188` status `ready` deltaP `3.0896` edge `0.0413` maxDD `-3.6151`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
