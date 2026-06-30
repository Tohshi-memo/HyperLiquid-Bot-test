# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-30T16:52:30.170252+00:00`
- Price records: `672`
- Market context records: `5266`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `9604`

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

- `market_context_high->unknown_24h` score `25.9917` n `147` status `ready` deltaP `29.8895` edge `1.9757` maxDD `-0.3859`
- `market_context_high->crypto_major_24h` score `10.2711` n `147` status `ready` deltaP `28.4297` edge `1.0268` maxDD `-22.166`
- `market_context_high->crypto_alt_4h` score `4.2215` n `162` status `ready` deltaP `15.3718` edge `0.4134` maxDD `-9.46`
- `market_context_high->crypto_major_4h` score `3.756` n `162` status `ready` deltaP `14.1523` edge `0.4479` maxDD `-14.0065`
- `market_context_high->equity_24h` score `3.4596` n `147` status `ready` deltaP `19.5118` edge `0.7211` maxDD `-40.0306`
- `market_context_high->unknown_4h` score `1.4642` n `162` status `ready` deltaP `15.5451` edge `0.1206` maxDD `-5.5109`
- `market_context_high->equity_4h` score `0.6798` n `162` status `ready` deltaP `8.7172` edge `0.1624` maxDD `-7.4425`
- `market_context_high->fx_24h` score `0.5149` n `147` status `ready` deltaP `12.6666` edge `0.048` maxDD `-0.8294`
- `market_context_high->crypto_alt_1h` score `0.4345` n `174` status `ready` deltaP `4.269` edge `0.1039` maxDD `-5.0257`
- `market_context_high->index_24h` score `0.2182` n `147` status `ready` deltaP `21.0247` edge `0.0513` maxDD `-7.413`
- `market_context_high->crypto_major_1h` score `0.2002` n `174` status `ready` deltaP `5.2395` edge `0.1063` maxDD `-6.9639`
- `market_context_high->equity_1h` score `0.063` n `174` status `ready` deltaP `6.327` edge `0.0596` maxDD `-5.0555`
- `market_context_high->crypto_alt_24h` score `0.0114` n `147` status `ready` deltaP `15.4018` edge `0.5283` maxDD `-38.6949`
- `market_context_high->index_1h` score `-0.0247` n `174` status `ready` deltaP `5.477` edge `0.0118` maxDD `-1.0296`
- `market_context_high->metal_1h` score `-0.1967` n `174` status `ready` deltaP `4.3947` edge `0.0135` maxDD `-2.0682`
- `market_context_high->fx_1h` score `-0.2779` n `174` status `ready` deltaP `1.3284` edge `0.0003` maxDD `-0.5823`
- `market_context_high->index_4h` score `-0.663` n `162` status `ready` deltaP `5.1284` edge `0.0223` maxDD `-2.9391`
- `market_context_high->fx_4h` score `-0.744` n `162` status `ready` deltaP `0.8901` edge `0.0016` maxDD `-1.567`
- `market_context_high->commodity_1h` score `-1.3762` n `174` status `ready` deltaP `-3.0474` edge `-0.0067` maxDD `-3.0135`
- `market_context_high->unknown_1h` score `-1.4827` n `174` status `ready` deltaP `6.8536` edge `-0.1051` maxDD `-2.7986`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
