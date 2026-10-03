# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-03T02:22:27.015204+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4818`

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

- `market_context_high->unknown_1h` score `364.8958` n `50` status `ready` deltaP `10.5749` edge `30.3424` maxDD `-0.0597`
- `market_context_high->unknown_4h` score `293.1899` n `50` status `ready` deltaP `10.2134` edge `24.3644` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `13.9738` n `70` status `ready` deltaP `30.4265` edge `1.0329` maxDD `-3.3673`
- `market_context_high->crypto_alt_24h` score `10.9579` n `50` status `ready` deltaP `21.5694` edge `0.9397` maxDD `-11.6271`
- `news_risk_high->equity_24h` score `10.0898` n `70` status `ready` deltaP `33.7351` edge `0.6644` maxDD `-2.8784`
- `market_context_high->crypto_major_24h` score `8.8906` n `50` status `ready` deltaP `31.3056` edge `0.6738` maxDD `-9.3299`
- `news_risk_high->crypto_alt_4h` score `7.8986` n `100` status `ready` deltaP `32.8841` edge `0.5734` maxDD `-6.4195`
- `market_context_high->crypto_major_4h` score `7.3969` n `50` status `ready` deltaP `17.5427` edge `0.5698` maxDD `-3.294`
- `news_risk_high->crypto_major_24h` score `6.9344` n `70` status `ready` deltaP `12.1627` edge `0.6053` maxDD `-4.6813`
- `news_risk_high->crypto_major_4h` score `6.2246` n `100` status `ready` deltaP `24.5427` edge `0.4287` maxDD `-3.2217`
- `market_context_high->crypto_alt_4h` score `5.8138` n `50` status `ready` deltaP `15.8841` edge `0.5075` maxDD `-7.6465`
- `news_risk_high->equity_4h` score `3.222` n `100` status `ready` deltaP `26.5305` edge `0.1529` maxDD `-2.9013`
- `market_context_high->crypto_alt_1h` score `3.2074` n `50` status `ready` deltaP `14.6527` edge `0.2359` maxDD `-3.6376`
- `market_context_high->crypto_major_1h` score `2.9941` n `50` status `ready` deltaP `13.4012` edge `0.2052` maxDD `-2.2692`
- `market_context_high->fx_4h` score `2.7909` n `50` status `ready` deltaP `31.1646` edge `0.0383` maxDD `-0.0791`
- `news_risk_high->index_24h` score `2.2256` n `70` status `ready` deltaP `21.746` edge `0.0772` maxDD `-0.2696`
- `news_risk_high->metal_24h` score `1.7906` n `70` status `ready` deltaP `9.6329` edge `0.1981` maxDD `-2.0483`
- `news_risk_high->crypto_alt_1h` score `1.5882` n `100` status `ready` deltaP `6.6527` edge `0.1399` maxDD `-2.4854`
- `market_context_high->fx_1h` score `1.4352` n `50` status `ready` deltaP `20.1916` edge `0.0114` maxDD `-0.113`
- `market_context_high->equity_24h` score `1.2242` n `50` status `ready` deltaP `6.0208` edge `0.303` maxDD `-11.8957`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
