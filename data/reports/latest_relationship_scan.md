# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-07T14:07:24.313640+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4099`

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

- `market_context_high->unknown_4h` score `223.6926` n `32` status `ready` deltaP `2.5152` edge `18.6407` maxDD `-0.3135`
- `market_context_high->fx_4h` score `3.4418` n `32` status `ready` deltaP `36.5854` edge `0.0519` maxDD `-0.0521`
- `market_context_high->equity_1h` score `3.0759` n `37` status `ready` deltaP `8.5613` edge `0.2452` maxDD `-2.3425`
- `market_context_high->index_4h` score `1.8024` n `32` status `ready` deltaP `23.5518` edge `0.0402` maxDD `-2.4279`
- `news_risk_high->equity_4h` score `1.1043` n `58` status `ready` deltaP `9.5826` edge `0.1516` maxDD `-4.2454`
- `market_context_high->crypto_major_1h` score `0.7004` n `37` status `ready` deltaP `9.3017` edge `0.0549` maxDD `-3.0172`
- `news_risk_high->fx_24h` score `0.6811` n `58` status `ready` deltaP `0.886` edge `0.0772` maxDD `-0.1077`
- `news_risk_high->index_4h` score `0.5442` n `58` status `ready` deltaP `14.3923` edge `0.0216` maxDD `-0.4888`
- `market_context_high->fx_1h` score `0.4948` n `37` status `ready` deltaP `7.9706` edge `0.0152` maxDD `-0.1681`
- `market_context_high->crypto_alt_1h` score `0.368` n `37` status `ready` deltaP `10.3496` edge `0.0597` maxDD `-3.1881`
- `news_risk_high->index_24h` score `0.3082` n `58` status `ready` deltaP `9.0936` edge `0.1457` maxDD `-6.6786`
- `market_context_high->index_1h` score `0.2733` n `37` status `ready` deltaP `1.6508` edge `0.0388` maxDD `-0.1621`
- `news_risk_high->index_1h` score `0.2311` n `58` status `ready` deltaP `10.6442` edge `0.004` maxDD `-0.2931`
- `market_context_high->commodity_1h` score `0.1693` n `37` status `ready` deltaP `9.9167` edge `0.0102` maxDD `-1.7019`
- `news_risk_high->equity_1h` score `0.0043` n `58` status `ready` deltaP `0.8259` edge `0.05` maxDD `-1.396`
- `news_risk_high->fx_4h` score `-0.0485` n `58` status `ready` deltaP `4.9044` edge `0.0053` maxDD `-0.2038`
- `market_context_high->metal_1h` score `-0.0988` n `37` status `ready` deltaP `0.6029` edge `0.0161` maxDD `-0.6226`
- `news_risk_high->fx_1h` score `-0.1388` n `58` status `ready` deltaP `2.705` edge `0.0027` maxDD `-0.0826`
- `market_context_high->commodity_4h` score `-0.2052` n `32` status `ready` deltaP `0.0` edge `0.0191` maxDD `-1.633`
- `news_risk_high->metal_1h` score `-0.6412` n `58` status `ready` deltaP `-5.9209` edge `-0.007` maxDD `-0.5256`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
