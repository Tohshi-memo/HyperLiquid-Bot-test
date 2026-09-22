# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-22T00:22:27.017809+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9940`

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

- `market_context_high->unknown_4h` score `34.3884` n `54` status `ready` deltaP `5.6176` edge `2.8349` maxDD `-0.1988`
- `market_context_high->crypto_major_24h` score `15.9228` n `51` status `ready` deltaP `10.2533` edge `1.7094` maxDD `-32.7349`
- `news_risk_high->crypto_major_24h` score `11.0703` n `101` status `ready` deltaP `0.1581` edge `1.6073` maxDD `-46.1999`
- `market_context_high->equity_24h` score `7.9176` n `51` status `ready` deltaP `3.4825` edge `0.8342` maxDD `-12.4758`
- `news_risk_high->crypto_alt_24h` score `6.5307` n `101` status `ready` deltaP `0.5432` edge `1.0287` maxDD `-32.7147`
- `news_risk_high->crypto_alt_4h` score `3.1138` n `101` status `ready` deltaP `15.108` edge `0.2797` maxDD `-7.675`
- `market_context_high->index_24h` score `3.0193` n `51` status `ready` deltaP `7.4755` edge `0.2593` maxDD `-1.269`
- `news_risk_high->commodity_24h` score `2.5096` n `101` status `ready` deltaP `31.0093` edge `0.2456` maxDD `-3.4467`
- `news_risk_high->crypto_alt_1h` score `2.3805` n `101` status `ready` deltaP `14.5847` edge `0.1477` maxDD `-2.058`
- `news_risk_high->crypto_major_4h` score `2.167` n `101` status `ready` deltaP `16.48` edge `0.1965` maxDD `-8.0625`
- `news_risk_high->crypto_major_1h` score `1.6431` n `101` status `ready` deltaP `16.0817` edge `0.082` maxDD `-2.8494`
- `market_context_high->crypto_alt_24h` score `1.3388` n `51` status `ready` deltaP `8.6193` edge `0.499` maxDD `-32.9252`
- `news_risk_high->fx_4h` score `0.513` n `101` status `ready` deltaP `11.8419` edge `0.0274` maxDD `-0.421`
- `news_risk_high->metal_1h` score `0.4268` n `101` status `ready` deltaP `12.6519` edge `0.0114` maxDD `-0.8144`
- `market_context_high->fx_1h` score `0.2879` n `54` status `ready` deltaP `8.0617` edge `0.0059` maxDD `-0.1854`
- `market_context_high->index_1h` score `0.2517` n `54` status `ready` deltaP `5.6277` edge `0.009` maxDD `-0.0435`
- `market_context_high->equity_1h` score `0.2492` n `54` status `ready` deltaP `1.5303` edge `0.0359` maxDD `-0.36`
- `market_context_high->metal_24h` score `0.2089` n `51` status `ready` deltaP `17.0241` edge `-0.0727` maxDD `-0.2042`
- `news_risk_high->metal_4h` score `0.1967` n `101` status `ready` deltaP `13.4403` edge `0.0322` maxDD `-2.0994`
- `market_context_high->metal_1h` score `0.1813` n `54` status `ready` deltaP `4.7128` edge `0.0145` maxDD `-0.1314`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
