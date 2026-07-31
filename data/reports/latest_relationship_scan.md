# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-31T05:37:34.158253+00:00`
- Price records: `672`
- Market context records: `8485`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5828`

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

- `news_risk_high->unknown_24h` score `6269.6921` n `52` status `ready` deltaP `44.0438` edge `522.2228` maxDD `-2.0332`
- `news_risk_high->equity_4h` score `6.0668` n `64` status `ready` deltaP `22.1799` edge `0.4174` maxDD `-3.4427`
- `news_risk_high->index_4h` score `2.0399` n `64` status `ready` deltaP `16.8064` edge `0.077` maxDD `-0.191`
- `news_risk_high->equity_1h` score `1.7169` n `64` status `ready` deltaP `16.1022` edge `0.0834` maxDD `-2.4803`
- `news_risk_high->crypto_alt_4h` score `1.0268` n `64` status `ready` deltaP `15.2439` edge `0.1692` maxDD `-5.8012`
- `news_risk_high->crypto_major_4h` score `0.9609` n `64` status `ready` deltaP `5.6784` edge `0.1629` maxDD `-3.5385`
- `news_risk_high->crypto_alt_1h` score `0.6214` n `64` status `ready` deltaP `10.2077` edge `0.0643` maxDD `-1.8813`
- `news_risk_high->crypto_major_1h` score `0.3345` n `64` status `ready` deltaP `6.9143` edge `0.048` maxDD `-2.0972`
- `news_risk_high->fx_1h` score `0.1251` n `64` status `ready` deltaP `6.0348` edge `0.0039` maxDD `-0.2475`
- `news_risk_high->fx_4h` score `0.0792` n `64` status `ready` deltaP `12.2332` edge `0.0208` maxDD `-0.6604`
- `news_risk_high->index_1h` score `0.0184` n `64` status `ready` deltaP `3.9203` edge `0.0079` maxDD `-0.5338`
- `news_risk_high->metal_4h` score `-0.2005` n `64` status `ready` deltaP `-0.4192` edge `0.0247` maxDD `-0.8085`
- `news_risk_high->metal_1h` score `-0.2857` n `64` status `ready` deltaP `1.759` edge `0.0048` maxDD `-0.5599`
- `news_risk_high->commodity_1h` score `-1.5225` n `64` status `ready` deltaP `-2.6572` edge `-0.0306` maxDD `-2.9516`
- `news_risk_high->fx_24h` score `-5.5477` n `52` status `ready` deltaP `-27.7244` edge `-0.0453` maxDD `-5.2413`
- `news_risk_high->commodity_4h` score `-7.4901` n `64` status `ready` deltaP `-19.3979` edge `-0.1621` maxDD `-13.2872`
- `news_risk_high->metal_24h` score `-9.3464` n `52` status `ready` deltaP `-36.6186` edge `-0.2577` maxDD `-10.8302`
- `news_risk_high->commodity_24h` score `-12.9594` n `52` status `ready` deltaP `-13.3013` edge `-0.3973` maxDD `-33.8515`
- `news_risk_high->index_24h` score `-14.7356` n `52` status `ready` deltaP `-36.4049` edge `-0.435` maxDD `-28.0214`
- `news_risk_high->crypto_major_24h` score `-40.8399` n `52` status `ready` deltaP `-31.7441` edge `-1.7392` maxDD `-103.8662`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
