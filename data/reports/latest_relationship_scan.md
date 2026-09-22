# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-22T10:37:40.459516+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9954`

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

- `market_context_high->unknown_4h` score `47.1502` n `46` status `ready` deltaP `7.3171` edge `3.8804` maxDD `0.0`
- `market_context_high->crypto_major_24h` score `32.3704` n `46` status `ready` deltaP `18.3953` edge `2.5905` maxDD `-0.5817`
- `market_context_high->crypto_alt_24h` score `17.2762` n `46` status `ready` deltaP `17.1875` edge `1.3251` maxDD `0.0`
- `market_context_high->equity_24h` score `16.6539` n `46` status `ready` deltaP `13.7078` edge `1.3065` maxDD `-0.1382`
- `market_context_high->index_24h` score `5.5908` n `46` status `ready` deltaP `20.1314` edge `0.3404` maxDD `-0.03`
- `news_risk_high->crypto_major_24h` score `4.6532` n `101` status `ready` deltaP `-6.9599` edge `1.12` maxDD `-46.1999`
- `news_risk_high->commodity_24h` score `3.0593` n `101` status `ready` deltaP `37.2593` edge `0.2744` maxDD `-3.4467`
- `news_risk_high->crypto_alt_4h` score `2.4777` n `101` status `ready` deltaP `12.2117` edge `0.246` maxDD `-7.675`
- `news_risk_high->crypto_alt_1h` score `2.2282` n `101` status `ready` deltaP `13.8362` edge `0.14` maxDD `-2.058`
- `market_context_high->index_4h` score `2.1631` n `46` status `ready` deltaP `24.9933` edge `0.027` maxDD `-0.0692`
- `news_risk_high->crypto_major_4h` score `2.0774` n `101` status `ready` deltaP `15.8702` edge `0.1931` maxDD `-8.0625`
- `news_risk_high->crypto_major_1h` score `1.558` n `101` status `ready` deltaP `15.4829` edge `0.0789` maxDD `-2.8494`
- `market_context_high->equity_4h` score `1.4995` n `46` status `ready` deltaP `9.6633` edge `0.0912` maxDD `-0.4529`
- `market_context_high->equity_1h` score `0.9672` n `46` status `ready` deltaP `7.6608` edge `0.0538` maxDD `-0.2751`
- `news_risk_high->fx_4h` score `0.9335` n `101` status `ready` deltaP `15.9578` edge `0.035` maxDD `-0.421`
- `market_context_high->crypto_alt_4h` score `0.9221` n `46` status `ready` deltaP `7.9069` edge `0.0836` maxDD `-2.7574`
- `news_risk_high->crypto_alt_24h` score `0.7952` n `101` status `ready` deltaP `-6.5749` edge `0.5982` maxDD `-32.7147`
- `market_context_high->index_1h` score `0.6854` n `46` status `ready` deltaP `10.6548` edge `0.0114` maxDD `-0.0249`
- `market_context_high->metal_24h` score `0.6174` n `46` status `ready` deltaP `19.4898` edge `-0.0551` maxDD `-0.2042`
- `news_risk_high->metal_1h` score `0.5706` n `101` status `ready` deltaP `14.1489` edge `0.0134` maxDD `-0.8144`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
