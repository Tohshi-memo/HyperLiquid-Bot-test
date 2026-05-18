# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-18T10:22:30.465844+00:00`
- Price records: `672`
- Market context records: `1108`
- Flow alert records: `5094`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8686`

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

- `market_context_high->crypto_major_24h` score `17.6346` n `150` status `ready` deltaP `38.25` edge `1.2609` maxDD `-3.3749`
- `market_context_high->crypto_alt_24h` score `7.1737` n `150` status `ready` deltaP `14.6111` edge `0.6238` maxDD `-9.5387`
- `market_context_high->equity_24h` score `6.2519` n `150` status `ready` deltaP `15.6527` edge `0.4663` maxDD `-3.6396`
- `market_context_high->metal_24h` score `5.3995` n `150` status `ready` deltaP `-2.5833` edge `0.6339` maxDD `-6.3373`
- `market_context_high->index_24h` score `4.9893` n `150` status `ready` deltaP `15.1319` edge `0.3457` maxDD `-2.1308`
- `market_context_high->equity_4h` score `1.7408` n `168` status `ready` deltaP `10.1844` edge `0.1435` maxDD `-3.6396`
- `market_context_high->index_4h` score `0.9299` n `168` status `ready` deltaP `8.5946` edge `0.0885` maxDD `-2.1308`
- `market_context_high->index_1h` score `0.4666` n `168` status `ready` deltaP `7.4957` edge `0.0206` maxDD `-0.5353`
- `market_context_high->equity_1h` score `0.2764` n `168` status `ready` deltaP `2.7302` edge `0.0426` maxDD `-1.3546`
- `market_context_high->fx_1h` score `0.1232` n `168` status `ready` deltaP `8.1658` edge `0.0014` maxDD `-0.3124`
- `market_context_high->crypto_major_1h` score `0.1137` n `168` status `ready` deltaP `7.4316` edge `0.0365` maxDD `-4.1256`
- `market_context_high->crypto_major_4h` score `0.0496` n `168` status `ready` deltaP `8.4567` edge `0.1421` maxDD `-8.3693`
- `market_context_high->metal_1h` score `-0.1968` n `168` status `ready` deltaP `6.9504` edge `-0.0017` maxDD `-2.2164`
- `market_context_high->crypto_alt_1h` score `-0.2094` n `168` status `ready` deltaP `3.2435` edge `0.0452` maxDD `-3.4088`
- `market_context_high->fx_4h` score `-0.6787` n `168` status `ready` deltaP `1.6986` edge `0.0013` maxDD `-1.6381`
- `market_context_high->commodity_1h` score `-0.7154` n `168` status `ready` deltaP `-1.4756` edge `-0.0011` maxDD `-3.7959`
- `market_context_high->crypto_alt_4h` score `-1.0357` n `168` status `ready` deltaP `5.3862` edge `0.1278` maxDD `-16.7194`
- `market_context_high->metal_4h` score `-2.3475` n `168` status `ready` deltaP `6.8525` edge `-0.0459` maxDD `-9.2991`
- `market_context_high->commodity_4h` score `-3.1298` n `168` status `ready` deltaP `-10.6635` edge `-0.0134` maxDD `-13.0076`
- `market_context_high->fx_24h` score `-3.3134` n `150` status `ready` deltaP `1.5208` edge `-0.0273` maxDD `-19.2774`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
