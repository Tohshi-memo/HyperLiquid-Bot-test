# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-07T20:52:25.129877+00:00`
- Price records: `672`
- Market context records: `3215`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `104`

- Symbol pattern count: `11248`

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

- `market_context_high->commodity_24h` score `13.7127` n `102` status `ready` deltaP `47.9473` edge `0.8659` maxDD `-2.0927`
- `market_context_high->crypto_alt_24h` score `12.0232` n `102` status `ready` deltaP `15.0225` edge `2.4389` maxDD `-71.142`
- `market_context_high->index_24h` score `9.3506` n `102` status `ready` deltaP `29.3198` edge `0.8392` maxDD `-16.1026`
- `market_context_high->equity_24h` score `5.3596` n `102` status `ready` deltaP `14.2872` edge `1.4335` maxDD `-53.663`
- `market_context_high->commodity_4h` score `3.4832` n `128` status `ready` deltaP `22.8849` edge `0.1835` maxDD `-1.9973`
- `market_context_high->commodity_1h` score `0.452` n `140` status `ready` deltaP `6.5441` edge `0.0363` maxDD `-1.7142`
- `market_context_high->fx_24h` score `-0.4439` n `102` status `ready` deltaP `5.5147` edge `-0.0086` maxDD `-1.2125`
- `market_context_high->unknown_4h` score `-0.8733` n `128` status `ready` deltaP `8.8605` edge `0.0938` maxDD `-15.0515`
- `market_context_high->crypto_alt_1h` score `-0.8962` n `140` status `ready` deltaP `4.3884` edge `0.0813` maxDD `-14.7034`
- `market_context_high->index_1h` score `-0.9509` n `140` status `ready` deltaP `2.8101` edge `0.0083` maxDD `-4.5023`
- `market_context_high->crypto_major_1h` score `-1.0225` n `140` status `ready` deltaP `4.5594` edge `0.0648` maxDD `-15.1032`
- `market_context_high->fx_4h` score `-1.0377` n `128` status `ready` deltaP `-5.9641` edge `-0.0048` maxDD `-1.4115`
- `market_context_high->fx_1h` score `-1.6431` n `140` status `ready` deltaP `-9.5167` edge `-0.0048` maxDD `-0.8278`
- `market_context_high->equity_1h` score `-1.78` n `140` status `ready` deltaP `1.497` edge `-0.0014` maxDD `-8.8863`
- `market_context_high->index_4h` score `-1.8149` n `128` status `ready` deltaP `12.8049` edge `0.0543` maxDD `-17.6057`
- `market_context_high->metal_1h` score `-2.3394` n `140` status `ready` deltaP `-5.1155` edge `-0.0128` maxDD `-8.177`
- `market_context_high->unknown_1h` score `-2.8291` n `140` status `ready` deltaP `0.9581` edge `-0.1212` maxDD `-17.8311`
- `market_context_high->crypto_major_24h` score `-3.7125` n `102` status `ready` deltaP `13.3885` edge `1.7341` maxDD `-166.279`
- `market_context_high->crypto_major_4h` score `-4.828` n `128` status `ready` deltaP `4.154` edge `0.1457` maxDD `-54.3896`
- `market_context_high->equity_4h` score `-5.0812` n `128` status `ready` deltaP `11.5091` edge `0.0304` maxDD `-36.7784`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
