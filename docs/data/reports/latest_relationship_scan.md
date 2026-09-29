# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-29T15:37:34.024757+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `7160`

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

- `news_risk_high->unknown_24h` score `2584.3548` n `139` status `ready` deltaP `1.2153` edge `215.3548` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `16.5462` n `139` status `ready` deltaP `32.2405` edge `1.5591` maxDD `-29.2814`
- `news_risk_high->equity_24h` score `10.2076` n `139` status `ready` deltaP `34.616` edge `0.8755` maxDD `-11.1179`
- `news_risk_high->crypto_major_24h` score `8.2117` n `139` status `ready` deltaP `24.8938` edge `0.9618` maxDD `-26.1424`
- `news_risk_high->index_24h` score `4.2196` n `139` status `ready` deltaP `38.8589` edge `0.1621` maxDD `-2.2287`
- `news_risk_high->metal_24h` score `3.793` n `139` status `ready` deltaP `31.586` edge `0.291` maxDD `-6.8392`
- `news_risk_high->equity_4h` score `2.73` n `142` status `ready` deltaP `27.9801` edge `0.2019` maxDD `-9.2079`
- `news_risk_high->crypto_alt_4h` score `1.1391` n `142` status `ready` deltaP `8.9381` edge `0.3013` maxDD `-15.9436`
- `news_risk_high->crypto_alt_1h` score `0.7933` n `142` status `ready` deltaP `6.9706` edge `0.1107` maxDD `-4.2849`
- `news_risk_high->equity_1h` score `0.5943` n `142` status `ready` deltaP `7.4028` edge `0.0663` maxDD `-1.957`
- `news_risk_high->index_1h` score `0.4682` n `142` status `ready` deltaP `8.6004` edge `0.0107` maxDD `-0.3214`
- `news_risk_high->index_4h` score `0.0672` n `142` status `ready` deltaP `9.1399` edge `0.03` maxDD `-1.493`
- `news_risk_high->crypto_major_1h` score `-0.3486` n `142` status `ready` deltaP `2.4395` edge `0.0673` maxDD `-7.2607`
- `news_risk_high->metal_1h` score `-0.5636` n `142` status `ready` deltaP `0.565` edge `0.0122` maxDD `-0.7016`
- `news_risk_high->fx_4h` score `-1.2858` n `142` status `ready` deltaP `9.4362` edge `-0.0064` maxDD `-3.0414`
- `news_risk_high->metal_4h` score `-1.3186` n `142` status `ready` deltaP `-7.6971` edge `0.0317` maxDD `-3.6214`
- `news_risk_high->crypto_major_4h` score `-1.7151` n `142` status `ready` deltaP `-4.5303` edge `0.0818` maxDD `-13.719`
- `news_risk_high->fx_1h` score `-1.8205` n `142` status `ready` deltaP `-8.9947` edge `-0.0037` maxDD `-1.0436`
- `news_risk_high->commodity_1h` score `-1.9227` n `142` status `ready` deltaP `-10.2028` edge `-0.011` maxDD `-3.3986`
- `news_risk_high->commodity_4h` score `-2.3536` n `142` status `ready` deltaP `-9.6122` edge `0.0042` maxDD `-8.6825`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
