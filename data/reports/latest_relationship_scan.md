# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-07T11:52:30.481979+00:00`
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

- `market_context_high->equity_1h` score `3.5349` n `35` status `ready` deltaP `12.1086` edge `0.2598` maxDD `-2.3425`
- `news_risk_high->equity_4h` score `1.2288` n `62` status `ready` deltaP `11.2264` edge `0.1566` maxDD `-4.2454`
- `market_context_high->crypto_major_1h` score `0.7733` n `35` status `ready` deltaP `9.5381` edge `0.0594` maxDD `-3.0172`
- `news_risk_high->index_4h` score `0.6251` n `62` status `ready` deltaP `11.8607` edge `0.0208` maxDD `-0.4888`
- `market_context_high->fx_1h` score `0.578` n `35` status `ready` deltaP `8.9649` edge `0.0155` maxDD `-0.1681`
- `market_context_high->index_1h` score `0.5752` n `35` status `ready` deltaP `5.0342` edge `0.0414` maxDD `-0.1621`
- `market_context_high->crypto_alt_1h` score `0.3694` n `35` status `ready` deltaP `10.586` edge `0.0583` maxDD `-3.1881`
- `news_risk_high->index_24h` score `0.3549` n `62` status `ready` deltaP `10.2766` edge `0.1438` maxDD `-6.6786`
- `market_context_high->commodity_1h` score `0.214` n `35` status `ready` deltaP `10.7613` edge `0.0103` maxDD `-1.7019`
- `market_context_high->metal_1h` score `0.0756` n `35` status `ready` deltaP `3.6869` edge `0.0179` maxDD `-0.6226`
- `news_risk_high->fx_24h` score `0.053` n `62` status `ready` deltaP `-2.7442` edge `0.0669` maxDD `-0.2016`
- `news_risk_high->index_1h` score `0.0466` n `62` status `ready` deltaP `7.2001` edge `0.0033` maxDD `-0.2931`
- `news_risk_high->equity_1h` score `-0.1017` n `62` status `ready` deltaP `-0.7485` edge `0.0469` maxDD `-1.396`
- `news_risk_high->fx_1h` score `-0.148` n `62` status `ready` deltaP `2.5594` edge `0.0025` maxDD `-0.0826`
- `news_risk_high->fx_4h` score `-0.2025` n `62` status `ready` deltaP `2.1194` edge `0.0045` maxDD `-0.2336`
- `news_risk_high->metal_1h` score `-0.5314` n `62` status `ready` deltaP `-3.8246` edge `-0.0069` maxDD `-0.5256`
- `news_risk_high->metal_4h` score `-0.9317` n `62` status `ready` deltaP `1.726` edge `-0.0404` maxDD `-1.5773`
- `news_risk_high->crypto_alt_1h` score `-1.1322` n `62` status `ready` deltaP `-1.3956` edge `-0.0203` maxDD `-5.2444`
- `news_risk_high->crypto_major_4h` score `-1.2202` n `62` status `ready` deltaP `-2.5521` edge `0.021` maxDD `-8.5004`
- `news_risk_high->commodity_1h` score `-1.6482` n `62` status `ready` deltaP `-11.7732` edge `-0.0029` maxDD `-1.1434`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
