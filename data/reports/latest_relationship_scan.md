# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-07T12:22:24.855475+00:00`
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

- `market_context_high->equity_1h` score `3.1239` n `37` status `ready` deltaP `9.0104` edge `0.2462` maxDD `-2.3425`
- `news_risk_high->equity_4h` score `1.247` n `62` status `ready` deltaP `11.5312` edge `0.1569` maxDD `-4.2454`
- `market_context_high->crypto_major_1h` score `0.7004` n `37` status `ready` deltaP `9.3017` edge `0.0549` maxDD `-3.0172`
- `news_risk_high->index_4h` score `0.6263` n `62` status `ready` deltaP `11.8607` edge `0.0209` maxDD `-0.4888`
- `market_context_high->fx_1h` score `0.5212` n `37` status `ready` deltaP `8.27` edge `0.0154` maxDD `-0.1681`
- `news_risk_high->index_24h` score `0.3745` n `62` status `ready` deltaP `10.6238` edge `0.144` maxDD `-6.6786`
- `market_context_high->crypto_alt_1h` score `0.368` n `37` status `ready` deltaP `10.3496` edge `0.0597` maxDD `-3.1881`
- `market_context_high->index_1h` score `0.3356` n `37` status `ready` deltaP `2.3993` edge `0.039` maxDD `-0.1621`
- `market_context_high->commodity_1h` score `0.1709` n `37` status `ready` deltaP `9.9167` edge `0.0104` maxDD `-1.7019`
- `news_risk_high->index_1h` score `0.0629` n `62` status `ready` deltaP `7.4995` edge `0.0034` maxDD `-0.2931`
- `news_risk_high->fx_24h` score `0.053` n `62` status `ready` deltaP `-2.7442` edge `0.0669` maxDD `-0.2016`
- `market_context_high->metal_1h` score `-0.0832` n `37` status `ready` deltaP `0.9023` edge `0.0161` maxDD `-0.6226`
- `news_risk_high->equity_1h` score `-0.0846` n `62` status `ready` deltaP `-0.4491` edge `0.0471` maxDD `-1.396`
- `news_risk_high->fx_1h` score `-0.148` n `62` status `ready` deltaP `2.5594` edge `0.0025` maxDD `-0.0826`
- `news_risk_high->fx_4h` score `-0.2191` n `62` status `ready` deltaP `1.8145` edge `0.0044` maxDD `-0.2336`
- `news_risk_high->metal_1h` score `-0.5237` n `62` status `ready` deltaP `-3.6749` edge `-0.0069` maxDD `-0.5256`
- `news_risk_high->metal_4h` score `-0.915` n `62` status `ready` deltaP `2.0309` edge `-0.0403` maxDD `-1.5773`
- `news_risk_high->crypto_alt_1h` score `-1.1221` n `62` status `ready` deltaP `-1.2459` edge `-0.02` maxDD `-5.2444`
- `news_risk_high->crypto_major_4h` score `-1.2029` n `62` status `ready` deltaP `-2.3997` edge `0.0222` maxDD `-8.5004`
- `news_risk_high->commodity_1h` score `-1.6601` n `62` status `ready` deltaP `-11.9229` edge `-0.0029` maxDD `-1.1434`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
