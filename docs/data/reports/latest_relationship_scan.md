# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-07T19:37:34.366402+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11773`

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

- `market_context_high->equity_24h` score `4.4275` n `92` status `ready` deltaP `-0.7029` edge `0.6838` maxDD `-21.1456`
- `market_context_high->metal_24h` score `3.4815` n `92` status `ready` deltaP `15.2584` edge `0.246` maxDD `-2.2743`
- `market_context_high->fx_24h` score `1.7396` n `92` status `ready` deltaP `27.1962` edge `0.0601` maxDD `-2.3821`
- `market_context_high->commodity_4h` score `1.5359` n `109` status `ready` deltaP `15.5977` edge `0.0913` maxDD `-2.7169`
- `market_context_high->index_24h` score `1.1797` n `92` status `ready` deltaP `11.1325` edge `0.1754` maxDD `-5.7715`
- `market_context_high->commodity_1h` score `0.8761` n `114` status `ready` deltaP `12.0023` edge `0.0299` maxDD `-0.9524`
- `market_context_high->fx_4h` score `-0.051` n `109` status `ready` deltaP `7.7814` edge `0.0067` maxDD `-1.6928`
- `market_context_high->fx_1h` score `-0.107` n `114` status `ready` deltaP `6.2901` edge `-0.0013` maxDD `-0.9639`
- `market_context_high->equity_1h` score `-0.2711` n `114` status `ready` deltaP `5.2448` edge `0.0253` maxDD `-4.6286`
- `market_context_high->index_1h` score `-0.3195` n `114` status `ready` deltaP `-0.5541` edge `-0.0025` maxDD `-0.7809`
- `market_context_high->index_4h` score `-0.3513` n `109` status `ready` deltaP `2.1551` edge `0.0011` maxDD `-1.1743`
- `market_context_high->equity_4h` score `-0.7319` n `109` status `ready` deltaP `9.3505` edge `0.0104` maxDD `-7.6983`
- `market_context_high->metal_1h` score `-0.8348` n `114` status `ready` deltaP `-2.7576` edge `-0.0016` maxDD `-0.9664`
- `market_context_high->metal_4h` score `-0.889` n `109` status `ready` deltaP `3.7047` edge `0.0021` maxDD `-2.7373`
- `market_context_high->crypto_alt_1h` score `-1.286` n `114` status `ready` deltaP `-5.1975` edge `-0.0096` maxDD `-2.3669`
- `market_context_high->crypto_major_1h` score `-2.4089` n `114` status `ready` deltaP `-7.0175` edge `-0.0472` maxDD `-5.2071`
- `market_context_high->crypto_alt_4h` score `-2.5741` n `109` status `ready` deltaP `-1.6727` edge `-0.0477` maxDD `-5.7857`
- `market_context_high->crypto_major_24h` score `-3.9841` n `92` status `ready` deltaP `3.753` edge `-0.1076` maxDD `-14.2873`
- `market_context_high->crypto_alt_24h` score `-4.6238` n `92` status `ready` deltaP `-16.8917` edge `-0.1284` maxDD `-4.5445`
- `market_context_high->crypto_major_4h` score `-6.5852` n `109` status `ready` deltaP `-7.6485` edge `-0.1771` maxDD `-17.9873`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
