# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-03T02:22:23.062483+00:00`
- Price records: `672`
- Market context records: `2721`
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

- `market_context_high->crypto_alt_24h` score `11.1379` n `111` status `ready` deltaP `16.3523` edge `1.1685` maxDD `-19.9486`
- `market_context_high->unknown_24h` score `8.6067` n `111` status `ready` deltaP `16.9576` edge `0.637` maxDD `-1.626`
- `market_context_high->unknown_4h` score `0.8974` n `143` status `ready` deltaP `6.249` edge `0.1381` maxDD `-3.7312`
- `market_context_high->crypto_major_24h` score `0.8383` n `111` status `ready` deltaP `6.5175` edge `0.8203` maxDD `-44.169`
- `market_context_high->index_4h` score `0.1609` n `143` status `ready` deltaP `10.8563` edge `0.0324` maxDD `-2.3986`
- `market_context_high->index_1h` score `-0.1371` n `143` status `ready` deltaP `3.4997` edge `0.0085` maxDD `-1.2855`
- `market_context_high->unknown_1h` score `-0.2111` n `143` status `ready` deltaP `2.5994` edge `0.0379` maxDD `-3.1587`
- `market_context_high->crypto_alt_4h` score `-0.4189` n `143` status `ready` deltaP `16.2108` edge `0.2911` maxDD `-28.7261`
- `market_context_high->fx_1h` score `-0.456` n `143` status `ready` deltaP `0.401` edge `0.0037` maxDD `-0.2164`
- `market_context_high->commodity_1h` score `-0.5039` n `143` status `ready` deltaP `1.3997` edge `0.0014` maxDD `-4.3601`
- `market_context_high->crypto_alt_1h` score `-0.533` n `143` status `ready` deltaP `6.2948` edge `0.0657` maxDD `-10.747`
- `market_context_high->metal_1h` score `-0.7286` n `143` status `ready` deltaP `-1.1003` edge `-0.0015` maxDD `-3.0996`
- `market_context_high->fx_24h` score `-0.9245` n `111` status `ready` deltaP `3.0077` edge `-0.0099` maxDD `-0.6418`
- `market_context_high->crypto_major_1h` score `-0.9284` n `143` status `ready` deltaP `3.6473` edge `0.0436` maxDD `-9.622`
- `market_context_high->fx_4h` score `-0.9898` n `143` status `ready` deltaP `-2.1161` edge `0.0095` maxDD `-0.5631`
- `market_context_high->equity_1h` score `-1.1756` n `143` status `ready` deltaP `-4.0366` edge `0.0128` maxDD `-2.7085`
- `market_context_high->commodity_4h` score `-1.2921` n `143` status `ready` deltaP `2.1235` edge `0.0122` maxDD `-10.0279`
- `market_context_high->commodity_24h` score `-1.4803` n `111` status `ready` deltaP `3.4488` edge `0.0966` maxDD `-12.4171`
- `market_context_high->equity_4h` score `-1.9657` n `143` status `ready` deltaP `-0.7291` edge `-0.0185` maxDD `-5.9024`
- `market_context_high->index_24h` score `-2.0706` n `111` status `ready` deltaP `-0.671` edge `-0.07` maxDD `-2.5127`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
