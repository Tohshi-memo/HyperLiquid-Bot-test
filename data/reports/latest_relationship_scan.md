# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-01T19:07:28.637169+00:00`
- Price records: `672`
- Market context records: `2589`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9200`

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

- `market_context_high->unknown_24h` score `7.6788` n `131` status `ready` deltaP `18.094` edge `0.5521` maxDD `-1.626`
- `market_context_high->crypto_alt_4h` score `5.9077` n `146` status `ready` deltaP `26.4158` edge `0.5841` maxDD `-15.4319`
- `market_context_high->crypto_major_4h` score `4.1362` n `146` status `ready` deltaP `17.2026` edge `0.411` maxDD `-10.1468`
- `market_context_high->crypto_alt_24h` score `1.893` n `131` status `ready` deltaP `3.5067` edge `0.7722` maxDD `-39.0265`
- `market_context_high->crypto_alt_1h` score `1.4719` n `146` status `ready` deltaP `12.0294` edge `0.1612` maxDD `-6.1656`
- `market_context_high->unknown_4h` score `1.0567` n `146` status `ready` deltaP `8.5992` edge `0.1357` maxDD `-3.7312`
- `market_context_high->index_24h` score `0.8943` n `131` status `ready` deltaP `8.6249` edge `0.1151` maxDD `-2.5127`
- `market_context_high->crypto_major_1h` score `0.8839` n `146` status `ready` deltaP `9.7613` edge `0.128` maxDD `-4.2199`
- `market_context_high->equity_24h` score `0.3309` n `131` status `ready` deltaP `17.1596` edge `-0.0198` maxDD `-2.3615`
- `market_context_high->index_4h` score `0.286` n `146` status `ready` deltaP `9.4325` edge `0.0451` maxDD `-2.3986`
- `market_context_high->index_1h` score `-0.1887` n `146` status `ready` deltaP `3.642` edge `0.0094` maxDD `-1.2855`
- `market_context_high->unknown_1h` score `-0.4104` n `146` status `ready` deltaP `1.8005` edge `0.0201` maxDD `-2.6375`
- `market_context_high->crypto_major_24h` score `-0.4123` n `131` status `ready` deltaP `6.0366` edge `0.4411` maxDD `-29.9226`
- `market_context_high->commodity_1h` score `-0.4662` n `146` status `ready` deltaP `5.0529` edge `0.0153` maxDD `-4.3601`
- `market_context_high->metal_4h` score `-0.5806` n `146` status `ready` deltaP `4.9594` edge `0.0573` maxDD `-4.7664`
- `market_context_high->metal_1h` score `-0.6332` n `146` status `ready` deltaP `1.1115` edge `0.0146` maxDD `-2.9823`
- `market_context_high->fx_1h` score `-0.7132` n `146` status `ready` deltaP `-1.4334` edge `0.0036` maxDD `-0.278`
- `market_context_high->equity_1h` score `-0.89` n `146` status `ready` deltaP `-0.8264` edge `0.0152` maxDD `-2.7085`
- `market_context_high->fx_4h` score `-0.912` n `146` status `ready` deltaP `-0.378` edge `0.0123` maxDD `-0.8621`
- `market_context_high->fx_24h` score `-0.9412` n `131` status `ready` deltaP `3.019` edge `0.0008` maxDD `-1.6157`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
