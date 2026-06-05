# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-05T13:07:27.030279+00:00`
- Price records: `672`
- Market context records: `2971`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `6954`

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

- `market_context_high->crypto_alt_24h` score `16.5367` n `111` status `ready` deltaP `9.4547` edge `1.7067` maxDD `-22.6673`
- `market_context_high->unknown_24h` score `9.4485` n `111` status `ready` deltaP `16.2819` edge `0.7253` maxDD `-1.7175`
- `market_context_high->commodity_24h` score `9.4231` n `111` status `ready` deltaP `34.6753` edge `0.5984` maxDD `-1.545`
- `market_context_high->equity_24h` score `7.2187` n `111` status `ready` deltaP `16.5494` edge `0.6916` maxDD `-12.6963`
- `market_context_high->index_24h` score `3.7798` n `111` status `ready` deltaP `15.7142` edge `0.3083` maxDD `-2.5127`
- `market_context_high->equity_4h` score `3.0565` n `112` status `ready` deltaP `16.0278` edge `0.1868` maxDD `-0.7819`
- `market_context_high->index_4h` score `1.7967` n `112` status `ready` deltaP `18.7283` edge `0.1037` maxDD `-1.9733`
- `market_context_high->crypto_alt_4h` score `1.2787` n `112` status `ready` deltaP `22.9747` edge `0.4669` maxDD `-30.8239`
- `market_context_high->equity_1h` score `0.9212` n `112` status `ready` deltaP `6.667` edge `0.0658` maxDD `-1.012`
- `market_context_high->index_1h` score `0.3811` n `112` status `ready` deltaP `7.4316` edge `0.0237` maxDD `-0.9858`
- `market_context_high->commodity_4h` score `0.3413` n `112` status `ready` deltaP `9.9521` edge `0.0719` maxDD `-5.2264`
- `market_context_high->crypto_alt_1h` score `0.3013` n `112` status `ready` deltaP `10.2652` edge `0.1337` maxDD `-10.747`
- `market_context_high->crypto_major_1h` score `0.1157` n `112` status `ready` deltaP `10.4309` edge `0.0989` maxDD `-9.622`
- `market_context_high->unknown_4h` score `-0.1449` n `112` status `ready` deltaP `2.1994` edge `0.0786` maxDD `-3.7602`
- `market_context_high->fx_1h` score `-0.397` n `112` status `ready` deltaP `-0.9089` edge `0.0037` maxDD `-0.1244`
- `market_context_high->commodity_1h` score `-0.5878` n `112` status `ready` deltaP `-1.3526` edge `-0.0038` maxDD `-3.3365`
- `market_context_high->metal_1h` score `-0.8423` n `112` status `ready` deltaP `-2.5128` edge `-0.0025` maxDD `-3.4325`
- `market_context_high->unknown_1h` score `-1.0151` n `112` status `ready` deltaP `2.2188` edge `-0.0263` maxDD `-3.1801`
- `market_context_high->crypto_major_4h` score `-1.3195` n `112` status `ready` deltaP `10.061` edge `0.2763` maxDD `-33.6701`
- `market_context_high->fx_4h` score `-1.3243` n `112` status `ready` deltaP `-5.2482` edge `0.0025` maxDD `-0.5631`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
