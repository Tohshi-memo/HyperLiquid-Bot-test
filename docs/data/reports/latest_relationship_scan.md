# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-09T01:07:29.689046+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `8733`

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

- `market_context_high->equity_24h` score `3.18` n `103` status `ready` deltaP `4.5729` edge `0.5405` maxDD `-21.1456`
- `market_context_high->metal_24h` score `2.5571` n `103` status `ready` deltaP `12.7326` edge `0.1858` maxDD `-2.2743`
- `market_context_high->commodity_4h` score `1.4084` n `118` status `ready` deltaP `13.6446` edge `0.0937` maxDD `-2.7169`
- `market_context_high->fx_24h` score `0.8513` n `103` status `ready` deltaP `22.0958` edge `0.0485` maxDD `-1.9329`
- `market_context_high->commodity_1h` score `0.8312` n `130` status `ready` deltaP `10.1497` edge `0.0359` maxDD `-0.7439`
- `market_context_high->index_24h` score `0.4752` n `103` status `ready` deltaP `9.1002` edge `0.1534` maxDD `-5.9181`
- `market_context_high->fx_1h` score `-0.3749` n `130` status `ready` deltaP `3.3763` edge `-0.0042` maxDD `-0.9639`
- `market_context_high->fx_4h` score `-0.5744` n `118` status `ready` deltaP `4.6585` edge `-0.0036` maxDD `-1.6928`
- `market_context_high->metal_1h` score `-0.5859` n `130` status `ready` deltaP `-2.8696` edge `-0.0064` maxDD `-0.9664`
- `market_context_high->index_4h` score `-0.6023` n `118` status `ready` deltaP `-0.5865` edge `-0.0128` maxDD `-1.1743`
- `market_context_high->index_1h` score `-0.7788` n `130` status `ready` deltaP `-2.8903` edge `-0.0067` maxDD `-0.7809`
- `market_context_high->equity_1h` score `-0.8165` n `130` status `ready` deltaP `1.1423` edge `0.0072` maxDD `-4.6286`
- `market_context_high->metal_4h` score `-1.0741` n `118` status `ready` deltaP `-3.0927` edge `-0.0162` maxDD `-2.7373`
- `market_context_high->crypto_alt_1h` score `-2.1055` n `130` status `ready` deltaP `-11.6513` edge `-0.0336` maxDD `-2.4677`
- `market_context_high->equity_4h` score `-2.2397` n `118` status `ready` deltaP `1.8577` edge `-0.0653` maxDD `-7.6983`
- `market_context_high->crypto_major_1h` score `-2.9951` n `130` status `ready` deltaP `-9.5969` edge `-0.0644` maxDD `-6.3636`
- `market_context_high->crypto_major_24h` score `-3.7231` n `103` status `ready` deltaP `6.2197` edge `-0.1023` maxDD `-14.2873`
- `market_context_high->crypto_alt_24h` score `-4.4638` n `103` status `ready` deltaP `-12.4461` edge `-0.1447` maxDD `-4.5445`
- `market_context_high->crypto_alt_4h` score `-4.6728` n `118` status `ready` deltaP `-12.7067` edge `-0.1395` maxDD `-6.5487`
- `market_context_high->unknown_1h` score `-8.2253` n `130` status `ready` deltaP `-4.8941` edge `-0.6081` maxDD `-1.2437`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
