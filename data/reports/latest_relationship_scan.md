# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-22T09:07:35.848495+00:00`
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

- `market_context_high->unknown_4h` score `47.4658` n `46` status `ready` deltaP `7.3171` edge `3.9067` maxDD `0.0`
- `market_context_high->crypto_major_24h` score `33.0213` n `46` status `ready` deltaP `19.4369` edge `2.6378` maxDD `-0.5817`
- `market_context_high->crypto_alt_24h` score `17.8371` n `46` status `ready` deltaP `18.2292` edge `1.3649` maxDD `0.0`
- `market_context_high->equity_24h` score `16.8024` n `46` status `ready` deltaP `14.2286` edge `1.3154` maxDD `-0.1382`
- `market_context_high->index_24h` score `5.6064` n `46` status `ready` deltaP `20.1314` edge `0.3417` maxDD `-0.03`
- `news_risk_high->crypto_major_24h` score `5.3042` n `101` status `ready` deltaP `-5.9183` edge `1.1673` maxDD `-46.1999`
- `news_risk_high->commodity_24h` score `2.958` n `101` status `ready` deltaP `36.3913` edge `0.2672` maxDD `-3.4467`
- `news_risk_high->crypto_alt_4h` score `2.5877` n `101` status `ready` deltaP `12.8215` edge `0.2511` maxDD `-7.675`
- `news_risk_high->crypto_major_4h` score `2.2054` n `101` status `ready` deltaP `16.48` edge `0.1997` maxDD `-8.0625`
- `news_risk_high->crypto_alt_1h` score `2.1874` n `101` status `ready` deltaP `13.5368` edge `0.1386` maxDD `-2.058`
- `market_context_high->index_4h` score `2.1619` n `46` status `ready` deltaP `24.9933` edge `0.0269` maxDD `-0.0692`
- `market_context_high->equity_4h` score `1.5443` n `46` status `ready` deltaP `9.9682` edge `0.0929` maxDD `-0.4529`
- `news_risk_high->crypto_major_1h` score `1.5305` n `101` status `ready` deltaP `15.1835` edge `0.0786` maxDD `-2.8494`
- `news_risk_high->crypto_alt_24h` score `1.3561` n `101` status `ready` deltaP `-5.5332` edge `0.638` maxDD `-32.7147`
- `market_context_high->crypto_alt_4h` score `1.0321` n `46` status `ready` deltaP `8.5167` edge `0.0887` maxDD `-2.7574`
- `market_context_high->equity_1h` score `0.9756` n `46` status `ready` deltaP `7.6608` edge `0.0545` maxDD `-0.2751`
- `news_risk_high->fx_4h` score `0.8861` n `101` status `ready` deltaP `15.5004` edge `0.0341` maxDD `-0.421`
- `market_context_high->index_1h` score `0.6842` n `46` status `ready` deltaP `10.6548` edge `0.0113` maxDD `-0.0249`
- `news_risk_high->metal_1h` score `0.555` n `101` status `ready` deltaP `13.9992` edge `0.0131` maxDD `-0.8144`
- `market_context_high->metal_24h` score `0.4476` n `46` status `ready` deltaP `18.4481` edge `-0.0623` maxDD `-0.2042`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
