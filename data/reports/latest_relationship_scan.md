# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-12T18:22:29.274091+00:00`
- Price records: `672`
- Market context records: `6526`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `64`

- Symbol pattern count: `7864`

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

- `news_risk_high->crypto_alt_24h` score `13.3219` n `32` status `ready` deltaP `36.211` edge `0.8835` maxDD `-0.5131`
- `news_risk_high->fx_24h` score `6.5482` n `32` status `ready` deltaP `54.0728` edge `0.1852` maxDD `0.0`
- `market_context_high->unknown_24h` score `6.3146` n `143` status `ready` deltaP `11.6312` edge `0.7787` maxDD `-15.0689`
- `news_risk_high->crypto_major_24h` score `4.8722` n `32` status `ready` deltaP `20.911` edge `0.5632` maxDD `-4.2368`
- `news_risk_high->fx_4h` score `3.6853` n `38` status `ready` deltaP `39.0164` edge `0.0516` maxDD `-0.0345`
- `market_context_high->unknown_1h` score `2.4326` n `187` status `ready` deltaP `-5.3364` edge `0.3284` maxDD `-3.2083`
- `news_risk_high->commodity_24h` score `2.1119` n `32` status `ready` deltaP `22.8499` edge `0.0442` maxDD `-0.3101`
- `news_risk_high->fx_1h` score `1.764` n `38` status `ready` deltaP `22.1636` edge `0.0173` maxDD `-0.1113`
- `market_context_high->commodity_24h` score `1.6592` n `143` status `ready` deltaP `14.6987` edge `0.2271` maxDD `-5.2791`
- `market_context_high->index_4h` score `0.6751` n `176` status `ready` deltaP `14.2045` edge `0.0292` maxDD `-0.4108`
- `news_risk_high->crypto_major_1h` score `0.6073` n `38` status `ready` deltaP `5.4995` edge `0.0949` maxDD `-2.6299`
- `market_context_high->crypto_alt_4h` score `0.4431` n `176` status `ready` deltaP `11.1142` edge `0.1182` maxDD `-6.7632`
- `news_risk_high->crypto_alt_1h` score `0.1116` n `38` status `ready` deltaP `2.0328` edge `0.0517` maxDD `-2.0756`
- `news_risk_high->index_24h` score `-0.2733` n `32` status `ready` deltaP `7.2032` edge `0.0041` maxDD `-2.3058`
- `market_context_high->equity_4h` score `-0.3928` n `176` status `ready` deltaP `9.2433` edge `0.0579` maxDD `-8.2573`
- `market_context_high->crypto_major_4h` score `-0.4204` n `176` status `ready` deltaP `12.6386` edge `0.0909` maxDD `-12.6576`
- `market_context_high->fx_1h` score `-0.4484` n `187` status `ready` deltaP `-0.803` edge `-0.0014` maxDD `-0.7249`
- `market_context_high->commodity_1h` score `-0.4638` n `187` status `ready` deltaP `1.5515` edge `-0.0015` maxDD `-2.1314`
- `market_context_high->unknown_4h` score `-0.4894` n `176` status `ready` deltaP `-20.1774` edge `0.3343` maxDD `-10.5788`
- `market_context_high->crypto_major_1h` score `-0.5486` n `187` status `ready` deltaP `6.4283` edge `0.0134` maxDD `-6.7936`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
