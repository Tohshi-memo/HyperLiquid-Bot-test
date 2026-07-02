# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-02T16:37:27.095623+00:00`
- Price records: `672`
- Market context records: `5473`
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

- `market_context_high->crypto_major_24h` score `3.5823` n `193` status `ready` deltaP `16.628` edge `0.6417` maxDD `-29.6555`
- `market_context_high->crypto_major_4h` score `2.3777` n `196` status `ready` deltaP `14.1737` edge `0.3329` maxDD `-14.0065`
- `market_context_high->equity_4h` score `2.3212` n `196` status `ready` deltaP `12.6151` edge `0.2732` maxDD `-7.4425`
- `market_context_high->crypto_alt_4h` score `1.9716` n `196` status `ready` deltaP `10.257` edge `0.26` maxDD `-9.46`
- `market_context_high->equity_24h` score `0.7322` n `193` status `ready` deltaP `9.3012` edge `0.5069` maxDD `-31.6316`
- `market_context_high->equity_1h` score `0.513` n `196` status `ready` deltaP `8.591` edge `0.082` maxDD `-5.0555`
- `market_context_high->index_1h` score `0.193` n `196` status `ready` deltaP `7.1429` edge `0.0178` maxDD `-0.9472`
- `market_context_high->fx_24h` score `0.1042` n `193` status `ready` deltaP `10.3807` edge `0.0322` maxDD `-1.0847`
- `market_context_high->fx_1h` score `-0.3336` n `196` status `ready` deltaP `0.8707` edge `0.0003` maxDD `-0.577`
- `market_context_high->metal_1h` score `-0.3808` n `196` status `ready` deltaP `3.2384` edge `0.0142` maxDD `-2.0682`
- `market_context_high->crypto_alt_1h` score `-0.4925` n `196` status `ready` deltaP `0.6324` edge `0.0509` maxDD `-5.0257`
- `market_context_high->crypto_major_1h` score `-0.6585` n `196` status `ready` deltaP `1.9461` edge `0.0567` maxDD `-6.9639`
- `market_context_high->index_4h` score `-0.8329` n `196` status `ready` deltaP `7.4881` edge `0.0416` maxDD `-2.874`
- `market_context_high->fx_4h` score `-0.9817` n `196` status `ready` deltaP `2.3706` edge `0.0049` maxDD `-1.5345`
- `market_context_high->commodity_1h` score `-1.4667` n `196` status `ready` deltaP `-2.9451` edge `-0.0078` maxDD `-3.5831`
- `market_context_high->index_24h` score `-1.8938` n `193` status `ready` deltaP `13.1827` edge `0.068` maxDD `-16.8946`
- `market_context_high->metal_4h` score `-4.2111` n `196` status `ready` deltaP `-9.1899` edge `-0.0372` maxDD `-12.8631`
- `market_context_high->commodity_4h` score `-4.2124` n `196` status `ready` deltaP `-5.5033` edge `-0.0429` maxDD `-14.3822`
- `market_context_high->crypto_alt_24h` score `-7.0451` n `193` status `ready` deltaP `7.8332` edge `0.2304` maxDD `-54.2437`
- `market_context_high->metal_24h` score `-7.0771` n `193` status `ready` deltaP `-3.3543` edge `-0.1472` maxDD `-33.021`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
