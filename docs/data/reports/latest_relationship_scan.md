# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-31T04:52:25.490178+00:00`
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

- `market_context_high->unknown_24h` score `1586.6559` n `134` status `ready` deltaP `-4.8741` edge `132.2968` maxDD `-1.1049`
- `news_risk_high->unknown_1h` score `127.2986` n `94` status `ready` deltaP `-2.4685` edge `10.6533` maxDD `-0.9571`
- `market_context_high->unknown_4h` score `40.319` n `134` status `ready` deltaP `1.6359` edge `3.3623` maxDD `-0.3966`
- `market_context_high->equity_24h` score `7.7132` n `134` status `ready` deltaP `19.4367` edge `0.7889` maxDD `-14.0571`
- `news_risk_high->crypto_alt_4h` score `7.1673` n `92` status `ready` deltaP `23.3629` edge `0.5076` maxDD `-3.6198`
- `market_context_high->index_24h` score `4.0034` n `134` status `ready` deltaP `38.3888` edge `0.096` maxDD `-0.1315`
- `news_risk_high->crypto_alt_1h` score `1.4435` n `94` status `ready` deltaP `11.1893` edge `0.1286` maxDD `-3.9659`
- `market_context_high->metal_1h` score `0.4179` n `134` status `ready` deltaP `11.5024` edge `0.0148` maxDD `-0.3659`
- `market_context_high->commodity_4h` score `0.3891` n `134` status `ready` deltaP `14.7001` edge `0.0563` maxDD `-1.0837`
- `market_context_high->metal_4h` score `0.3264` n `134` status `ready` deltaP `14.9163` edge `0.032` maxDD `-1.8344`
- `market_context_high->equity_1h` score `0.2042` n `134` status `ready` deltaP `4.3324` edge `0.0757` maxDD `-2.3383`
- `market_context_high->crypto_major_1h` score `-0.0024` n `134` status `ready` deltaP `7.4649` edge `0.0528` maxDD `-5.2213`
- `market_context_high->equity_4h` score `-0.1001` n `134` status `ready` deltaP `1.0193` edge `0.1388` maxDD `-6.008`
- `market_context_high->fx_1h` score `-0.1166` n `134` status `ready` deltaP `3.28` edge `-0.001` maxDD `-0.1986`
- `market_context_high->commodity_1h` score `-0.2229` n `134` status `ready` deltaP `2.6924` edge `0.0149` maxDD `-0.4475`
- `market_context_high->fx_4h` score `-0.4887` n `134` status `ready` deltaP `-0.0159` edge `-0.0027` maxDD `-0.4545`
- `market_context_high->metal_24h` score `-0.5844` n `134` status `ready` deltaP `3.9257` edge `0.1636` maxDD `-10.5088`
- `market_context_high->index_1h` score `-0.7312` n `134` status `ready` deltaP `-0.8982` edge `0.0009` maxDD `-1.1344`
- `news_risk_high->index_1h` score `-0.8231` n `94` status `ready` deltaP `2.2933` edge `-0.0039` maxDD `-1.3981`
- `news_risk_high->fx_1h` score `-0.8668` n `94` status `ready` deltaP `-5.4529` edge `-0.0047` maxDD `-0.6065`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
