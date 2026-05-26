# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-26T13:07:22.263350+00:00`
- Price records: `672`
- Market context records: `1940`
- Flow alert records: `7482`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `7547`

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

- `market_context_high->crypto_alt_4h` score `7.1216` n `226` status `ready` deltaP `22.2945` edge `0.5593` maxDD `-5.1574`
- `market_context_high->crypto_major_4h` score `6.4757` n `226` status `ready` deltaP `25.9569` edge `0.4912` maxDD `-4.9684`
- `market_context_high->unknown_4h` score `2.5882` n `226` status `ready` deltaP `14.2166` edge `0.3233` maxDD `-9.8581`
- `market_context_high->equity_4h` score `2.0361` n `226` status `ready` deltaP `13.8794` edge `0.1866` maxDD `-5.0894`
- `market_context_high->crypto_major_1h` score `0.7076` n `232` status `ready` deltaP `7.8577` edge `0.1052` maxDD `-3.2225`
- `market_context_high->unknown_24h` score `0.6788` n `199` status `ready` deltaP `14.5367` edge `0.4917` maxDD `-35.8966`
- `market_context_high->crypto_alt_1h` score `0.5433` n `232` status `ready` deltaP `7.177` edge `0.1088` maxDD `-4.9097`
- `market_context_high->metal_24h` score `0.233` n `199` status `ready` deltaP `11.9871` edge `0.1821` maxDD `-12.7414`
- `market_context_high->index_24h` score `0.1513` n `199` status `ready` deltaP `4.1922` edge `0.1075` maxDD `-4.1604`
- `market_context_high->index_4h` score `0.1433` n `226` status `ready` deltaP `8.4657` edge `0.0644` maxDD `-3.7119`
- `market_context_high->equity_1h` score `-0.1471` n `232` status `ready` deltaP `5.103` edge `0.0331` maxDD `-2.6836`
- `market_context_high->fx_24h` score `-0.2759` n `199` status `ready` deltaP `9.9323` edge `0.0157` maxDD `-1.3925`
- `market_context_high->index_1h` score `-0.6014` n `232` status `ready` deltaP `0.7437` edge `0.0081` maxDD `-1.7205`
- `market_context_high->fx_1h` score `-0.6347` n `232` status `ready` deltaP `-2.7522` edge `0.0002` maxDD `-0.3914`
- `market_context_high->equity_24h` score `-0.8957` n `199` status `ready` deltaP `8.6107` edge `0.3578` maxDD `-33.1875`
- `market_context_high->fx_4h` score `-0.968` n `226` status `ready` deltaP `-5.0832` edge `-0.0014` maxDD `-1.1056`
- `market_context_high->metal_1h` score `-1.1533` n `232` status `ready` deltaP `3.5808` edge `0.0136` maxDD `-6.3532`
- `market_context_high->unknown_1h` score `-1.4356` n `232` status `ready` deltaP `0.7282` edge `-0.0293` maxDD `-3.6151`
- `market_context_high->metal_4h` score `-1.6318` n `226` status `ready` deltaP `6.8251` edge `0.0877` maxDD `-12.5349`
- `market_context_high->commodity_1h` score `-1.9942` n `232` status `ready` deltaP `0.9946` edge `-0.0065` maxDD `-15.7972`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
