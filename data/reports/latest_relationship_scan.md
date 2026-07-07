# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-07T15:07:27.742684+00:00`
- Price records: `672`
- Market context records: `5992`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11236`

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

- `news_risk_high->fx_24h` score `7.5311` n `30` status `ready` deltaP `68.9236` edge `0.1681` maxDD `0.0`
- `news_risk_high->commodity_24h` score `4.3746` n `30` status `ready` deltaP `33.1945` edge `0.1638` maxDD `-0.3101`
- `news_risk_high->fx_4h` score `4.1421` n `30` status `ready` deltaP `42.8963` edge `0.0638` maxDD `-0.0345`
- `news_risk_high->fx_1h` score `2.2298` n `30` status `ready` deltaP `26.7764` edge `0.0212` maxDD `-0.1113`
- `market_context_high->equity_4h` score `1.1085` n `229` status `ready` deltaP `7.5181` edge `0.1517` maxDD `-4.0887`
- `news_risk_high->crypto_major_1h` score `0.7858` n `30` status `ready` deltaP `9.8902` edge `0.0815` maxDD `-2.0691`
- `news_risk_high->crypto_alt_1h` score `0.1951` n `30` status `ready` deltaP `5.3194` edge `0.0357` maxDD `-1.6923`
- `news_risk_high->index_24h` score `0.0914` n `30` status `ready` deltaP `9.2361` edge `0.0373` maxDD `-2.3058`
- `market_context_high->equity_1h` score `-0.393` n `229` status `ready` deltaP `3.9243` edge `0.0363` maxDD `-4.3608`
- `news_risk_high->metal_1h` score `-0.4126` n `30` status `ready` deltaP `1.5369` edge `-0.0265` maxDD `-1.2643`
- `market_context_high->metal_1h` score `-0.5015` n `229` status `ready` deltaP `2.3521` edge `-0.0001` maxDD `-2.0564`
- `market_context_high->equity_24h` score `-0.5132` n `202` status `ready` deltaP `22.4577` edge `0.3443` maxDD `-31.2762`
- `market_context_high->commodity_1h` score `-0.5992` n `229` status `ready` deltaP `-0.6426` edge `0.0023` maxDD `-0.8358`
- `market_context_high->fx_1h` score `-0.8008` n `229` status `ready` deltaP `-2.0154` edge `-0.0018` maxDD `-0.7864`
- `news_risk_high->index_1h` score `-1.0259` n `30` status `ready` deltaP `-9.2515` edge `-0.0184` maxDD `-1.1161`
- `market_context_high->commodity_4h` score `-1.101` n `229` status `ready` deltaP `-0.2756` edge `-0.0002` maxDD `-3.7964`
- `market_context_high->crypto_major_1h` score `-1.1186` n `229` status `ready` deltaP `2.4521` edge `0.017` maxDD `-9.807`
- `market_context_high->index_1h` score `-1.1503` n `229` status `ready` deltaP `-1.2166` edge `0.0036` maxDD `-1.3078`
- `market_context_high->index_4h` score `-1.1962` n `229` status `ready` deltaP `0.0246` edge `0.0152` maxDD `-3.165`
- `market_context_high->crypto_alt_1h` score `-1.1966` n `229` status `ready` deltaP `1.4911` edge `0.0119` maxDD `-9.3536`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
