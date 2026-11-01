# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-01T05:07:36.315599+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `6373`

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

- `market_context_high->unknown_24h` score `6013.4628` n `62` status `ready` deltaP `0.5432` edge `501.1268` maxDD `-0.3486`
- `market_context_high->unknown_4h` score `302.4839` n `62` status `ready` deltaP `5.5517` edge `25.1743` maxDD `-0.0124`
- `news_risk_high->unknown_1h` score `81.646` n `108` status `ready` deltaP `-5.1951` edge `6.8671` maxDD `-0.9571`
- `market_context_high->unknown_1h` score `19.4826` n `62` status `ready` deltaP `3.646` edge `1.6103` maxDD `-0.2178`
- `market_context_high->equity_24h` score `18.6262` n `62` status `ready` deltaP `36.7496` edge `1.3698` maxDD `-2.6757`
- `news_risk_high->crypto_alt_24h` score `13.4997` n `98` status `ready` deltaP `32.0685` edge `1.0468` maxDD `-6.8493`
- `market_context_high->index_24h` score `6.5029` n `62` status `ready` deltaP `55.4044` edge `0.1862` maxDD `-0.0926`
- `news_risk_high->crypto_alt_4h` score `5.2027` n `108` status `ready` deltaP `19.6646` edge `0.4411` maxDD `-7.4246`
- `market_context_high->commodity_24h` score `2.91` n `62` status `ready` deltaP `37.3879` edge `0.2038` maxDD `-4.0649`
- `market_context_high->commodity_4h` score `2.7738` n `62` status `ready` deltaP `26.6325` edge `0.087` maxDD `-0.3387`
- `market_context_high->crypto_major_4h` score `2.4663` n `62` status `ready` deltaP `21.9069` edge `0.1691` maxDD `-6.1029`
- `market_context_high->crypto_alt_24h` score `1.9662` n `62` status `ready` deltaP `-8.4845` edge `0.3722` maxDD `-8.8096`
- `market_context_high->crypto_major_24h` score `1.5655` n `62` status `ready` deltaP `6.1044` edge `0.2452` maxDD `-4.4817`
- `market_context_high->equity_4h` score `1.4871` n `62` status `ready` deltaP `0.6983` edge `0.2562` maxDD `-2.283`
- `market_context_high->crypto_alt_4h` score `1.4631` n `62` status `ready` deltaP `15.6323` edge `0.2143` maxDD `-7.8087`
- `market_context_high->metal_4h` score `1.3329` n `62` status `ready` deltaP `16.1044` edge `0.0462` maxDD `-0.7323`
- `news_risk_high->crypto_alt_1h` score `0.7953` n `108` status `ready` deltaP `8.5773` edge `0.1045` maxDD `-3.9659`
- `market_context_high->metal_1h` score `0.6868` n `62` status `ready` deltaP `8.9965` edge `0.0221` maxDD `-0.3209`
- `market_context_high->fx_1h` score `0.5473` n `62` status `ready` deltaP `13.3185` edge `-0.0002` maxDD `-0.1407`
- `market_context_high->equity_1h` score `0.2751` n `62` status `ready` deltaP `-2.9264` edge `0.1309` maxDD `-2.0894`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
