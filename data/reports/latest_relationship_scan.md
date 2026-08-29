# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-29T14:37:27.711385+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11444`

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

- `news_risk_high->unknown_24h` score `48.1521` n `58` status `ready` deltaP `13.4638` edge `3.9957` maxDD `-3.1563`
- `news_risk_high->crypto_alt_24h` score `22.8035` n `58` status `ready` deltaP `34.8419` edge `1.9332` maxDD `-17.8818`
- `market_context_high->unknown_24h` score `8.2392` n `104` status `ready` deltaP `19.5646` edge `0.6294` maxDD `-3.1917`
- `news_risk_high->unknown_4h` score `6.3775` n `80` status `ready` deltaP `11.5854` edge `0.5132` maxDD `-1.7183`
- `market_context_high->metal_24h` score `4.4252` n `104` status `ready` deltaP `32.1581` edge `0.2563` maxDD `-3.1535`
- `news_risk_high->unknown_1h` score `2.6308` n `80` status `ready` deltaP `5.3743` edge `0.2191` maxDD `-0.8558`
- `news_risk_high->fx_4h` score `2.468` n `80` status `ready` deltaP `35.7317` edge `0.0224` maxDD `-0.3953`
- `market_context_high->unknown_4h` score `2.3998` n `115` status `ready` deltaP `17.455` edge `0.1268` maxDD `-0.788`
- `news_risk_high->equity_24h` score `2.2357` n `58` status `ready` deltaP `22.9346` edge `0.3548` maxDD `-15.0185`
- `news_risk_high->crypto_major_24h` score `1.5953` n `58` status `ready` deltaP `19.2888` edge `0.3687` maxDD `-20.0879`
- `news_risk_high->metal_24h` score `1.4244` n `58` status `ready` deltaP `35.8717` edge `0.0389` maxDD `-4.9676`
- `market_context_high->unknown_1h` score `1.1186` n `127` status `ready` deltaP `9.5278` edge `0.0778` maxDD `-1.5148`
- `news_risk_high->fx_1h` score `0.7603` n `80` status `ready` deltaP `14.491` edge `0.0056` maxDD `-0.108`
- `news_risk_high->index_24h` score `0.735` n `58` status `ready` deltaP `19.0913` edge `0.0221` maxDD `-1.4118`
- `news_risk_high->commodity_1h` score `0.3995` n `80` status `ready` deltaP `11.7515` edge `0.0049` maxDD `-0.5618`
- `market_context_high->crypto_major_4h` score `-0.1788` n `115` status `ready` deltaP `18.0408` edge `0.2099` maxDD `-20.9394`
- `market_context_high->metal_4h` score `-0.3191` n `115` status `ready` deltaP `6.421` edge `0.008` maxDD `-3.3377`
- `news_risk_high->index_1h` score `-0.391` n `80` status `ready` deltaP `0.3069` edge `-0.0085` maxDD `-0.8275`
- `market_context_high->commodity_1h` score `-0.4941` n `127` status `ready` deltaP `-0.3548` edge `0.0084` maxDD `-1.5507`
- `news_risk_high->index_4h` score `-0.5444` n `80` status `ready` deltaP `1.6159` edge `-0.0164` maxDD `-1.7996`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
