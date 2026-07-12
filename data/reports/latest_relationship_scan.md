# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-12T05:07:28.026467+00:00`
- Price records: `672`
- Market context records: `6465`
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

- `news_risk_high->crypto_alt_24h` score `12.0523` n `32` status `ready` deltaP `31.7708` edge `0.8073` maxDD `-0.5131`
- `market_context_high->unknown_24h` score `7.0642` n `151` status `ready` deltaP `16.4114` edge `0.8093` maxDD `-15.0689`
- `news_risk_high->fx_24h` score `6.3142` n `32` status `ready` deltaP `52.2569` edge `0.1778` maxDD `0.0`
- `news_risk_high->fx_4h` score `4.0962` n `32` status `ready` deltaP `42.6067` edge `0.0619` maxDD `-0.0345`
- `news_risk_high->crypto_major_24h` score `3.7377` n `32` status `ready` deltaP `14.0625` edge `0.4634` maxDD `-4.2368`
- `news_risk_high->commodity_24h` score `3.4823` n `32` status `ready` deltaP `31.25` edge `0.1024` maxDD `-0.3101`
- `news_risk_high->fx_1h` score `1.9965` n `36` status `ready` deltaP `24.2348` edge `0.0187` maxDD `-0.1113`
- `market_context_high->unknown_1h` score `1.5626` n `172` status `ready` deltaP `-5.6364` edge `0.2579` maxDD `-3.2083`
- `news_risk_high->crypto_major_1h` score `0.8579` n `36` status `ready` deltaP `7.9674` edge `0.1064` maxDD `-2.2956`
- `market_context_high->commodity_24h` score `0.3849` n `151` status `ready` deltaP `7.1399` edge `0.1713` maxDD `-5.2791`
- `news_risk_high->crypto_alt_1h` score `0.3518` n `36` status `ready` deltaP `4.358` edge `0.0622` maxDD `-1.6923`
- `market_context_high->index_4h` score `0.3406` n `172` status `ready` deltaP `10.2773` edge `0.0275` maxDD `-0.4108`
- `market_context_high->unknown_4h` score `0.2475` n `172` status `ready` deltaP `-15.2404` edge `0.3628` maxDD `-10.5788`
- `market_context_high->crypto_alt_4h` score `0.146` n `172` status `ready` deltaP `7.941` edge `0.1146` maxDD `-6.7632`
- `market_context_high->metal_4h` score `0.0445` n `172` status `ready` deltaP `10.3694` edge `0.0434` maxDD `-2.7056`
- `news_risk_high->index_24h` score `-0.4618` n `32` status `ready` deltaP `4.6875` edge `-0.0033` maxDD `-2.3058`
- `news_risk_high->unknown_1h` score `-0.5477` n `36` status `ready` deltaP `4.4411` edge `-0.0381` maxDD `-0.9718`
- `market_context_high->metal_1h` score `-0.5513` n `172` status `ready` deltaP `0.8982` edge `0.0011` maxDD `-1.8877`
- `market_context_high->equity_4h` score `-0.581` n `172` status `ready` deltaP `6.6151` edge `0.0513` maxDD `-8.2573`
- `market_context_high->commodity_1h` score `-0.5837` n `172` status `ready` deltaP `-0.3342` edge `-0.0043` maxDD `-2.1314`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
