# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-11T23:07:27.909528+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `88`

- Symbol pattern count: `9132`

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

- `market_context_high->unknown_24h` score `1406.9481` n `40` status `ready` deltaP `-22.5694` edge `117.4325` maxDD `-1.2425`
- `market_context_high->unknown_4h` score `44.5569` n `101` status `ready` deltaP `-5.3958` edge `3.8071` maxDD `-2.3109`
- `market_context_high->equity_24h` score `8.808` n `40` status `ready` deltaP `27.6736` edge `0.5924` maxDD `-1.0977`
- `market_context_high->index_24h` score `6.4204` n `40` status `ready` deltaP `52.4306` edge `0.1855` maxDD `0.0`
- `market_context_high->unknown_1h` score `3.3651` n `113` status `ready` deltaP `-3.398` edge `0.3367` maxDD `-1.0231`
- `market_context_high->fx_24h` score `3.0049` n `40` status `ready` deltaP `34.1667` edge `0.0356` maxDD `-0.0374`
- `risk_on_high->crypto_alt_1h` score `1.993` n `34` status `ready` deltaP `12.707` edge `0.1369` maxDD `-2.4421`
- `risk_on_and_context->crypto_alt_1h` score `1.993` n `34` status `ready` deltaP `12.707` edge `0.1369` maxDD `-2.4421`
- `risk_on_high->commodity_1h` score `1.9803` n `34` status `ready` deltaP `24.322` edge `0.0166` maxDD `-0.0975`
- `risk_on_and_context->commodity_1h` score `1.9803` n `34` status `ready` deltaP `24.322` edge `0.0166` maxDD `-0.0975`
- `market_context_high->crypto_major_24h` score `1.378` n `40` status `ready` deltaP `-21.1111` edge `0.5704` maxDD `-17.8526`
- `market_context_high->commodity_4h` score `0.6727` n `101` status `ready` deltaP `13.6636` edge `0.0183` maxDD `-1.6002`
- `risk_on_high->crypto_major_1h` score `0.4869` n `34` status `ready` deltaP `5.8824` edge `0.0885` maxDD `-3.2233`
- `risk_on_and_context->crypto_major_1h` score `0.4869` n `34` status `ready` deltaP `5.8824` edge `0.0885` maxDD `-3.2233`
- `risk_on_high->metal_1h` score `0.4473` n `34` status `ready` deltaP `9.8186` edge `0.0158` maxDD `-0.2466`
- `risk_on_and_context->metal_1h` score `0.4473` n `34` status `ready` deltaP `9.8186` edge `0.0158` maxDD `-0.2466`
- `market_context_high->commodity_1h` score `0.3618` n `113` status `ready` deltaP `7.7421` edge `0.0069` maxDD `-0.6025`
- `market_context_high->fx_4h` score `0.2961` n `101` status `ready` deltaP `8.9456` edge `0.0059` maxDD `-0.2692`
- `market_context_high->crypto_alt_1h` score `0.1677` n `113` status `ready` deltaP `5.2369` edge `0.09` maxDD `-4.9401`
- `market_context_high->metal_4h` score `-0.06` n `101` status `ready` deltaP `7.1963` edge `0.0193` maxDD `-1.1153`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
