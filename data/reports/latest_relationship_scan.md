# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-07T12:07:29.180322+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4001`

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

- `market_context_high->equity_1h` score `3.3244` n `36` status `ready` deltaP `10.5123` edge `0.2529` maxDD `-2.3425`
- `news_risk_high->equity_4h` score `1.2375` n `62` status `ready` deltaP `11.3788` edge `0.1567` maxDD `-4.2454`
- `news_risk_high->index_4h` score `0.6263` n `62` status `ready` deltaP `11.8607` edge `0.0209` maxDD `-0.4888`
- `market_context_high->crypto_major_1h` score `0.6091` n `36` status `ready` deltaP `8.1005` edge `0.0553` maxDD `-3.0172`
- `market_context_high->index_1h` score `0.451` n `36` status `ready` deltaP `3.676` edge `0.0401` maxDD `-0.1621`
- `market_context_high->fx_1h` score `0.4431` n `36` status `ready` deltaP `7.3686` edge `0.0149` maxDD `-0.1681`
- `news_risk_high->index_24h` score `0.3647` n `62` status `ready` deltaP `10.4502` edge `0.1439` maxDD `-6.6786`
- `market_context_high->crypto_alt_1h` score `0.2728` n `36` status `ready` deltaP `9.1484` edge `0.0555` maxDD `-3.1881`
- `market_context_high->commodity_1h` score `0.2622` n `36` status `ready` deltaP `11.6434` edge `0.0106` maxDD `-1.7019`
- `news_risk_high->index_1h` score `0.0551` n `62` status `ready` deltaP `7.3498` edge `0.0034` maxDD `-0.2931`
- `news_risk_high->fx_24h` score `0.053` n `62` status `ready` deltaP `-2.7442` edge `0.0669` maxDD `-0.2016`
- `market_context_high->metal_1h` score `-0.0028` n `36` status `ready` deltaP `2.3287` edge `0.0169` maxDD `-0.6226`
- `news_risk_high->equity_1h` score `-0.0924` n `62` status `ready` deltaP `-0.5988` edge `0.0471` maxDD `-1.396`
- `news_risk_high->fx_1h` score `-0.1402` n `62` status `ready` deltaP `2.7091` edge `0.0025` maxDD `-0.0826`
- `news_risk_high->fx_4h` score `-0.2104` n `62` status `ready` deltaP `1.9669` edge `0.0045` maxDD `-0.2336`
- `news_risk_high->metal_1h` score `-0.5237` n `62` status `ready` deltaP `-3.6749` edge `-0.0069` maxDD `-0.5256`
- `news_risk_high->metal_4h` score `-0.9237` n `62` status `ready` deltaP `1.8784` edge `-0.0404` maxDD `-1.5773`
- `news_risk_high->crypto_alt_1h` score `-1.1213` n `62` status `ready` deltaP `-1.2459` edge `-0.0199` maxDD `-5.2444`
- `news_risk_high->crypto_major_4h` score `-1.2163` n `62` status `ready` deltaP `-2.5521` edge `0.0215` maxDD `-8.5004`
- `news_risk_high->commodity_1h` score `-1.6601` n `62` status `ready` deltaP `-11.9229` edge `-0.0029` maxDD `-1.1434`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
