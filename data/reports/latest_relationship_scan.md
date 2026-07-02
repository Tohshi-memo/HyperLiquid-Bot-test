# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-02T09:22:40.483389+00:00`
- Price records: `672`
- Market context records: `5440`
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

- `market_context_high->equity_24h` score `4.3899` n `185` status `ready` deltaP `11.8694` edge `0.6403` maxDD `-21.6219`
- `market_context_high->crypto_major_24h` score `3.8236` n `185` status `ready` deltaP `18.4591` edge `0.6496` maxDD `-29.6555`
- `market_context_high->crypto_major_4h` score `3.7514` n `196` status `ready` deltaP `16.7652` edge `0.4301` maxDD `-14.0065`
- `market_context_high->equity_4h` score `2.9897` n `196` status `ready` deltaP `13.5764` edge `0.3225` maxDD `-7.4425`
- `market_context_high->crypto_alt_4h` score `2.9168` n `196` status `ready` deltaP `11.828` edge `0.3283` maxDD `-9.46`
- `market_context_high->equity_1h` score `0.5706` n `197` status `ready` deltaP `8.577` edge `0.0869` maxDD `-5.0555`
- `market_context_high->fx_24h` score `0.2163` n `185` status `ready` deltaP `10.8239` edge `0.0354` maxDD `-0.8294`
- `market_context_high->index_1h` score `0.1518` n `197` status `ready` deltaP `6.7031` edge `0.0173` maxDD `-0.9472`
- `market_context_high->crypto_alt_1h` score `-0.2051` n `197` status `ready` deltaP `1.6596` edge `0.068` maxDD `-5.0257`
- `market_context_high->crypto_major_1h` score `-0.284` n `197` status `ready` deltaP `2.6817` edge `0.083` maxDD `-6.9639`
- `market_context_high->metal_1h` score `-0.3206` n `197` status `ready` deltaP `3.3907` edge `0.0182` maxDD `-2.0682`
- `market_context_high->fx_1h` score `-0.5498` n `197` status `ready` deltaP `0.4293` edge `0.0002` maxDD `-0.577`
- `market_context_high->index_4h` score `-0.7493` n `196` status `ready` deltaP `7.9921` edge `0.0452` maxDD `-2.874`
- `market_context_high->index_24h` score `-1.0926` n `185` status `ready` deltaP `16.1627` edge `0.0998` maxDD `-12.5551`
- `market_context_high->fx_4h` score `-1.1734` n `196` status `ready` deltaP `0.2894` edge `0.0028` maxDD `-1.5345`
- `market_context_high->commodity_1h` score `-1.5068` n `197` status `ready` deltaP `-3.5662` edge `-0.007` maxDD `-3.5831`
- `market_context_high->metal_4h` score `-2.6797` n `196` status `ready` deltaP `-8.5802` edge `-0.0339` maxDD `-12.8631`
- `market_context_high->commodity_4h` score `-4.3571` n `196` status `ready` deltaP `-7.5846` edge `-0.0487` maxDD `-14.1062`
- `market_context_high->crypto_alt_24h` score `-6.89` n `185` status `ready` deltaP `9.1714` edge `0.2344` maxDD `-54.2437`
- `market_context_high->metal_24h` score `-7.4565` n `185` status `ready` deltaP `-5.7742` edge `-0.1797` maxDD `-33.021`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
