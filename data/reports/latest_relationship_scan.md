# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-03T07:07:25.675628+00:00`
- Price records: `672`
- Market context records: `2741`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9230`

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
- `market_context_high->unknown_24h` score `8.4102` n `111` status `ready` deltaP `17.3048` edge `0.6183` maxDD `-1.6255`
- `market_context_high->crypto_major_24h` score `1.3929` n `111` status `ready` deltaP `6.5175` edge `0.8914` maxDD `-44.169`
- `market_context_high->unknown_4h` score `1.1513` n `143` status `ready` deltaP `7.3161` edge `0.1525` maxDD `-3.7602`
- `market_context_high->index_4h` score `0.0995` n `143` status `ready` deltaP `10.2465` edge `0.0286` maxDD `-2.3986`
- `market_context_high->unknown_1h` score `-0.086` n `143` status `ready` deltaP `3.4976` edge `0.0426` maxDD `-3.1801`
- `market_context_high->index_1h` score `-0.1955` n `143` status `ready` deltaP `2.6015` edge `0.007` maxDD `-1.2855`
- `market_context_high->fx_1h` score `-0.5087` n `143` status `ready` deltaP `-0.1978` edge `0.0033` maxDD `-0.2164`
- `market_context_high->commodity_1h` score `-0.6075` n `143` status `ready` deltaP `0.0524` edge `-0.0029` maxDD `-4.3601`
- `market_context_high->crypto_alt_1h` score `-0.6212` n `143` status `ready` deltaP `6.1451` edge `0.0554` maxDD `-10.747`
- `market_context_high->crypto_alt_4h` score `-0.6275` n `143` status `ready` deltaP `16.3633` edge `0.2727` maxDD `-28.7261`
- `market_context_high->metal_1h` score `-0.7645` n `143` status `ready` deltaP `-1.25` edge `-0.0051` maxDD `-3.0996`
- `market_context_high->crypto_major_1h` score `-0.9534` n `143` status `ready` deltaP `3.6473` edge `0.0404` maxDD `-9.622`
- `market_context_high->fx_4h` score `-1.0895` n `143` status `ready` deltaP `-3.1831` edge `0.0083` maxDD `-0.5631`
- `market_context_high->fx_24h` score `-1.2447` n `111` status `ready` deltaP `-0.2909` edge `-0.0146` maxDD `-0.6418`
- `market_context_high->equity_1h` score `-1.3262` n `143` status `ready` deltaP `-5.1337` edge `0.007` maxDD `-2.6634`
- `market_context_high->commodity_4h` score `-1.5355` n `143` status `ready` deltaP `0.2943` edge `-0.0068` maxDD `-10.0279`
- `market_context_high->commodity_24h` score `-1.7478` n `111` status `ready` deltaP `2.5807` edge `0.0681` maxDD `-12.4171`
- `market_context_high->equity_4h` score `-2.0459` n `143` status `ready` deltaP `-1.2493` edge `-0.0242` maxDD `-5.7037`
- `market_context_high->crypto_major_4h` score `-2.2835` n `143` status `ready` deltaP `6.9046` edge `0.1518` maxDD `-32.2466`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
