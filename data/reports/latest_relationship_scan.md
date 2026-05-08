# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-08T11:43:20.455439+00:00`
- Price records: `642`
- Market context records: `751`
- Flow alert records: `2120`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `1117`

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

- `market_context_high->crypto_major_24h` score `13.0707` n `146` status `ready` deltaP `31.1581` edge `0.9149` maxDD `-1.3382`
- `market_context_high->crypto_alt_24h` score `6.6465` n `146` status `ready` deltaP `7.5569` edge `0.5083` maxDD `-0.0508`
- `market_context_high->index_24h` score `0.4003` n `146` status `ready` deltaP `2.5451` edge `0.2159` maxDD `-5.9609`
- `market_context_high->equity_24h` score `-0.2038` n `146` status `ready` deltaP `0.9883` edge `0.2369` maxDD `-10.5047`
- `market_context_high->fx_1h` score `-0.2534` n `168` status `ready` deltaP `3.4081` edge `0.0026` maxDD `-0.291`
- `market_context_high->fx_4h` score `-0.453` n `157` status `ready` deltaP `6.0141` edge `0.0093` maxDD `-1.6381`
- `market_context_high->commodity_1h` score `-0.5962` n `168` status `ready` deltaP `1.4045` edge `0.0384` maxDD `-3.7959`
- `market_context_high->index_1h` score `-0.9651` n `168` status `ready` deltaP `0.3042` edge `0.0029` maxDD `-2.8282`
- `market_context_high->crypto_major_1h` score `-1.0155` n `168` status `ready` deltaP `6.4208` edge `-0.0007` maxDD `-11.4508`
- `market_context_high->equity_1h` score `-1.1525` n `168` status `ready` deltaP `-2.0261` edge `-0.0015` maxDD `-4.4826`
- `market_context_high->crypto_alt_1h` score `-1.3384` n `168` status `ready` deltaP `5.1948` edge `-0.0147` maxDD `-8.1842`
- `market_context_high->unknown_1h` score `-1.5777` n `168` status `ready` deltaP `-4.5754` edge `-0.0238` maxDD `-3.5069`
- `market_context_high->crypto_major_4h` score `-1.6299` n `157` status `ready` deltaP `17.1862` edge `0.1202` maxDD `-22.648`
- `market_context_high->index_4h` score `-1.7698` n `157` status `ready` deltaP `1.618` edge `-0.006` maxDD `-6.5149`
- `market_context_high->metal_1h` score `-2.0032` n `168` status `ready` deltaP `-3.7636` edge `-0.0358` maxDD `-9.0076`
- `market_context_high->crypto_alt_4h` score `-2.2097` n `157` status `ready` deltaP `2.33` edge `0.0573` maxDD `-15.2248`
- `market_context_high->equity_4h` score `-2.6041` n `157` status `ready` deltaP `-1.2759` edge `0.0067` maxDD `-10.5498`
- `market_context_high->commodity_4h` score `-3.7226` n `157` status `ready` deltaP `-5.6434` edge `0.0775` maxDD `-13.0076`
- `market_context_high->unknown_4h` score `-3.7535` n `157` status `ready` deltaP `4.9084` edge `-0.1577` maxDD `-8.3588`
- `market_context_high->fx_24h` score `-5.443` n `146` status `ready` deltaP `-16.2514` edge `-0.0723` maxDD `-21.0414`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
