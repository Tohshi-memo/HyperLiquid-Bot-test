# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-18T01:07:23.685711+00:00`
- Price records: `672`
- Market context records: `7088`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11502`

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

- `market_context_high->fx_4h` score `0.7601` n `167` status `ready` deltaP `17.9156` edge `0.0139` maxDD `-0.9333`
- `market_context_high->fx_1h` score `-0.1353` n `167` status `ready` deltaP `4.6407` edge `0.0029` maxDD `-0.276`
- `market_context_high->unknown_1h` score `-0.2299` n `167` status `ready` deltaP `0.1497` edge `0.0357` maxDD `-1.4688`
- `market_context_high->crypto_alt_1h` score `-0.3678` n `167` status `ready` deltaP `1.3473` edge `0.0303` maxDD `-4.5815`
- `market_context_high->index_1h` score `-0.4343` n `167` status `ready` deltaP `1.6467` edge `-0.0047` maxDD `-2.2895`
- `market_context_high->crypto_major_1h` score `-0.5958` n `167` status `ready` deltaP `3.5928` edge `0.0349` maxDD `-7.1523`
- `market_context_high->commodity_1h` score `-0.9115` n `167` status `ready` deltaP `-5.2395` edge `-0.0203` maxDD `-1.9306`
- `market_context_high->metal_1h` score `-1.4425` n `167` status `ready` deltaP `-5.8383` edge `-0.0045` maxDD `-2.1427`
- `market_context_high->commodity_4h` score `-1.5309` n `167` status `ready` deltaP `-6.92` edge `-0.0466` maxDD `-2.9494`
- `market_context_high->unknown_4h` score `-1.7571` n `167` status `ready` deltaP `-8.344` edge `-0.0062` maxDD `-4.742`
- `market_context_high->equity_1h` score `-1.9705` n `167` status `ready` deltaP `3.7425` edge `-0.0353` maxDD `-14.716`
- `market_context_high->index_4h` score `-2.1921` n `167` status `ready` deltaP `3.8493` edge `-0.0368` maxDD `-12.2591`
- `market_context_high->commodity_24h` score `-2.7083` n `167` status `ready` deltaP `-4.4265` edge `-0.0653` maxDD `-4.4704`
- `market_context_high->crypto_major_4h` score `-2.9848` n `167` status `ready` deltaP `4.1971` edge `0.0178` maxDD `-24.6094`
- `market_context_high->crypto_alt_4h` score `-3.137` n `167` status `ready` deltaP `-1.4313` edge `-0.0141` maxDD `-22.2831`
- `market_context_high->metal_4h` score `-3.9522` n `167` status `ready` deltaP `-3.5746` edge `-0.0072` maxDD `-5.5324`
- `market_context_high->fx_24h` score `-3.9692` n `167` status `ready` deltaP `-4.7779` edge `-0.0162` maxDD `-3.9503`
- `market_context_high->equity_4h` score `-8.1617` n `167` status `ready` deltaP `2.8151` edge `-0.1781` maxDD `-63.963`
- `market_context_high->unknown_24h` score `-8.631` n `167` status `ready` deltaP `-21.7752` edge `-0.0594` maxDD `-23.5076`
- `market_context_high->metal_24h` score `-15.345` n `167` status `ready` deltaP `-23.7172` edge `-0.121` maxDD `-43.9706`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
