# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-31T13:37:24.794137+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `7269`

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

- `market_context_high->unknown_24h` score `2442.5548` n `109` status `ready` deltaP `-7.7838` edge `203.6411` maxDD `-1.1049`
- `news_risk_high->unknown_1h` score `87.0132` n `100` status `ready` deltaP `-5.5749` edge `7.3169` maxDD `-0.9571`
- `market_context_high->unknown_4h` score `63.4235` n `109` status `ready` deltaP `1.0475` edge `5.2916` maxDD `-0.3966`
- `news_risk_high->crypto_alt_24h` score `17.225` n `48` status `ready` deltaP `45.4861` edge `1.1373` maxDD `-0.0763`
- `market_context_high->equity_24h` score `10.9586` n `109` status `ready` deltaP `27.0642` edge `1.0085` maxDD `-14.0571`
- `market_context_high->index_24h` score `4.7181` n `109` status `ready` deltaP `42.463` edge `0.1284` maxDD `-0.1315`
- `news_risk_high->crypto_alt_4h` score `4.6508` n `98` status `ready` deltaP `17.2661` edge `0.4111` maxDD `-7.4246`
- `market_context_high->metal_4h` score `1.7326` n `109` status `ready` deltaP `21.7009` edge `0.0422` maxDD `-0.7323`
- `market_context_high->equity_4h` score `1.1757` n `109` status `ready` deltaP `7.036` edge `0.1904` maxDD `-4.48`
- `market_context_high->metal_1h` score `0.6031` n `109` status `ready` deltaP `13.414` edge `0.0169` maxDD `-0.3209`
- `market_context_high->equity_1h` score `0.5962` n `109` status `ready` deltaP `6.5621` edge `0.0935` maxDD `-2.3383`
- `news_risk_high->crypto_alt_1h` score `0.5328` n `100` status `ready` deltaP `6.2455` edge `0.094` maxDD `-3.9659`
- `market_context_high->crypto_major_1h` score `0.5014` n `109` status `ready` deltaP `9.6523` edge `0.0802` maxDD `-5.2213`
- `market_context_high->fx_1h` score `0.2372` n `109` status `ready` deltaP `7.0689` edge `-0.0006` maxDD `-0.1407`
- `market_context_high->metal_24h` score `0.1459` n `109` status `ready` deltaP `14.0242` edge `0.1899` maxDD `-10.5088`
- `market_context_high->commodity_4h` score `0.021` n `109` status `ready` deltaP `10.8413` edge `0.0523` maxDD `-1.0837`
- `market_context_high->fx_4h` score `-0.0336` n `109` status `ready` deltaP `5.5116` edge `-0.0004` maxDD `-0.1315`
- `market_context_high->crypto_major_4h` score `-0.0705` n `109` status `ready` deltaP `16.3711` edge `0.159` maxDD `-14.5879`
- `market_context_high->index_1h` score `-0.3503` n `109` status `ready` deltaP `3.6986` edge `0.002` maxDD `-1.1344`
- `market_context_high->commodity_1h` score `-0.4389` n `109` status `ready` deltaP `0.0824` edge `0.0143` maxDD `-0.4475`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
