# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-24T21:37:17.152095+00:00`
- Price records: `672`
- Market context records: `1779`
- Flow alert records: `7018`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8882`

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

- `market_context_high->metal_24h` score `7.1391` n `181` status `ready` deltaP `28.2487` edge `0.6492` maxDD `-12.7414`
- `market_context_high->crypto_alt_4h` score `5.9736` n `194` status `ready` deltaP `21.7076` edge `0.5297` maxDD `-9.1295`
- `news_risk_high->commodity_4h` score `5.8854` n `30` status `ready` deltaP `27.124` edge `0.3751` maxDD `-3.5713`
- `market_context_high->crypto_major_4h` score `4.5916` n `194` status `ready` deltaP `22.935` edge `0.4703` maxDD `-10.9117`
- `market_context_high->unknown_4h` score `3.49` n `194` status `ready` deltaP `14.9924` edge `0.418` maxDD `-11.1695`
- `market_context_high->index_24h` score `3.4658` n `181` status `ready` deltaP `17.4532` edge `0.2953` maxDD `-4.1604`
- `market_context_high->equity_4h` score `3.0947` n `194` status `ready` deltaP `16.6269` edge `0.2565` maxDD `-5.0894`
- `news_risk_high->commodity_1h` score `3.0384` n `30` status `ready` deltaP `23.6727` edge `0.1271` maxDD `-1.2043`
- `market_context_high->equity_24h` score `2.2673` n `181` status `ready` deltaP `16.3482` edge `0.5698` maxDD `-33.1875`
- `market_context_high->unknown_24h` score `1.9022` n `181` status `ready` deltaP `13.2242` edge `0.6024` maxDD `-35.8966`
- `market_context_high->index_4h` score `0.9607` n `194` status `ready` deltaP `12.4591` edge `0.1059` maxDD `-3.7119`
- `market_context_high->crypto_alt_1h` score `0.8682` n `195` status `ready` deltaP `8.417` edge `0.1186` maxDD `-4.1892`
- `news_risk_high->fx_4h` score `0.8071` n `30` status `ready` deltaP `20.2643` edge `-0.0044` maxDD `-0.1774`
- `news_risk_high->unknown_4h` score `0.3778` n `30` status `ready` deltaP `10.2845` edge `0.0522` maxDD `-2.7857`
- `market_context_high->crypto_major_1h` score `0.3327` n `195` status `ready` deltaP `5.5758` edge `0.0979` maxDD `-3.9211`
- `market_context_high->equity_1h` score `0.1105` n `195` status `ready` deltaP `5.3785` edge `0.0542` maxDD `-2.8014`
- `market_context_high->index_1h` score `-0.1013` n `195` status `ready` deltaP `4.9102` edge `0.022` maxDD `-1.7205`
- `market_context_high->metal_4h` score `-0.1432` n `194` status `ready` deltaP `13.4743` edge `0.161` maxDD `-12.5349`
- `market_context_high->crypto_major_24h` score `-0.2879` n `181` status `ready` deltaP `17.8637` edge `0.7155` maxDD `-62.3533`
- `news_risk_high->unknown_1h` score `-0.4248` n `30` status `ready` deltaP `17.1557` edge `-0.1216` maxDD `-2.1115`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
