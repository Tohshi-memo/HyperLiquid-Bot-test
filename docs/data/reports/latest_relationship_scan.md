# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-03T06:37:24.456754+00:00`
- Price records: `672`
- Market context records: `2739`
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

- `market_context_high->crypto_alt_24h` score `11.0335` n `111` status `ready` deltaP `16.3523` edge `1.1598` maxDD `-19.9486`
- `market_context_high->unknown_24h` score `8.4618` n `111` status `ready` deltaP `17.3048` edge `0.6226` maxDD `-1.6255`
- `market_context_high->crypto_major_24h` score `1.4061` n `111` status `ready` deltaP `6.5175` edge `0.8931` maxDD `-44.169`
- `market_context_high->unknown_4h` score `1.196` n `143` status `ready` deltaP `7.6209` edge `0.1542` maxDD `-3.7602`
- `market_context_high->index_4h` score `0.0941` n `143` status `ready` deltaP `10.2465` edge `0.0279` maxDD `-2.3986`
- `market_context_high->unknown_1h` score `-0.1196` n `143` status `ready` deltaP `3.1982` edge `0.0418` maxDD `-3.1801`
- `market_context_high->index_1h` score `-0.1962` n `143` status `ready` deltaP `2.6015` edge `0.0069` maxDD `-1.2855`
- `market_context_high->fx_1h` score `-0.5087` n `143` status `ready` deltaP `-0.1978` edge `0.0033` maxDD `-0.2164`
- `market_context_high->crypto_alt_4h` score `-0.5421` n `143` status `ready` deltaP `16.5157` edge `0.2788` maxDD `-28.7261`
- `market_context_high->commodity_1h` score `-0.5826` n `143` status `ready` deltaP `0.3518` edge `-0.0017` maxDD `-4.3601`
- `market_context_high->crypto_alt_1h` score `-0.6157` n `143` status `ready` deltaP `6.1451` edge `0.0561` maxDD `-10.747`
- `market_context_high->metal_1h` score `-0.7661` n `143` status `ready` deltaP `-1.25` edge `-0.0053` maxDD `-3.0996`
- `market_context_high->crypto_major_1h` score `-0.9573` n `143` status `ready` deltaP `3.6473` edge `0.0399` maxDD `-9.622`
- `market_context_high->fx_4h` score `-1.0603` n `143` status `ready` deltaP `-2.8783` edge `0.0087` maxDD `-0.5631`
- `market_context_high->fx_24h` score `-1.211` n `111` status `ready` deltaP `0.0563` edge `-0.0141` maxDD `-0.6418`
- `market_context_high->equity_1h` score `-1.3478` n `143` status `ready` deltaP `-5.2834` edge `0.0062` maxDD `-2.6634`
- `market_context_high->commodity_4h` score `-1.4962` n `143` status `ready` deltaP `0.5991` edge `-0.0038` maxDD `-10.0279`
- `market_context_high->commodity_24h` score `-1.7189` n `111` status `ready` deltaP `2.5807` edge `0.0718` maxDD `-12.4171`
- `market_context_high->equity_4h` score `-2.0603` n `143` status `ready` deltaP `-1.2493` edge `-0.0254` maxDD `-5.7037`
- `market_context_high->crypto_major_4h` score `-2.2686` n `143` status `ready` deltaP `6.9046` edge `0.1537` maxDD `-32.2466`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
