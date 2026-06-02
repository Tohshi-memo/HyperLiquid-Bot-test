# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-02T16:37:25.110699+00:00`
- Price records: `672`
- Market context records: `2680`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9240`

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

- `market_context_high->crypto_alt_24h` score `9.1385` n `111` status `ready` deltaP `16.0051` edge `1.0042` maxDD `-19.9486`
- `market_context_high->unknown_24h` score `8.7553` n `111` status `ready` deltaP `17.8256` edge `0.6436` maxDD `-1.626`
- `market_context_high->crypto_alt_4h` score `2.5191` n `131` status `ready` deltaP `19.9137` edge `0.361` maxDD `-16.7069`
- `market_context_high->unknown_4h` score `1.4365` n `131` status `ready` deltaP `7.5568` edge `0.1743` maxDD `-3.7312`
- `market_context_high->index_4h` score `0.0775` n `131` status `ready` deltaP `9.8527` edge `0.0284` maxDD `-2.3986`
- `market_context_high->crypto_major_4h` score `-0.0089` n `131` status `ready` deltaP `8.0106` edge `0.2036` maxDD `-16.3181`
- `market_context_high->index_1h` score `-0.1461` n `140` status `ready` deltaP `3.101` edge `0.01` maxDD `-1.2855`
- `market_context_high->fx_24h` score `-0.2652` n `111` status `ready` deltaP `9.7786` edge `-0.0001` maxDD `-0.6418`
- `market_context_high->unknown_1h` score `-0.3195` n `140` status `ready` deltaP `2.4893` edge `0.0296` maxDD `-3.1587`
- `market_context_high->commodity_1h` score `-0.4065` n `140` status `ready` deltaP `2.1771` edge `0.0087` maxDD `-4.3601`
- `market_context_high->fx_1h` score `-0.4607` n `140` status `ready` deltaP `0.3122` edge `0.0039` maxDD `-0.2164`
- `market_context_high->commodity_24h` score `-0.5179` n `111` status `ready` deltaP `7.9627` edge `0.1899` maxDD `-12.4171`
- `market_context_high->crypto_alt_1h` score `-0.5193` n `140` status `ready` deltaP `6.8435` edge `0.0638` maxDD `-10.747`
- `market_context_high->index_24h` score `-0.5295` n `111` status `ready` deltaP `5.7527` edge `0.0156` maxDD `-2.5127`
- `market_context_high->fx_4h` score `-0.567` n `131` status `ready` deltaP `0.8436` edge `0.0125` maxDD `-0.5631`
- `market_context_high->metal_1h` score `-0.7701` n `140` status `ready` deltaP `-1.8435` edge `-0.0041` maxDD `-2.9203`
- `market_context_high->crypto_major_1h` score `-0.977` n `140` status `ready` deltaP `3.6869` edge `0.0371` maxDD `-9.622`
- `market_context_high->equity_1h` score `-1.2015` n `140` status `ready` deltaP `-4.3156` edge `0.0125` maxDD `-2.7085`
- `market_context_high->crypto_major_24h` score `-1.2542` n `111` status `ready` deltaP `5.9967` edge `0.5555` maxDD `-44.169`
- `market_context_high->commodity_4h` score `-1.2566` n `131` status `ready` deltaP `3.2862` edge `0.009` maxDD `-10.0279`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
