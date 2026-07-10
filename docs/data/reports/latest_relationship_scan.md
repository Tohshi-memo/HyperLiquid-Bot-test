# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-10T19:37:25.343749+00:00`
- Price records: `672`
- Market context records: `6314`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11133`

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

- `news_risk_high->crypto_alt_24h` score `15.3462` n `32` status `ready` deltaP `43.2292` edge `1.0054` maxDD `-0.5131`
- `news_risk_high->fx_24h` score `6.0145` n `32` status `ready` deltaP `50.5208` edge `0.1644` maxDD `0.0`
- `news_risk_high->crypto_major_24h` score `4.2904` n `32` status `ready` deltaP `16.6667` edge `0.5169` maxDD `-4.2368`
- `news_risk_high->fx_4h` score `4.2021` n `32` status `ready` deltaP `43.8262` edge `0.0626` maxDD `-0.0345`
- `news_risk_high->commodity_24h` score `3.3184` n `32` status `ready` deltaP `29.8611` edge `0.098` maxDD `-0.3101`
- `news_risk_high->fx_1h` score `2.3883` n `32` status `ready` deltaP `28.7425` edge `0.0213` maxDD `-0.1113`
- `news_risk_high->crypto_major_1h` score `1.4764` n `32` status `ready` deltaP `14.5771` edge `0.1388` maxDD `-2.0691`
- `news_risk_high->crypto_alt_1h` score `0.9571` n `32` status `ready` deltaP `12.0696` edge `0.0884` maxDD `-1.6923`
- `market_context_high->unknown_1h` score `0.5886` n `208` status `ready` deltaP `-4.9401` edge `0.1828` maxDD `-3.7317`
- `market_context_high->metal_4h` score `-0.0488` n `196` status `ready` deltaP `8.2877` edge `0.037` maxDD `-2.7056`
- `market_context_high->metal_24h` score `-0.1339` n `159` status `ready` deltaP `21.0724` edge `0.0992` maxDD `-11.8809`
- `market_context_high->fx_1h` score `-0.4538` n `208` status `ready` deltaP `-0.5844` edge `-0.002` maxDD `-0.8494`
- `news_risk_high->index_24h` score `-0.4803` n `32` status `ready` deltaP `4.1667` edge `-0.0022` maxDD `-2.3058`
- `market_context_high->metal_1h` score `-0.4834` n `208` status `ready` deltaP `2.2628` edge `0.0007` maxDD `-1.8877`
- `market_context_high->commodity_1h` score `-0.5921` n `208` status `ready` deltaP `-1.0796` edge `-0.0004` maxDD `-2.1314`
- `news_risk_high->metal_1h` score `-0.7107` n `32` status `ready` deltaP `-2.5449` edge `-0.0244` maxDD `-1.6464`
- `market_context_high->index_1h` score `-0.841` n `208` status `ready` deltaP `-3.4517` edge `0.0021` maxDD `-0.9531`
- `market_context_high->index_4h` score `-0.8573` n `196` status `ready` deltaP `2.1186` edge `0.0178` maxDD `-1.3472`
- `news_risk_high->unknown_1h` score `-1.0261` n `32` status `ready` deltaP `4.4349` edge `-0.0806` maxDD `-0.7581`
- `market_context_high->equity_1h` score `-1.0357` n `208` status `ready` deltaP `-2.9307` edge `-0.0017` maxDD `-4.2573`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
