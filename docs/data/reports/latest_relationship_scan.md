# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-06T21:37:24.117699+00:00`
- Price records: `672`
- Market context records: `3114`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `7023`

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

- `market_context_high->commodity_24h` score `14.6592` n `93` status `ready` deltaP `46.399` edge `0.9551` maxDD `-2.0927`
- `market_context_high->crypto_alt_24h` score `13.8852` n `93` status `ready` deltaP `11.772` edge `2.4182` maxDD `-48.6557`
- `market_context_high->unknown_24h` score `13.2524` n `93` status `ready` deltaP `22.7654` edge `1.0014` maxDD `-1.9039`
- `market_context_high->index_24h` score `10.4014` n `93` status `ready` deltaP `32.975` edge `0.9024` maxDD `-16.1026`
- `market_context_high->equity_24h` score `5.8998` n `93` status `ready` deltaP `14.3593` edge `1.3379` maxDD `-44.846`
- `market_context_high->commodity_4h` score `2.9906` n `120` status `ready` deltaP `17.9878` edge `0.1751` maxDD `-1.9973`
- `market_context_high->commodity_1h` score `0.0306` n `131` status `ready` deltaP `2.5518` edge `0.0278` maxDD `-1.7142`
- `market_context_high->index_1h` score `-0.4056` n `131` status `ready` deltaP `5.0818` edge `0.0204` maxDD `-4.5023`
- `market_context_high->fx_24h` score `-0.5716` n `93` status `ready` deltaP `3.8138` edge `-0.0003` maxDD `-0.4876`
- `market_context_high->crypto_alt_1h` score `-0.7617` n `131` status `ready` deltaP `3.3905` edge `0.0927` maxDD `-14.7034`
- `market_context_high->equity_1h` score `-1.0237` n `131` status `ready` deltaP `0.9953` edge `0.0107` maxDD `-8.8863`
- `market_context_high->fx_4h` score `-1.3454` n `120` status `ready` deltaP `-12.7235` edge `-0.0033` maxDD `-1.0829`
- `market_context_high->index_4h` score `-1.432` n `120` status `ready` deltaP `9.4817` edge `0.0441` maxDD `-17.6057`
- `market_context_high->fx_1h` score `-1.5199` n `131` status `ready` deltaP `-10.0208` edge `-0.0054` maxDD `-0.6895`
- `market_context_high->unknown_4h` score `-2.0346` n `120` status `ready` deltaP `4.1362` edge `0.0046` maxDD `-13.8046`
- `market_context_high->crypto_major_1h` score `-2.0739` n `131` status `ready` deltaP `-0.3657` edge `0.0559` maxDD `-15.1032`
- `market_context_high->metal_1h` score `-2.2743` n `131` status `ready` deltaP `-6.2634` edge `-0.0084` maxDD `-7.4828`
- `market_context_high->unknown_1h` score `-2.8132` n `131` status `ready` deltaP `2.5963` edge `-0.0491` maxDD `-14.2111`
- `market_context_high->crypto_alt_4h` score `-3.9698` n `120` status `ready` deltaP `11.9004` edge `0.2162` maxDD `-58.6918`
- `market_context_high->equity_4h` score `-4.0672` n `120` status `ready` deltaP `5.9146` edge `-0.0303` maxDD `-36.7784`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
