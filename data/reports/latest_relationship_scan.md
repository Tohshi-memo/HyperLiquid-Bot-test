# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-31T07:37:25.529107+00:00`
- Price records: `672`
- Market context records: `8494`
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

- `news_risk_high->unknown_24h` score `6271.9637` n `52` status `ready` deltaP `44.0438` edge `522.4121` maxDD `-2.0332`
- `news_risk_high->equity_4h` score `6.074` n `64` status `ready` deltaP `22.1799` edge `0.418` maxDD `-3.4427`
- `news_risk_high->index_4h` score `2.0375` n `64` status `ready` deltaP `16.8064` edge `0.0768` maxDD `-0.191`
- `news_risk_high->equity_1h` score `1.7733` n `64` status `ready` deltaP `16.1022` edge `0.0881` maxDD `-2.4803`
- `news_risk_high->crypto_alt_4h` score `1.0182` n `64` status `ready` deltaP `15.2439` edge `0.1681` maxDD `-5.8012`
- `news_risk_high->crypto_major_4h` score `0.9727` n `64` status `ready` deltaP `5.8308` edge `0.1634` maxDD `-3.5385`
- `news_risk_high->crypto_alt_1h` score `0.6549` n `64` status `ready` deltaP `10.5071` edge `0.0666` maxDD `-1.8813`
- `news_risk_high->crypto_major_1h` score `0.3937` n `64` status `ready` deltaP `7.3634` edge `0.0526` maxDD `-2.0972`
- `news_risk_high->fx_1h` score `0.1773` n `64` status `ready` deltaP `6.933` edge `0.0046` maxDD `-0.2475`
- `news_risk_high->fx_4h` score `0.0694` n `64` status `ready` deltaP `12.0808` edge `0.021` maxDD `-0.6604`
- `news_risk_high->index_1h` score `0.0231` n `64` status `ready` deltaP `3.9203` edge `0.0085` maxDD `-0.5338`
- `news_risk_high->metal_4h` score `-0.1486` n `64` status `ready` deltaP `0.0381` edge `0.0283` maxDD `-0.8085`
- `news_risk_high->metal_1h` score `-0.2066` n `64` status `ready` deltaP `2.5075` edge `0.0064` maxDD `-0.5599`
- `news_risk_high->commodity_1h` score `-1.6351` n `64` status `ready` deltaP `-3.7051` edge `-0.033` maxDD `-2.9516`
- `news_risk_high->fx_24h` score `-5.5357` n `52` status `ready` deltaP `-27.7244` edge `-0.0443` maxDD `-5.2413`
- `news_risk_high->commodity_4h` score `-7.6161` n `64` status `ready` deltaP `-20.3125` edge `-0.1665` maxDD `-13.2872`
- `news_risk_high->metal_24h` score `-9.4244` n `52` status `ready` deltaP `-36.6186` edge `-0.2642` maxDD `-10.8302`
- `news_risk_high->commodity_24h` score `-12.9342` n `52` status `ready` deltaP `-13.3013` edge `-0.3952` maxDD `-33.8515`
- `news_risk_high->index_24h` score `-15.0903` n `52` status `ready` deltaP `-37.7938` edge `-0.4553` maxDD `-28.0214`
- `news_risk_high->crypto_major_24h` score `-41.299` n `52` status `ready` deltaP `-33.133` edge `-1.7682` maxDD `-103.8662`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
