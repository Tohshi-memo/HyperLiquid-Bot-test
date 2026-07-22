# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-22T18:22:33.759998+00:00`
- Price records: `672`
- Market context records: `7590`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `14550`

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

- `market_context_high->commodity_24h` score `0.1103` n `145` status `ready` deltaP `13.9866` edge `0.0743` maxDD `-7.0012`
- `market_context_high->commodity_4h` score `0.0463` n `153` status `ready` deltaP `8.6047` edge `0.0225` maxDD `-2.4139`
- `market_context_high->index_1h` score `0.0077` n `153` status `ready` deltaP `5.7941` edge `0.0112` maxDD `-0.9072`
- `market_context_high->unknown_24h` score `-0.0466` n `146` status `ready` deltaP `10.9042` edge `0.0993` maxDD `-7.2371`
- `market_context_high->commodity_1h` score `-0.2517` n `153` status `ready` deltaP `5.0167` edge `0.0028` maxDD `-1.5775`
- `market_context_high->fx_24h` score `-0.3568` n `145` status `ready` deltaP `9.2803` edge `0.0174` maxDD `-3.0537`
- `market_context_high->crypto_alt_1h` score `-0.4621` n `153` status `ready` deltaP `0.4765` edge `0.0122` maxDD `-3.6359`
- `market_context_high->crypto_major_1h` score `-0.4778` n `153` status `ready` deltaP `6.2639` edge `0.0122` maxDD `-5.5504`
- `market_context_high->metal_1h` score `-0.6052` n `153` status `ready` deltaP `1.6594` edge `0.0159` maxDD `-1.0307`
- `market_context_high->index_4h` score `-0.6397` n `153` status `ready` deltaP `9.1983` edge `0.0293` maxDD `-3.4775`
- `market_context_high->equity_1h` score `-0.6471` n `153` status `ready` deltaP `5.5909` edge `0.0493` maxDD `-8.8965`
- `market_context_high->fx_1h` score `-0.6778` n `153` status `ready` deltaP `-0.7419` edge `-0.0016` maxDD `-0.6615`
- `market_context_high->unknown_1h` score `-0.9594` n `153` status `ready` deltaP `0.0675` edge `-0.0611` maxDD `-1.3217`
- `market_context_high->crypto_alt_4h` score `-1.2131` n `153` status `ready` deltaP `1.3291` edge `0.0454` maxDD `-10.1158`
- `market_context_high->crypto_major_4h` score `-1.5639` n `153` status `ready` deltaP `6.5578` edge `0.0533` maxDD `-16.468`
- `market_context_high->metal_4h` score `-1.6899` n `153` status `ready` deltaP `-1.8094` edge `0.0436` maxDD `-4.8549`
- `market_context_high->equity_4h` score `-1.7691` n `153` status `ready` deltaP `1.9668` edge `0.1968` maxDD `-21.9375`
- `market_context_high->equity_24h` score `-1.8971` n `145` status `ready` deltaP `16.9771` edge `0.4735` maxDD `-59.725`
- `market_context_high->fx_4h` score `-2.3612` n `153` status `ready` deltaP `-3.7657` edge `-0.0032` maxDD `-2.1439`
- `market_context_high->unknown_4h` score `-2.6227` n `153` status `ready` deltaP `11.152` edge `-0.1897` maxDD `-5.0044`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
