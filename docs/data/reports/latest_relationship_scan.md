# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-02T04:22:29.612575+00:00`
- Price records: `672`
- Market context records: `5419`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11474`

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

- `market_context_high->crypto_major_4h` score `3.9181` n `203` status `ready` deltaP `16.6887` edge `0.4445` maxDD `-14.0065`
- `market_context_high->crypto_major_24h` score `3.8105` n `192` status `ready` deltaP `19.2708` edge `0.6431` maxDD `-29.6555`
- `market_context_high->crypto_alt_4h` score `3.0751` n `203` status `ready` deltaP `12.1268` edge `0.3395` maxDD `-9.46`
- `market_context_high->equity_4h` score `2.5001` n `203` status `ready` deltaP `12.316` edge `0.2901` maxDD `-7.4425`
- `market_context_high->equity_24h` score `1.1052` n `192` status `ready` deltaP `8.8542` edge `0.5222` maxDD `-32.4635`
- `market_context_high->equity_1h` score `0.4344` n `203` status `ready` deltaP `7.9836` edge `0.0795` maxDD `-5.0555`
- `market_context_high->index_1h` score `0.1319` n `203` status `ready` deltaP `6.6502` edge `0.016` maxDD `-0.9472`
- `market_context_high->fx_24h` score `0.0596` n `192` status `ready` deltaP `9.375` edge `0.032` maxDD `-0.8294`
- `market_context_high->crypto_major_1h` score `-0.1159` n `203` status `ready` deltaP `3.8391` edge `0.0893` maxDD `-6.9639`
- `market_context_high->crypto_alt_1h` score `-0.1731` n `203` status `ready` deltaP `1.4439` edge `0.0721` maxDD `-5.0257`
- `market_context_high->fx_1h` score `-0.4106` n `203` status `ready` deltaP `-0.4587` edge `-0.0007` maxDD `-0.577`
- `market_context_high->metal_1h` score `-0.582` n `203` status `ready` deltaP `1.188` edge `0.0111` maxDD `-2.0682`
- `market_context_high->index_4h` score `-0.9714` n `203` status `ready` deltaP `6.2508` edge `0.0383` maxDD `-2.874`
- `market_context_high->fx_4h` score `-1.2315` n `203` status `ready` deltaP `-0.256` edge `0.0016` maxDD `-1.5345`
- `market_context_high->commodity_1h` score `-1.4747` n `203` status `ready` deltaP `-3.2455` edge `-0.0068` maxDD `-3.5563`
- `market_context_high->index_24h` score `-1.5411` n `192` status `ready` deltaP `13.5416` edge `0.0799` maxDD `-12.5551`
- `market_context_high->metal_4h` score `-2.6089` n `203` status `ready` deltaP `-7.2487` edge `-0.0337` maxDD `-12.8631`
- `market_context_high->commodity_4h` score `-4.2287` n `203` status `ready` deltaP `-6.5346` edge `-0.045` maxDD `-14.1062`
- `market_context_high->crypto_alt_24h` score `-6.5096` n `192` status `ready` deltaP `10.4167` edge `0.2578` maxDD `-54.2437`
- `market_context_high->metal_24h` score `-7.1825` n `192` status `ready` deltaP `-5.0347` edge `-0.1495` maxDD `-33.021`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
