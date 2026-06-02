# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-02T12:52:28.351676+00:00`
- Price records: `672`
- Market context records: `2664`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9230`

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

- `market_context_high->crypto_alt_24h` score `8.6073` n `114` status `ready` deltaP `15.0951` edge `0.966` maxDD `-19.9486`
- `market_context_high->unknown_24h` score `8.2979` n `114` status `ready` deltaP `17.2971` edge `0.609` maxDD `-1.626`
- `market_context_high->crypto_alt_4h` score `4.3283` n `121` status `ready` deltaP `22.4539` edge `0.4789` maxDD `-15.4319`
- `market_context_high->crypto_major_4h` score `2.6088` n `121` status `ready` deltaP `11.2049` edge `0.3237` maxDD `-10.1468`
- `market_context_high->unknown_4h` score `1.132` n `121` status `ready` deltaP `6.0459` edge `0.159` maxDD `-3.7312`
- `market_context_high->crypto_alt_1h` score `0.6865` n `133` status `ready` deltaP `8.4969` edge `0.1193` maxDD `-6.1656`
- `market_context_high->index_24h` score `0.0781` n `114` status `ready` deltaP `8.3973` edge `0.0486` maxDD `-2.5127`
- `market_context_high->crypto_major_1h` score `0.0515` n `133` status `ready` deltaP `5.6425` edge `0.0884` maxDD `-4.2199`
- `market_context_high->fx_24h` score `-0.18` n `114` status `ready` deltaP `10.2887` edge `0.0036` maxDD `-0.6418`
- `market_context_high->unknown_1h` score `-0.2319` n `133` status `ready` deltaP `2.3423` edge `0.023` maxDD `-1.9684`
- `market_context_high->index_4h` score `-0.2646` n `121` status `ready` deltaP `6.8245` edge `0.0166` maxDD `-2.3986`
- `market_context_high->commodity_1h` score `-0.2854` n `133` status `ready` deltaP `4.132` edge `0.0112` maxDD `-4.3601`
- `market_context_high->index_1h` score `-0.3331` n `133` status `ready` deltaP `2.0463` edge `0.008` maxDD `-1.2855`
- `market_context_high->fx_1h` score `-0.5523` n `133` status `ready` deltaP `-0.8183` edge `0.0038` maxDD `-0.2164`
- `market_context_high->metal_1h` score `-0.568` n `133` status `ready` deltaP `-0.6787` edge `0.0011` maxDD `-1.8854`
- `market_context_high->fx_4h` score `-0.5736` n `121` status `ready` deltaP `0.6702` edge `0.0131` maxDD `-0.5631`
- `market_context_high->metal_4h` score `-0.6493` n `121` status `ready` deltaP `2.2022` edge `0.014` maxDD `-2.6233`
- `market_context_high->commodity_24h` score `-1.1783` n `114` status `ready` deltaP `6.3505` edge `0.157` maxDD `-15.699`
- `market_context_high->commodity_4h` score `-1.2187` n `121` status `ready` deltaP `3.326` edge `0.0136` maxDD `-10.0279`
- `market_context_high->equity_1h` score `-1.3699` n `133` status `ready` deltaP `-5.5952` edge `0.007` maxDD `-2.7085`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
