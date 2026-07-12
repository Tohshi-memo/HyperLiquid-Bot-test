# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-12T05:22:26.868825+00:00`
- Price records: `672`
- Market context records: `6466`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5907`

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

- `news_risk_high->crypto_alt_24h` score `12.0938` n `32` status `ready` deltaP `31.9444` edge `0.8096` maxDD `-0.5131`
- `market_context_high->unknown_24h` score `6.9611` n `152` status `ready` deltaP `16.1275` edge `0.8026` maxDD `-15.0689`
- `news_risk_high->fx_24h` score `6.3166` n `32` status `ready` deltaP `52.2569` edge `0.178` maxDD `0.0`
- `news_risk_high->fx_4h` score `4.0962` n `32` status `ready` deltaP `42.6067` edge `0.0619` maxDD `-0.0345`
- `news_risk_high->crypto_major_24h` score `3.781` n `32` status `ready` deltaP `14.2361` edge `0.4678` maxDD `-4.2368`
- `news_risk_high->commodity_24h` score `3.4552` n `32` status `ready` deltaP `31.0764` edge `0.1013` maxDD `-0.3101`
- `news_risk_high->fx_1h` score `1.7915` n `37` status `ready` deltaP `22.358` edge `0.0183` maxDD `-0.1113`
- `market_context_high->unknown_1h` score `1.5399` n `172` status `ready` deltaP `-5.7861` edge `0.257` maxDD `-3.2083`
- `news_risk_high->crypto_major_1h` score `0.6627` n `37` status `ready` deltaP `6.3158` edge `0.096` maxDD `-2.5846`
- `market_context_high->commodity_24h` score `0.4028` n `152` status `ready` deltaP `7.2277` edge `0.1722` maxDD `-5.2791`
- `market_context_high->index_4h` score `0.354` n `172` status `ready` deltaP `10.4297` edge `0.0276` maxDD `-0.4108`
- `market_context_high->unknown_4h` score `0.2559` n `172` status `ready` deltaP `-15.2404` edge `0.3635` maxDD `-10.5788`
- `news_risk_high->crypto_alt_1h` score `0.1675` n `37` status `ready` deltaP `2.8565` edge `0.0523` maxDD `-1.9894`
- `market_context_high->crypto_alt_4h` score `0.1206` n `172` status `ready` deltaP `7.7886` edge `0.1135` maxDD `-6.7632`
- `market_context_high->metal_4h` score `0.0323` n `172` status `ready` deltaP `10.2169` edge `0.0434` maxDD `-2.7056`
- `news_risk_high->unknown_1h` score `-0.4372` n `37` status `ready` deltaP `5.4176` edge `-0.0354` maxDD `-0.9718`
- `news_risk_high->index_24h` score `-0.4618` n `32` status `ready` deltaP `4.6875` edge `-0.0033` maxDD `-2.3058`
- `market_context_high->metal_1h` score `-0.5513` n `172` status `ready` deltaP `0.8982` edge `0.0011` maxDD `-1.8877`
- `market_context_high->equity_4h` score `-0.5802` n `172` status `ready` deltaP `6.6151` edge `0.0514` maxDD `-8.2573`
- `market_context_high->commodity_1h` score `-0.5923` n `172` status `ready` deltaP `-0.4839` edge `-0.0044` maxDD `-2.1314`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
