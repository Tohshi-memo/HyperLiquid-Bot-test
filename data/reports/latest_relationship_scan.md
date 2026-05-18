# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-18T04:22:13.758733+00:00`
- Price records: `672`
- Market context records: `1082`
- Flow alert records: `5021`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8728`

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

- `market_context_high->crypto_major_24h` score `16.5179` n `158` status `ready` deltaP `35.3611` edge `1.1871` maxDD `-3.3749`
- `market_context_high->crypto_alt_24h` score `5.8027` n `158` status `ready` deltaP `12.1439` edge `0.526` maxDD `-9.5387`
- `market_context_high->equity_24h` score `5.4775` n `158` status `ready` deltaP `14.7478` edge `0.4078` maxDD `-3.6396`
- `market_context_high->metal_24h` score `4.5837` n `158` status `ready` deltaP `-2.536` edge `0.5656` maxDD `-6.3373`
- `market_context_high->index_24h` score `4.5232` n `158` status `ready` deltaP `14.8697` edge `0.3086` maxDD `-2.1308`
- `market_context_high->equity_4h` score `1.5562` n `161` status `ready` deltaP `9.1671` edge `0.1474` maxDD `-3.6396`
- `market_context_high->crypto_major_4h` score `1.441` n `161` status `ready` deltaP `13.2584` edge `0.2003` maxDD `-6.4882`
- `market_context_high->index_4h` score `0.8826` n `161` status `ready` deltaP `7.5974` edge `0.0912` maxDD `-2.1308`
- `market_context_high->index_1h` score `0.6166` n `173` status `ready` deltaP `8.1409` edge `0.0288` maxDD `-0.5353`
- `market_context_high->equity_1h` score `0.4818` n `173` status `ready` deltaP `3.0468` edge `0.0576` maxDD `-1.3546`
- `market_context_high->crypto_major_1h` score `0.0971` n `173` status `ready` deltaP `6.8637` edge `0.0389` maxDD `-4.1256`
- `market_context_high->fx_1h` score `0.0248` n `173` status `ready` deltaP `6.9511` edge `0.0013` maxDD `-0.3124`
- `market_context_high->metal_1h` score `-0.1048` n `173` status `ready` deltaP `7.2756` edge `0.0038` maxDD `-2.2164`
- `market_context_high->crypto_alt_1h` score `-0.2984` n `173` status `ready` deltaP `2.6721` edge `0.0416` maxDD `-3.4088`
- `market_context_high->crypto_alt_4h` score `-0.3522` n `161` status `ready` deltaP `7.3929` edge `0.1718` maxDD `-13.0347`
- `market_context_high->fx_4h` score `-0.6741` n `161` status `ready` deltaP `1.7734` edge `0.0014` maxDD `-1.6381`
- `market_context_high->commodity_1h` score `-1.0728` n `173` status `ready` deltaP `-1.3828` edge `0.0006` maxDD `-3.7959`
- `market_context_high->unknown_4h` score `-1.687` n `161` status `ready` deltaP `9.0403` edge `-0.0792` maxDD `-6.7322`
- `market_context_high->metal_4h` score `-1.9988` n `161` status `ready` deltaP `4.2077` edge `-0.0889` maxDD `-9.2991`
- `market_context_high->fx_24h` score `-3.0998` n `158` status `ready` deltaP `4.8336` edge `-0.022` maxDD `-19.2774`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
