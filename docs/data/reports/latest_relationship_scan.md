# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-25T16:37:29.740150+00:00`
- Price records: `672`
- Market context records: `4741`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `7454`

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

- `market_context_high->unknown_1h` score `79.9772` n `140` status `ready` deltaP `14.1489` edge `6.6122` maxDD `-1.674`
- `market_context_high->unknown_4h` score `5.2034` n `137` status `ready` deltaP `13.2544` edge `0.4663` maxDD `-4.6834`
- `market_context_high->unknown_24h` score `3.3588` n `128` status `ready` deltaP `16.5799` edge `0.2617` maxDD `-4.7201`
- `market_context_high->index_4h` score `-0.4355` n `137` status `ready` deltaP `6.9666` edge `0.0046` maxDD `-5.5505`
- `market_context_high->commodity_1h` score `-0.5401` n `140` status `ready` deltaP `1.9333` edge `0.0217` maxDD `-2.0345`
- `market_context_high->equity_4h` score `-0.7069` n `137` status `ready` deltaP `5.1696` edge `0.0435` maxDD `-8.8203`
- `market_context_high->fx_4h` score `-0.91` n `137` status `ready` deltaP `-0.9658` edge `-0.0028` maxDD `-1.9274`
- `market_context_high->equity_1h` score `-0.9288` n `140` status `ready` deltaP `-1.3131` edge `-0.0138` maxDD `-5.3889`
- `market_context_high->fx_1h` score `-1.263` n `140` status `ready` deltaP `-5.0128` edge `-0.0052` maxDD `-0.9971`
- `market_context_high->index_1h` score `-1.5701` n `140` status `ready` deltaP `-3.4089` edge `-0.0077` maxDD `-2.6999`
- `market_context_high->commodity_4h` score `-1.7176` n `137` status `ready` deltaP `7.1134` edge `0.0202` maxDD `-9.1941`
- `market_context_high->crypto_alt_1h` score `-2.5777` n `140` status `ready` deltaP `0.5988` edge `-0.0366` maxDD `-19.8288`
- `market_context_high->metal_1h` score `-2.6184` n `140` status `ready` deltaP `-4.1146` edge `-0.0702` maxDD `-15.7119`
- `market_context_high->crypto_major_1h` score `-3.1746` n `140` status `ready` deltaP `0.402` edge `-0.062` maxDD `-25.1479`
- `market_context_high->commodity_24h` score `-3.9595` n `128` status `ready` deltaP `17.0139` edge `0.0675` maxDD `-27.5371`
- `market_context_high->fx_24h` score `-4.5611` n `128` status `ready` deltaP `-14.4966` edge `-0.0203` maxDD `-5.0518`
- `market_context_high->crypto_alt_4h` score `-6.1496` n `137` status `ready` deltaP `0.3093` edge `-0.0632` maxDD `-52.848`
- `market_context_high->index_24h` score `-7.6573` n `128` status `ready` deltaP `-11.5451` edge `-0.1043` maxDD `-25.2139`
- `market_context_high->metal_4h` score `-8.4608` n `137` status `ready` deltaP `2.083` edge `-0.2705` maxDD `-61.5819`
- `market_context_high->crypto_major_4h` score `-9.105` n `137` status `ready` deltaP `0.6787` edge `-0.177` maxDD `-74.253`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
