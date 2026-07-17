# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-17T10:22:25.414807+00:00`
- Price records: `672`
- Market context records: `7018`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11529`

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

- `market_context_high->fx_1h` score `-0.2731` n `225` status `ready` deltaP `1.8736` edge `0.001` maxDD `-0.5468`
- `market_context_high->unknown_24h` score `-0.5321` n `212` status `ready` deltaP `-6.1354` edge `0.4277` maxDD `-18.7342`
- `market_context_high->crypto_alt_1h` score `-0.6226` n `225` status `ready` deltaP `1.0878` edge `0.0273` maxDD `-4.5815`
- `market_context_high->metal_1h` score `-0.6811` n `225` status `ready` deltaP `-1.6401` edge `0.0004` maxDD `-2.1427`
- `market_context_high->index_1h` score `-0.6994` n `225` status `ready` deltaP `0.1284` edge `0.0006` maxDD `-2.2895`
- `market_context_high->crypto_major_1h` score `-0.7358` n `225` status `ready` deltaP `2.7299` edge `0.0227` maxDD `-7.1523`
- `market_context_high->fx_4h` score `-1.0127` n `225` status `ready` deltaP `9.9268` edge `0.0059` maxDD `-2.1531`
- `market_context_high->commodity_1h` score `-1.2877` n `225` status `ready` deltaP `-2.7532` edge `-0.0168` maxDD `-2.4388`
- `market_context_high->unknown_1h` score `-1.2915` n `225` status `ready` deltaP `-2.2528` edge `-0.0025` maxDD `-3.2083`
- `market_context_high->commodity_4h` score `-1.7204` n `225` status `ready` deltaP `-4.8083` edge `-0.0404` maxDD `-5.5157`
- `market_context_high->index_4h` score `-1.7953` n `225` status `ready` deltaP `7.6402` edge `-0.0112` maxDD `-12.2591`
- `market_context_high->metal_4h` score `-1.9096` n `225` status `ready` deltaP `6.4505` edge `0.0105` maxDD `-5.5324`
- `market_context_high->unknown_4h` score `-2.386` n `225` status `ready` deltaP `-5.8929` edge `0.0725` maxDD `-9.8971`
- `market_context_high->crypto_alt_4h` score `-2.757` n `225` status `ready` deltaP `1.0617` edge `0.018` maxDD `-22.2831`
- `market_context_high->commodity_24h` score `-2.8841` n `212` status `ready` deltaP `-4.1797` edge `-0.0816` maxDD `-4.4704`
- `market_context_high->equity_1h` score `-2.9346` n `225` status `ready` deltaP `3.2348` edge `-0.0107` maxDD `-15.7664`
- `market_context_high->fx_24h` score `-4.1167` n `212` status `ready` deltaP `-5.2149` edge `-0.0151` maxDD `-4.7888`
- `market_context_high->crypto_major_4h` score `-4.8736` n `225` status `ready` deltaP `1.7723` edge `0.0105` maxDD `-24.6094`
- `market_context_high->equity_4h` score `-11.5434` n `225` status `ready` deltaP `4.3144` edge `-0.069` maxDD `-66.7371`
- `market_context_high->metal_24h` score `-13.4315` n `212` status `ready` deltaP `-10.1186` edge `-0.0549` maxDD `-39.4213`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
