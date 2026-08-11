# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-11T02:37:28.513843+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11744`

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

- `market_context_high->unknown_24h` score `24.574` n `144` status `ready` deltaP `-14.7831` edge `2.3918` maxDD `-9.6329`
- `market_context_high->fx_24h` score `1.0839` n `144` status `ready` deltaP `20.234` edge `0.0362` maxDD `-1.4613`
- `market_context_high->commodity_4h` score `0.9353` n `168` status `ready` deltaP `12.4201` edge `0.0666` maxDD `-2.7169`
- `market_context_high->commodity_1h` score `0.6789` n `180` status `ready` deltaP `9.3114` edge `0.0288` maxDD `-0.7439`
- `market_context_high->fx_1h` score `-0.1418` n `180` status `ready` deltaP `4.1218` edge `-0.0005` maxDD `-0.613`
- `market_context_high->fx_4h` score `-0.1975` n `168` status `ready` deltaP `4.4788` edge `0.0048` maxDD `-0.4647`
- `market_context_high->index_1h` score `-0.8397` n `180` status `ready` deltaP `-6.67` edge `-0.0044` maxDD `-1.0359`
- `market_context_high->metal_1h` score `-1.2888` n `180` status `ready` deltaP `-5.2195` edge `-0.009` maxDD `-2.0884`
- `market_context_high->equity_1h` score `-1.4731` n `180` status `ready` deltaP `-6.4604` edge `-0.0181` maxDD `-6.8818`
- `market_context_high->metal_24h` score `-1.7092` n `144` status `ready` deltaP `2.3854` edge `-0.0259` maxDD `-2.9283`
- `market_context_high->index_4h` score `-1.9173` n `168` status `ready` deltaP `-7.7018` edge `-0.019` maxDD `-1.4876`
- `market_context_high->index_24h` score `-2.1769` n `144` status `ready` deltaP `-9.443` edge `-0.0066` maxDD `-6.7627`
- `market_context_high->commodity_24h` score `-2.1808` n `144` status `ready` deltaP `8.0963` edge `0.0858` maxDD `-24.5488`
- `market_context_high->crypto_alt_1h` score `-2.6715` n `180` status `ready` deltaP `-9.5143` edge `-0.0406` maxDD `-6.4874`
- `market_context_high->metal_4h` score `-3.2526` n `168` status `ready` deltaP `-8.5439` edge `-0.0377` maxDD `-6.1111`
- `market_context_high->crypto_major_1h` score `-3.6197` n `180` status `ready` deltaP `-9.0186` edge `-0.0511` maxDD `-11.9002`
- `market_context_high->equity_4h` score `-4.5665` n `168` status `ready` deltaP `-17.2402` edge `-0.1596` maxDD `-15.8728`
- `market_context_high->crypto_major_24h` score `-6.6584` n `144` status `ready` deltaP `-12.9164` edge `-0.1904` maxDD `-33.5037`
- `market_context_high->crypto_alt_4h` score `-6.7512` n `168` status `ready` deltaP `-12.6742` edge `-0.1433` maxDD `-20.1177`
- `market_context_high->crypto_alt_24h` score `-9.5606` n `144` status `ready` deltaP `-12.884` edge `-0.231` maxDD `-27.3857`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
