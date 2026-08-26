# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-26T11:07:24.223807+00:00`
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

- `news_risk_high->unknown_24h` score `44.6226` n `53` status `ready` deltaP `11.6319` edge `3.641` maxDD `0.0`
- `news_risk_high->unknown_4h` score `11.8768` n `53` status `ready` deltaP `23.4555` edge `0.8433` maxDD `-0.1281`
- `news_risk_high->crypto_alt_24h` score `8.7585` n `53` status `ready` deltaP `30.2542` edge `0.5723` maxDD `-2.8629`
- `news_risk_high->equity_24h` score `7.0665` n `53` status `ready` deltaP `30.1134` edge `0.4812` maxDD `-4.7801`
- `news_risk_high->index_24h` score `4.027` n `53` status `ready` deltaP `39.9404` edge `0.0845` maxDD `-0.2147`
- `news_risk_high->fx_4h` score `2.8353` n `53` status `ready` deltaP `34.201` edge `0.0217` maxDD `-0.0746`
- `news_risk_high->unknown_1h` score `2.7339` n `53` status `ready` deltaP `15.2638` edge `0.1616` maxDD `-0.8426`
- `market_context_high->unknown_4h` score `2.5099` n `136` status `ready` deltaP `21.763` edge `0.1049` maxDD `-0.5994`
- `news_risk_high->equity_4h` score `1.7465` n `53` status `ready` deltaP `19.889` edge `0.09` maxDD `-2.164`
- `news_risk_high->metal_24h` score `1.73` n `53` status `ready` deltaP `29.1896` edge `-0.0462` maxDD `-0.0053`
- `news_risk_high->fx_1h` score `1.1021` n `53` status `ready` deltaP `15.47` edge `0.0057` maxDD `-0.0257`
- `market_context_high->unknown_1h` score `1.0523` n `136` status `ready` deltaP `11.3376` edge `0.057` maxDD `-1.5916`
- `news_risk_high->commodity_1h` score `0.4871` n `53` status `ready` deltaP `11.2756` edge `-0.0033` maxDD `-0.5024`
- `news_risk_high->equity_1h` score `0.4045` n `53` status `ready` deltaP `12.476` edge `0.0051` maxDD `-0.9128`
- `news_risk_high->index_4h` score `0.1839` n `53` status `ready` deltaP `7.1186` edge `0.0076` maxDD `-0.1788`
- `news_risk_high->index_1h` score `-0.0807` n `53` status `ready` deltaP `3.7002` edge `0.0003` maxDD `-0.1583`
- `news_risk_high->metal_4h` score `-0.3642` n `53` status `ready` deltaP `5.4245` edge `-0.0134` maxDD `-0.249`
- `news_risk_high->metal_1h` score `-0.4055` n `53` status `ready` deltaP `-0.0141` edge `-0.0111` maxDD `-0.1413`
- `market_context_high->fx_1h` score `-0.4224` n `136` status `ready` deltaP `3.0116` edge `-0.001` maxDD `-0.8587`
- `news_risk_high->commodity_4h` score `-0.9511` n `53` status `ready` deltaP `-0.7536` edge `0.0064` maxDD `-1.1986`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
