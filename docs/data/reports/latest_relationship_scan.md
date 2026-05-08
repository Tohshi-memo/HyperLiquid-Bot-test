# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-08T04:07:13.355621+00:00`
- Price records: `612`
- Market context records: `716`
- Flow alert records: `2024`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `901`

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

- `market_context_high->crypto_major_24h` score `11.3692` n `146` status `ready` deltaP `27.6335` edge `0.7966` maxDD `-1.3382`
- `market_context_high->crypto_alt_24h` score `6.3693` n `146` status `ready` deltaP `8.036` edge `0.482` maxDD `-0.0508`
- `market_context_high->fx_4h` score `-0.2825` n `149` status `ready` deltaP `6.1978` edge `0.0096` maxDD `-1.6381`
- `market_context_high->fx_1h` score `-0.2922` n `149` status `ready` deltaP `2.7512` edge `0.002` maxDD `-0.291`
- `market_context_high->commodity_1h` score `-0.4353` n `149` status `ready` deltaP `2.6357` edge `0.0436` maxDD `-3.7959`
- `market_context_high->index_1h` score `-0.6281` n `149` status `ready` deltaP `0.3034` edge `0.0028` maxDD `-2.8282`
- `market_context_high->index_24h` score `-0.6785` n `146` status `ready` deltaP `-1.5197` edge `0.1531` maxDD `-5.9609`
- `market_context_high->crypto_major_4h` score `-1.0421` n `149` status `ready` deltaP `17.1141` edge `0.1229` maxDD `-22.648`
- `market_context_high->unknown_1h` score `-1.1493` n `149` status `ready` deltaP `-3.8161` edge `-0.01` maxDD `-2.1602`
- `market_context_high->equity_1h` score `-1.1762` n `149` status `ready` deltaP `-1.6923` edge `-0.0057` maxDD `-4.4826`
- `market_context_high->crypto_alt_1h` score `-1.3853` n `149` status `ready` deltaP `4.5346` edge `-0.0142` maxDD `-8.1842`
- `market_context_high->crypto_major_1h` score `-1.5903` n `149` status `ready` deltaP `6.2511` edge `-0.0019` maxDD `-11.4508`
- `market_context_high->equity_24h` score `-1.642` n `146` status `ready` deltaP `-3.3684` edge `0.1461` maxDD `-10.5047`
- `market_context_high->index_4h` score `-1.8039` n `149` status `ready` deltaP `1.5962` edge `-0.0087` maxDD `-6.5149`
- `market_context_high->crypto_alt_4h` score `-1.9616` n `149` status `ready` deltaP `3.6912` edge `0.0689` maxDD `-15.2248`
- `market_context_high->equity_4h` score `-2.7448` n `149` status `ready` deltaP `-1.4443` edge `-0.0039` maxDD `-10.5498`
- `market_context_high->metal_1h` score `-3.384` n `149` status `ready` deltaP `-5.0655` edge `-0.0523` maxDD `-9.0076`
- `market_context_high->commodity_4h` score `-3.6835` n `149` status `ready` deltaP `-5.8146` edge `0.0819` maxDD `-13.0076`
- `market_context_high->unknown_4h` score `-4.1641` n `149` status `ready` deltaP `3.6913` edge `-0.1838` maxDD `-8.3588`
- `market_context_high->fx_24h` score `-5.1359` n `146` status `ready` deltaP `-13.0298` edge `-0.0544` maxDD `-21.0414`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
