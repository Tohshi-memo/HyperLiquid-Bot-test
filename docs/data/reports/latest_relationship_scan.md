# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-25T09:37:28.787094+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `7880`

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

- `market_context_high->unknown_4h` score `38.2171` n `110` status `ready` deltaP `-0.6458` edge `3.2226` maxDD `-1.016`
- `market_context_high->unknown_1h` score `3.9984` n `114` status `ready` deltaP `4.3334` edge `0.3532` maxDD `-1.5781`
- `market_context_high->crypto_alt_24h` score `0.9463` n `45` status `ready` deltaP `13.9583` edge `0.2631` maxDD `-15.4532`
- `market_context_high->commodity_24h` score `0.945` n `45` status `ready` deltaP `19.0278` edge `0.0852` maxDD `-3.6055`
- `market_context_high->crypto_major_24h` score `0.351` n `45` status `ready` deltaP `5.8333` edge `0.0963` maxDD `-5.8084`
- `market_context_high->fx_4h` score `0.0141` n `110` status `ready` deltaP `7.8992` edge `0.009` maxDD `-0.4545`
- `market_context_high->fx_1h` score `-0.0736` n `114` status `ready` deltaP `3.4011` edge `0.0028` maxDD `-0.1258`
- `market_context_high->commodity_1h` score `-0.4835` n `114` status `ready` deltaP `0.0867` edge `0.0092` maxDD `-1.0053`
- `market_context_high->metal_1h` score `-0.558` n `114` status `ready` deltaP `5.5179` edge `-0.0041` maxDD `-1.6682`
- `market_context_high->index_1h` score `-0.6285` n `114` status `ready` deltaP `-1.5417` edge `-0.0051` maxDD `-1.2155`
- `market_context_high->fx_24h` score `-0.8139` n `45` status `ready` deltaP `1.0764` edge `0.0066` maxDD `-1.1167`
- `market_context_high->commodity_4h` score `-0.8591` n `110` status `ready` deltaP `-2.766` edge `0.0312` maxDD `-1.165`
- `market_context_high->crypto_major_1h` score `-1.3273` n `114` status `ready` deltaP `2.1615` edge `-0.0265` maxDD `-9.3126`
- `market_context_high->metal_4h` score `-1.8961` n `110` status `ready` deltaP `4.77` edge `-0.0188` maxDD `-5.3474`
- `market_context_high->index_4h` score `-2.0952` n `110` status `ready` deltaP `-6.6574` edge `-0.0368` maxDD `-4.3282`
- `market_context_high->crypto_alt_1h` score `-2.9775` n `114` status `ready` deltaP `-1.5207` edge `-0.0506` maxDD `-11.3243`
- `market_context_high->metal_24h` score `-3.0564` n `45` status `ready` deltaP `-7.743` edge `-0.0133` maxDD `-6.8492`
- `market_context_high->equity_1h` score `-3.7132` n `114` status `ready` deltaP `0.4044` edge `-0.0848` maxDD `-12.1865`
- `market_context_high->index_24h` score `-5.1455` n `45` status `ready` deltaP `-19.1319` edge `-0.1711` maxDD `-5.078`
- `market_context_high->crypto_major_4h` score `-9.8013` n `110` status `ready` deltaP `-11.8016` edge `-0.2384` maxDD `-33.3092`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
