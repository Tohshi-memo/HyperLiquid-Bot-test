# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-22T08:37:27.390908+00:00`
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

- `market_context_high->unknown_4h` score `47.5786` n `46` status `ready` deltaP `7.3171` edge `3.9161` maxDD `0.0`
- `market_context_high->crypto_major_24h` score `33.2603` n `46` status `ready` deltaP `19.7841` edge `2.6554` maxDD `-0.5817`
- `market_context_high->crypto_alt_24h` score `18.0713` n `46` status `ready` deltaP `18.5764` edge `1.3821` maxDD `0.0`
- `market_context_high->equity_24h` score `16.8216` n `46` status `ready` deltaP `14.2286` edge `1.317` maxDD `-0.1382`
- `market_context_high->index_24h` score `5.6076` n `46` status `ready` deltaP `20.1314` edge `0.3418` maxDD `-0.03`
- `news_risk_high->crypto_major_24h` score `5.5431` n `101` status `ready` deltaP `-5.5711` edge `1.1849` maxDD `-46.1999`
- `news_risk_high->commodity_24h` score `2.9227` n `101` status `ready` deltaP `36.044` edge `0.265` maxDD `-3.4467`
- `news_risk_high->crypto_alt_4h` score `2.5949` n `101` status `ready` deltaP `12.8215` edge `0.2517` maxDD `-7.675`
- `news_risk_high->crypto_major_4h` score `2.1982` n `101` status `ready` deltaP `16.48` edge `0.1991` maxDD `-8.0625`
- `news_risk_high->crypto_alt_1h` score `2.1839` n `101` status `ready` deltaP `13.3871` edge `0.1393` maxDD `-2.058`
- `market_context_high->index_4h` score `2.1279` n `46` status `ready` deltaP `24.6884` edge `0.0261` maxDD `-0.0692`
- `news_risk_high->crypto_alt_24h` score `1.5903` n `101` status `ready` deltaP `-5.186` edge `0.6552` maxDD `-32.7147`
- `news_risk_high->crypto_major_1h` score `1.5413` n `101` status `ready` deltaP `15.1835` edge `0.0795` maxDD `-2.8494`
- `market_context_high->equity_4h` score `1.4851` n `46` status `ready` deltaP `9.6633` edge `0.09` maxDD `-0.4529`
- `market_context_high->crypto_alt_4h` score `1.0393` n `46` status `ready` deltaP `8.5167` edge `0.0893` maxDD `-2.7574`
- `market_context_high->equity_1h` score `0.9708` n `46` status `ready` deltaP `7.6608` edge `0.0541` maxDD `-0.2751`
- `news_risk_high->fx_4h` score `0.8849` n `101` status `ready` deltaP `15.5004` edge `0.034` maxDD `-0.421`
- `market_context_high->index_1h` score `0.683` n `46` status `ready` deltaP `10.6548` edge `0.0112` maxDD `-0.0249`
- `news_risk_high->metal_1h` score `0.5574` n `101` status `ready` deltaP `13.9992` edge `0.0133` maxDD `-0.8144`
- `market_context_high->crypto_major_1h` score `0.4534` n `46` status `ready` deltaP `0.6119` edge `0.086` maxDD `-2.1836`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
