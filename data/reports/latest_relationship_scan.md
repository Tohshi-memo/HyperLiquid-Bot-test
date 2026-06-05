# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-05T07:07:24.116663+00:00`
- Price records: `672`
- Market context records: `2947`
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

- `market_context_high->crypto_alt_24h` score `16.8697` n `135` status `ready` deltaP `15.0579` edge `1.6971` maxDD `-22.6673`
- `market_context_high->equity_24h` score `8.0606` n `135` status `ready` deltaP `18.4028` edge `0.7494` maxDD `-12.6963`
- `market_context_high->unknown_24h` score `7.3917` n `135` status `ready` deltaP `16.7014` edge `0.5511` maxDD `-1.7175`
- `market_context_high->commodity_24h` score `3.1599` n `135` status `ready` deltaP `18.993` edge `0.3958` maxDD `-10.7275`
- `market_context_high->index_24h` score `3.0036` n `135` status `ready` deltaP `14.3519` edge `0.2527` maxDD `-2.5127`
- `market_context_high->equity_4h` score `1.619` n `136` status `ready` deltaP `10.608` edge `0.1676` maxDD `-4.6056`
- `market_context_high->index_4h` score `0.7845` n `136` status `ready` deltaP `15.2888` edge `0.0828` maxDD `-2.3986`
- `market_context_high->crypto_alt_4h` score `0.6034` n `136` status `ready` deltaP `17.2076` edge `0.3917` maxDD `-30.8239`
- `market_context_high->unknown_4h` score `0.3512` n `136` status `ready` deltaP `4.08` edge `0.1074` maxDD `-3.7602`
- `market_context_high->index_1h` score `0.1243` n `136` status `ready` deltaP `6.5912` edge `0.0214` maxDD `-1.2855`
- `market_context_high->equity_1h` score `-0.2141` n `136` status `ready` deltaP `1.4046` edge `0.0506` maxDD `-2.2244`
- `market_context_high->crypto_alt_1h` score `-0.251` n `136` status `ready` deltaP `6.4679` edge `0.1007` maxDD `-10.747`
- `market_context_high->fx_1h` score `-0.3608` n `136` status `ready` deltaP `-0.3258` edge `0.0032` maxDD `-0.154`
- `market_context_high->crypto_major_1h` score `-0.4912` n `136` status `ready` deltaP `5.9352` edge `0.0844` maxDD `-9.622`
- `market_context_high->metal_1h` score `-0.6403` n `136` status `ready` deltaP `0.2025` edge `0.0053` maxDD `-3.4325`
- `market_context_high->commodity_1h` score `-0.7464` n `136` status `ready` deltaP `-1.5234` edge `-0.0102` maxDD `-4.3601`
- `market_context_high->unknown_1h` score `-0.7543` n `136` status `ready` deltaP `1.5939` edge `-0.0004` maxDD `-3.1801`
- `market_context_high->fx_4h` score `-0.8124` n `136` status `ready` deltaP `0.2511` edge `0.0085` maxDD `-0.5631`
- `market_context_high->commodity_4h` score `-1.1925` n `136` status `ready` deltaP `2.8246` edge `0.0203` maxDD `-10.0279`
- `market_context_high->crypto_major_4h` score `-1.3549` n `136` status `ready` deltaP `8.2855` edge `0.2836` maxDD `-33.6701`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
