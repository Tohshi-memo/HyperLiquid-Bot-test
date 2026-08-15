# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-15T08:07:31.718324+00:00`
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

- `market_context_high->unknown_24h` score `137.0666` n `128` status `ready` deltaP `-27.7554` edge `11.8985` maxDD `-9.6329`
- `risk_on_high->unknown_24h` score `33.3723` n `32` status `ready` deltaP `-41.0366` edge `4.6271` maxDD `-1.6689`
- `risk_on_and_context->unknown_24h` score `33.3723` n `32` status `ready` deltaP `-41.0366` edge `4.6271` maxDD `-1.6689`
- `news_risk_high->equity_24h` score `12.0365` n `36` status `ready` deltaP `21.8082` edge `0.8956` maxDD `-1.0358`
- `news_risk_high->equity_4h` score `7.5514` n `36` status `ready` deltaP `39.1172` edge `0.3685` maxDD `0.0`
- `market_context_high->commodity_24h` score `5.1078` n `128` status `ready` deltaP `29.0254` edge `0.2379` maxDD `-0.1266`
- `risk_on_high->commodity_24h` score `4.6839` n `32` status `ready` deltaP `31.3692` edge `0.1812` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `4.6839` n `32` status `ready` deltaP `31.3692` edge `0.1812` maxDD `0.0`
- `risk_on_high->crypto_major_24h` score `4.1354` n `32` status `ready` deltaP `27.5076` edge `0.4624` maxDD `-6.2481`
- `risk_on_and_context->crypto_major_24h` score `4.1354` n `32` status `ready` deltaP `27.5076` edge `0.4624` maxDD `-6.2481`
- `news_risk_high->index_24h` score `3.2077` n `36` status `ready` deltaP `25.9965` edge `0.094` maxDD `0.0`
- `risk_on_high->commodity_4h` score `2.8528` n `32` status `ready` deltaP `20.5908` edge `0.1187` maxDD `-0.1258`
- `risk_on_and_context->commodity_4h` score `2.8528` n `32` status `ready` deltaP `20.5908` edge `0.1187` maxDD `-0.1258`
- `market_context_high->commodity_4h` score `1.905` n `128` status `ready` deltaP `19.0283` edge `0.079` maxDD `-0.7687`
- `news_risk_high->index_4h` score `1.8003` n `36` status `ready` deltaP `20.7762` edge `0.0247` maxDD `-0.0546`
- `news_risk_high->equity_1h` score `1.6783` n `36` status `ready` deltaP `7.8344` edge `0.1195` maxDD `-0.5496`
- `risk_on_high->commodity_1h` score `1.2755` n `32` status `ready` deltaP `13.5105` edge `0.0395` maxDD `-0.1957`
- `risk_on_and_context->commodity_1h` score `1.2755` n `32` status `ready` deltaP `13.5105` edge `0.0395` maxDD `-0.1957`
- `market_context_high->commodity_1h` score `0.6389` n `128` status `ready` deltaP `8.823` edge `0.0241` maxDD `-0.3742`
- `risk_on_high->fx_4h` score `0.5606` n `32` status `ready` deltaP `6.8731` edge `0.015` maxDD `-0.1285`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
