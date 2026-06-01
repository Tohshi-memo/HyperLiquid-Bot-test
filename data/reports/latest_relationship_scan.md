# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-01T11:07:21.785936+00:00`
- Price records: `672`
- Market context records: `2555`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9252`

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

- `market_context_high->crypto_alt_4h` score `5.6943` n `149` status `ready` deltaP `24.7084` edge `0.5777` maxDD `-15.4319`
- `market_context_high->unknown_24h` score `5.3468` n `118` status `ready` deltaP `19.3032` edge `0.3497` maxDD `-1.626`
- `market_context_high->crypto_major_24h` score `4.9225` n `118` status `ready` deltaP `12.1704` edge `0.5944` maxDD `-15.2264`
- `market_context_high->crypto_major_4h` score `3.9835` n `149` status `ready` deltaP `17.7535` edge `0.3946` maxDD `-10.1468`
- `market_context_high->unknown_4h` score `1.7839` n `149` status `ready` deltaP `10.3096` edge `0.1849` maxDD `-3.7312`
- `market_context_high->crypto_alt_1h` score `1.2133` n `149` status `ready` deltaP `9.8762` edge `0.154` maxDD `-6.1656`
- `market_context_high->equity_24h` score `1.2` n `118` status `ready` deltaP `18.9972` edge `0.0317` maxDD `-2.0014`
- `market_context_high->index_24h` score `0.7581` n `118` status `ready` deltaP `7.1328` edge `0.1137` maxDD `-2.5127`
- `market_context_high->crypto_major_1h` score `0.6838` n `149` status `ready` deltaP `8.2345` edge `0.1215` maxDD `-4.2199`
- `market_context_high->crypto_alt_24h` score `0.169` n `118` status `ready` deltaP `-0.9592` edge `0.6685` maxDD `-39.2351`
- `market_context_high->index_4h` score `-0.0226` n `149` status `ready` deltaP `6.6848` edge `0.0377` maxDD `-2.3986`
- `market_context_high->index_1h` score `-0.2041` n `149` status `ready` deltaP `3.2995` edge `0.0104` maxDD `-1.2855`
- `market_context_high->unknown_1h` score `-0.2437` n `149` status `ready` deltaP `2.7157` edge `0.0306` maxDD `-2.8543`
- `market_context_high->metal_1h` score `-0.4589` n `149` status `ready` deltaP `1.0117` edge `0.0092` maxDD `-2.9823`
- `market_context_high->fx_1h` score `-0.5417` n `149` status `ready` deltaP `0.635` edge `0.0041` maxDD `-0.278`
- `market_context_high->commodity_1h` score `-0.5446` n `149` status `ready` deltaP `4.2077` edge `0.0144` maxDD `-4.3601`
- `market_context_high->fx_24h` score `-0.7334` n `118` status `ready` deltaP `1.4301` edge `0.0041` maxDD `-1.946`
- `market_context_high->equity_1h` score `-0.8237` n `149` status `ready` deltaP `-0.4481` edge `0.0182` maxDD `-2.7085`
- `market_context_high->metal_4h` score `-0.8576` n `149` status `ready` deltaP `3.6872` edge `0.0427` maxDD `-4.7664`
- `market_context_high->fx_4h` score `-0.8951` n `149` status `ready` deltaP `-0.1535` edge `0.0124` maxDD `-0.8774`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
