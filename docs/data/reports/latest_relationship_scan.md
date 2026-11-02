# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-02T05:07:34.798260+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5060`

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

- `market_context_high->unknown_24h` score `6922.5595` n `40` status `ready` deltaP `1.3889` edge `576.8707` maxDD `0.0`
- `market_context_high->unknown_4h` score `508.0233` n `43` status `ready` deltaP `9.1463` edge `42.2743` maxDD `0.0`
- `market_context_high->unknown_1h` score `95.0638` n `45` status `ready` deltaP `6.5303` edge `7.8895` maxDD `-0.2178`
- `market_context_high->equity_24h` score `19.0019` n `40` status `ready` deltaP `42.1181` edge `1.3263` maxDD `-1.5546`
- `news_risk_high->crypto_alt_24h` score `13.8826` n `94` status `ready` deltaP `34.2605` edge `1.0641` maxDD `-6.8493`
- `market_context_high->commodity_24h` score `6.9731` n `40` status `ready` deltaP `44.2014` edge `0.3175` maxDD `-0.8203`
- `market_context_high->crypto_alt_4h` score `6.6822` n `43` status `ready` deltaP `29.1867` edge `0.3917` maxDD `-1.6876`
- `market_context_high->index_24h` score `6.5526` n `40` status `ready` deltaP `49.1319` edge `0.2185` maxDD `0.0`
- `market_context_high->crypto_major_4h` score `5.2822` n `43` status `ready` deltaP `27.7368` edge `0.2889` maxDD `-1.6901`
- `market_context_high->equity_4h` score `4.8495` n `43` status `ready` deltaP `8.6748` edge `0.4165` maxDD `-2.283`
- `market_context_high->commodity_4h` score `2.8167` n `43` status `ready` deltaP `29.3747` edge `0.0646` maxDD `-1.0567`
- `news_risk_high->crypto_alt_4h` score `2.2518` n `126` status `ready` deltaP `9.0132` edge `0.2662` maxDD `-7.4246`
- `market_context_high->equity_1h` score `1.7367` n `45` status `ready` deltaP `3.0339` edge `0.177` maxDD `-1.5336`
- `market_context_high->crypto_alt_24h` score `1.4974` n `40` status `ready` deltaP `-9.4097` edge `0.3393` maxDD `-8.8096`
- `market_context_high->fx_1h` score `1.0178` n `45` status `ready` deltaP `13.9953` edge `0.0091` maxDD `-0.0736`
- `market_context_high->metal_4h` score `1.0123` n `43` status `ready` deltaP `18.4309` edge `0.0494` maxDD `-0.7323`
- `market_context_high->crypto_alt_1h` score `0.9309` n `45` status `ready` deltaP `1.4105` edge `0.1294` maxDD `-2.2314`
- `market_context_high->crypto_major_1h` score `0.9268` n `45` status `ready` deltaP `3.0339` edge `0.1079` maxDD `-1.4048`
- `market_context_high->crypto_major_24h` score `0.5294` n `40` status `ready` deltaP `-2.7778` edge `0.1303` maxDD `-3.0799`
- `market_context_high->metal_1h` score `0.4868` n `45` status `ready` deltaP `7.5249` edge `0.0161` maxDD `-0.3895`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
