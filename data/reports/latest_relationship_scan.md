# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-02T07:52:44.233588+00:00`
- Price records: `672`
- Market context records: `5434`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11450`

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

- `market_context_high->equity_24h` score `4.6263` n `185` status `ready` deltaP `11.8694` edge `0.66` maxDD `-21.6219`
- `market_context_high->crypto_major_24h` score `4.3425` n `185` status `ready` deltaP `19.5008` edge `0.6859` maxDD `-29.6555`
- `market_context_high->crypto_major_4h` score `3.8138` n `196` status `ready` deltaP `16.7652` edge `0.4353` maxDD `-14.0065`
- `market_context_high->crypto_alt_4h` score `3.018` n `196` status `ready` deltaP `12.1329` edge `0.3347` maxDD `-9.46`
- `market_context_high->equity_4h` score `2.8522` n `196` status `ready` deltaP `12.9666` edge `0.3151` maxDD `-7.4425`
- `market_context_high->equity_1h` score `0.6052` n `196` status `ready` deltaP `8.8293` edge `0.0881` maxDD `-5.0555`
- `market_context_high->index_1h` score `0.1952` n `196` status `ready` deltaP `7.2315` edge `0.0174` maxDD `-0.9472`
- `market_context_high->fx_24h` score `0.121` n `185` status `ready` deltaP `9.7822` edge `0.0344` maxDD `-0.8294`
- `market_context_high->crypto_alt_1h` score `-0.1209` n `196` status `ready` deltaP `2.3066` edge `0.0707` maxDD `-5.0257`
- `market_context_high->crypto_major_1h` score `-0.2041` n `196` status `ready` deltaP `3.3209` edge `0.0854` maxDD `-6.9639`
- `market_context_high->metal_1h` score `-0.3147` n `196` status `ready` deltaP `3.4492` edge `0.0183` maxDD `-2.0682`
- `market_context_high->fx_1h` score `-0.5526` n `196` status `ready` deltaP `0.3941` edge `0.0002` maxDD `-0.577`
- `market_context_high->index_4h` score `-0.8343` n `196` status `ready` deltaP `7.2299` edge `0.0432` maxDD `-2.874`
- `market_context_high->index_24h` score `-1.0566` n `185` status `ready` deltaP `16.1627` edge `0.1028` maxDD `-12.5551`
- `market_context_high->fx_4h` score `-1.177` n `196` status `ready` deltaP `0.2894` edge `0.0025` maxDD `-1.5345`
- `market_context_high->commodity_1h` score `-1.4949` n `196` status `ready` deltaP `-3.4828` edge `-0.0069` maxDD `-3.5563`
- `market_context_high->metal_4h` score `-2.7048` n `196` status `ready` deltaP `-8.7326` edge `-0.0361` maxDD `-12.8631`
- `market_context_high->commodity_4h` score `-4.4057` n `196` status `ready` deltaP `-8.0419` edge `-0.0497` maxDD `-14.1062`
- `market_context_high->crypto_alt_24h` score `-6.3111` n `185` status `ready` deltaP `10.213` edge `0.2757` maxDD `-54.2437`
- `market_context_high->metal_24h` score `-7.3941` n `185` status `ready` deltaP `-5.7742` edge `-0.1717` maxDD `-33.021`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
