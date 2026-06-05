# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-05T13:37:24.147042+00:00`
- Price records: `672`
- Market context records: `2973`
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

- `market_context_high->crypto_alt_24h` score `16.2558` n `109` status `ready` deltaP `8.7936` edge `1.6877` maxDD `-22.6673`
- `market_context_high->commodity_24h` score `9.9544` n `109` status `ready` deltaP `36.3118` edge `0.6179` maxDD `-1.1023`
- `market_context_high->unknown_24h` score `9.6288` n `109` status `ready` deltaP `16.0009` edge `0.7422` maxDD `-1.7175`
- `market_context_high->equity_24h` score `7.0736` n `109` status `ready` deltaP `16.4007` edge `0.6805` maxDD `-12.6963`
- `market_context_high->index_24h` score `3.9176` n `109` status `ready` deltaP `16.3258` edge `0.3157` maxDD `-2.5127`
- `market_context_high->equity_4h` score `2.9413` n `110` status `ready` deltaP `15.862` edge `0.1783` maxDD `-0.7819`
- `market_context_high->index_4h` score `1.8818` n `110` status `ready` deltaP `19.2378` edge `0.1074` maxDD `-1.9733`
- `market_context_high->equity_1h` score `1.1073` n `110` status `ready` deltaP `7.7872` edge `0.0737` maxDD `-1.0004`
- `market_context_high->crypto_alt_4h` score `0.9635` n `110` status `ready` deltaP `22.4779` edge `0.4298` maxDD `-30.8239`
- `market_context_high->commodity_4h` score `0.6128` n `110` status `ready` deltaP `11.1696` edge `0.0837` maxDD `-4.0344`
- `market_context_high->index_1h` score `0.5609` n `110` status `ready` deltaP `8.503` edge `0.0292` maxDD `-0.7983`
- `market_context_high->crypto_alt_1h` score `0.3115` n `110` status `ready` deltaP `10.3103` edge `0.1347` maxDD `-10.747`
- `market_context_high->crypto_major_1h` score `0.1155` n `110` status `ready` deltaP `10.4273` edge `0.0989` maxDD `-9.622`
- `market_context_high->fx_1h` score `-0.3264` n `110` status `ready` deltaP `-0.117` edge `0.0043` maxDD `-0.1244`
- `market_context_high->unknown_4h` score `-0.3744` n `110` status `ready` deltaP `1.3553` edge `0.0651` maxDD `-3.7602`
- `market_context_high->commodity_1h` score `-0.6303` n `110` status `ready` deltaP `-1.9461` edge `-0.0053` maxDD `-3.3365`
- `market_context_high->metal_1h` score `-0.7331` n `110` status `ready` deltaP `-1.7012` edge `0.0061` maxDD `-3.4325`
- `market_context_high->unknown_1h` score `-0.9346` n `110` status `ready` deltaP `2.9096` edge `-0.0242` maxDD `-3.1801`
- `market_context_high->fx_4h` score `-1.3997` n `110` status `ready` deltaP `-6.0699` edge `0.0017` maxDD `-0.5631`
- `market_context_high->crypto_major_4h` score `-1.6498` n `110` status `ready` deltaP `9.3043` edge `0.239` maxDD `-33.6701`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
