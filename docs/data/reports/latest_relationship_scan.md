# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-01T19:02:25.052269+00:00`
- Price records: `672`
- Market context records: `2588`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9200`

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

- `market_context_high->unknown_24h` score `7.6656` n `131` status `ready` deltaP `18.094` edge `0.551` maxDD `-1.626`
- `market_context_high->crypto_alt_4h` score `5.9077` n `146` status `ready` deltaP `26.4158` edge `0.5841` maxDD `-15.4319`
- `market_context_high->crypto_major_4h` score `4.1374` n `146` status `ready` deltaP `17.2026` edge `0.4111` maxDD `-10.1468`
- `market_context_high->crypto_alt_24h` score `1.8918` n `131` status `ready` deltaP `3.5067` edge `0.7721` maxDD `-39.0265`
- `market_context_high->crypto_alt_1h` score `1.4731` n `146` status `ready` deltaP `12.0294` edge `0.1613` maxDD `-6.1656`
- `market_context_high->unknown_4h` score `1.0579` n `146` status `ready` deltaP `8.5992` edge `0.1358` maxDD `-3.7312`
- `market_context_high->index_24h` score `0.8943` n `131` status `ready` deltaP `8.6249` edge `0.1151` maxDD `-2.5127`
- `market_context_high->crypto_major_1h` score `0.8851` n `146` status `ready` deltaP `9.7613` edge `0.1281` maxDD `-4.2199`
- `market_context_high->equity_24h` score `0.3381` n `131` status `ready` deltaP `17.1596` edge `-0.0192` maxDD `-2.3615`
- `market_context_high->index_4h` score `0.286` n `146` status `ready` deltaP `9.4325` edge `0.0451` maxDD `-2.3986`
- `market_context_high->index_1h` score `-0.1875` n `146` status `ready` deltaP `3.642` edge `0.0095` maxDD `-1.2855`
- `market_context_high->unknown_1h` score `-0.4092` n `146` status `ready` deltaP `1.8005` edge `0.0202` maxDD `-2.6375`
- `market_context_high->crypto_major_24h` score `-0.4207` n `131` status `ready` deltaP `6.0366` edge `0.4409` maxDD `-29.9631`
- `market_context_high->commodity_1h` score `-0.465` n `146` status `ready` deltaP `5.0529` edge `0.0154` maxDD `-4.3601`
- `market_context_high->metal_4h` score `-0.5818` n `146` status `ready` deltaP `4.9594` edge `0.0572` maxDD `-4.7664`
- `market_context_high->metal_1h` score `-0.6344` n `146` status `ready` deltaP `1.1115` edge `0.0145` maxDD `-2.9823`
- `market_context_high->fx_1h` score `-0.7251` n `146` status `ready` deltaP `-1.5831` edge `0.0036` maxDD `-0.278`
- `market_context_high->equity_1h` score `-0.8912` n `146` status `ready` deltaP `-0.8264` edge `0.0151` maxDD `-2.7085`
- `market_context_high->fx_4h` score `-0.912` n `146` status `ready` deltaP `-0.378` edge `0.0123` maxDD `-0.8621`
- `market_context_high->fx_24h` score `-0.9412` n `131` status `ready` deltaP `3.019` edge `0.0008` maxDD `-1.6157`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
