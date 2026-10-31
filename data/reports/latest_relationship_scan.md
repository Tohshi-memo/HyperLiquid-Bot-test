# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-31T04:37:25.072796+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `7260`

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

- `market_context_high->unknown_24h` score `1586.5911` n `134` status `ready` deltaP `-4.8741` edge `132.2914` maxDD `-1.1049`
- `news_risk_high->unknown_1h` score `131.1017` n `93` status `ready` deltaP `-2.6287` edge `10.9713` maxDD `-0.9571`
- `market_context_high->unknown_4h` score `40.4728` n `134` status `ready` deltaP `1.7883` edge `3.3741` maxDD `-0.3966`
- `market_context_high->equity_24h` score `7.6369` n `134` status `ready` deltaP `19.2631` edge `0.7837` maxDD `-14.0571`
- `news_risk_high->crypto_alt_4h` score `7.1625` n `92` status `ready` deltaP `23.3629` edge `0.5072` maxDD `-3.6198`
- `market_context_high->index_24h` score `3.9847` n `134` status `ready` deltaP `38.2152` edge `0.0956` maxDD `-0.1315`
- `news_risk_high->crypto_alt_1h` score `1.5601` n `93` status `ready` deltaP `11.807` edge `0.1342` maxDD `-3.9659`
- `market_context_high->metal_1h` score `0.4179` n `134` status `ready` deltaP `11.5024` edge `0.0148` maxDD `-0.3659`
- `market_context_high->commodity_4h` score `0.3879` n `134` status `ready` deltaP `14.7001` edge `0.0562` maxDD `-1.0837`
- `market_context_high->metal_4h` score `0.3264` n `134` status `ready` deltaP `14.9163` edge `0.032` maxDD `-1.8344`
- `market_context_high->equity_1h` score `0.2042` n `134` status `ready` deltaP `4.3324` edge `0.0757` maxDD `-2.3383`
- `market_context_high->crypto_major_1h` score `-0.0036` n `134` status `ready` deltaP `7.4649` edge `0.0527` maxDD `-5.2213`
- `market_context_high->equity_4h` score `-0.0986` n `134` status `ready` deltaP `1.0193` edge `0.139` maxDD `-6.008`
- `market_context_high->fx_1h` score `-0.1244` n `134` status `ready` deltaP `3.1303` edge `-0.001` maxDD `-0.1986`
- `market_context_high->commodity_1h` score `-0.2229` n `134` status `ready` deltaP `2.6924` edge `0.0149` maxDD `-0.4475`
- `market_context_high->fx_4h` score `-0.4887` n `134` status `ready` deltaP `-0.0159` edge `-0.0027` maxDD `-0.4545`
- `market_context_high->metal_24h` score `-0.5922` n `134` status `ready` deltaP `3.9257` edge `0.1626` maxDD `-10.5088`
- `market_context_high->index_1h` score `-0.7432` n `134` status `ready` deltaP `-1.0479` edge `0.0009` maxDD `-1.1344`
- `news_risk_high->index_1h` score `-0.7869` n `93` status `ready` deltaP `2.7155` edge `-0.0037` maxDD `-1.3981`
- `news_risk_high->fx_1h` score `-0.8483` n `93` status `ready` deltaP `-5.1107` edge `-0.0046` maxDD `-0.6065`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
