# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-07T19:37:22.583569+00:00`
- Price records: `672`
- Market context records: `3210`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `104`

- Symbol pattern count: `10910`

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

- `market_context_high->commodity_24h` score `13.8027` n `98` status `ready` deltaP `47.5871` edge `0.8758` maxDD `-2.0927`
- `market_context_high->crypto_alt_24h` score `11.2591` n `98` status `ready` deltaP `12.5815` edge `2.3572` maxDD `-71.142`
- `market_context_high->index_24h` score `9.2652` n `98` status `ready` deltaP `28.373` edge `0.8384` maxDD `-16.1026`
- `market_context_high->equity_24h` score `4.9012` n `98` status `ready` deltaP `12.3264` edge `1.3878` maxDD `-53.663`
- `market_context_high->commodity_4h` score `3.3811` n `124` status `ready` deltaP `22.1037` edge `0.1802` maxDD `-1.9973`
- `market_context_high->commodity_1h` score `0.5924` n `136` status `ready` deltaP `7.3397` edge `0.0427` maxDD `-1.7142`
- `market_context_high->fx_24h` score `0.1602` n `98` status `ready` deltaP `8.8684` edge `-0.0053` maxDD `-0.9048`
- `market_context_high->unknown_4h` score `0.1139` n `124` status `ready` deltaP `10.2921` edge `0.1631` maxDD `-14.7778`
- `market_context_high->index_1h` score `-0.9564` n `136` status `ready` deltaP `2.6814` edge `0.0087` maxDD `-4.5023`
- `market_context_high->crypto_major_1h` score `-1.084` n `136` status `ready` deltaP `4.218` edge `0.0592` maxDD `-15.1032`
- `market_context_high->fx_4h` score `-1.0866` n `124` status `ready` deltaP `-6.845` edge `-0.0052` maxDD `-1.4115`
- `market_context_high->crypto_alt_1h` score `-1.3493` n `136` status `ready` deltaP `4.152` edge `0.077` maxDD `-14.7034`
- `market_context_high->index_4h` score `-1.5562` n `124` status `ready` deltaP `15.0177` edge `0.0611` maxDD `-17.6057`
- `market_context_high->equity_1h` score `-1.6211` n `136` status `ready` deltaP `1.9329` edge `0.0006` maxDD `-8.8863`
- `market_context_high->fx_1h` score `-1.6444` n `136` status `ready` deltaP `-9.5324` edge `-0.0048` maxDD `-0.8278`
- `market_context_high->metal_1h` score `-2.1296` n `136` status `ready` deltaP `-3.5268` edge `-0.0115` maxDD `-7.7299`
- `market_context_high->unknown_1h` score `-2.8325` n `136` status `ready` deltaP `0.9555` edge `-0.1242` maxDD `-17.6244`
- `market_context_high->crypto_alt_4h` score `-3.541` n `124` status `ready` deltaP `12.4804` edge `0.2673` maxDD `-58.6918`
- `market_context_high->unknown_24h` score `-3.5839` n `98` status `ready` deltaP `11.0722` edge `0.1393` maxDD `-50.14`
- `market_context_high->crypto_major_4h` score `-4.6916` n `124` status `ready` deltaP `5.4583` edge `0.1545` maxDD `-54.3896`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
