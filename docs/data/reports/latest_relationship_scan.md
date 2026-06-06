# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-06T23:37:22.424747+00:00`
- Price records: `672`
- Market context records: `3124`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `7027`

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

- `market_context_high->commodity_24h` score `14.4517` n `101` status `ready` deltaP `47.1655` edge `0.9327` maxDD `-2.0927`
- `market_context_high->unknown_24h` score `12.0714` n `101` status `ready` deltaP `21.2029` edge `0.9134` maxDD `-1.9039`
- `market_context_high->crypto_alt_24h` score `11.5574` n `101` status `ready` deltaP `10.4322` edge `2.3264` maxDD `-64.4722`
- `market_context_high->index_24h` score `6.6158` n `101` status `ready` deltaP `32.314` edge `0.8882` maxDD `-16.1026`
- `market_context_high->equity_24h` score `4.6525` n `101` status `ready` deltaP `11.9156` edge `1.3149` maxDD `-51.8289`
- `market_context_high->commodity_4h` score `3.0379` n `127` status `ready` deltaP `18.9085` edge `0.1729` maxDD `-1.9973`
- `market_context_high->commodity_1h` score `-0.0367` n `139` status `ready` deltaP `2.0107` edge `0.0258` maxDD `-1.7142`
- `market_context_high->index_1h` score `-0.4479` n `139` status `ready` deltaP `4.4641` edge `0.0191` maxDD `-4.5023`
- `market_context_high->fx_24h` score `-0.5164` n `101` status `ready` deltaP `4.6393` edge `-0.0012` maxDD `-0.4876`
- `market_context_high->crypto_alt_1h` score `-0.7082` n `139` status `ready` deltaP `3.7447` edge `0.0972` maxDD `-14.7034`
- `market_context_high->equity_1h` score `-0.9928` n `139` status `ready` deltaP `1.2288` edge `0.0131` maxDD `-8.8863`
- `market_context_high->fx_1h` score `-1.1521` n `139` status `ready` deltaP `-11.0929` edge `-0.0057` maxDD `-0.7779`
- `market_context_high->crypto_major_1h` score `-1.2726` n `139` status `ready` deltaP `0.5008` edge `0.0598` maxDD `-15.1032`
- `market_context_high->index_4h` score `-1.2864` n `127` status `ready` deltaP `11.3669` edge `0.0502` maxDD `-17.6057`
- `market_context_high->fx_4h` score `-1.4452` n `127` status `ready` deltaP `-13.9823` edge `-0.0077` maxDD `-1.0829`
- `market_context_high->metal_1h` score `-2.21` n `139` status `ready` deltaP `-5.82` edge `-0.006` maxDD `-7.4828`
- `market_context_high->unknown_4h` score `-2.2263` n `127` status `ready` deltaP `2.1449` edge `0.0224` maxDD `-14.7778`
- `market_context_high->unknown_1h` score `-3.0302` n `139` status `ready` deltaP `1.7738` edge `-0.0617` maxDD `-14.2111`
- `market_context_high->crypto_alt_4h` score `-3.5855` n `127` status `ready` deltaP `14.5957` edge `0.2475` maxDD `-58.6918`
- `market_context_high->equity_4h` score `-3.737` n `127` status `ready` deltaP `8.3949` edge `-0.0045` maxDD `-36.7784`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
