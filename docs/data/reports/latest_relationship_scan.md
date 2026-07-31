# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-31T05:07:22.057869+00:00`
- Price records: `672`
- Market context records: `8483`
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

- `news_risk_high->unknown_24h` score `6269.1185` n `52` status `ready` deltaP `44.0438` edge `522.175` maxDD `-2.0332`
- `news_risk_high->equity_4h` score `6.0931` n `62` status `ready` deltaP `21.4743` edge `0.4243` maxDD `-3.4427`
- `news_risk_high->index_4h` score `2.1082` n `62` status `ready` deltaP `17.5109` edge `0.078` maxDD `-0.191`
- `news_risk_high->equity_1h` score `1.7241` n `64` status `ready` deltaP `16.1022` edge `0.084` maxDD `-2.4803`
- `news_risk_high->crypto_major_4h` score `1.2861` n `62` status `ready` deltaP `7.2384` edge `0.186` maxDD `-2.8833`
- `news_risk_high->crypto_alt_4h` score `1.278` n `62` status `ready` deltaP `16.9551` edge `0.19` maxDD `-5.8012`
- `news_risk_high->crypto_alt_1h` score `0.6315` n `64` status `ready` deltaP `10.3574` edge `0.0646` maxDD `-1.8813`
- `news_risk_high->crypto_major_1h` score `0.3391` n `64` status `ready` deltaP `6.9143` edge `0.0486` maxDD `-2.0972`
- `news_risk_high->fx_1h` score `0.1243` n `64` status `ready` deltaP `6.0348` edge `0.0038` maxDD `-0.2475`
- `news_risk_high->fx_4h` score `0.1014` n `62` status `ready` deltaP `12.4361` edge `0.0213` maxDD `-0.6604`
- `news_risk_high->index_1h` score `0.02` n `64` status `ready` deltaP `3.9203` edge `0.0081` maxDD `-0.5338`
- `news_risk_high->metal_1h` score `-0.2857` n `64` status `ready` deltaP `1.759` edge `0.0048` maxDD `-0.5599`
- `news_risk_high->metal_4h` score `-0.4149` n `62` status `ready` deltaP `-1.7801` edge `0.0249` maxDD `-0.8085`
- `news_risk_high->commodity_1h` score `-1.5249` n `64` status `ready` deltaP `-2.6572` edge `-0.0308` maxDD `-2.9516`
- `news_risk_high->fx_24h` score `-5.5489` n `52` status `ready` deltaP `-27.7244` edge `-0.0454` maxDD `-5.2413`
- `news_risk_high->commodity_4h` score `-7.4289` n `62` status `ready` deltaP `-18.8435` edge `-0.1627` maxDD `-13.1269`
- `news_risk_high->metal_24h` score `-9.326` n `52` status `ready` deltaP `-36.6186` edge `-0.256` maxDD `-10.8302`
- `news_risk_high->commodity_24h` score `-12.9642` n `52` status `ready` deltaP `-13.3013` edge `-0.3977` maxDD `-33.8515`
- `news_risk_high->index_24h` score `-14.6478` n `52` status `ready` deltaP `-36.0577` edge `-0.43` maxDD `-28.0214`
- `news_risk_high->crypto_major_24h` score `-40.7317` n `52` status `ready` deltaP `-31.3969` edge `-1.7325` maxDD `-103.8662`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
