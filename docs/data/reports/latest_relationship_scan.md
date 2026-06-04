# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-04T20:37:21.481459+00:00`
- Price records: `672`
- Market context records: `2901`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `6912`

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

- `market_context_high->crypto_alt_24h` score `10.9827` n `142` status `ready` deltaP `10.5145` edge `1.2368` maxDD `-22.6673`
- `market_context_high->equity_24h` score `5.9317` n `142` status `ready` deltaP `12.2065` edge `0.6133` maxDD `-12.6963`
- `market_context_high->unknown_24h` score `5.2581` n `142` status `ready` deltaP `10.7614` edge `0.4129` maxDD `-1.7175`
- `market_context_high->index_24h` score `2.2018` n `142` status `ready` deltaP `10.2382` edge `0.2133` maxDD `-2.5127`
- `market_context_high->commodity_24h` score `1.7424` n `142` status `ready` deltaP `15.5516` edge `0.3509` maxDD `-12.4171`
- `market_context_high->index_4h` score `0.4578` n `142` status `ready` deltaP `12.996` edge `0.0562` maxDD `-2.3986`
- `market_context_high->unknown_4h` score `0.158` n `142` status `ready` deltaP `4.966` edge `0.0854` maxDD `-3.7602`
- `market_context_high->equity_4h` score `-0.0039` n `142` status `ready` deltaP `5.316` edge `0.1022` maxDD `-5.7037`
- `market_context_high->index_1h` score `-0.0711` n `142` status `ready` deltaP `3.7489` edge `0.0153` maxDD `-1.2855`
- `market_context_high->unknown_1h` score `-0.2462` n `142` status `ready` deltaP `4.6302` edge `0.0217` maxDD `-3.1801`
- `market_context_high->crypto_alt_1h` score `-0.5603` n `142` status `ready` deltaP `5.5453` edge `0.0672` maxDD `-10.747`
- `market_context_high->fx_1h` score `-0.5646` n `142` status `ready` deltaP `-0.837` edge `0.0029` maxDD `-0.2164`
- `market_context_high->equity_1h` score `-0.5718` n `142` status `ready` deltaP `-0.6536` edge `0.04` maxDD `-2.6634`
- `market_context_high->commodity_1h` score `-0.6023` n `142` status `ready` deltaP `-0.5819` edge `0.002` maxDD `-4.3601`
- `market_context_high->crypto_alt_4h` score `-0.6261` n `142` status `ready` deltaP `14.4903` edge `0.2853` maxDD `-28.7261`
- `market_context_high->crypto_major_1h` score `-0.6676` n `142` status `ready` deltaP `5.7224` edge `0.0632` maxDD `-9.622`
- `market_context_high->metal_1h` score `-0.6917` n `142` status `ready` deltaP `-0.6157` edge `0.0` maxDD `-3.0996`
- `market_context_high->fx_4h` score `-1.1261` n `142` status `ready` deltaP `-3.2957` edge `0.006` maxDD `-0.5631`
- `market_context_high->commodity_4h` score `-1.1561` n `142` status `ready` deltaP `3.2098` edge `0.0224` maxDD `-10.0279`
- `market_context_high->fx_24h` score `-1.3056` n `142` status `ready` deltaP `-1.7116` edge `-0.0102` maxDD `-0.6418`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
