# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-11T14:14:51.851755+00:00`
- Price records: `672`
- Market context records: `6398`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11075`

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

- `news_risk_high->crypto_alt_24h` score `13.7673` n `32` status `ready` deltaP `35.7639` edge `0.9236` maxDD `-0.5131`
- `news_risk_high->fx_24h` score `6.6104` n `32` status `ready` deltaP `55.5556` edge `0.1805` maxDD `0.0`
- `news_risk_high->commodity_24h` score `4.3887` n `32` status `ready` deltaP `38.0208` edge `0.1328` maxDD `-0.3101`
- `news_risk_high->crypto_major_24h` score `4.222` n `32` status `ready` deltaP `17.3611` edge `0.5035` maxDD `-4.2368`
- `news_risk_high->fx_4h` score `4.0364` n `32` status `ready` deltaP `41.8445` edge `0.062` maxDD `-0.0345`
- `news_risk_high->fx_1h` score `2.4218` n `32` status `ready` deltaP `29.1916` edge `0.0211` maxDD `-0.1113`
- `news_risk_high->crypto_major_1h` score `1.4398` n `32` status `ready` deltaP `13.6789` edge `0.1401` maxDD `-2.0691`
- `news_risk_high->crypto_alt_1h` score `0.8325` n `32` status `ready` deltaP `10.2732` edge `0.0844` maxDD `-1.6923`
- `market_context_high->metal_4h` score `0.5146` n `216` status `ready` deltaP `12.246` edge `0.0409` maxDD `-2.7056`
- `market_context_high->unknown_1h` score `0.3551` n `219` status `ready` deltaP `-5.8199` edge `0.1692` maxDD `-3.7317`
- `market_context_high->index_4h` score `0.0948` n `216` status `ready` deltaP `8.1357` edge `0.0213` maxDD `-0.4108`
- `market_context_high->unknown_24h` score `0.0255` n `146` status `ready` deltaP `6.5021` edge `0.3698` maxDD `-21.5483`
- `news_risk_high->unknown_1h` score `-0.2009` n `32` status `ready` deltaP `6.9798` edge `-0.0288` maxDD `-0.7581`
- `market_context_high->metal_24h` score `-0.3305` n `146` status `ready` deltaP `19.6205` edge `0.0985` maxDD `-11.8809`
- `market_context_high->equity_4h` score `-0.4749` n `216` status `ready` deltaP `8.7003` edge `0.051` maxDD `-8.2573`
- `market_context_high->metal_1h` score `-0.495` n `219` status `ready` deltaP `1.7704` edge `0.0025` maxDD `-1.8877`
- `news_risk_high->metal_1h` score `-0.6453` n `32` status `ready` deltaP `-1.1976` edge `-0.025` maxDD `-1.6464`
- `market_context_high->index_1h` score `-0.686` n `219` status `ready` deltaP `-2.8033` edge `0.0027` maxDD `-0.7564`
- `market_context_high->fx_1h` score `-0.7081` n `219` status `ready` deltaP `-0.6029` edge `-0.0016` maxDD `-0.9376`
- `news_risk_high->index_24h` score `-0.7487` n `32` status `ready` deltaP `0.5208` edge `-0.0123` maxDD `-2.3058`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
