# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-22T13:52:28.012644+00:00`
- Price records: `672`
- Market context records: `7570`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `14496`

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

- `market_context_high->commodity_4h` score `0.2291` n `168` status `ready` deltaP `9.7204` edge `0.0303` maxDD `-2.4139`
- `market_context_high->index_1h` score `-0.1255` n `168` status `ready` deltaP `5.3893` edge `0.0072` maxDD `-1.7373`
- `market_context_high->commodity_24h` score `-0.224` n `153` status `ready` deltaP `12.4024` edge `0.057` maxDD `-7.0012`
- `market_context_high->commodity_1h` score `-0.2954` n `168` status `ready` deltaP `4.4402` edge `0.003` maxDD `-1.5775`
- `market_context_high->fx_1h` score `-0.4623` n `168` status `ready` deltaP `1.6517` edge `0.0004` maxDD `-0.6615`
- `market_context_high->index_4h` score `-0.4813` n `168` status `ready` deltaP `11.3751` edge `0.0351` maxDD `-3.4775`
- `market_context_high->metal_1h` score `-0.7974` n `168` status `ready` deltaP `-0.278` edge `0.01` maxDD `-1.4971`
- `market_context_high->fx_24h` score `-0.8288` n `153` status `ready` deltaP `8.9488` edge `0.0153` maxDD `-3.8554`
- `market_context_high->crypto_major_1h` score `-0.8313` n `168` status `ready` deltaP `4.4661` edge `0.0047` maxDD `-7.6171`
- `market_context_high->crypto_alt_1h` score `-0.8354` n `168` status `ready` deltaP `-0.7378` edge `0.0017` maxDD `-5.9775`
- `market_context_high->unknown_4h` score `-0.8709` n `168` status `ready` deltaP `10.2933` edge `0.0556` maxDD `-6.2031`
- `market_context_high->unknown_1h` score `-0.9852` n `168` status `ready` deltaP `1.4934` edge `-0.0297` maxDD `-1.3217`
- `market_context_high->unknown_24h` score `-1.3656` n `154` status `ready` deltaP `5.4631` edge `0.0634` maxDD `-9.9917`
- `market_context_high->equity_1h` score `-1.4828` n `168` status `ready` deltaP `3.7538` edge `0.0233` maxDD `-14.4075`
- `market_context_high->metal_4h` score `-1.4828` n `168` status `ready` deltaP `0.9582` edge `0.0517` maxDD `-4.8549`
- `market_context_high->crypto_alt_4h` score `-1.8045` n `168` status `ready` deltaP `0.1815` edge `0.0329` maxDD `-14.5695`
- `market_context_high->equity_4h` score `-1.8659` n `168` status `ready` deltaP `3.211` edge `0.2011` maxDD `-23.9375`
- `market_context_high->fx_4h` score `-2.0575` n `168` status `ready` deltaP `-0.7045` edge `0.0017` maxDD `-2.1439`
- `market_context_high->crypto_major_4h` score `-2.4923` n `168` status `ready` deltaP `4.5006` edge `0.0352` maxDD `-23.1116`
- `market_context_high->index_24h` score `-4.0095` n `153` status `ready` deltaP `-19.281` edge `-0.0025` maxDD `-15.9733`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
