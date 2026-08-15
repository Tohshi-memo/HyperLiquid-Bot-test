# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-15T13:22:29.420479+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11700`

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

- `market_context_high->unknown_24h` score `137.5642` n `128` status `ready` deltaP `-24.1159` edge `11.9157` maxDD `-9.6329`
- `risk_on_high->unknown_24h` score `33.6957` n `32` status `ready` deltaP `-37.3971` edge `4.6443` maxDD `-1.6689`
- `risk_on_and_context->unknown_24h` score `33.6957` n `32` status `ready` deltaP `-37.3971` edge `4.6443` maxDD `-1.6689`
- `news_risk_high->equity_24h` score `12.7752` n `36` status `ready` deltaP `25.4477` edge `0.9329` maxDD `-1.0358`
- `news_risk_high->equity_4h` score `7.7245` n `36` status `ready` deltaP `40.3963` edge `0.3744` maxDD `0.0`
- `market_context_high->commodity_24h` score `5.4117` n `128` status `ready` deltaP `31.2784` edge `0.2482` maxDD `-0.1266`
- `risk_on_high->commodity_24h` score `4.9878` n `32` status `ready` deltaP `33.6222` edge `0.1915` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `4.9878` n `32` status `ready` deltaP `33.6222` edge `0.1915` maxDD `0.0`
- `risk_on_high->crypto_major_24h` score `4.2393` n `32` status `ready` deltaP `28.2008` edge `0.4711` maxDD `-6.2481`
- `risk_on_and_context->crypto_major_24h` score `4.2393` n `32` status `ready` deltaP `28.2008` edge `0.4711` maxDD `-6.2481`
- `news_risk_high->index_24h` score `3.5781` n `36` status `ready` deltaP `29.636` edge `0.1006` maxDD `0.0`
- `risk_on_high->commodity_4h` score `2.9282` n `32` status `ready` deltaP `21.1128` edge `0.1215` maxDD `-0.1258`
- `risk_on_and_context->commodity_4h` score `2.9282` n `32` status `ready` deltaP `21.1128` edge `0.1215` maxDD `-0.1258`
- `market_context_high->commodity_4h` score `1.9803` n `128` status `ready` deltaP `19.5503` edge `0.0818` maxDD `-0.7687`
- `news_risk_high->index_4h` score `1.9388` n `36` status `ready` deltaP `22.3577` edge `0.0257` maxDD `-0.0546`
- `news_risk_high->equity_1h` score `1.7574` n `36` status `ready` deltaP `8.5829` edge `0.1211` maxDD `-0.5496`
- `risk_on_high->commodity_1h` score `1.3473` n `32` status `ready` deltaP `14.4087` edge `0.0395` maxDD `-0.1957`
- `risk_on_and_context->commodity_1h` score `1.3473` n `32` status `ready` deltaP `14.4087` edge `0.0395` maxDD `-0.1957`
- `market_context_high->commodity_1h` score `0.7108` n `128` status `ready` deltaP `9.7212` edge `0.0241` maxDD `-0.3742`
- `risk_on_high->equity_24h` score `0.6578` n `32` status `ready` deltaP `13.9894` edge `0.169` maxDD `-11.2348`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
