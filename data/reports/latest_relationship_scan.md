# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-25T08:52:19.856502+00:00`
- Price records: `672`
- Market context records: `1827`
- Flow alert records: `7157`
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

- `market_context_high->crypto_alt_4h` score `6.902` n `190` status `ready` deltaP `22.5048` edge `0.5396` maxDD `-5.1574`
- `market_context_high->metal_24h` score `6.7796` n `178` status `ready` deltaP `27.0697` edge `0.6271` maxDD `-12.7414`
- `market_context_high->crypto_major_4h` score `6.4603` n `190` status `ready` deltaP `26.2147` edge `0.4882` maxDD `-4.9684`
- `news_risk_high->commodity_4h` score `6.4542` n `30` status `ready` deltaP `28.9533` edge `0.4103` maxDD `-3.5713`
- `market_context_high->unknown_4h` score `4.4943` n `190` status `ready` deltaP `16.9224` edge `0.4641` maxDD `-9.8581`
- `market_context_high->index_24h` score `3.607` n `178` status `ready` deltaP `17.8683` edge `0.3043` maxDD `-4.1604`
- `news_risk_high->commodity_1h` score `3.2147` n `30` status `ready` deltaP `24.4212` edge `0.1368` maxDD `-1.2043`
- `market_context_high->equity_4h` score `2.9934` n `190` status `ready` deltaP `16.5597` edge `0.2485` maxDD `-5.0894`
- `market_context_high->unknown_24h` score `2.6624` n `178` status `ready` deltaP `14.3864` edge `0.658` maxDD `-35.8966`
- `market_context_high->equity_24h` score `2.3195` n `178` status `ready` deltaP `16.2355` edge `0.5749` maxDD `-33.1875`
- `news_risk_high->fx_4h` score `0.9026` n `30` status `ready` deltaP `21.6362` edge `-0.0013` maxDD `-0.1774`
- `market_context_high->index_4h` score `0.7955` n `190` status `ready` deltaP `11.7138` edge `0.0971` maxDD `-3.7119`
- `market_context_high->crypto_major_1h` score `0.4602` n `196` status `ready` deltaP `6.4891` edge `0.0937` maxDD `-3.2225`
- `market_context_high->crypto_alt_1h` score `0.3218` n `196` status `ready` deltaP `6.5227` edge `0.0947` maxDD `-4.9097`
- `news_risk_high->unknown_4h` score `0.1811` n `30` status `ready` deltaP `8.1504` edge `0.0412` maxDD `-2.7857`
- `market_context_high->equity_1h` score `0.0056` n `196` status `ready` deltaP `5.1815` edge `0.0453` maxDD `-2.6836`
- `market_context_high->crypto_major_24h` score `-0.049` n `178` status `ready` deltaP `18.1648` edge `0.7334` maxDD `-62.3533`
- `market_context_high->fx_24h` score `-0.149` n `178` status `ready` deltaP `11.6086` edge `0.0151` maxDD `-1.3925`
- `news_risk_high->unknown_1h` score `-0.452` n `30` status `ready` deltaP `16.4072` edge `-0.1201` maxDD `-2.1115`
- `market_context_high->unknown_1h` score `-0.5199` n `196` status `ready` deltaP `3.0399` edge `0.0316` maxDD `-3.6151`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
