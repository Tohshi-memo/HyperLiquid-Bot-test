# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-02T16:52:26.975646+00:00`
- Price records: `672`
- Market context records: `5474`
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

- `market_context_high->crypto_major_24h` score `3.5895` n `193` status `ready` deltaP `16.628` edge `0.6423` maxDD `-29.6555`
- `market_context_high->equity_4h` score `2.3886` n `196` status `ready` deltaP `12.7675` edge `0.2778` maxDD `-7.4425`
- `market_context_high->crypto_major_4h` score `2.3837` n `196` status `ready` deltaP `14.1737` edge `0.3334` maxDD `-14.0065`
- `market_context_high->crypto_alt_4h` score `1.9946` n `196` status `ready` deltaP `10.4094` edge `0.2609` maxDD `-9.46`
- `market_context_high->equity_24h` score `0.7934` n `193` status `ready` deltaP `9.3012` edge `0.512` maxDD `-31.6316`
- `market_context_high->equity_1h` score `0.525` n `196` status `ready` deltaP `8.591` edge `0.083` maxDD `-5.0555`
- `market_context_high->index_1h` score `0.2073` n `196` status `ready` deltaP `7.2926` edge `0.018` maxDD `-0.9472`
- `market_context_high->fx_24h` score `0.1054` n `193` status `ready` deltaP `10.3807` edge `0.0323` maxDD `-1.0847`
- `market_context_high->fx_1h` score `-0.3259` n `196` status `ready` deltaP `1.0204` edge `0.0003` maxDD `-0.577`
- `market_context_high->metal_1h` score `-0.3808` n `196` status `ready` deltaP `3.2384` edge `0.0142` maxDD `-2.0682`
- `market_context_high->crypto_alt_1h` score `-0.4829` n `196` status `ready` deltaP `0.6324` edge `0.0517` maxDD `-5.0257`
- `market_context_high->crypto_major_1h` score `-0.6441` n `196` status `ready` deltaP `1.9461` edge `0.0579` maxDD `-6.9639`
- `market_context_high->index_4h` score `-0.8099` n `196` status `ready` deltaP `7.6406` edge `0.0425` maxDD `-2.874`
- `market_context_high->fx_4h` score `-0.9683` n `196` status `ready` deltaP `2.5231` edge `0.005` maxDD `-1.5345`
- `market_context_high->commodity_1h` score `-1.4691` n `196` status `ready` deltaP `-2.9451` edge `-0.008` maxDD `-3.5831`
- `market_context_high->index_24h` score `-1.8923` n `193` status `ready` deltaP `13.1827` edge `0.0682` maxDD `-16.8946`
- `market_context_high->metal_4h` score `-4.2123` n `196` status `ready` deltaP `-9.1899` edge `-0.0373` maxDD `-12.8631`
- `market_context_high->commodity_4h` score `-4.2306` n `196` status `ready` deltaP `-5.6558` edge `-0.0434` maxDD `-14.3822`
- `market_context_high->crypto_alt_24h` score `-7.0223` n `193` status `ready` deltaP `7.8332` edge `0.2323` maxDD `-54.2437`
- `market_context_high->metal_24h` score `-7.0779` n `193` status `ready` deltaP `-3.3543` edge `-0.1473` maxDD `-33.021`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
