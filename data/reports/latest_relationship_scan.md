# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-02T22:10:51.172781+00:00`
- Price records: `672`
- Market context records: `2704`
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

- `market_context_high->crypto_alt_24h` score `10.4347` n `111` status `ready` deltaP `16.3523` edge `1.1099` maxDD `-19.9486`
- `market_context_high->unknown_24h` score `8.593` n `111` status `ready` deltaP `17.1312` edge `0.6347` maxDD `-1.626`
- `market_context_high->unknown_4h` score `0.8346` n `143` status `ready` deltaP `5.9441` edge `0.1349` maxDD `-3.7312`
- `market_context_high->index_4h` score `0.2578` n `143` status `ready` deltaP `12.0758` edge `0.0367` maxDD `-2.3986`
- `market_context_high->crypto_major_24h` score `-0.1406` n `111` status `ready` deltaP `6.5175` edge `0.6948` maxDD `-44.169`
- `market_context_high->index_1h` score `-0.1604` n `143` status `ready` deltaP `3.0506` edge `0.0085` maxDD `-1.2855`
- `market_context_high->unknown_1h` score `-0.283` n `143` status `ready` deltaP `2.4497` edge `0.0329` maxDD `-3.1587`
- `market_context_high->fx_1h` score `-0.4284` n `143` status `ready` deltaP `0.7004` edge `0.004` maxDD `-0.2164`
- `market_context_high->commodity_1h` score `-0.472` n `143` status `ready` deltaP `1.8488` edge `0.0025` maxDD `-4.3601`
- `market_context_high->crypto_alt_4h` score `-0.5425` n `143` status `ready` deltaP `16.2108` edge `0.2808` maxDD `-28.7261`
- `market_context_high->crypto_alt_1h` score `-0.5829` n `143` status `ready` deltaP `5.9954` edge `0.0613` maxDD `-10.747`
- `market_context_high->fx_24h` score `-0.6391` n `111` status `ready` deltaP `5.9591` edge `-0.0058` maxDD `-0.6418`
- `market_context_high->metal_1h` score `-0.7543` n `143` status `ready` deltaP `-1.3997` edge `-0.0028` maxDD `-3.0996`
- `market_context_high->fx_4h` score `-0.8814` n `143` status `ready` deltaP `-0.8966` edge `0.0104` maxDD `-0.5631`
- `market_context_high->commodity_24h` score `-1.0114` n `111` status `ready` deltaP `6.2266` edge `0.1382` maxDD `-12.4171`
- `market_context_high->crypto_major_1h` score `-1.0212` n `143` status `ready` deltaP `3.0485` edge `0.0357` maxDD `-9.622`
- `market_context_high->commodity_4h` score `-1.0532` n `143` status `ready` deltaP `4.2577` edge `0.0286` maxDD `-10.0279`
- `market_context_high->index_24h` score `-1.2153` n `111` status `ready` deltaP `2.2804` edge `-0.0184` maxDD `-2.5127`
- `market_context_high->equity_1h` score `-1.2511` n `143` status `ready` deltaP `-4.4857` edge `0.0095` maxDD `-2.7085`
- `market_context_high->equity_4h` score `-1.9829` n `143` status `ready` deltaP `-1.034` edge `-0.0179` maxDD `-5.9024`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
