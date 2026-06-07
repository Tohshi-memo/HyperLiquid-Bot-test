# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-07T11:07:21.678962+00:00`
- Price records: `672`
- Market context records: `3171`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `88`

- Symbol pattern count: `8854`

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

- `market_context_high->commodity_24h` score `13.8835` n `101` status `ready` deltaP `47.2171` edge `0.885` maxDD `-2.0927`
- `market_context_high->unknown_24h` score `11.9664` n `101` status `ready` deltaP `20.2643` edge `0.9109` maxDD `-1.9039`
- `market_context_high->crypto_alt_24h` score `11.6398` n `101` status `ready` deltaP `14.7587` edge `2.3915` maxDD `-71.142`
- `market_context_high->index_24h` score `6.1867` n `101` status `ready` deltaP `29.2216` edge `0.8538` maxDD `-16.1026`
- `market_context_high->equity_24h` score `4.5318` n `101` status `ready` deltaP `13.3234` edge `1.3338` maxDD `-53.663`
- `market_context_high->commodity_4h` score `3.0918` n `134` status `ready` deltaP `19.5077` edge `0.1734` maxDD `-1.9973`
- `market_context_high->fx_24h` score `0.7524` n `101` status `ready` deltaP `12.3539` edge `0.0031` maxDD `-0.4876`
- `market_context_high->commodity_1h` score `0.2838` n `136` status `ready` deltaP `5.1471` edge `0.0316` maxDD `-1.7142`
- `market_context_high->unknown_4h` score `0.099` n `134` status `ready` deltaP `11.0506` edge `0.1568` maxDD `-14.7778`
- `market_context_high->index_1h` score `-0.3984` n `136` status `ready` deltaP `5.4597` edge `0.0188` maxDD `-4.5023`
- `market_context_high->crypto_alt_1h` score `-0.4178` n `136` status `ready` deltaP `5.9088` edge `0.12` maxDD `-14.7034`
- `market_context_high->index_4h` score `-0.9429` n `134` status `ready` deltaP `15.3189` edge `0.0679` maxDD `-17.6057`
- `market_context_high->crypto_major_1h` score `-1.0544` n `136` status `ready` deltaP `2.8971` edge `0.0718` maxDD `-15.1032`
- `market_context_high->fx_4h` score `-1.3552` n `134` status `ready` deltaP `-11.7401` edge `-0.007` maxDD `-1.4115`
- `market_context_high->equity_1h` score `-1.3725` n `136` status `ready` deltaP `3.3903` edge `0.0116` maxDD `-8.8863`
- `market_context_high->fx_1h` score `-1.6458` n `136` status `ready` deltaP `-9.5192` edge `-0.0053` maxDD `-0.8046`
- `market_context_high->metal_1h` score `-2.1072` n `136` status `ready` deltaP `-4.0992` edge `-0.0089` maxDD `-7.4828`
- `market_context_high->crypto_alt_4h` score `-2.1607` n `134` status `ready` deltaP `17.9651` edge `0.4077` maxDD `-58.6918`
- `market_context_high->unknown_1h` score `-3.026` n `136` status `ready` deltaP `2.5757` edge `-0.0667` maxDD `-14.2111`
- `market_context_high->crypto_major_4h` score `-3.6197` n `134` status `ready` deltaP `11.0553` edge `0.2546` maxDD `-54.3896`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
