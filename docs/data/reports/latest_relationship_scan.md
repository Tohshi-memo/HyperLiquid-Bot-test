# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-02T23:52:19.851554+00:00`
- Price records: `672`
- Market context records: `2711`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9250`

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

- `market_context_high->crypto_alt_24h` score `10.8595` n `111` status `ready` deltaP `16.3523` edge `1.1453` maxDD `-19.9486`
- `market_context_high->unknown_24h` score `8.5971` n `111` status `ready` deltaP `16.9576` edge `0.6362` maxDD `-1.626`
- `market_context_high->unknown_4h` score `0.8552` n `143` status `ready` deltaP `6.0965` edge `0.1356` maxDD `-3.7312`
- `market_context_high->crypto_major_24h` score `0.3422` n `111` status `ready` deltaP `6.5175` edge `0.7567` maxDD `-44.169`
- `market_context_high->index_4h` score `0.2704` n `143` status `ready` deltaP `12.2282` edge `0.0373` maxDD `-2.3986`
- `market_context_high->index_1h` score `-0.1191` n `143` status `ready` deltaP `3.6494` edge `0.0098` maxDD `-1.2855`
- `market_context_high->unknown_1h` score `-0.283` n `143` status `ready` deltaP `2.3` edge `0.0339` maxDD `-3.1587`
- `market_context_high->fx_1h` score `-0.3793` n `143` status `ready` deltaP `1.2992` edge `0.0041` maxDD `-0.2164`
- `market_context_high->crypto_alt_4h` score `-0.4055` n `143` status `ready` deltaP `16.3633` edge `0.2912` maxDD `-28.7261`
- `market_context_high->crypto_alt_1h` score `-0.452` n `143` status `ready` deltaP `6.5942` edge `0.0741` maxDD `-10.747`
- `market_context_high->commodity_1h` score `-0.4875` n `143` status `ready` deltaP `1.5494` edge `0.0025` maxDD `-4.3601`
- `market_context_high->metal_1h` score `-0.6756` n `143` status `ready` deltaP `-0.5015` edge `0.0013` maxDD `-3.0996`
- `market_context_high->fx_24h` score `-0.7592` n `111` status `ready` deltaP `4.7438` edge `-0.0077` maxDD `-0.6418`
- `market_context_high->fx_4h` score `-0.8948` n `143` status `ready` deltaP `-1.049` edge `0.0103` maxDD `-0.5631`
- `market_context_high->crypto_major_1h` score `-0.9058` n `143` status `ready` deltaP `3.797` edge `0.0455` maxDD `-9.622`
- `market_context_high->commodity_4h` score `-1.1577` n `143` status `ready` deltaP `3.343` edge `0.0213` maxDD `-10.0279`
- `market_context_high->commodity_24h` score `-1.2005` n `111` status `ready` deltaP `5.1849` edge `0.1209` maxDD `-12.4171`
- `market_context_high->equity_1h` score `-1.202` n `143` status `ready` deltaP `-4.336` edge `0.0126` maxDD `-2.7085`
- `market_context_high->index_24h` score `-1.4829` n `111` status `ready` deltaP `1.0652` edge `-0.0326` maxDD `-2.5127`
- `market_context_high->equity_4h` score `-1.9681` n `143` status `ready` deltaP `-0.7291` edge `-0.0187` maxDD `-5.9024`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
