# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-08T12:37:28.232658+00:00`
- Price records: `672`
- Market context records: `6087`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11095`

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

- `news_risk_high->fx_24h` score `8.1582` n `30` status `ready` deltaP `72.7431` edge `0.1949` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `5.966` n `30` status `ready` deltaP `32.2222` edge `0.2971` maxDD `-0.5131`
- `news_risk_high->fx_4h` score `4.3005` n `32` status `ready` deltaP `44.7409` edge `0.0647` maxDD `-0.0345`
- `news_risk_high->fx_1h` score `2.4195` n `32` status `ready` deltaP `29.0419` edge `0.0219` maxDD `-0.1113`
- `market_context_high->equity_4h` score `2.0265` n `199` status `ready` deltaP `10.4991` edge `0.1906` maxDD `-2.671`
- `news_risk_high->crypto_major_1h` score `1.1178` n `32` status `ready` deltaP `12.9304` edge `0.1038` maxDD `-2.0691`
- `news_risk_high->crypto_alt_1h` score `0.587` n `32` status `ready` deltaP `8.6265` edge `0.0639` maxDD `-1.6923`
- `news_risk_high->commodity_24h` score `0.491` n `30` status `ready` deltaP `18.2639` edge `-0.0603` maxDD `-0.3101`
- `news_risk_high->index_24h` score `0.1086` n `30` status `ready` deltaP `9.2361` edge `0.0395` maxDD `-2.3058`
- `market_context_high->fx_1h` score `-0.2551` n `199` status `ready` deltaP `1.7806` edge `0.0` maxDD `-0.5659`
- `market_context_high->metal_1h` score `-0.3289` n `199` status `ready` deltaP `4.3353` edge `0.0088` maxDD `-2.0564`
- `market_context_high->equity_1h` score `-0.4013` n `199` status `ready` deltaP `2.7744` edge `0.0416` maxDD `-4.2573`
- `market_context_high->index_4h` score `-0.6918` n `199` status `ready` deltaP `4.04` edge `0.0308` maxDD `-1.381`
- `market_context_high->metal_4h` score `-0.6975` n `199` status `ready` deltaP `5.1186` edge `0.0265` maxDD `-3.4996`
- `market_context_high->commodity_1h` score `-0.7103` n `199` status `ready` deltaP `-1.5986` edge `-0.0039` maxDD `-0.5708`
- `news_risk_high->metal_1h` score `-0.7318` n `32` status `ready` deltaP `-1.9461` edge `-0.0311` maxDD `-1.6464`
- `market_context_high->crypto_alt_1h` score `-0.7883` n `199` status `ready` deltaP `4.5279` edge `0.044` maxDD `-9.3536`
- `market_context_high->crypto_major_1h` score `-0.8529` n `199` status `ready` deltaP `4.5918` edge `0.0368` maxDD `-9.807`
- `news_risk_high->index_1h` score `-1.0182` n `32` status `ready` deltaP `-8.4768` edge `-0.0177` maxDD `-1.1725`
- `market_context_high->index_1h` score `-1.0896` n `199` status `ready` deltaP `-1.3631` edge `0.0052` maxDD `-0.9531`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
