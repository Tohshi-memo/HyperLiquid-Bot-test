# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-02T15:52:31.365955+00:00`
- Price records: `672`
- Market context records: `5469`
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

- `market_context_high->crypto_major_24h` score `3.5691` n `193` status `ready` deltaP `16.628` edge `0.6406` maxDD `-29.6555`
- `market_context_high->crypto_major_4h` score `2.3547` n `196` status `ready` deltaP `14.0213` edge `0.332` maxDD `-14.0065`
- `market_context_high->equity_4h` score `2.1478` n `196` status `ready` deltaP `12.1578` edge `0.2618` maxDD `-7.4425`
- `market_context_high->crypto_alt_4h` score `1.9558` n `196` status `ready` deltaP `10.1045` edge `0.2597` maxDD `-9.46`
- `market_context_high->equity_24h` score `0.557` n `193` status `ready` deltaP `9.3012` edge `0.4923` maxDD `-31.6316`
- `market_context_high->equity_1h` score `0.4758` n `196` status `ready` deltaP `8.4413` edge `0.0799` maxDD `-5.0555`
- `market_context_high->index_1h` score `0.175` n `196` status `ready` deltaP `6.9932` edge `0.0173` maxDD `-0.9472`
- `market_context_high->fx_24h` score `0.1042` n `193` status `ready` deltaP `10.3807` edge `0.0322` maxDD `-1.0847`
- `market_context_high->fx_1h` score `-0.3344` n `196` status `ready` deltaP `0.8707` edge `0.0002` maxDD `-0.577`
- `market_context_high->metal_1h` score `-0.3844` n `196` status `ready` deltaP `3.2384` edge `0.0139` maxDD `-2.0682`
- `market_context_high->crypto_alt_1h` score `-0.4661` n `196` status `ready` deltaP `0.7821` edge `0.0521` maxDD `-5.0257`
- `market_context_high->crypto_major_1h` score `-0.6657` n `196` status `ready` deltaP `1.9461` edge `0.0561` maxDD `-6.9639`
- `market_context_high->index_4h` score `-0.8812` n `196` status `ready` deltaP `7.1833` edge `0.0396` maxDD `-2.874`
- `market_context_high->fx_4h` score `-1.0207` n `196` status `ready` deltaP `1.9133` edge `0.0047` maxDD `-1.5345`
- `market_context_high->commodity_1h` score `-1.4331` n `196` status `ready` deltaP `-2.6457` edge `-0.007` maxDD `-3.5831`
- `market_context_high->index_24h` score `-1.8977` n `193` status `ready` deltaP `13.1827` edge `0.0675` maxDD `-16.8946`
- `market_context_high->metal_4h` score `-4.1651` n `196` status `ready` deltaP `-8.885` edge `-0.0354` maxDD `-12.8631`
- `market_context_high->commodity_4h` score `-4.2016` n `196` status `ready` deltaP `-5.5033` edge `-0.042` maxDD `-14.3822`
- `market_context_high->metal_24h` score `-7.0803` n `193` status `ready` deltaP `-3.3543` edge `-0.1476` maxDD `-33.021`
- `market_context_high->crypto_alt_24h` score `-7.0907` n `193` status `ready` deltaP `7.8332` edge `0.2266` maxDD `-54.2437`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
