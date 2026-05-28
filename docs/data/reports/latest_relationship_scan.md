# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-28T13:52:22.333171+00:00`
- Price records: `672`
- Market context records: `2147`
- Flow alert records: `8077`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9168`

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

- `market_context_high->crypto_alt_4h` score `13.5425` n `154` status `ready` deltaP `37.9612` edge `0.9691` maxDD `-5.1574`
- `market_context_high->crypto_major_4h` score `12.018` n `154` status `ready` deltaP `42.089` edge `0.7739` maxDD `-1.9063`
- `market_context_high->unknown_4h` score `6.4911` n `154` status `ready` deltaP `25.2059` edge `0.4478` maxDD `-2.6599`
- `news_risk_high->commodity_4h` score `6.2068` n `33` status `ready` deltaP `28.0442` edge `0.3974` maxDD `-3.0367`
- `market_context_high->equity_4h` score `5.0714` n `154` status `ready` deltaP `26.4551` edge `0.3557` maxDD `-5.0894`
- `market_context_high->index_24h` score `3.7686` n `154` status `ready` deltaP `14.9531` edge `0.3372` maxDD `-4.1604`
- `market_context_high->crypto_major_1h` score `3.473` n `154` status `ready` deltaP `18.5298` edge `0.2136` maxDD `-1.817`
- `market_context_high->crypto_alt_1h` score `3.2214` n `154` status `ready` deltaP `16.5332` edge `0.2446` maxDD `-4.9097`
- `market_context_high->metal_4h` score `3.1908` n `154` status `ready` deltaP `21.7275` edge `0.2598` maxDD `-4.7664`
- `market_context_high->equity_24h` score `3.1739` n `154` status `ready` deltaP `26.4498` edge `0.578` maxDD `-33.1875`
- `market_context_high->index_4h` score `3.1545` n `154` status `ready` deltaP `22.7906` edge `0.1793` maxDD `-1.8022`
- `market_context_high->unknown_24h` score `2.7501` n `154` status `ready` deltaP `27.0473` edge `0.5809` maxDD `-35.8966`
- `news_risk_high->fx_4h` score `2.3567` n `33` status `ready` deltaP `30.7326` edge `0.0099` maxDD `-0.1382`
- `market_context_high->crypto_major_24h` score `2.1255` n `154` status `ready` deltaP `21.4624` edge `0.988` maxDD `-62.3533`
- `news_risk_high->unknown_4h` score `1.5232` n `33` status `ready` deltaP `18.496` edge `0.1443` maxDD `-2.7857`
- `news_risk_high->unknown_1h` score `1.2274` n `41` status `ready` deltaP `19.9832` edge `0.016` maxDD `-1.7548`
- `market_context_high->equity_1h` score `0.8897` n `154` status `ready` deltaP `10.6463` edge `0.082` maxDD `-2.6402`
- `news_risk_high->commodity_1h` score `0.8127` n `41` status `ready` deltaP `10.9756` edge `0.099` maxDD `-2.1052`
- `news_risk_high->fx_1h` score `0.7357` n `41` status `ready` deltaP `11.275` edge `0.0118` maxDD `-0.0524`
- `market_context_high->metal_1h` score `0.6657` n `154` status `ready` deltaP `9.4895` edge `0.0592` maxDD `-2.3594`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
