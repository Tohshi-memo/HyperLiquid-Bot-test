# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-21T14:21:34.786525+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `8866`

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

- `market_context_high->unknown_4h` score `31.1785` n `58` status `ready` deltaP `1.23` edge `2.605` maxDD `-0.5326`
- `news_risk_high->crypto_major_24h` score `19.5446` n `101` status `ready` deltaP `7.1026` edge `2.2672` maxDD `-46.1999`
- `news_risk_high->crypto_alt_24h` score `13.5782` n `101` status `ready` deltaP `7.4876` edge `1.5697` maxDD `-32.7147`
- `news_risk_high->crypto_alt_4h` score `3.4205` n `101` status `ready` deltaP `16.6324` edge `0.2951` maxDD `-7.675`
- `news_risk_high->crypto_major_4h` score `3.1375` n `101` status `ready` deltaP `19.9861` edge `0.254` maxDD `-8.0625`
- `news_risk_high->crypto_alt_1h` score `2.4236` n `101` status `ready` deltaP `14.8841` edge `0.1493` maxDD `-2.058`
- `news_risk_high->crypto_major_1h` score `1.7835` n `101` status `ready` deltaP `16.5308` edge `0.0907` maxDD `-2.8494`
- `news_risk_high->commodity_24h` score `1.3911` n `101` status `ready` deltaP `24.0649` edge `0.1485` maxDD `-3.4467`
- `market_context_high->equity_1h` score `0.7288` n `58` status `ready` deltaP `5.2602` edge `0.051` maxDD `-0.36`
- `market_context_high->index_1h` score `0.5759` n `58` status `ready` deltaP `9.0801` edge `0.013` maxDD `-0.0435`
- `news_risk_high->metal_1h` score `0.4771` n `101` status `ready` deltaP `13.2507` edge `0.0116` maxDD `-0.8144`
- `market_context_high->fx_1h` score `0.4085` n `58` status `ready` deltaP `9.5241` edge `0.0062` maxDD `-0.1854`
- `news_risk_high->metal_4h` score `0.2895` n `101` status `ready` deltaP `14.6598` edge `0.0318` maxDD `-2.0994`
- `news_risk_high->fx_4h` score `0.2891` n `101` status `ready` deltaP `9.4029` edge `0.025` maxDD `-0.421`
- `market_context_high->index_4h` score `0.2568` n `58` status `ready` deltaP `13.5618` edge `0.0062` maxDD `-1.0949`
- `market_context_high->metal_1h` score `0.1992` n `58` status `ready` deltaP `4.8008` edge `0.0154` maxDD `-0.1314`
- `news_risk_high->fx_1h` score `-0.1405` n `101` status `ready` deltaP `3.8907` edge `0.0067` maxDD `-0.2147`
- `news_risk_high->equity_1h` score `-0.346` n `101` status `ready` deltaP `0.873` edge `0.0059` maxDD `-0.9112`
- `market_context_high->fx_4h` score `-0.448` n `58` status `ready` deltaP `1.209` edge `-0.0031` maxDD `-0.6588`
- `news_risk_high->metal_24h` score `-0.4757` n `101` status `ready` deltaP `8.7355` edge `-0.0348` maxDD `-2.4203`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
