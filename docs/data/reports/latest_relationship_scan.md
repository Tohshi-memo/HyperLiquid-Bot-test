# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-02T17:07:37.276774+00:00`
- Price records: `672`
- Market context records: `5475`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11462`

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

- `market_context_high->crypto_major_24h` score `3.5991` n `193` status `ready` deltaP `16.628` edge `0.6431` maxDD `-29.6555`
- `market_context_high->equity_4h` score `2.4548` n `196` status `ready` deltaP `12.92` edge `0.2823` maxDD `-7.4425`
- `market_context_high->crypto_major_4h` score `2.3921` n `196` status `ready` deltaP `14.1737` edge `0.3341` maxDD `-14.0065`
- `market_context_high->crypto_alt_4h` score `2.0212` n `196` status `ready` deltaP `10.5619` edge `0.2621` maxDD `-9.46`
- `market_context_high->equity_24h` score `0.8768` n `193` status `ready` deltaP `9.4748` edge `0.5178` maxDD `-31.6316`
- `market_context_high->equity_1h` score `0.5525` n `196` status `ready` deltaP `8.7407` edge `0.0843` maxDD `-5.0555`
- `market_context_high->index_1h` score `0.2217` n `196` status `ready` deltaP `7.4423` edge `0.0182` maxDD `-0.9472`
- `market_context_high->fx_24h` score `0.1066` n `193` status `ready` deltaP `10.3807` edge `0.0324` maxDD `-1.0847`
- `market_context_high->fx_1h` score `-0.3173` n `196` status `ready` deltaP `1.1701` edge `0.0004` maxDD `-0.577`
- `market_context_high->metal_1h` score `-0.3808` n `196` status `ready` deltaP `3.2384` edge `0.0142` maxDD `-2.0682`
- `market_context_high->crypto_alt_1h` score `-0.4565` n `196` status `ready` deltaP `0.7821` edge `0.0529` maxDD `-5.0257`
- `market_context_high->crypto_major_1h` score `-0.6105` n `196` status `ready` deltaP `2.0958` edge `0.0597` maxDD `-6.9639`
- `market_context_high->index_4h` score `-0.7881` n `196` status `ready` deltaP `7.793` edge `0.0433` maxDD `-2.874`
- `market_context_high->fx_4h` score `-0.9537` n `196` status `ready` deltaP `2.6755` edge `0.0052` maxDD `-1.5345`
- `market_context_high->commodity_1h` score `-1.4667` n `196` status `ready` deltaP `-2.9451` edge `-0.0078` maxDD `-3.5831`
- `market_context_high->index_24h` score `-1.8899` n `193` status `ready` deltaP `13.1827` edge `0.0685` maxDD `-16.8946`
- `market_context_high->metal_4h` score `-4.2147` n `196` status `ready` deltaP `-9.1899` edge `-0.0375` maxDD `-12.8631`
- `market_context_high->commodity_4h` score `-4.2476` n `196` status `ready` deltaP `-5.8082` edge `-0.0438` maxDD `-14.3822`
- `market_context_high->crypto_alt_24h` score `-6.9923` n `193` status `ready` deltaP `7.8332` edge `0.2348` maxDD `-54.2437`
- `market_context_high->metal_24h` score `-7.0787` n `193` status `ready` deltaP `-3.3543` edge `-0.1474` maxDD `-33.021`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
