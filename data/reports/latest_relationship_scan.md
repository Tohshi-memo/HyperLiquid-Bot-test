# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-31T07:22:25.896207+00:00`
- Price records: `672`
- Market context records: `8492`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5871`

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

- `news_risk_high->unknown_24h` score `6271.6805` n `52` status `ready` deltaP `44.0438` edge `522.3885` maxDD `-2.0332`
- `news_risk_high->equity_4h` score `6.068` n `64` status `ready` deltaP `22.1799` edge `0.4175` maxDD `-3.4427`
- `news_risk_high->index_4h` score `2.0375` n `64` status `ready` deltaP `16.8064` edge `0.0768` maxDD `-0.191`
- `news_risk_high->equity_1h` score `1.7649` n `64` status `ready` deltaP `16.1022` edge `0.0874` maxDD `-2.4803`
- `news_risk_high->crypto_alt_4h` score `1.0229` n `64` status `ready` deltaP `15.2439` edge `0.1687` maxDD `-5.8012`
- `news_risk_high->crypto_major_4h` score `0.9712` n `64` status `ready` deltaP `5.8308` edge `0.1632` maxDD `-3.5385`
- `news_risk_high->crypto_alt_1h` score `0.644` n `64` status `ready` deltaP `10.3574` edge `0.0662` maxDD `-1.8813`
- `news_risk_high->crypto_major_1h` score `0.3758` n `64` status `ready` deltaP `7.2137` edge `0.0513` maxDD `-2.0972`
- `news_risk_high->fx_1h` score `0.178` n `64` status `ready` deltaP `6.933` edge `0.0047` maxDD `-0.2475`
- `news_risk_high->fx_4h` score `0.0694` n `64` status `ready` deltaP `12.0808` edge `0.021` maxDD `-0.6604`
- `news_risk_high->index_1h` score `0.0223` n `64` status `ready` deltaP `3.9203` edge `0.0084` maxDD `-0.5338`
- `news_risk_high->metal_4h` score `-0.1604` n `64` status `ready` deltaP `-0.1143` edge `0.0278` maxDD `-0.8085`
- `news_risk_high->metal_1h` score `-0.2222` n `64` status `ready` deltaP `2.3578` edge `0.0061` maxDD `-0.5599`
- `news_risk_high->commodity_1h` score `-1.6184` n `64` status `ready` deltaP `-3.5554` edge `-0.0326` maxDD `-2.9516`
- `news_risk_high->fx_24h` score `-5.5369` n `52` status `ready` deltaP `-27.7244` edge `-0.0444` maxDD `-5.2413`
- `news_risk_high->commodity_4h` score `-7.6003` n `64` status `ready` deltaP `-20.1601` edge `-0.1662` maxDD `-13.2872`
- `news_risk_high->metal_24h` score `-9.4148` n `52` status `ready` deltaP `-36.6186` edge `-0.2634` maxDD `-10.8302`
- `news_risk_high->commodity_24h` score `-12.939` n `52` status `ready` deltaP `-13.3013` edge `-0.3956` maxDD `-33.8515`
- `news_risk_high->index_24h` score `-15.044` n `52` status `ready` deltaP `-37.6202` edge `-0.4526` maxDD `-28.0214`
- `news_risk_high->crypto_major_24h` score `-41.2455` n `52` status `ready` deltaP `-32.9594` edge `-1.7649` maxDD `-103.8662`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
