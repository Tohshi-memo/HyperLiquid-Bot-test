# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-07T01:22:18.223709+00:00`
- Price records: `505`
- Market context records: `599`
- Flow alert records: `1694`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `807`

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

- `market_context_high->crypto_alt_24h` score `4.5763` n `146` status `ready` deltaP `6.8946` edge `0.3402` maxDD `-0.0508`
- `market_context_high->crypto_major_24h` score `3.6462` n `146` status `ready` deltaP `10.8517` edge `0.2649` maxDD `-1.3382`
- `market_context_high->fx_4h` score `0.0414` n `146` status `ready` deltaP `11.0027` edge `0.0191` maxDD `-1.6381`
- `market_context_high->fx_1h` score `-0.3327` n `146` status `ready` deltaP `1.7185` edge `0.0037` maxDD `-0.291`
- `market_context_high->index_1h` score `-0.6317` n `146` status `ready` deltaP `0.9991` edge `-0.0023` maxDD `-2.8282`
- `market_context_high->commodity_1h` score `-0.6595` n `146` status `ready` deltaP `1.0639` edge `0.0354` maxDD `-3.7959`
- `market_context_high->unknown_1h` score `-1.1007` n `146` status `ready` deltaP `-3.7787` edge `-0.0062` maxDD `-2.1602`
- `market_context_high->crypto_alt_1h` score `-1.1363` n `146` status `ready` deltaP `5.5014` edge `0.0001` maxDD `-8.1842`
- `market_context_high->equity_1h` score `-1.1756` n `146` status `ready` deltaP `-1.4153` edge `-0.0075` maxDD `-4.4826`
- `market_context_high->crypto_major_1h` score `-1.7558` n `146` status `ready` deltaP `5.098` edge `-0.008` maxDD `-11.4508`
- `market_context_high->crypto_alt_4h` score `-1.9893` n `146` status `ready` deltaP `3.6151` edge `0.0671` maxDD `-15.2248`
- `market_context_high->index_4h` score `-2.1926` n `146` status `ready` deltaP `0.5324` edge `-0.034` maxDD `-6.5149`
- `market_context_high->index_24h` score `-2.4679` n `146` status `ready` deltaP `-6.8476` edge `0.0395` maxDD `-5.9609`
- `market_context_high->crypto_major_4h` score `-2.6806` n `146` status `ready` deltaP `13.0221` edge `0.0604` maxDD `-22.648`
- `market_context_high->equity_4h` score `-3.1935` n `146` status `ready` deltaP `-2.9727` edge `-0.0311` maxDD `-10.5498`
- `market_context_high->metal_1h` score `-3.3128` n `146` status `ready` deltaP `-4.7453` edge `-0.0485` maxDD `-9.0076`
- `market_context_high->commodity_4h` score `-3.8415` n `146` status `ready` deltaP `-7.6091` edge `0.0807` maxDD `-13.0076`
- `market_context_high->fx_24h` score `-4.3329` n `146` status `ready` deltaP `-3.3317` edge `-0.0161` maxDD `-21.0414`
- `market_context_high->equity_24h` score `-4.5004` n `146` status `ready` deltaP `-10.5834` edge `-0.044` maxDD `-10.5047`
- `market_context_high->unknown_4h` score `-4.9853` n `146` status `ready` deltaP `1.1219` edge `-0.2351` maxDD `-8.3588`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
