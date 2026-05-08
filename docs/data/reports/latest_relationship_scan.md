# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-08T15:07:21.674051+00:00`
- Price records: `656`
- Market context records: `767`
- Flow alert records: `2162`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `1170`

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

- `market_context_high->crypto_major_24h` score `13.4061` n `147` status `ready` deltaP `31.8708` edge `0.9381` maxDD `-1.3382`
- `market_context_high->crypto_alt_24h` score `6.7156` n `147` status `ready` deltaP `7.3554` edge `0.5154` maxDD `-0.0508`
- `risk_on_high->metal_1h` score `1.3204` n `32` status `ready` deltaP `15.1265` edge `0.0322` maxDD `-0.5074`
- `risk_on_and_context->metal_1h` score `1.3204` n `32` status `ready` deltaP `15.1265` edge `0.0322` maxDD `-0.5074`
- `market_context_high->index_24h` score `0.5686` n `147` status `ready` deltaP `3.2239` edge `0.2254` maxDD `-5.9609`
- `risk_on_high->fx_1h` score `0.4241` n `32` status `ready` deltaP `10.5324` edge `0.0031` maxDD `-0.1827`
- `risk_on_and_context->fx_1h` score `0.4241` n `32` status `ready` deltaP `10.5324` edge `0.0031` maxDD `-0.1827`
- `risk_on_high->commodity_1h` score `0.1855` n `32` status `ready` deltaP `6.5201` edge `0.0179` maxDD `-0.6739`
- `risk_on_and_context->commodity_1h` score `0.1855` n `32` status `ready` deltaP `6.5201` edge `0.0179` maxDD `-0.6739`
- `risk_on_high->crypto_major_1h` score `0.1022` n `32` status `ready` deltaP `6.7676` edge `-0.0035` maxDD `-0.948`
- `risk_on_and_context->crypto_major_1h` score `0.1022` n `32` status `ready` deltaP `6.7676` edge `-0.0035` maxDD `-0.948`
- `market_context_high->equity_24h` score `0.0134` n `147` status `ready` deltaP `1.7692` edge `0.2498` maxDD `-10.5047`
- `risk_on_high->index_1h` score `-0.3501` n `32` status `ready` deltaP `-1.4275` edge `0.0087` maxDD `-0.2687`
- `risk_on_and_context->index_1h` score `-0.3501` n `32` status `ready` deltaP `-1.4275` edge `0.0087` maxDD `-0.2687`
- `risk_on_high->crypto_alt_1h` score `-0.3981` n `32` status `ready` deltaP `3.6043` edge `-0.0248` maxDD `-0.9258`
- `risk_on_and_context->crypto_alt_1h` score `-0.3981` n `32` status `ready` deltaP `3.6043` edge `-0.0248` maxDD `-0.9258`
- `market_context_high->fx_4h` score `-0.4266` n `170` status `ready` deltaP `3.7569` edge `0.0074` maxDD `-1.6381`
- `market_context_high->commodity_1h` score `-0.4841` n `182` status `ready` deltaP `2.2962` edge `0.0418` maxDD `-3.7959`
- `market_context_high->fx_1h` score `-0.5056` n `182` status `ready` deltaP `2.0503` edge `0.002` maxDD `-0.291`
- `market_context_high->equity_1h` score `-0.5253` n `182` status `ready` deltaP `0.2238` edge `0.0122` maxDD `-4.4826`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
