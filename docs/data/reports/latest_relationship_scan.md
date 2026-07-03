# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-03T21:52:26.231558+00:00`
- Price records: `672`
- Market context records: `5598`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11433`

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

- `market_context_high->equity_24h` score `3.6067` n `174` status `ready` deltaP `15.0084` edge `0.7084` maxDD `-31.6316`
- `market_context_high->crypto_major_4h` score `1.3741` n `212` status `ready` deltaP `12.4885` edge `0.2605` maxDD `-14.0065`
- `market_context_high->fx_24h` score `1.1213` n `174` status `ready` deltaP `20.2227` edge `0.056` maxDD `-1.457`
- `market_context_high->crypto_alt_4h` score `0.6752` n `212` status `ready` deltaP `7.5673` edge `0.1699` maxDD `-9.46`
- `market_context_high->equity_4h` score `0.5869` n `212` status `ready` deltaP `6.9863` edge `0.1662` maxDD `-7.4425`
- `market_context_high->equity_1h` score `-0.3127` n `224` status `ready` deltaP `5.9159` edge `0.0352` maxDD `-5.0555`
- `market_context_high->fx_1h` score `-0.3256` n `224` status `ready` deltaP `0.7378` edge `0.0009` maxDD `-0.472`
- `market_context_high->crypto_alt_1h` score `-0.5662` n `224` status `ready` deltaP `1.3152` edge `0.0402` maxDD `-5.0257`
- `market_context_high->crypto_major_1h` score `-0.5674` n `224` status `ready` deltaP `4.3146` edge `0.0485` maxDD `-6.9639`
- `market_context_high->metal_1h` score `-0.569` n `224` status `ready` deltaP `-0.8902` edge `0.0005` maxDD `-2.0682`
- `market_context_high->index_1h` score `-0.6604` n `224` status `ready` deltaP `1.3259` edge `0.0063` maxDD `-0.9472`
- `market_context_high->crypto_major_24h` score `-0.6683` n `174` status `ready` deltaP `11.195` edge `0.3237` maxDD `-29.6555`
- `market_context_high->commodity_1h` score `-1.2468` n `224` status `ready` deltaP `-2.978` edge `-0.0075` maxDD `-3.7906`
- `market_context_high->fx_4h` score `-1.3567` n `212` status `ready` deltaP `2.4879` edge `0.0081` maxDD `-1.0194`
- `market_context_high->index_4h` score `-1.5543` n `212` status `ready` deltaP `2.6548` edge `0.0137` maxDD `-2.874`
- `market_context_high->index_24h` score `-2.29` n `174` status `ready` deltaP `11.1291` edge `0.0309` maxDD `-16.8946`
- `market_context_high->metal_4h` score `-2.9248` n `212` status `ready` deltaP `-12.0024` edge `-0.0566` maxDD `-11.7351`
- `market_context_high->commodity_4h` score `-4.1565` n `212` status `ready` deltaP `-5.2232` edge `-0.044` maxDD `-14.071`
- `market_context_high->metal_24h` score `-8.0794` n `174` status `ready` deltaP `-8.6746` edge `-0.2419` maxDD `-32.8874`
- `market_context_high->crypto_alt_24h` score `-10.7504` n `174` status `ready` deltaP `0.9818` edge `-0.0327` maxDD `-54.2437`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
