# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-22T15:07:27.750267+00:00`
- Price records: `672`
- Market context records: `7576`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `14512`

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

- `market_context_high->commodity_4h` score `0.2686` n `165` status `ready` deltaP `10.064` edge `0.0313` maxDD `-2.4139`
- `market_context_high->index_1h` score `-0.0353` n `165` status `ready` deltaP `5.5802` edge `0.009` maxDD `-1.058`
- `market_context_high->commodity_24h` score `-0.1294` n `155` status `ready` deltaP `12.7144` edge `0.0628` maxDD `-7.0012`
- `market_context_high->commodity_1h` score `-0.2423` n `165` status `ready` deltaP `5.0286` edge `0.0035` maxDD `-1.5775`
- `market_context_high->index_4h` score `-0.4482` n `165` status `ready` deltaP `11.682` edge `0.0373` maxDD `-3.4775`
- `market_context_high->fx_1h` score `-0.4798` n `165` status `ready` deltaP `1.4933` edge `0.0` maxDD `-0.6615`
- `market_context_high->crypto_alt_1h` score `-0.7243` n `165` status `ready` deltaP `-0.3103` edge `0.0029` maxDD `-5.1624`
- `market_context_high->metal_1h` score `-0.7897` n `165` status `ready` deltaP `-0.3393` edge `0.0099` maxDD `-1.3768`
- `market_context_high->crypto_major_1h` score `-0.8337` n `165` status `ready` deltaP `4.5455` edge `0.0025` maxDD `-7.5081`
- `market_context_high->fx_24h` score `-0.9715` n `155` status `ready` deltaP `7.2856` edge `0.0145` maxDD `-3.8554`
- `market_context_high->unknown_24h` score `-0.9833` n `156` status `ready` deltaP `6.9177` edge `0.086` maxDD `-9.6544`
- `market_context_high->equity_1h` score `-1.096` n `165` status `ready` deltaP `4.0623` edge `0.0309` maxDD `-11.213`
- `market_context_high->unknown_1h` score `-1.4105` n `165` status `ready` deltaP `0.9018` edge `-0.0612` maxDD `-1.3217`
- `market_context_high->metal_4h` score `-1.4675` n `165` status `ready` deltaP `1.0726` edge `0.0529` maxDD `-4.8549`
- `market_context_high->crypto_alt_4h` score `-1.5431` n `165` status `ready` deltaP `0.4592` edge `0.0379` maxDD `-12.4367`
- `market_context_high->equity_4h` score `-1.5565` n `165` status `ready` deltaP `3.3556` edge `0.2148` maxDD `-21.9375`
- `market_context_high->unknown_4h` score `-1.837` n `165` status `ready` deltaP `9.8919` edge `-0.0658` maxDD `-6.1862`
- `market_context_high->fx_4h` score `-2.0936` n `165` status `ready` deltaP `-0.9897` edge `0.0006` maxDD `-2.1439`
- `market_context_high->crypto_major_4h` score `-2.2685` n `165` status `ready` deltaP `5.0065` edge `0.039` maxDD `-21.39`
- `market_context_high->index_24h` score `-3.7671` n `155` status `ready` deltaP `-18.7355` edge `0.0041` maxDD `-14.3063`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
