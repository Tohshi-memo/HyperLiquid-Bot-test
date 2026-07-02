# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-02T07:22:32.298978+00:00`
- Price records: `672`
- Market context records: `5432`
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

- `market_context_high->equity_24h` score `4.6839` n `185` status `ready` deltaP `11.8694` edge `0.6648` maxDD `-21.6219`
- `market_context_high->crypto_major_24h` score `4.4831` n `185` status `ready` deltaP `19.848` edge `0.6953` maxDD `-29.6555`
- `market_context_high->crypto_major_4h` score `3.8366` n `196` status `ready` deltaP `16.7652` edge `0.4372` maxDD `-14.0065`
- `market_context_high->crypto_alt_4h` score `3.0384` n `196` status `ready` deltaP `12.1329` edge `0.3364` maxDD `-9.46`
- `market_context_high->equity_4h` score `2.809` n `196` status `ready` deltaP `12.9666` edge `0.3115` maxDD `-7.4425`
- `market_context_high->equity_1h` score `0.6004` n `196` status `ready` deltaP `8.8293` edge `0.0877` maxDD `-5.0555`
- `market_context_high->index_1h` score `0.194` n `196` status `ready` deltaP `7.2315` edge `0.0173` maxDD `-0.9472`
- `market_context_high->fx_24h` score `0.0896` n `185` status `ready` deltaP `9.435` edge `0.0341` maxDD `-0.8294`
- `market_context_high->crypto_alt_1h` score `-0.1185` n `196` status `ready` deltaP `2.3066` edge `0.0709` maxDD `-5.0257`
- `market_context_high->crypto_major_1h` score `-0.1885` n `196` status `ready` deltaP `3.4706` edge `0.0857` maxDD `-6.9639`
- `market_context_high->metal_1h` score `-0.3494` n `196` status `ready` deltaP `3.1498` edge `0.0174` maxDD `-2.0682`
- `market_context_high->fx_1h` score `-0.579` n `196` status `ready` deltaP `0.0947` edge `0.0` maxDD `-0.577`
- `market_context_high->index_4h` score `-0.8427` n `196` status `ready` deltaP `7.2299` edge `0.0425` maxDD `-2.874`
- `market_context_high->index_24h` score `-1.059` n `185` status `ready` deltaP `16.1627` edge `0.1026` maxDD `-12.5551`
- `market_context_high->fx_4h` score `-1.1782` n `196` status `ready` deltaP `0.2894` edge `0.0024` maxDD `-1.5345`
- `market_context_high->commodity_1h` score `-1.4661` n `196` status `ready` deltaP `-3.1834` edge `-0.0065` maxDD `-3.5563`
- `market_context_high->metal_4h` score `-2.7277` n `196` status `ready` deltaP `-9.0375` edge `-0.037` maxDD `-12.8631`
- `market_context_high->commodity_4h` score `-4.3911` n `196` status `ready` deltaP `-7.8895` edge `-0.0495` maxDD `-14.1062`
- `market_context_high->crypto_alt_24h` score `-6.1405` n `185` status `ready` deltaP `10.5603` edge `0.2876` maxDD `-54.2437`
- `market_context_high->metal_24h` score `-7.3808` n `185` status `ready` deltaP `-5.7742` edge `-0.17` maxDD `-33.021`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
