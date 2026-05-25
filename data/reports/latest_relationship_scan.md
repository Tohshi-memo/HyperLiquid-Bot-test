# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-25T03:07:17.178825+00:00`
- Price records: `672`
- Market context records: `1803`
- Flow alert records: `7087`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8872`

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

- `market_context_high->metal_24h` score `6.924` n `184` status `ready` deltaP `28.1401` edge `0.632` maxDD `-12.7414`
- `news_risk_high->commodity_4h` score `6.4824` n `30` status `ready` deltaP `29.4106` edge `0.4096` maxDD `-3.5713`
- `market_context_high->crypto_alt_4h` score `6.4177` n `189` status `ready` deltaP `21.9488` edge `0.5277` maxDD `-7.1373`
- `market_context_high->crypto_major_4h` score `5.4916` n `189` status `ready` deltaP `25.0879` edge `0.4727` maxDD `-7.5853`
- `market_context_high->unknown_4h` score `4.2309` n `189` status `ready` deltaP `16.7119` edge `0.4568` maxDD `-10.2508`
- `news_risk_high->commodity_1h` score `3.2374` n `30` status `ready` deltaP `24.5709` edge `0.1377` maxDD `-1.2043`
- `market_context_high->index_24h` score `3.1069` n `184` status `ready` deltaP `15.157` edge `0.2807` maxDD `-4.1604`
- `market_context_high->equity_4h` score `2.9701` n `189` status `ready` deltaP `16.4344` edge `0.2474` maxDD `-5.0894`
- `market_context_high->equity_24h` score `2.2355` n `184` status `ready` deltaP `17.3158` edge `0.5607` maxDD `-33.1875`
- `market_context_high->unknown_24h` score `1.4991` n `184` status `ready` deltaP `12.0849` edge `0.5764` maxDD `-35.8966`
- `news_risk_high->fx_4h` score `0.9026` n `30` status `ready` deltaP `21.6362` edge `-0.0013` maxDD `-0.1774`
- `market_context_high->index_4h` score `0.8729` n `189` status `ready` deltaP `12.3807` edge `0.0991` maxDD `-3.7119`
- `market_context_high->crypto_major_1h` score `0.4346` n `189` status `ready` deltaP `6.335` edge `0.0926` maxDD `-3.2225`
- `news_risk_high->unknown_4h` score `0.3508` n `30` status `ready` deltaP `9.6748` edge `0.0528` maxDD `-2.7857`
- `market_context_high->crypto_alt_1h` score `0.3065` n `189` status `ready` deltaP `6.7944` edge `0.0914` maxDD `-4.8924`
- `market_context_high->equity_1h` score `-0.1537` n `189` status `ready` deltaP `3.9707` edge `0.0401` maxDD `-2.6836`
- `market_context_high->index_1h` score `-0.3974` n `189` status `ready` deltaP `2.2131` edge `0.0153` maxDD `-1.7205`
- `market_context_high->fx_24h` score `-0.454` n `184` status `ready` deltaP `8.7863` edge `0.0085` maxDD `-1.3925`
- `news_risk_high->fx_1h` score `-0.471` n `30` status `ready` deltaP `-5.1297` edge `0.0` maxDD `-0.0948`
- `news_risk_high->unknown_1h` score `-0.4808` n `30` status `ready` deltaP `16.4072` edge `-0.1238` maxDD `-2.1115`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
