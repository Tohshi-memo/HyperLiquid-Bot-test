# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-11T07:07:27.356005+00:00`
- Price records: `672`
- Market context records: `6367`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11120`

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

- `news_risk_high->crypto_alt_24h` score `14.628` n `32` status `ready` deltaP `39.7569` edge `0.9687` maxDD `-0.5131`
- `news_risk_high->fx_24h` score `6.3088` n `32` status `ready` deltaP `52.4306` edge `0.1762` maxDD `0.0`
- `news_risk_high->crypto_major_24h` score `4.3909` n `32` status `ready` deltaP `17.5347` edge `0.524` maxDD `-4.2368`
- `news_risk_high->fx_4h` score `4.0388` n `32` status `ready` deltaP `41.8445` edge `0.0622` maxDD `-0.0345`
- `news_risk_high->commodity_24h` score `3.9783` n `32` status `ready` deltaP `34.375` edge `0.1229` maxDD `-0.3101`
- `news_risk_high->fx_1h` score `2.362` n `32` status `ready` deltaP `28.4431` edge `0.0211` maxDD `-0.1113`
- `news_risk_high->crypto_major_1h` score `1.5512` n `32` status `ready` deltaP `15.0262` edge `0.1454` maxDD `-2.0691`
- `news_risk_high->crypto_alt_1h` score `0.9205` n `32` status `ready` deltaP `11.4708` edge `0.0877` maxDD `-1.6923`
- `market_context_high->metal_4h` score `0.5323` n `211` status `ready` deltaP `15.8543` edge `0.0422` maxDD `-2.7056`
- `market_context_high->unknown_1h` score `0.2079` n `220` status `ready` deltaP `-6.7746` edge `0.1633` maxDD `-3.7317`
- `market_context_high->index_4h` score `0.1144` n `211` status `ready` deltaP `8.3047` edge `0.0218` maxDD `-0.4108`
- `news_risk_high->unknown_1h` score `-0.3939` n `32` status `ready` deltaP `5.7822` edge `-0.0369` maxDD `-0.7581`
- `market_context_high->metal_1h` score `-0.4106` n `220` status `ready` deltaP `3.3642` edge `0.0027` maxDD `-1.8877`
- `market_context_high->metal_24h` score `-0.5498` n `132` status `ready` deltaP `16.209` edge `0.0783` maxDD `-11.8809`
- `market_context_high->commodity_24h` score `-0.5519` n `132` status `ready` deltaP `-3.7879` edge `0.1409` maxDD `-6.2457`
- `market_context_high->index_1h` score `-0.616` n `220` status `ready` deltaP `-1.5024` edge `0.003` maxDD `-0.7564`
- `market_context_high->fx_1h` score `-0.6741` n `220` status `ready` deltaP `-0.1933` edge `-0.0015` maxDD `-0.9376`
- `news_risk_high->index_24h` score `-0.712` n `32` status `ready` deltaP `0.5208` edge `-0.0076` maxDD `-2.3058`
- `news_risk_high->metal_1h` score `-0.7169` n `32` status `ready` deltaP `-2.5449` edge `-0.0252` maxDD `-1.6464`
- `market_context_high->equity_4h` score `-0.9634` n `211` status `ready` deltaP `6.3454` edge `0.0473` maxDD `-8.2573`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
