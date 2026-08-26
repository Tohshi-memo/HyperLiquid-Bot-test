# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-26T11:22:29.588750+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `14760`

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

- `news_risk_high->unknown_24h` score `44.661` n `53` status `ready` deltaP `11.6319` edge `3.6442` maxDD `0.0`
- `news_risk_high->unknown_4h` score `11.9094` n `53` status `ready` deltaP `23.6079` edge `0.845` maxDD `-0.1281`
- `news_risk_high->crypto_alt_24h` score `8.9512` n `53` status `ready` deltaP `30.4278` edge `0.5872` maxDD `-2.8629`
- `news_risk_high->equity_24h` score `7.0581` n `53` status `ready` deltaP `30.1134` edge `0.4805` maxDD `-4.7801`
- `news_risk_high->index_24h` score `4.0282` n `53` status `ready` deltaP `39.9404` edge `0.0846` maxDD `-0.2147`
- `news_risk_high->fx_4h` score `2.8487` n `53` status `ready` deltaP `34.3535` edge `0.0218` maxDD `-0.0746`
- `news_risk_high->unknown_1h` score `2.7363` n `53` status `ready` deltaP `15.2638` edge `0.1618` maxDD `-0.8426`
- `market_context_high->unknown_4h` score `2.5425` n `136` status `ready` deltaP `21.9154` edge `0.1066` maxDD `-0.5994`
- `news_risk_high->metal_24h` score `1.7444` n `53` status `ready` deltaP `29.1896` edge `-0.045` maxDD `-0.0053`
- `news_risk_high->equity_4h` score `1.7271` n `53` status `ready` deltaP `19.7365` edge `0.0894` maxDD `-2.164`
- `news_risk_high->fx_1h` score `1.0902` n `53` status `ready` deltaP `15.3203` edge `0.0057` maxDD `-0.0257`
- `market_context_high->unknown_1h` score `1.0547` n `136` status `ready` deltaP `11.3376` edge `0.0572` maxDD `-1.5916`
- `news_risk_high->commodity_1h` score `0.4871` n `53` status `ready` deltaP `11.2756` edge `-0.0033` maxDD `-0.5024`
- `news_risk_high->equity_1h` score `0.3928` n `53` status `ready` deltaP `12.3263` edge `0.0046` maxDD `-0.9128`
- `news_risk_high->index_4h` score `0.1851` n `53` status `ready` deltaP `7.1186` edge `0.0077` maxDD `-0.1788`
- `news_risk_high->index_1h` score `-0.0807` n `53` status `ready` deltaP `3.7002` edge `0.0003` maxDD `-0.1583`
- `news_risk_high->metal_4h` score `-0.3388` n `53` status `ready` deltaP `5.5769` edge `-0.0123` maxDD `-0.249`
- `news_risk_high->metal_1h` score `-0.4043` n `53` status `ready` deltaP `-0.0141` edge `-0.011` maxDD `-0.1413`
- `market_context_high->fx_1h` score `-0.4302` n `136` status `ready` deltaP `2.8619` edge `-0.001` maxDD `-0.8587`
- `news_risk_high->commodity_4h` score `-0.9496` n `53` status `ready` deltaP `-0.7536` edge `0.0066` maxDD `-1.1986`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
