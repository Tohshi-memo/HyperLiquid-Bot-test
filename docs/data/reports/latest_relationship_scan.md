# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-22T09:22:35.167800+00:00`
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

- `market_context_high->unknown_4h` score `47.3374` n `46` status `ready` deltaP `7.3171` edge `3.896` maxDD `0.0`
- `market_context_high->crypto_major_24h` score `32.9102` n `46` status `ready` deltaP `19.2633` edge `2.6297` maxDD `-0.5817`
- `market_context_high->crypto_alt_24h` score `17.7404` n `46` status `ready` deltaP `18.0556` edge `1.358` maxDD `0.0`
- `market_context_high->equity_24h` score `16.7952` n `46` status `ready` deltaP `14.2286` edge `1.3148` maxDD `-0.1382`
- `market_context_high->index_24h` score `5.6052` n `46` status `ready` deltaP `20.1314` edge `0.3416` maxDD `-0.03`
- `news_risk_high->crypto_major_24h` score `5.1931` n `101` status `ready` deltaP `-6.0919` edge `1.1592` maxDD `-46.1999`
- `news_risk_high->commodity_24h` score `2.9756` n `101` status `ready` deltaP `36.5649` edge `0.2683` maxDD `-3.4467`
- `news_risk_high->crypto_alt_4h` score `2.5841` n `101` status `ready` deltaP `12.8215` edge `0.2508` maxDD `-7.675`
- `news_risk_high->crypto_major_4h` score `2.2042` n `101` status `ready` deltaP `16.48` edge `0.1996` maxDD `-8.0625`
- `news_risk_high->crypto_alt_1h` score `2.2006` n `101` status `ready` deltaP `13.6865` edge `0.1387` maxDD `-2.058`
- `market_context_high->index_4h` score `2.1777` n `46` status `ready` deltaP `25.1458` edge `0.0272` maxDD `-0.0692`
- `market_context_high->equity_4h` score `1.5673` n `46` status `ready` deltaP `10.1207` edge `0.0938` maxDD `-0.4529`
- `news_risk_high->crypto_major_1h` score `1.5269` n `101` status `ready` deltaP `15.1835` edge `0.0783` maxDD `-2.8494`
- `news_risk_high->crypto_alt_24h` score `1.2595` n `101` status `ready` deltaP `-5.7068` edge `0.6311` maxDD `-32.7147`
- `market_context_high->crypto_alt_4h` score `1.0285` n `46` status `ready` deltaP `8.5167` edge `0.0884` maxDD `-2.7574`
- `market_context_high->equity_1h` score `0.9768` n `46` status `ready` deltaP `7.6608` edge `0.0546` maxDD `-0.2751`
- `news_risk_high->fx_4h` score `0.8873` n `101` status `ready` deltaP `15.5004` edge `0.0342` maxDD `-0.421`
- `market_context_high->index_1h` score `0.6854` n `46` status `ready` deltaP `10.6548` edge `0.0114` maxDD `-0.0249`
- `news_risk_high->metal_1h` score `0.555` n `101` status `ready` deltaP `13.9992` edge `0.0131` maxDD `-0.8144`
- `market_context_high->metal_24h` score `0.4771` n `46` status `ready` deltaP `18.6217` edge `-0.061` maxDD `-0.2042`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
