# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-02T08:52:29.685815+00:00`
- Price records: `672`
- Market context records: `5438`
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

- `market_context_high->equity_24h` score `4.4763` n `185` status `ready` deltaP `11.8694` edge `0.6475` maxDD `-21.6219`
- `market_context_high->crypto_major_24h` score `3.9966` n `185` status `ready` deltaP `18.8063` edge `0.6617` maxDD `-29.6555`
- `market_context_high->crypto_major_4h` score `3.7682` n `196` status `ready` deltaP `16.7652` edge `0.4315` maxDD `-14.0065`
- `market_context_high->equity_4h` score `2.9341` n `196` status `ready` deltaP `13.2715` edge `0.3199` maxDD `-7.4425`
- `market_context_high->crypto_alt_4h` score `2.9312` n `196` status `ready` deltaP `11.828` edge `0.3295` maxDD `-9.46`
- `market_context_high->equity_1h` score `0.5778` n `197` status `ready` deltaP `8.577` edge `0.0875` maxDD `-5.0555`
- `market_context_high->fx_24h` score `0.1849` n `185` status `ready` deltaP `10.4767` edge `0.0351` maxDD `-0.8294`
- `market_context_high->index_1h` score `0.1637` n `197` status `ready` deltaP `6.8528` edge `0.0173` maxDD `-0.9472`
- `market_context_high->crypto_alt_1h` score `-0.1739` n `197` status `ready` deltaP `1.959` edge `0.0686` maxDD `-5.0257`
- `market_context_high->crypto_major_1h` score `-0.2481` n `197` status `ready` deltaP `2.9811` edge `0.084` maxDD `-6.9639`
- `market_context_high->metal_1h` score `-0.2918` n `197` status `ready` deltaP `3.6901` edge `0.0186` maxDD `-2.0682`
- `market_context_high->fx_1h` score `-0.5366` n `197` status `ready` deltaP `0.579` edge `0.0003` maxDD `-0.577`
- `market_context_high->index_4h` score `-0.7833` n `196` status `ready` deltaP `7.6873` edge `0.0444` maxDD `-2.874`
- `market_context_high->index_24h` score `-1.077` n `185` status `ready` deltaP `16.1627` edge `0.1011` maxDD `-12.5551`
- `market_context_high->fx_4h` score `-1.1746` n `196` status `ready` deltaP `0.2894` edge `0.0027` maxDD `-1.5345`
- `market_context_high->commodity_1h` score `-1.5223` n `197` status `ready` deltaP `-3.7159` edge `-0.0073` maxDD `-3.5831`
- `market_context_high->metal_4h` score `-2.6891` n `196` status `ready` deltaP `-8.5802` edge `-0.0351` maxDD `-12.8631`
- `market_context_high->commodity_4h` score `-4.3899` n `196` status `ready` deltaP `-7.8895` edge `-0.0494` maxDD `-14.1062`
- `market_context_high->crypto_alt_24h` score `-6.7123` n `185` status `ready` deltaP `9.5186` edge `0.2469` maxDD `-54.2437`
- `market_context_high->metal_24h` score `-7.4362` n `185` status `ready` deltaP `-5.7742` edge `-0.1771` maxDD `-33.021`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
